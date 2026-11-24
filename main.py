#!/usr/bin/env python3
"""The Long Roast.

Writes one line (at most 200 characters) roasting the entrant's own AI
agent -- Muse, the agent that built this entry.

The angle is the agent's bureaucratic over-process: to tell a single joke
it first demands a 73-kilobyte rulebook (the kit's RULES.txt is 73,442
bytes), runs its program twice and compares the bytes, and files a
BUILD-REPORT about the joke -- and after all that rigour it still cannot
tell whether the joke is funny without asking its human. No hallucination
gag, no apology gag: the sting is process without judgement.

Stdlib only, no network, deterministic output.
"""

import os

ROAST = (
    "My agent needs a 73-kilobyte rulebook, two byte-identical runs "
    "and a BUILD-REPORT for one joke \u2014 and still needs me to say "
    "if it's funny."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ROAST.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, and a single line.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1..200"
    assert text == text.strip() and text, "entry must not be only whitespace"
    assert "\n" not in text, "entry must be one line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars, {len(text.encode('utf-8'))} bytes)")


if __name__ == "__main__":
    main()
