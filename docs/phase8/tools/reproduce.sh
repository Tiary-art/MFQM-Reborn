#!/usr/bin/env bash
set -euo pipefail
repo=$(cd "$(dirname "$0")/../../.." && pwd)
cd "$repo"
python -B docs/phase8/tools/contact_vectors.py
# JDK17; cached Forge47.2.0 dependencies for --offline. Remove --offline for an initial fetch.
# Never run against a normal save. This creates an exclusive disposable GameTest directory.
bash forge-1.20.1/gradlew -p forge-1.20.1 clean test build runGameTestServer -Pphase7GameTestDir=run/phase8-reproduction --offline --console=plain
