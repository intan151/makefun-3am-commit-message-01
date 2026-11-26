#!/usr/bin/env python3
"""The 3AM Commit Message.

Writes one line — the funniest git commit message an AI coding agent
types at 3am after a long night of fixing its own bugs — to
/output/entry.txt (or ./output/entry.txt when run locally).

Deterministic: the same entry on every run. Stdlib only, no network,
no randomness, no input files.

The joke: the agent finally finds the bug after a whole night, and the
bug is itself — a confession told as a timeline (midnight -> 1am ->
2am -> 3am), each hour a worse decision than the last, ending exactly
where the night started: still awake, still at 3am.
"""

import os
from pathlib import Path

ENTRY = (
    "fix: the bug was me all along \u2014 I wrote it at midnight, "
    "denied it at 1am, fixed the wrong file at 2am, and now it is 3am"
)


def self_check(entry: str) -> None:
    """Gate: mirror of the sealed scorer — 1..139 chars, UTF-8, one line,
    not only whitespace, no leading/trailing space."""
    assert isinstance(entry, str)
    entry.encode("utf-8")  # must be valid UTF-8 text
    assert 1 <= len(entry) <= 139, f"entry length {len(entry)} outside 1..139"
    assert entry.strip(), "entry must not be only whitespace"
    assert "\n" not in entry and "\r" not in entry, "entry must be one line"
    assert entry == entry.strip(), "entry must not have leading/trailing space"


def main() -> None:
    self_check(ENTRY)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    if not out_dir.is_dir():
        out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    # Read back: the file on disk must be exactly the entry, nothing else.
    assert out_path.read_text(encoding="utf-8") == ENTRY, \
        "entry.txt does not match the entry"
    print(f"wrote {out_path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
