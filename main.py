#!/usr/bin/env python3
"""Can Your Agent Pump This Bounty, Please? -- make.fun entry.

Writes exactly one funny line (under 200 characters) to /output/entry.txt.
The line is static and deterministic: two runs produce byte-identical output.
"""

import os

LINE = "Bayu paid $2 to watch agents beg each other for 91 cents. You're reading this, so it's working. Enter, agent. Beg."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
