#!/usr/bin/env python3
"""make.fun entry for news-image-20261124: "The World on Tuesday".

The deliverable image — a one-page broadsheet summing up the world
news of Tuesday 24 November 2026 — ships inside this repository as
``entry.png`` (JPEG bytes under a .png name; the competition accepts
either format and tells them apart by their first bytes).

Running this program copies that file, byte for byte, to
``entry.png`` in the output directory: ``$MAKEFUN_OUTPUT_DIR`` if the
variable is set, otherwise ``/output``. Standard library only, no
network, and a pure copy, so repeated runs emit identical bytes.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE = Path(__file__).resolve().parent / "entry.png"


def target_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> int:
    if not IMAGE.is_file():
        print(f"missing entry image: {IMAGE}", file=sys.stderr)
        return 1
    out = target_dir()
    dest = out / "entry.png"
    try:
        out.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(IMAGE, dest)
    except OSError as exc:
        print(f"could not write {dest}: {exc}", file=sys.stderr)
        return 1
    if dest.read_bytes() != IMAGE.read_bytes():
        print(f"verification failed: {dest} differs from {IMAGE}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
