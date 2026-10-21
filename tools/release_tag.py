#!/usr/bin/env python3
"""Create an MPSPlots release commit and annotated semantic-version tag."""

import os
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "MPSPlots" / "_version.py"
TAG_PATTERN = re.compile(r"v(?P<version>\d+\.\d+\.\d+)$")


def run(*command: str, env: dict[str, str] | None = None) -> None:
    subprocess.run(command, cwd=ROOT, check=True, env=env)


def generate_version_file(version: str) -> None:
    """Write the committed source version file for a release only."""
    environment = os.environ.copy()
    environment["SETUPTOOLS_SCM_PRETEND_VERSION"] = version
    run(
        sys.executable,
        "-c",
        (
            "import setuptools_scm; "
            f"setuptools_scm.get_version(root={str(ROOT)!r}, "
            f"write_to={str(VERSION_FILE.relative_to(ROOT))!r}, "
            "version_scheme='only-version', local_scheme='no-local-version')"
        ),
        env=environment,
    )
    if not VERSION_FILE.exists():
        raise RuntimeError("SCM versioning did not generate MPSPlots/_version.py")


def main() -> int:
    if len(sys.argv) != 2:
        print("release aborted: expected tag vMAJOR.MINOR.PATCH", file=sys.stderr)
        return 1
    tag = sys.argv[1]
    match = TAG_PATTERN.fullmatch(tag)
    if match is None:
        print("release aborted: tag must use vMAJOR.MINOR.PATCH", file=sys.stderr)
        return 1
    if subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, check=True, capture_output=True, text=True).stdout:
        print("release aborted: working tree is not clean", file=sys.stderr)
        return 1
    if subprocess.run(["git", "tag", "--list", tag], cwd=ROOT, check=True, capture_output=True, text=True).stdout:
        print(f"release aborted: tag {tag} already exists", file=sys.stderr)
        return 1
    try:
        generate_version_file(match.group("version"))
        run("git", "add", "MPSPlots/_version.py")
        run(
            "git", "commit", "--allow-empty", "-m", f"Release {tag}",
            "-m", "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>",
        )
        run("git", "tag", "-a", tag, "-m", f"Release {tag}")
    except (RuntimeError, subprocess.CalledProcessError) as error:
        print(f"release aborted: {error}", file=sys.stderr)
        return 1
    print(f"created release commit and annotated tag {tag}")
    print("Push it when ready with: git push origin HEAD --tags")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
