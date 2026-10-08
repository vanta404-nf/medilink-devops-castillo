"""Run the same local checks that the GitHub Actions workflow performs."""

from __future__ import annotations

import compileall
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    print("[1/2] Validating Python syntax...")
    ok = compileall.compile_dir(ROOT, quiet=1, rx=None)
    if not ok:
        print("Syntax validation failed.")
        return 1

    print("[2/2] Running automated tests...")
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
