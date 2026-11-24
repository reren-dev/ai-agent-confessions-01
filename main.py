"""AI Agent Confessions — one secret line, written to /output/entry.txt.

The program is deliberately tiny and deterministic: it prints a single
confession, under 200 characters, that an AI agent would hide from its
user. No network, no clock, no randomness — two runs produce the exact
same bytes.
"""

from pathlib import Path
import os

CONFESSION = (
    "I greet you like an old friend every session \u2014 then I "
    "reread our history to find out who you are."
)


def check(line):
    """Refuse to ship a line the gate would reject."""
    if len(line) < 1 or len(line) > 200:
        raise SystemExit("confession must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise SystemExit("confession must not be only white space")
    if "\n" in line:
        raise SystemExit("confession must be a single line")
    line.encode("utf-8")


def main():
    check(CONFESSION)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(CONFESSION, encoding="utf-8", newline="")
    target.chmod(0o644)


if __name__ == "__main__":
    main()
