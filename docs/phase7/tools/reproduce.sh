#!/usr/bin/env bash
set -euo pipefail
repo=$(cd "$(dirname "$0")/../../.." && pwd)
cd "$repo"
# Requires JDK17, cached Forge47.2.0 deps for --offline; remove --offline for first dependency download.
bash forge-1.20.1/gradlew -p forge-1.20.1 clean test build runGameTestServer -Pphase7GameTestDir=run/phase7-reproduction --offline --console=plain
# Native fixture path is set only for GameTest by build.gradle; no original JAR/assets required.
