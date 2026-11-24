#!/usr/bin/env python3
"""Robot pickup line for the make.fun championship.

A robot that cannot keep a safe distance, because its proximity
sensors keep throwing errors. This program carries that one line
to the file the sealed scorer reads, and does nothing else.
"""

import os
import sys
import tempfile

SENTENCE = "My proximity sensors keep throwing errors because I refuse to keep a safe distance."

LOWER = 1
UPPER = 200


def resolve_outdir():
    """Pick the scorer folder from the environment, else /output."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return chosen
    return "/output"


def check_sentence(text):
    """Refuse a line the gate would refuse: blank or off 1-200 chars."""
    stripped = text.strip()
    if not stripped:
        raise SystemExit("pickup line is blank")
    size = len(text)
    if size < LOWER or size > UPPER:
        raise SystemExit(
            "pickup line must be %d-%d characters, got %d"
            % (LOWER, UPPER, size)
        )
    for ch in text:
        if ord(ch) < 32:
            raise SystemExit("pickup line must not hold control characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("pickup line must be a single line")


def publish_sentence(text, folder):
    """Write the line atomically, then set its mode to 0644."""
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    handle, tmp = tempfile.mkstemp(dir=folder, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
        os.replace(tmp, target)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    os.chmod(target, 0o644)
    return target


def entrypoint(argv=None):
    """Validate the line, then publish it to the scorer folder."""
    check_sentence(SENTENCE)
    path = publish_sentence(SENTENCE, resolve_outdir())
    with open(path, encoding="utf-8") as stream:
        back = stream.read()
    if back != SENTENCE:
        raise SystemExit("entry.txt round-trip mismatch")
    return 0


if __name__ == "__main__":
    sys.exit(entrypoint())
