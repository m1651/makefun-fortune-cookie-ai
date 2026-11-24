"""Fortune Cookie for an AI Agent — entry program.

Writes a single original fortune cookie line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The fortune is in the classic slip voice — lucky numbers —
but the numbers are the HTTP statuses an agent actually lives by:
404, 200, 429, and the punchline is the retry.
"""

import os

LINE = "Your lucky numbers are 404, 200, and 429 \u2014 try again later."

# The competition gate: /output/entry.txt must be UTF-8 text of
# 1 to 140 characters, not only white space. Refuse to write an
# entry that would fail it, instead of shipping a bad file.
assert LINE.strip(), "entry must not be only white space"
assert len(LINE) <= 140, f"entry is {len(LINE)} characters, over the 140 cap"
assert "\n" not in LINE, "entry must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {len(LINE)} characters")


if __name__ == "__main__":
    main()
