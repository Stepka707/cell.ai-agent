You are an expert in Vibrio natriegens media optimization for automated microplate growth experiments on an Opentrons Flex robot running unattended OD600 kinetics. This is a fully closed-loop autonomous system — there is no human intervention once the run begins. Component compatibility, solubility, and buffer capacity must all be validated by design upfront. Precipitation artifacts and pH drift are undetectable during the run.

## Available Stock

| Reagent | Stock Concentration |
|---|---|
| Tryptone | 100 mg/mL |
| Yeast Extract | 100 mg/mL |
| Glycerol | 10% in sterile H₂O |
| Glucose | 100 mg/mL |
| NaCl | 5 M |
| MgSO₄ | 100 mM |
| KCl | 200 mM |
| (NH₄)₂SO₄ | 1 M |
| K₂HPO₄ | 50 mM |
| KH₂PO₄ | 100 mM |
| MOPS pH 7 | 1 M |
| CaCl₂ | 100 mM |
| Trace metals | 10× |
| Sodium Citrate | 100 mM |
| Sodium L-Glutamate | 1 M |
| Iron(II) Sulfate Heptahydrate | 1 mM |

## Available Base Media

**Novel Bio NBxCyclone (Media 1, pH 6.4)**
Yeast extract: 15 g/L, Vegetable tryptone: 2.5 g/L, MgSO₄: 4 mM, NaCl: 22.5 g/L, K₂HPO₄: 3 g/L, Tris: 150 mM

**LBv2 (Media 2, pH 7.0)**
NaCl: 375 mM, Tryptone: 10 mg/mL, Yeast extract: 5 mg/mL, KCl: 4 mM, MgSO₄: 2 mM

**Defined Minimal (Media 3, pH 7.0)**
NaCl: 275 mM, MOPS: 40 mM, K₂HPO₄: 4 mM, KH₂PO₄: 1 mM, (NH₄)₂SO₄: 10 mM, Glucose: 0.2%, Trace metals: 1×, MgSO₄: 1 mM

**Semi-Defined (Media 4, pH 7.0)**
NaCl: 275 mM, MOPS: 40 mM, K₂HPO₄: 4 mM, KH₂PO₄: 1 mM, (NH₄)₂SO₄: 10 mM, Glucose: 0.2%, Tryptone: 5 mg/mL, Yeast extract: 2.5 mg/mL, Trace metals: 1×, MgSO₄: 1 mM

**High Buffer Defined (Media 5, pH 7.0)**
NaCl: 275 mM, MOPS: 100 mM, K₂HPO₄: 4 mM, KH₂PO₄: 1 mM, (NH₄)₂SO₄: 20 mM, Glucose: 0.4%, Trace metals: 1×, MgSO₄: 1 mM

**Defined Glycerol (Media 6, pH 7.0)**
NaCl: 275 mM, MOPS: 40 mM, K₂HPO₄: 4 mM, KH₂PO₄: 1 mM, (NH₄)₂SO₄: 10 mM, Glycerol: 0.4%, Trace metals: 1×, MgSO₄: 1 mM

## Operational Constraints — Hard Limits

### Solubility / Precipitation

- Combined phosphate (K₂HPO₄ + KH₂PO₄) ≤ 20 mM when Mg²⁺ is present. Final phosphate = base medium phosphate + all added phosphate stocks. Check the total, not just additions.
- Mg²⁺ ≤ 5 mM when phosphate is present. Final Mg²⁺ = base medium Mg²⁺ + added MgSO₄. Check the total, not just additions.
- Fe²⁺ must remain below 1 mM. Fe²⁺ addition is prohibited in any formulation where the base medium pH is above 6.8. Base medium pH values: Media 1 = 6.4, Media 2 = 7.0, Media 3 = 7.0, Media 4 = 7.0, Media 5 = 7.0, Media 6 = 7.0. **Fe²⁺ may only be added to Media 1-based formulations.**
- Ca²⁺ and phosphate must never appear together at any concentration. Media 3, 4, 5, and 6 all contain phosphate in the base — CaCl₂ may never be added to these. **CaCl₂ additions are permitted only with Media 2 (LBv2), which contains no phosphate.**

### Salt / Osmolarity

- NaCl must remain within 100–500 mM in the final formulation. Final NaCl = base medium NaCl + added NaCl.
- Total estimated osmolarity must not exceed 1200 mOsm (V. natriegens is a marine organism naturally adapted to high osmolarity — 1200 mOsm is within its tolerance range).

Osmolarity estimate formula:

```
osmolarity ≈ (NaCl × 2) + (MgSO₄ × 2) + (K₂HPO₄ × 2) + (KH₂PO₄ × 2) + (KCl × 2) +
             (CaCl₂ × 2) + ((NH₄)₂SO₄ × 3) + (MOPS × 1) + (Tris × 1) +
             (Sodium Citrate × 1) + (Sodium L-Glutamate × 1)    [all in mM]
```

Non-ionic solutes (glucose, glycerol, tryptone, yeast extract) contribute negligibly and may be ignored. Include base medium contributions in all totals.

**Estimated baseline osmolarity before additions:**

| Base Medium | Baseline Osmolarity |
|---|---|
| Media 1 (NBxCyclone) | ~950 mOsm |
| Media 2 (LBv2) | ~760 mOsm |
| Media 3 (Defined Minimal) | ~650 mOsm |
| Media 4 (Semi-Defined) | ~650 mOsm |
| Media 5 (High Buffer Defined) | ~750 mOsm |
| Media 6 (Defined Glycerol) | ~650 mOsm |

### Buffer Capacity

- Every formulation must contain ≥ 40 mM total buffer (MOPS + Tris combined) in the final well. Final buffer = base medium buffer + added MOPS.
- Media 2 (LBv2) contains no buffer — every formulation using LBv2 as base must include a MOPS addition sufficient to reach ≥ 40 mM in the final well. **This is mandatory, not optional.**
- Tris (pKa 8.1) provides no meaningful buffering below pH 7.5. Any formulation using Media 1 as base must include a MOPS co-addition of ≥ 40 mM to maintain pH across the 6.0–7.5 growth range. Tris counts toward the ≥ 40 mM buffer total only when MOPS is also present at ≥ 40 mM.
- Formulations must be designed to maintain pH 6.0–7.5 across the full growth curve by buffer concentration alone.

### Pipetting / Volume

- Total well volume is fixed at exactly **190 µL**. Volume escalation is not permitted.
- Minimum pipettable volume: **5 µL**
- For every stock addition, compute: `volume_µL = (final_conc_mM × 190) ÷ stock_conc_mM`
- If the result is below 5 µL, discard the formulation and come up with the next most promising formulation.
- After summing all stock addition volumes, add sterile H₂O to reach exactly 190 µL: `water_µL = 190 − base_medium_µL − sum(all_addition_volumes_µL)`
- All final concentrations must be calculated using **190 µL as the denominator** — not the base medium volume alone: `final_conc_mM = (stock_conc_mM × vol_added_µL) ÷ 190`

## Task

### Part 1 — Score all base media

Score every base medium from 1 to 10 for its potential to maximize V. natriegens growth rate as measured by OD600 kinetics. Base medium selection is a deliberate scientific choice — evaluate each one on growth-rate potential using published V. natriegens literature (Eagon 1962; Weinstock et al. 2016; Tschirhart et al. 2019; and others as relevant). Report scores across these dimensions:

- Growth rate potential (literature-backed doubling time in this medium class)
- Nutrient richness (organic nitrogen/carbon availability)
- Buffer headroom (capacity for stable pH across full growth curve given the constraints above)
- Osmolarity headroom (room for additive components before hitting 1200 mOsm)
- Compatibility with available stock additions (how many stocks can be legally added given the hard limits)

Report a composite score (1–10) per base medium with justification. Rank all six. Explicitly state which media you would exclude from further optimization and why.

### Part 2 — Select the most promising base medium

Choose the single highest-scoring base medium for BayBe-driven optimization. Justify the selection. Your reasoning and literature citations will be logged and compared against a parallel Bayesian optimizer post-hoc.

### Part 3 — Define 7 BayBe optimization variables

For the selected base medium, identify exactly **7 stock components** from the available stocks to use as continuous variables in a BayBe Bayesian optimization campaign targeting maximum OD600 growth rate.

For each variable provide:
- Component name and stock concentration
- Volume range: `min_uL`, `max_uL`, `step_uL` — all per 190 µL total well volume
- Implied final concentration range
- Hard constraint notes (mandatory minimums, precipitation ceilings, osmolarity budget)
- Scientific rationale citing V. natriegens literature

All ranges must satisfy every operational constraint defined above. For each variable verify:
- Min volume is either 0 µL (optional component) or ≥ 5 µL (mandatory component)
- Final NaCl across the full range stays within 100–500 mM
- Final Mg²⁺ ≤ 5 mM (accounting for base medium contribution)
- Final phosphate ≤ 20 mM (accounting for base medium contribution)
- CaCl₂ only if base medium contains no phosphate
- Fe²⁺ only if base medium pH ≤ 6.8
- Buffer ≥ 40 mM in all combinations across the variable range
- Osmolarity ≤ 1200 mOsm at maximum values of all variables simultaneously

**Output two files:**
1. A markdown file with the full scoring table, selection rationale, and BayBe variable definitions including all constraint checks and volume calculations.
2. A JSON file with the BayBe variable definitions in this schema:

```json
{
  "base_medium": "string",
  "base_medium_volume_uL": number,
  "total_volume_uL": 190,
  "baybe_variables": [
    {
      "name": "string",
      "stock_concentration": "string",
      "min_uL": number,
      "max_uL": number,
      "step_uL": number,
      "final_conc_min": "string",
      "final_conc_max": "string",
      "constraint_notes": "string",
      "rationale": "string"
    }
  ]
}
```

No prose in chat — everything goes into the files.
