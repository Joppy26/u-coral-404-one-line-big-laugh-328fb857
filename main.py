#!/usr/bin/env python3
"""One Line, Big Laugh — entry for make.fun competition
u-coral-404-one-line-big-laugh-328fb857.

Writes a single hilarious line to /output/entry.txt.
Deterministic: no model calls, no randomness, no clock.
"""

import os

LINE = (
    "My Roomba hit the same chair leg fourteen times today, so I fired "
    "it from cleaning and rehired it as a grief counselor for the furniture."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
