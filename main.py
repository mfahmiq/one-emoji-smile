"""Write exactly one emoji to /output/entry.txt.

The emoji: heart hands (U+1FAF6). Warm, friendly, universal, and chosen
rather than the default smiley -- the kind of warmth a stranger reads at a
glance and smiles back at. Stdlib only, no network, deterministic: the
same bytes on every run. The entry must be exactly one emoji and nothing
else, so the file holds the emoji with no trailing newline.
"""

import os

EMOJI = "🫶"

assert len(EMOJI) == 1, "entry must be exactly one emoji"
assert EMOJI.strip(), "entry must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
