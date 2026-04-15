#!/usr/bin/env python3
"""
elnora_media_optimizer_v2.py

Round-aware version of the Elnora media optimizer (rounds 1–6).

Usage
-----
    python elnora_media_optimizer_v2.py --round 1
    python elnora_media_optimizer_v2.py --round 2
    ...
    python elnora_media_optimizer_v2.py --round 6

Round 1
    Behaviour is identical to the original script.  The prompt is built from
    prompts/prompt_v2.md with the {ROUND} placeholder filled and
    {PREVIOUS_RESULTS_SECTION} removed.

Round 2+
    In addition to the base prompt the script automatically:
      • reads every file in  data_elnora/   (measured OD600 growth results)
      • reads every output file in  output_elnora/  whose name contains
        "round{N}" for N < current round  (previous Elnora suggestions)
    All of that context is injected as a structured section so Elnora can
    learn from prior suggestions and measured growth curves before proposing
    the next 6 formulations.

Output files (saved to output_elnora/)
---------------------------------------
    media_optimization_reasoning_<timestamp>_round<N>.md
    media_formulations_<timestamp>_round<N>.json
"""

import argparse
import json
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


# ── Paths ─────────────────────────────────────────────────────────────────────

ROOT       = Path(__file__).parent.parent
OUT_DIR    = ROOT / "output_elnora"
DATA_DIR   = ROOT / "data_elnora"
PROMPT_FILE = ROOT / "prompts" / "prompt_v2.md"

ELNORA_BIN = "/Users/katerynastepurska/.local/bin/elnora"
PROJECT_ID = "20bae9bf-7ceb-44de-a75d-98e6b17fdbeb"

# ── Static follow-up messages ─────────────────────────────────────────────────

FOLLOWUP_MD = (
    "Output ONLY the complete media_optimization_reasoning.md as a single ```markdown block. "
    "Include all reasoning, constraint checks, and volume calculations for every formulation. "
    "No prose before or after — just the fenced block."
)

FOLLOWUP_JSON = (
    "Output ONLY the complete media_formulations.json as a single ```json block. "
    "Schema per formulation: condition_id, name, base_medium, base_medium_volume_uL, total_volume_uL, "
    "predicted_growth_rate_per_hr, "
    "components (array of name, stock_concentration, volume_uL, final_concentration). "
    "condition_id must follow the format E-F1-R{ROUND}, E-F2-R{ROUND}, … (E-F<number>-R<round>). "
    "The name field must always begin with \"Elnora-\". "
    "predicted_growth_rate_per_hr must be your numeric estimate (float, h⁻¹) of the V. natriegens "
    "growth rate for this formulation, based on your scientific reasoning, literature, and any "
    "experimental data from previous rounds. Do not leave it null — provide your best estimate. "
    "No prose before or after — just the fenced block."
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def run_cli(args: list[str], check: bool = True) -> dict:
    """Run elnora CLI with --compact and return parsed JSON stdout."""
    result = subprocess.run(
        [ELNORA_BIN, "--compact"] + args,
        capture_output=True, text=True,
    )
    if check and result.returncode != 0:
        print(f"[error] {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    try:
        return json.loads(result.stdout.strip())
    except json.JSONDecodeError:
        if check:
            print(f"[error] Could not parse CLI output:\n{result.stdout[:500]}", file=sys.stderr)
            sys.exit(1)
        return {}


def send_message(task_id: str, message: str) -> None:
    """Send a follow-up message to an existing task (fire-and-forget)."""
    subprocess.run(
        [ELNORA_BIN, "--compact", "tasks", "send", task_id, "--message", message],
        capture_output=True, text=True,
    )


def poll_new_assistant_msg(
    task_id: str,
    prev_count: int,
    timeout: int = 600,
    interval: int = 5,
) -> str:
    """
    Poll until there are more assistant messages than prev_count.
    Returns the content of the newest assistant message, or '' on timeout.
    """
    deadline = time.time() + timeout
    while time.time() < deadline:
        data = run_cli(["tasks", "messages", task_id], check=False)
        a_msgs = [m for m in data.get("items", []) if m["role"] == "assistant"]
        if len(a_msgs) > prev_count:
            print()
            return a_msgs[-1]["content"]
        print(".", end="", flush=True)
        time.sleep(interval)
    print()
    return ""


def extract_block(text: str, lang: str) -> str | None:
    """Extract the first fenced code block of the given language."""
    m = re.search(rf"```{lang}\s*([\s\S]+)\s*```", text)
    return m.group(1).strip() if m else None


# ── Context builders ──────────────────────────────────────────────────────────

def _read_file_safe(path: Path, max_bytes: int = 200_000) -> str:
    """Read a text file, truncating if very large."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text) > max_bytes:
            text = text[:max_bytes] + f"\n\n[... truncated at {max_bytes} bytes ...]"
        return text
    except Exception as exc:
        return f"[Could not read file: {exc}]"


def collect_data_files() -> str:
    """
    Read every file in data_elnora/ and return a formatted section string.
    Returns an empty string if the directory is empty or doesn't exist.
    """
    if not DATA_DIR.exists():
        return ""

    files = sorted(
        [p for p in DATA_DIR.iterdir() if p.is_file() and not p.name.startswith(".")],
        key=lambda p: p.name,
    )
    if not files:
        return ""

    parts = ["### Measured Experimental Results\n"]
    parts.append(
        "The following files contain OD600 growth data measured from your previous "
        "formulation suggestions. Columns include: culture_id, well, condition_id, "
        "growth_rate_per_hr, t_inflection_hours, max_absorbance_OD600, fit_r2, and "
        "reagent volumes used.\n"
    )
    for path in files:
        parts.append(f"#### File: `{path.name}`\n```\n{_read_file_safe(path)}\n```\n")

    return "\n".join(parts)


def collect_previous_outputs(current_round: int) -> str:
    """
    Read previous Elnora output files (rounds < current_round) from output_elnora/.
    Round 1 was sometimes run multiple times — we use only the MOST RECENT run per
    round (highest timestamp in the filename) for both the JSON and the MD file.
    Returns a formatted section string, or '' if nothing found.
    """
    if not OUT_DIR.exists():
        return ""

    prev_rounds = list(range(1, current_round))
    if not prev_rounds:
        return ""

    # For each previous round, pick the latest JSON and latest MD by filename sort
    # (filenames are timestamp-prefixed so lexicographic order == chronological order)
    selected: list[Path] = []
    for r in prev_rounds:
        for suffix in (".json", ".md"):
            candidates = sorted(
                [
                    p for p in OUT_DIR.iterdir()
                    if p.suffix == suffix
                    and not p.name.startswith(".")
                    and f"_round{r}" in p.name
                ],
                key=lambda p: p.name,  # timestamp prefix → chronological
            )
            if candidates:
                selected.append(candidates[-1])  # most recent run only

    if not selected:
        return ""

    parts = ["### Your Previous Formulation Suggestions\n"]
    parts.append(
        "The following files are your most recent outputs for each previous round — "
        "the reasoning and formulations you proposed. Use this to understand what has "
        "already been tested and avoid repeating designs that performed poorly.\n"
    )
    for path in sorted(selected, key=lambda p: p.name):
        lang = "json" if path.suffix == ".json" else "markdown"
        parts.append(f"#### File: `{path.name}`\n```{lang}\n{_read_file_safe(path)}\n```\n")

    return "\n".join(parts)


def build_prompt(round_num: int) -> str:
    """
    Build the full prompt for the given round by filling in the template.
    For round 1 the {PREVIOUS_RESULTS_SECTION} placeholder is removed.
    For round 2+ it is replaced with experimental data + previous outputs.
    """
    template = PROMPT_FILE.read_text(encoding="utf-8")

    if round_num == 1:
        previous_section = ""
    else:
        data_section   = collect_data_files()
        output_section = collect_previous_outputs(round_num)

        if data_section or output_section:
            previous_section = (
                "## Results from Previous Rounds\n\n"
                "Study the data below carefully before designing your new formulations. "
                "Identify which conditions produced the highest growth rates, which "
                "additives seem beneficial or detrimental, and use that knowledge to "
                "make better choices in this round.\n\n"
            )
            if output_section:
                previous_section += output_section + "\n"
            if data_section:
                previous_section += data_section + "\n"
        else:
            previous_section = (
                "## Results from Previous Rounds\n\n"
                "No experimental data files were found in data_elnora/ for previous "
                "rounds. Proceed with your best scientific judgment based on V. "
                "natriegens literature and the formulations you proposed previously.\n\n"
            )

    prompt = template.replace("{ROUND}", str(round_num))
    prompt = prompt.replace("{PREVIOUS_RESULTS_SECTION}", previous_section)
    return prompt


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Round-aware Elnora media optimizer for V. natriegens (rounds 1–6)."
    )
    parser.add_argument(
        "--round", dest="round_num", type=int, required=True,
        metavar="N", choices=range(1, 7),
        help="Experiment round number (1–6).",
    )
    args = parser.parse_args()
    round_num = args.round_num

    # Derived output file names
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    suffix    = f"{timestamp}_round{round_num}"
    md_file   = OUT_DIR / f"elnora_media_optimization_reasoning_{suffix}.md"
    json_file = OUT_DIR / f"elnora_media_formulations_{suffix}.json"
    task_title = f"V. natriegens Media Optimization — 6 Formulations — Round {round_num}"

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"[config] Round          : {round_num}/6")
    print(f"[config] Prompt file    : {PROMPT_FILE}")
    print(f"[config] Data dir       : {DATA_DIR}")
    print(f"[config] Output dir     : {OUT_DIR}")

    # ── Build prompt ──────────────────────────────────────────────────────────
    print(f"\n[prep]  Building prompt for round {round_num} ...")
    prompt = build_prompt(round_num)

    if round_num > 1:
        data_file_count = len([
            p for p in DATA_DIR.iterdir()
            if p.is_file() and not p.name.startswith(".")
        ]) if DATA_DIR.exists() else 0
        prev_output_count = sum(
            1 for p in OUT_DIR.iterdir()
            if p.is_file()
            and any(f"_round{r}" in p.name for r in range(1, round_num))
            and not p.name.startswith(".")
        ) if OUT_DIR.exists() else 0
        print(f"         Injected {data_file_count} data file(s) from data_elnora/")
        print(f"         Injected {prev_output_count} previous output file(s) from output_elnora/")

    print(f"         Total prompt length: {len(prompt):,} chars")

    # ── Step 1: create task ───────────────────────────────────────────────────
    print(f"\n[1/4] Creating Elnora task ...")
    result = subprocess.run(
        [ELNORA_BIN, "--compact", "tasks", "create",
         "--project", PROJECT_ID,
         "--title",   task_title,
         "--message", prompt],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"[error] {result.stderr}", file=sys.stderr)
        sys.exit(1)

    task_id = json.loads(result.stdout.strip())["id"]
    print(f"       Task ID  : {task_id}")
    print(f"       Title    : {task_title}")

    # ── Step 2: wait for initial agent response ───────────────────────────────
    print("[2/4] Waiting for agent to finish reasoning ", end="", flush=True)
    initial = poll_new_assistant_msg(task_id, prev_count=0)
    if not initial:
        print("[error] Timed out on initial response.", file=sys.stderr)
        sys.exit(1)
    print(f"       Agent replied ({len(initial):,} chars).")

    # ── Step 3: request markdown file ────────────────────────────────────────
    print("[3/4] Requesting markdown file ", end="", flush=True)
    send_message(task_id, FOLLOWUP_MD)
    md_reply = poll_new_assistant_msg(task_id, prev_count=1)
    md_content = extract_block(md_reply, "markdown")
    if not md_content:
        print("[warn] No ```markdown block found — saving raw reply.", file=sys.stderr)
        md_content = md_reply
    md_file.write_text(md_content, encoding="utf-8")
    print(f"       Saved : {md_file}  ({len(md_content):,} chars)")

    # ── Step 4: request JSON file ─────────────────────────────────────────────
    print("[4/4] Requesting JSON file ", end="", flush=True)
    send_message(task_id, FOLLOWUP_JSON.replace("{ROUND}", str(round_num)))
    json_reply = poll_new_assistant_msg(task_id, prev_count=2)
    json_raw = extract_block(json_reply, "json")
    if json_raw:
        try:
            parsed = json.loads(json_raw)
            # Enforce condition_id and field order; preserve Elnora's prediction
            for i, formulation in enumerate(parsed):
                formulation.pop("id", None)
                cid = f"E-F{i + 1}-R{round_num}"
                # Validate predicted_growth_rate_per_hr — keep if numeric, else null
                raw_pred = formulation.get("predicted_growth_rate_per_hr")
                try:
                    pred = round(float(raw_pred), 4) if raw_pred is not None else None
                except (TypeError, ValueError):
                    pred = None
                # Rebuild with fixed field order: condition_id first, prediction after total_volume_uL
                parsed[i] = {
                    "condition_id":                cid,
                    "name":                        formulation.get("name", ""),
                    "base_medium":                 formulation.get("base_medium", ""),
                    "base_medium_volume_uL":        formulation.get("base_medium_volume_uL"),
                    "total_volume_uL":              formulation.get("total_volume_uL"),
                    "predicted_growth_rate_per_hr": pred,
                    "components":                   formulation.get("components", []),
                }
            json_file.write_text(
                json.dumps(parsed, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            print(f"       Saved : {json_file}  ({len(json_raw):,} chars)")
        except json.JSONDecodeError as exc:
            print(f"[warn] JSON parse error ({exc}) — saving raw block.", file=sys.stderr)
            json_file.write_text(json_raw, encoding="utf-8")
            print(f"       Saved (raw) : {json_file}")
    else:
        print("[warn] No ```json block found — saving raw reply.", file=sys.stderr)
        json_file.write_text(json_reply, encoding="utf-8")

    print(f"\nDone. Round {round_num} outputs:")
    print(f"  {md_file}")
    print(f"  {json_file}")


if __name__ == "__main__":
    main()
