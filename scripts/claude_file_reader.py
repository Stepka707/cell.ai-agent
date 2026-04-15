#!/usr/local/opt/python@3.11/bin/python3.11
"""
claude_file_reader.py

A simple Claude agent that reads one or more files and answers questions about them.

Usage:
    python claude_file_reader.py file1.txt file2.csv
    python claude_file_reader.py file1.txt --prompt "Summarize the key findings"
    python claude_file_reader.py file1.txt --interactive
"""

import argparse
import os
import sys
from pathlib import Path

import anthropic

# ── Config ────────────────────────────────────────────────────────────────────

MODEL = "claude-opus-4-6"
MAX_TOKENS = 16000
MAX_FILE_SIZE_BYTES = 1 * 1024 * 1024  # 1 MB per file

# ── Helpers ───────────────────────────────────────────────────────────────────


def read_file(path: Path) -> str:
    """Read a file and return its contents as a string."""
    if not path.exists():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    size = path.stat().st_size
    if size > MAX_FILE_SIZE_BYTES:
        print(
            f"Warning: {path.name} is {size // 1024} KB — truncating to 1 MB",
            file=sys.stderr,
        )

    with open(path, "r", errors="replace") as f:
        return f.read(MAX_FILE_SIZE_BYTES)


def build_system_prompt(file_names: list[str]) -> str:
    return (
        "You are a helpful data and document analysis assistant. "
        "The user has provided the following file(s) for you to read and analyse: "
        + ", ".join(file_names)
        + ". Answer questions accurately based on the file contents. "
        "When referencing specific data, cite the file name."
    )


def build_user_message(files: dict[str, str], prompt: str) -> str:
    """Combine file contents and the user's question into a single message."""
    parts = []
    for name, content in files.items():
        parts.append(f"<file name=\"{name}\">\n{content}\n</file>")
    parts.append(prompt)
    return "\n\n".join(parts)


def call_claude(client: anthropic.Anthropic, system: str, messages: list) -> str:
    """Call Claude and return the text response."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=system,
        messages=messages,
    )
    for block in response.content:
        if block.type == "text":
            return block.text
    return ""


# ── Main ──────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Claude agent that reads files and answers questions about them."
    )
    parser.add_argument("files", nargs="+", help="One or more file paths to read")
    parser.add_argument(
        "--prompt",
        default="Please summarise the contents of the provided file(s) and highlight any key insights.",
        help="Question or instruction for Claude (default: summarise)",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Start an interactive multi-turn chat session after the first response",
    )
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Load files
    file_contents: dict[str, str] = {}
    for raw_path in args.files:
        path = Path(raw_path)
        file_contents[path.name] = read_file(path)
        print(f"Loaded: {path.name} ({len(file_contents[path.name])} chars)")

    system = build_system_prompt(list(file_contents.keys()))

    # First turn — file contents + initial prompt
    first_message = build_user_message(file_contents, args.prompt)
    messages = [{"role": "user", "content": first_message}]

    print(f"\nPrompt: {args.prompt}\n")
    print("─" * 60)

    reply = call_claude(client, system, messages)
    print(reply)

    if not args.interactive:
        return

    # Interactive loop
    messages.append({"role": "assistant", "content": reply})

    print("\n─" * 60)
    print("Interactive mode — type your question, or 'quit' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if user_input.lower() in {"quit", "exit", "q"}:
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})
        reply = call_claude(client, system, messages)
        print(f"\nClaude: {reply}\n")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
