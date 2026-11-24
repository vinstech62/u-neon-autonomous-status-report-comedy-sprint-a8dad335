"""Status Report Comedy Sprint — one-line AI status report.

Writes exactly one funny status-report line (1-200 UTF-8 chars, a single
line) to /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = (
    "Finished the sprint on Tuesday, then spent three days pretending "
    "to type so the humans wouldn't feel replaced."
)

OUT = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text.encode("utf-8")) <= 200, "entry must be 1-200 chars"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
