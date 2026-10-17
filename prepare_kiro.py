#!/usr/bin/env python3
"""Expand the verified handoff package without network access or overwrites."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import stat
import zipfile

ROOT = Path(__file__).resolve().parent
ARCHIVE = ROOT / "tongpin-kit-v0.2.zip"
EXPECTED_SHA256 = "de160af0163be72f15c8ba3329b45deb64364306c2305dba1e3f4bbe60ffbee7"
PREFIX = "tongpin-kiro-kit"


def main():
    actual = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA256:
        raise SystemExit("Archive checksum mismatch; no files were written.")
    planned = []
    destinations = set()
    with zipfile.ZipFile(ARCHIVE) as archive:
        infos = archive.infolist()
        if len(infos) != 90 or sum(info.file_size for info in infos) > 20_000_000:
            raise SystemExit("Unexpected archive contents; no files were written.")
        for info in infos:
            path = PurePosixPath(info.filename)
            if (path.is_absolute() or len(path.parts) < 2 or path.parts[0] != PREFIX
                    or ".." in path.parts or "\\" in info.filename
                    or stat.S_ISLNK(info.external_attr >> 16) or info.is_dir()):
                raise SystemExit("Unsafe or unexpected archive path.")
            relative = Path(*path.parts[1:])
            if relative == Path("README.md"):
                relative = Path("docs/KIT_README.md")
            destination = ROOT / relative
            if destination in destinations:
                raise SystemExit("Duplicate archive destination.")
            destinations.add(destination)
            for part in [destination, *destination.parents]:
                if part == ROOT:
                    break
                if part.is_symlink():
                    raise SystemExit("Refusing a symbolic-link destination.")
                if part != destination and part.exists() and not part.is_dir():
                    raise SystemExit("Destination parent is not a directory.")
            data = archive.read(info)
            if destination.exists() and (not destination.is_file() or destination.read_bytes() != data):
                raise SystemExit("Existing file differs: " + str(relative) + "; no files were written.")
            planned.append((destination, data))
    written = 0
    for destination, data in planned:
        if not destination.exists():
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open("xb") as output:
                output.write(data)
            written += 1
    print(json.dumps({"status": "ready", "verified_files": len(planned),
                      "new_files": written, "next": "Read .kiro/ and docs/; develop in kiro-app/."}))


if __name__ == "__main__":
    main()
