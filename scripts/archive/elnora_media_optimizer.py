#!/usr/bin/env python3
"""
elnora_media_optimizer.py

Sends the V. natriegens media optimization prompt to Elnora,
waits for the agent's response, then saves:
  - media_optimization_reasoning.md
  - media_formulations.json

Strategy
--------
1. Create the task with the full science prompt (no --wait, avoids 120s CLI timeout).
2. Poll until the agent replies.
3. Send a follow-up asking ONLY for the markdown file content in a fenced block.
4. Send another follow-up asking ONLY for the JSON file content in a fenced block.
   (Two separate messages avoid the ~12 KB per-message truncation limit.)
5. Parse both blocks and write the files.
"""

import json
import re
import subprocess
import sys
import time
from pathlib import Path
from datetime import datetime


# ── Config ────────────────────────────────────────────────────────────────────

ELNORA_BIN = "/Users/katerynastepurska/.local/bin/elnora"
PROJECT_ID = "20bae9bf-7ceb-44de-a75d-98e6b17fdbeb"
TASK_TITLE = "V. natriegens Media Optimization — 6 Formulations"
OUT_DIR    = Path(__file__).parent.parent/ "output_elnora"
ROUND      = 1

# Timestamp + round stamped at import time so both files share the same prefix
_TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
_SUFFIX    = f"{_TIMESTAMP}_round{ROUND}"
MD_FILE    = OUT_DIR / f"media_optimization_reasoning_{_SUFFIX}.md"
JSON_FILE  = OUT_DIR / f"media_formulations_{_SUFFIX}.json"

PROMPT_FILE = Path(__file__).parent.parent/"prompts"/ "prompt.md"
PROMPT = PROMPT_FILE.read_text(encoding="utf-8")

FOLLOWUP_MD = (
    "Output ONLY the complete media_optimization_reasoning.md as a single ```markdown block. "
    "Include all reasoning, constraint checks, and volume calculations for every formulation. "
    "No prose before or after — just the fenced block."
)

FOLLOWUP_JSON = (
    "Output ONLY the complete media_formulations.json as a single ```json block. "
    "Schema per formulation: id, name, base_medium, base_medium_volume_uL, total_volume_uL, "
    "components (array of name, stock_concentration, volume_uL, final_concentration). "
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
    """Extract the first fenced code block of the given language. Returns content or None."""
    # Use a greedy match so the last ``` closes the block (handles nested backticks)
    m = re.search(rf"```{lang}\s*([\s\S]+)\s*```", text)
    return m.group(1).strip() if m else None


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    # ── Step 1: create task ───────────────────────────────────────────────────
    print(f"[1/4] Creating Elnora task ...")
    result = subprocess.run(
        [ELNORA_BIN, "--compact", "tasks", "create",
         "--project", PROJECT_ID,
         "--title",   TASK_TITLE,
         "--message", PROMPT],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"[error] {result.stderr}", file=sys.stderr)
        sys.exit(1)

    task_id = json.loads(result.stdout.strip())["id"]
    print(f"      Task ID : {task_id}")

    # ── Step 2: wait for initial agent response ───────────────────────────────
    print("[2/4] Waiting for agent to finish reasoning ", end="", flush=True)
    initial = poll_new_assistant_msg(task_id, prev_count=0)
    if not initial:
        print("[error] Timed out on initial response.", file=sys.stderr)
        sys.exit(1)
    print(f"      Agent replied ({len(initial)} chars).")

    # ── Step 3: request markdown file ────────────────────────────────────────
    print("[3/4] Requesting markdown file ", end="", flush=True)
    send_message(task_id, FOLLOWUP_MD)
    md_reply = poll_new_assistant_msg(task_id, prev_count=1)
    md_content = extract_block(md_reply, "markdown")
    if not md_content:
        print("[warn] No ```markdown block found — saving raw reply.", file=sys.stderr)
        md_content = md_reply
    MD_FILE.write_text(md_content, encoding="utf-8")
    print(f"      Saved : {MD_FILE}  ({len(md_content):,} chars)")

    # ── Step 4: request JSON file ─────────────────────────────────────────────
    print("[4/4] Requesting JSON file ", end="", flush=True)
    send_message(task_id, FOLLOWUP_JSON)
    json_reply = poll_new_assistant_msg(task_id, prev_count=2)
    json_raw = extract_block(json_reply, "json")
    if json_raw:
        try:
            parsed = json.loads(json_raw)
            JSON_FILE.write_text(
                json.dumps(parsed, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            print(f"      Saved : {JSON_FILE}  ({len(json_raw):,} chars)")
        except json.JSONDecodeError as exc:
            print(f"[warn] JSON parse error ({exc}) — saving raw block.", file=sys.stderr)
            JSON_FILE.write_text(json_raw, encoding="utf-8")
            print(f"      Saved (raw) : {JSON_FILE}")
    else:
        print("[warn] No ```json block found — saving raw reply.", file=sys.stderr)
        JSON_FILE.write_text(json_reply, encoding="utf-8")

    print("\nDone.")


if __name__ == "__main__":
    main()
