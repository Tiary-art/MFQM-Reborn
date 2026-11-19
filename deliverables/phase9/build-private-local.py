#!/usr/bin/env python3
"""Run from an extracted complete repository ZIP; original assets remain local/ignored."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parents[2]/'docs/phase9/tools/build_private.py'),run_name='__main__')
