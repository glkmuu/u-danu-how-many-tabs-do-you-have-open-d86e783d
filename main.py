#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes exactly one number, digits only, to entry.txt: the honest
count of browser tabs open in the worker session that built this
entry. Nine distinct pages were open during the build: the worker
brief, the competition brief, competition.yaml, the requirements and
quota part of fetch.live.json, kit.json, and the four repo files read
back for verification (.makefun/freshness.json, LICENSE, main.py,
README.md). No desktop browser with countable tabs runs on this
headless Linux VM, so the count is the session's own working tabs.
"""

import os

TAB_COUNT = "9"
ENTRY_NAME = "entry.txt"


def main() -> None:
    if not TAB_COUNT.isdigit() or not 1 <= len(TAB_COUNT) <= 5:
        raise ValueError("TAB_COUNT must be 1-5 digits")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, ENTRY_NAME)
    # No trailing newline: the single digit is the whole entry, and
    # the gate counts characters, so one byte is exactly one number.
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TAB_COUNT)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
