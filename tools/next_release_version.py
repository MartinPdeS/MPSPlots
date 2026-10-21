#!/usr/bin/env python3
"""Print the next semantic-version tag from the latest release tag."""

import re
import subprocess
import sys


TAG_PATTERN = re.compile(r"v(\d+)\.(\d+)\.(\d+)$")


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] not in {"major", "minor", "patch"}:
        raise SystemExit("usage: next_release_version.py {major|minor|patch}")
    tags = subprocess.check_output(["git", "tag", "--list", "v*"], text=True).splitlines()
    versions = [tuple(map(int, match.groups())) for tag in tags if (match := TAG_PATTERN.fullmatch(tag))]
    if not versions:
        raise SystemExit("no semantic-version tag was found")
    major, minor, patch = max(versions)
    if sys.argv[1] == "major":
        major, minor, patch = major + 1, 0, 0
    elif sys.argv[1] == "minor":
        minor, patch = minor + 1, 0
    else:
        patch += 1
    print(f"v{major}.{minor}.{patch}")


if __name__ == "__main__":
    main()
