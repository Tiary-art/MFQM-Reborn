#!/usr/bin/env python3
"""Validate the Task 002 resource graph and ensure legacy image bytes are not shipped."""
import csv
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
resources = ROOT / "src/main/resources"
checks = []

def check(condition, description):
    if not condition:
        raise AssertionError(description)
    checks.append(description)

for file in resources.rglob("*.json"):
    json.loads(file.read_text())
check(not list(resources.rglob("*.png")), "No PNG files bundled; vanilla texture referenced externally")
check(not list(resources.rglob("*.ogg")), "No legacy audio bundled")
blockstate = json.loads((resources / "assets/mfqm/blockstates/dev_test_block.json").read_text())
check(blockstate["variants"][""]["model"] == "mfqm:block/dev_test_block", "Blockstate references registered development model")
model = json.loads((resources / "assets/mfqm/models/block/dev_test_block.json").read_text())
check(model["textures"]["all"] == "minecraft:block/sand", "Default model uses Minecraft sand texture without copying/resampling")
item = json.loads((resources / "assets/mfqm/models/item/dev_test_block.json").read_text())
check(item["parent"] == "mfqm:block/dev_test_block", "Item model references development block model")
for locale in ["en_us", "zh_cn"]:
    lang = json.loads((resources / ("assets/mfqm/lang/" + locale + ".json")).read_text())
    check(bool(lang.get("block.mfqm.dev_test_block")), locale + " block translation present")
loot = json.loads((resources / "data/mfqm/loot_tables/blocks/dev_test_block.json").read_text())
check(loot["pools"][0]["entries"][0]["name"] == "mfqm:dev_test_block", "Survival loot references registered BlockItem")
with (ROOT / "docs/texture_mapping_draft.csv").open(encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
check(len(rows) == 162, "All 162 legacy block textures mapped")
check(len({row["proposed_path"] for row in rows}) == 162, "Proposed paths have no case-normalization collisions")
check(all(row["integrated"] == "false" for row in rows), "All legacy texture entries explicitly unintegrated")
check(sum(row["mcmeta_exists"] == "true" for row in rows) == 48, "All 48 animation metadata records preserved")
check(all(re.fullmatch(r"assets/mfqm/textures/block/legacy_draft/[a-z0-9_]+\.png", row["proposed_path"]) for row in rows), "All proposed resource paths use modern lowercase names")
check(any(row["original_filename"] == "Mucus_Flowing.png" and row["width"] == "32" and row["height"] == "304" for row in rows), "Mucus_Flowing anomalous dimensions preserved")
for file in (ROOT / "src/main/java").rglob("*.java"):
    if "client" not in file.relative_to(ROOT / "src/main/java").parts:
        check("net.minecraft.client" not in file.read_text(), "No client class reference in " + str(file.relative_to(ROOT)))
if len(sys.argv) > 1:
    with zipfile.ZipFile(sys.argv[1]) as jar:
        names = jar.namelist()
        check(not any(name.endswith((".png", ".ogg")) for name in names), "Built JAR contains no legacy image/audio files")
        toml = jar.read("META-INF/mods.toml").decode()
        check('${' not in toml and 'modId="mfqm"' in toml, "Built metadata expanded and modid correct")
        bytecode = jar.read("art/tiary/mfqm/MfqmReborn.class")
        check(int.from_bytes(bytecode[6:8], "big") == 61, "Compiled class version 61 (Java 17)")
print(json.dumps({"status": "PASS", "count": len(checks), "checks": checks}, ensure_ascii=False, indent=2))
