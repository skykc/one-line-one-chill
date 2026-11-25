#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt. The line is a fixed string: the scare lives in one
concrete detail (a child's family drawing) whose last clause reframes
everything before it.
"""

import os

LINE = (
    "My daughter's drawing of our family has four stick figures, "
    "and the fifth one, holding her hand, has my face."
)

# The judge names these images as played-out cliches; the line must earn
# its scare from one concrete detail instead, so refuse to ship if any
# of them ever creeps into the text.
CLICHE_WORDS = ("mirror", "doll", "basement", "ghost", "demon", "blood")


def validate(text: str) -> None:
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1, "entry must be a single sentence"
    assert text == text.strip(), "entry must not start or end with whitespace"
    lowered = text.lower()
    for word in CLICHE_WORDS:
        assert word not in lowered, f"entry leans on the cliche {word!r}"
    assert "\n" not in text, "entry must be a single line"


def main() -> None:
    text = LINE.strip()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
