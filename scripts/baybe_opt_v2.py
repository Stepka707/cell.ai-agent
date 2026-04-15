#!/usr/bin/env python3
"""
baybe_opt.py — Bayesian optimization workflow for V. natriegens growth media.

Loads historical plate data, runs per-base-media BayBE campaigns, annotates
proposals with a sklearn GP surrogate prediction, and writes results in
*_plate_condition_map.csv format with an added predicted_growth_rate_per_hr column.

Volume constraint: base_media_vol + reagents + cells + water = 200 µL
  → BayBE enforces: base_media_vol + sum(reagents) + cells ≤ 200 µL
  → water fills the remainder, always ≥ 0
  → cells is an optimizable parameter (not fixed)

Usage:
    python scripts/baybe_opt.py                         # defaults (6 proposals)
    python scripts/baybe_opt.py --round 3 --n-proposals 6
    python scripts/baybe_opt.py --data-dir data --output results/round3.csv
    python scripts/baybe_opt.py --exclude-media "Defined Glycerol Media"
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import warnings
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from baybe import Campaign
from baybe.constraints import ContinuousLinearConstraint
from baybe.objectives import SingleTargetObjective
from baybe.parameters import CategoricalParameter, NumericalContinuousParameter
from baybe.recommenders import BotorchRecommender, RandomRecommender
from baybe.searchspace import SearchSpace
from baybe.targets import NumericalTarget

# ── Constants ──────────────────────────────────────────────────────────────────

TOTAL_VOL_UL = 200

# Reagent columns — order determines column order in output CSV
REAGENT_COLS = ["Yeast_extract", "MgSO4", "K2HPO4", "NH4_2SO4", "MOPS", "Na_L_glut", "Tryptone"]

# All reagents are search parameters for BayBE
VARIED_REAGENTS = ["Yeast_extract", "MgSO4", "K2HPO4", "NH4_2SO4", "MOPS", "Na_L_glut", "Tryptone"]

# Cells volume is fixed — not a search parameter.
FIXED_CELLS_UL = 10

# ALL_VOL_COLS: columns used when joining condition maps to growth data
ALL_VOL_COLS = ["base_media_vol"] + REAGENT_COLS + ["cells"]

# Volume bounds (µL)
REAGENT_VOL_BOUNDS = (0, 40)        # per-reagent cap fallback
MAX_REAGENT_SUM_UL = 60             # total additive volume across all reagents
MIN_PIPETTE_UL = 5.0                # minimum pipettable volume; values below this snap to 0

# Tighter per-reagent bounds for specialty supplements introduced in round 2.
# These are biologically active at low doses; cap well below REAGENT_VOL_BOUNDS.
SPECIALTY_REAGENT_BOUNDS: dict[str, tuple[float, float]] = {
    "Yeast_extract": (0, 30),   # 100 mg/mL stock; historical max ~25 µL
    "MgSO4":         (0, 10),   # 100 mM stock
    "K2HPO4":        (0, 29),   # 50 mM stock
    "NH4_2SO4":      (0, 20),   # 1 M stock; 20 µL → 100 mM final
    "MOPS":          (0, 30),   # 1 M stock; 8 µL → 40 mM final, 20 µL → 100 mM final
    "Na_L_glut":     (0, 14),   # 1 M stock
    "Tryptone":      (0, 30),   # 100 mg/mL stock; historical max 28 µL
}

BASE_MEDIA_OPTIONS = [
    "Novel Bio NBxCyclone Media",
    "Prepared LBv2 Media",
    "Defined-Minimal Media",
    "Semi-Defined Media",
    "High Buffer Defined Media",
    "Defined Glycerol Media",
]

# Media excluded from BayBE campaigns regardless of performance ranking.
EXCLUDED_MEDIA: set[str] = {}

TARGET_COL = "mean_growth_rate_per_hr"
RANDOM_SEED = 42

# Short abbreviations used in formulation names ("Baybe-<abbrev>-…")
MEDIA_ABBREV: dict[str, str] = {
    #"Novel Bio NBxCyclone Media":  "NBx",
    "Prepared LBv2 Media":         "LBv2",
   # "Defined-Minimal Media":       "DMin",
    "Semi-Defined Media":          "SDef",
    "High Buffer Defined Media":   "HBD",
   # "Defined Glycerol Media":      "DGly",
}

# Per-reagent metadata for JSON output
# (display_name, stock_concentration_str, stock_conc_numeric, unit)
# final_concentration = stock_conc_numeric * vol_uL / total_vol_uL  [unit]
REAGENT_META: dict[str, dict] = {
    "Yeast_extract": {"display": "Yeast Extract",       "stock_str": "100 mg/mL", "stock_num": 100,  "unit": "mg/mL"},
    "MgSO4":         {"display": "MgSO₄",               "stock_str": "100 mM",    "stock_num": 100,  "unit": "mM"},
    "K2HPO4":        {"display": "K₂HPO₄",              "stock_str": "50 mM",     "stock_num": 50,   "unit": "mM"},
    "NH4_2SO4":      {"display": "(NH₄)₂SO₄",           "stock_str": "1000 mM",   "stock_num": 1000, "unit": "mM"},
    "MOPS":          {"display": "MOPS pH 7",            "stock_str": "1000 mM",   "stock_num": 1000, "unit": "mM"},
    "Na_L_glut":     {"display": "Sodium L-Glutamate",   "stock_str": "1000 mM",   "stock_num": 1000, "unit": "mM"},
    "Tryptone":      {"display": "Tryptone",             "stock_str": "100 mg/mL", "stock_num": 100,  "unit": "mg/mL"},
}

# Mapping from raw CSV column names → internal script names.
# ── Data loading ───────────────────────────────────────────────────────────────

# Reverse mapping: JSON display name → internal column name (built from REAGENT_META)
DISPLAY_TO_COL: dict[str, str] = {meta["display"]: col for col, meta in REAGENT_META.items()}


def load_history(data_dir: str | Path, json_dir: str | Path | None = None) -> pd.DataFrame:
    """
    Build training data by joining *_growth.csv (growth rates, in data_dir) to
    baybe_*.json formulation files (in json_dir, defaults to output_baybe/) on
    the `name` column.

    Growth CSVs must contain columns: `name`, `growth_rate_per_hr`.
    JSON files are read from json_dir (output_baybe/ by default) so no manual
    copying is needed — the output of each round is directly used as input for
    the next.

    Replicate wells sharing the same formulation name are averaged.
    Returns an empty DataFrame when no data is found (triggers exploratory mode).
    """
    data_dir = Path(data_dir)
    json_dir = Path(json_dir) if json_dir else Path(__file__).parent.parent / "output_baybe"

    # ── 1. Build formulation lookup from all baybe_*.json files ──────────────
    formulation_lookup: dict[str, dict] = {}
    for json_file in sorted(json_dir.glob("baybe_*.json")):
        try:
            formulations = json.loads(json_file.read_text(encoding="utf-8"))
            for f in formulations:
                record: dict = {
                    "base_media":     f["base_medium"],
                    "base_media_vol": float(f["base_medium_volume_uL"]),
                }
                for col in REAGENT_COLS:
                    record[col] = 0.0
                for comp in f.get("components", []):
                    col = DISPLAY_TO_COL.get(comp["name"])
                    if col:
                        record[col] = float(comp["volume_uL"])
                formulation_lookup[f["condition_id"]] = record
        except Exception as exc:
            print(f"  [warn] Could not read {json_file.name}: {exc}", file=sys.stderr)

    # ── 2. Load growth CSVs and join to formulation lookup on `name` ──────────
    growth_files = sorted(data_dir.glob("*_growth.csv"))
    if not growth_files or not formulation_lookup:
        return pd.DataFrame()

    all_rows: list[pd.DataFrame] = []
    for growth_file in growth_files:
        growth = pd.read_csv(growth_file)

        if "condition_id" not in growth.columns:
            print(f"  [warn] {growth_file.name} missing `condition_id` column — skipping.", file=sys.stderr)
            continue

        growth = growth[["condition_id", "growth_rate_per_hr"]].dropna(subset=["growth_rate_per_hr"])

        records = []
        for _, row in growth.iterrows():
            form = formulation_lookup.get(row["condition_id"])
            if form is None:
                print(f"  [warn] No formulation found for condition_id '{row['condition_id']}' — skipping.", file=sys.stderr)
                continue
            rec = {TARGET_COL: row["growth_rate_per_hr"], **form}
            records.append(rec)

        if records:
            all_rows.append(pd.DataFrame(records))

    if not all_rows:
        return pd.DataFrame()

    combined = pd.concat(all_rows, ignore_index=True)

    # ── 3. Average replicates (same formulation name → same recipe) ───────────
    group_cols = ["base_media", "base_media_vol"] + REAGENT_COLS
    combined = combined.groupby(group_cols, as_index=False)[TARGET_COL].mean()

    return combined.reset_index(drop=True)


# ── GP surrogate for growth-rate predictions ───────────────────────────────────

class GrowthRatePredictor:
    """
    Thin sklearn GP wrapper that one-hot encodes base_media and scales volumes
    before fitting/predicting. Used only to annotate proposed conditions with a
    predicted growth rate — BayBE uses its own internal surrogate for acquisition.
    """

    def __init__(self) -> None:
        kernel = ConstantKernel(1.0) * Matern(nu=2.5) + WhiteKernel(noise_level=0.01)
        self._gp = GaussianProcessRegressor(
            kernel=kernel,
            n_restarts_optimizer=5,
            normalize_y=True,
            random_state=RANDOM_SEED,
        )
        self._ohe = OneHotEncoder(handle_unknown="ignore")
        self._scaler = StandardScaler()
        self._fitted = False

    def _featurize(self, df: pd.DataFrame) -> np.ndarray:
        media_enc = self._ohe.transform(df[["base_media"]])
        if hasattr(media_enc, "toarray"):
            media_enc = media_enc.toarray()
        vols = self._scaler.transform(df[self._vol_cols])
        return np.hstack([media_enc, vols])

    def fit(self, df: pd.DataFrame) -> "GrowthRatePredictor":
        self._vol_cols = [c for c in ALL_VOL_COLS if c in df.columns]
        self._ohe.fit(df[["base_media"]])
        self._scaler.fit(df[self._vol_cols])
        X = self._featurize(df)
        y = df[TARGET_COL].values
        self._gp.fit(X, y)
        self._fitted = True
        return self

    def predict(self, df: pd.DataFrame) -> np.ndarray:
        if not self._fitted:
            return np.full(len(df), np.nan)
        X = self._featurize(df)
        return self._gp.predict(X)


# ── Unified BayBE campaign ────────────────────────────────────────────────────

def _make_searchspace(media_options: list[str], active_reagents: list[str]) -> SearchSpace:
    """
    Build a single BayBE SearchSpace that jointly explores:
      • base_media      — categorical over all available media options
      • active_reagents — continuous additive volumes

    base_media_vol is NOT a search parameter — it is computed after recommendations
    as the remainder: TOTAL_VOL_UL - FIXED_CELLS_UL - sum(reagents).
    No water is added; base media fills the balance.

    One linear constraint caps total reagent volume so base media always has room.
    """
    parameters = [
        CategoricalParameter("base_media", values=media_options),
        *[
            NumericalContinuousParameter(
                col, bounds=SPECIALTY_REAGENT_BOUNDS.get(col, REAGENT_VOL_BOUNDS)
            )
            for col in active_reagents
        ],
    ]
    constraints = [
        # Reagent cap: ensures base_media_vol stays positive and biologically sensible
        ContinuousLinearConstraint(
            parameters=active_reagents,
            operator="<=",
            coefficients=[1.0] * len(active_reagents),
            rhs=float(MAX_REAGENT_SUM_UL),
        ),
    ]
    return SearchSpace.from_product(parameters=parameters, constraints=constraints)


def propose_conditions(
    history: pd.DataFrame,
    n_proposals: int = 6,
    exclude_media: set[str] | None = None,
) -> pd.DataFrame:
    """
    Run a single BayBE campaign that jointly optimises base_media (categorical)
    and all reagent volumes (continuous).  BayBE's acquisition function decides
    which media to explore — no manual splitting or top-N pre-selection needed.

    Uses BotorchRecommender when training data is available, RandomRecommender
    for cold-start (no history).
    """
    excluded = EXCLUDED_MEDIA if exclude_media is None else exclude_media
    media_options = [m for m in BASE_MEDIA_OPTIONS if m not in excluded]

    has_data = not history.empty
    recommender = BotorchRecommender() if has_data else RandomRecommender()

    campaign = Campaign(
        searchspace=_make_searchspace(media_options, VARIED_REAGENTS),
        objective=SingleTargetObjective(NumericalTarget(name=TARGET_COL, mode="MAX")),
        recommender=recommender,
    )

    if has_data:
        # Search space columns: no base_media_vol (it's computed, not optimised)
        sp_cols = ["base_media"] + VARIED_REAGENTS
        measurements = history.loc[history["base_media"].isin(media_options)].copy()
        # Zero-fill any search-space columns absent from historical data
        # (e.g. NaCl was not varied in earlier rounds)
        for col in sp_cols:
            if col not in measurements.columns:
                measurements[col] = 0.0
        measurements = measurements[sp_cols + [TARGET_COL]]
        if not measurements.empty:
            campaign.add_measurements(
                measurements,
                numerical_measurements_must_be_within_tolerance=False,
            )
            print(f"  Added {len(measurements)} historical observations to campaign.")

    recs = campaign.recommend(batch_size=n_proposals).copy()

    # Round and clip reagent volumes
    for col in VARIED_REAGENTS:
        if col in recs.columns:
            recs[col] = recs[col].clip(lower=0).round(1)

    # Enforce minimum pipettable volume: snap values in (0, MIN_PIPETTE_UL) to 0
    for col in VARIED_REAGENTS:
        if col in recs.columns:
            recs[col] = recs[col].where((recs[col] == 0) | (recs[col] >= MIN_PIPETTE_UL), 0.0)

    # Fill any missing reagent columns with 0
    for col in REAGENT_COLS:
        if col not in recs.columns:
            recs[col] = 0.0

    # base_media fills the remainder — no water added
    recs["cells"] = float(FIXED_CELLS_UL)
    recs["base_media_vol"] = (
        TOTAL_VOL_UL - FIXED_CELLS_UL - recs[VARIED_REAGENTS].sum(axis=1)
    ).round(1)
    recs["total"] = TOTAL_VOL_UL

    print(f"  Media distribution: {recs['base_media'].value_counts().to_dict()}")
    return recs.reset_index(drop=True)


# ── Output formatting ──────────────────────────────────────────────────────────

def format_output(
    proposals: pd.DataFrame,
    predicted: np.ndarray,
    round_num: int | None = None,
) -> pd.DataFrame:
    """
    Format proposals to match *_plate_condition_map.csv column order, sorted by
    predicted growth rate (descending), with an added predicted_growth_rate_per_hr
    column. Condition names are assigned after sorting (Rank-1, Rank-2, …).
    """
    prefix = f"R{round_num}-" if round_num else "Proposal-"
    n = len(proposals)
    out = pd.DataFrame({
        "condition":                    [f"{prefix}{i+1}" for i in range(n)],
        "base_media":                   proposals["base_media"].values,
        "base_media_vol":               proposals["base_media_vol"].values,
        "Yeast_extract":                proposals["Yeast_extract"].values,
        "MgSO4":                        proposals["MgSO4"].values,
        "K2HPO4":                       proposals["K2HPO4"].values,
        "NH4_2SO4":                     proposals["NH4_2SO4"].values,
        "MOPS":                         proposals["MOPS"].values,
        "Na_L_glut":                    proposals["Na_L_glut"].values,
        "Tryptone":                     proposals["Tryptone"].values,
        "cells":                        proposals["cells"].values,
        "total":                        proposals["total"].values,
        "predicted_growth_rate_per_hr": np.round(predicted, 4),
    })

    out = out.sort_values(
        "predicted_growth_rate_per_hr", ascending=False, na_position="last"
    ).reset_index(drop=True)

    # Re-number conditions by rank after sorting
    out["condition"] = [f"{prefix}{i+1}" for i in range(n)]

    return out


def to_json_formulations(output_df: pd.DataFrame, round_num: int | None = None, total_vol: float = TOTAL_VOL_UL) -> list[dict]:
    """
    Convert the formatted proposals DataFrame into the same JSON schema used by
    Elnora, with "Baybe-" prefix on every formulation name.

    Schema per formulation:
      id, name, base_medium, base_medium_volume_uL, total_volume_uL,
      components (array of name, stock_concentration, volume_uL, final_concentration)
    """
    formulations = []
    for i, row in output_df.iterrows():
        media = row["base_medium"] if "base_medium" in row.index else row["base_media"]
        abbrev = MEDIA_ABBREV.get(media, media.split()[0])

        # Build components from non-zero reagents
        components = []
        reagent_tags = []
        for col, meta in REAGENT_META.items():
            vol = float(row.get(col, 0.0))
            if vol <= 0:
                continue
            final = meta["stock_num"] * vol / total_vol
            unit = meta["unit"]
            if unit == "x":
                final_str = f"{final:.2f}x"
            elif unit == "mg/mL":
                final_str = f"{final:.2f} mg/mL"
            else:
                final_str = f"{final:.2f} mM"
            components.append({
                "name":                 meta["display"],
                "stock_concentration":  meta["stock_str"],
                "volume_uL":            round(vol, 1),
                "final_concentration":  final_str,
            })
            reagent_tags.append(col.replace("_", ""))

        # Auto-generate name: "Baybe-<MediaAbbrev>-<Reagent1>-<Reagent2>…"
        tag_str = "-".join(reagent_tags) if reagent_tags else "BaseOnly"
        name = f"Baybe-{abbrev}-{tag_str}"

        pred = row.get("predicted_growth_rate_per_hr", float("nan"))
        pred_val = None if (pred != pred) else round(float(pred), 4)  # NaN → null

        condition_id = f"B-F{i + 1}-R{round_num}" if round_num else f"B-F{i + 1}"
        formulations.append({
            "condition_id":                condition_id,
            "name":                        name,
            "base_medium":                 media,
            "base_medium_volume_uL":       round(float(row["base_media_vol"]), 1),
            "total_volume_uL":             total_vol,
            "predicted_growth_rate_per_hr": pred_val,
            "components":                  components,
        })

    return formulations


# ── Entry point ────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="BayBE Bayesian optimization for V. natriegens growth media",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--data-dir", default=str(Path(__file__).parent.parent / "data_baybe"),
        help="Directory containing *_growth.csv and *_plate_condition_map.csv files",
    )
    parser.add_argument(
        "--n-proposals", type=int, default=6,
        help="Total number of conditions to propose",
    )
    parser.add_argument(
        "--round", type=int, default=None,
        help="Round number used in condition name prefix (e.g. 3 → R3-1, R3-2, …)",
    )
    parser.add_argument(
        "--output", default=None,
        help="Output CSV path (default: output_baybe/next_round_plate_condition_map.csv)",
    )
    parser.add_argument(
        "--exclude-media", nargs="*", default=None,
        help=(
            "Base media names to exclude from campaign selection. "
            "Defaults to EXCLUDED_MEDIA constant (currently: Prepared LBv2 Media). "
            "Pass an empty list (--exclude-media) to disable all exclusions."
        ),
    )
    args = parser.parse_args()

    np.random.seed(RANDOM_SEED)

    # 1. Load historical data
    out_dir = Path(__file__).parent.parent / "output_baybe"
    print(f"Loading historical data from {args.data_dir!r} (JSONs from {out_dir}) ...")
    history = load_history(args.data_dir, json_dir=out_dir)
    if history.empty:
        print("  No historical data found — running in exploratory (random) mode.")
    else:
        print(f"  {len(history)} unique conditions across {history['base_media'].nunique()} media type(s)")
        print(f"  Growth rate range: {history[TARGET_COL].min():.3f} – {history[TARGET_COL].max():.3f} h⁻¹")

    # 2. Fit GP surrogate for annotating predicted growth rates
    predictor = GrowthRatePredictor()
    if len(history) >= 2:
        predictor.fit(history)
        print("  GP surrogate fitted.")
    else:
        print("  GP predictions will be NaN (no training data yet).")

    # 3. Run unified BayBE campaign
    exclude_media = set(args.exclude_media) if args.exclude_media is not None else None
    mode = "exploratory/random" if history.empty else "Bayesian"
    print(f"\nRunning unified BayBE campaign [{mode} mode] ({args.n_proposals} proposals, reagents: {VARIED_REAGENTS}) ...")
    proposals = propose_conditions(
        history,
        n_proposals=args.n_proposals,
        exclude_media=exclude_media,
    )

    # 4. Annotate with GP surrogate predictions
    predicted = predictor.predict(proposals) if predictor._fitted else np.full(len(proposals), np.nan)

    # 5. Format and save
    output_df = format_output(proposals, predicted, round_num=args.round)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    round_suffix = f"_round{args.round}" if args.round else ""
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / f"baybe_{timestamp}{round_suffix}.json"
    formulations = to_json_formulations(output_df, round_num=args.round)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(formulations, f, indent=2, ensure_ascii=False)

    print(f"\nSaved {len(output_df)} proposals → {json_path}")
    print("\nTop proposals:")
    display_cols = ["condition", "base_media", "base_media_vol", "predicted_growth_rate_per_hr"]
    print(output_df[display_cols].head(10).to_string(index=False))


if __name__ == "__main__":
    main()
