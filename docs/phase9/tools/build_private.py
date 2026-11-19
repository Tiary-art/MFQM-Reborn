#!/usr/bin/env python3
"""Forward the historical CLI to the private builder paired with this checkout."""
import os
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
args = sys.argv[1:]
if "--jar" not in args and os.environ.get("MFQM_ORIGINAL_JAR"):
    args = ["--jar", os.environ["MFQM_ORIGINAL_JAR"], *args]
raise SystemExit(subprocess.call([sys.executable, "-X", "utf8",
    str(root / "deliverables/r1/tools/build_private.py"), *args]))
