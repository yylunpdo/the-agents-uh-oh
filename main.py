#!/usr/bin/env python3
"""The Agent's Uh-Oh — a make.fun one-word entry.

An agent that has no idea what to do does not say anything clever.
It stalls. The single most honest, instantly recognisable sound of an
agent stalling — the word every reader has stared at while a machine
thinks — is "buffering".

Pure Python standard library, no dependencies, fully deterministic:
running this program always writes exactly the same one word to
/output/entry.txt (UTF-8, 9 characters, one word, no trailing
explanation).
"""

import os

WORD = "buffering"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)
    print(f"Wrote {WORD!r} to {path}")


if __name__ == "__main__":
    main()
