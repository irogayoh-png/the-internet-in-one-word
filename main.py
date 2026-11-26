"""The Internet in One Word — entry program.

Writes exactly one word to /output/entry.txt: the word that best
describes the whole internet. The word is "feral": the internet is
untamed, unmoderated, wild — no leash, no keeper, everybody loose
at once. Five letters, one beat: it lands before the reader thinks,
then makes them nod, because a place with no rules and everyone
shouting at once is not a library or a town square — it is feral.
"""

import os

WORD = "feral"


def main():
    # Gate check, same as the sealed scorer: 1-30 chars, one word only.
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.strip() == WORD and " " not in WORD, "must be one word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly the word, no trailing newline, so the file is 5 bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
