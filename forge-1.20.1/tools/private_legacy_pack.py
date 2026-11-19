#!/usr/bin/env python3
"""Opt-in private pack. Input JAR/PNG/mcmeta are read-only; nothing is written to src/."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import struct
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = "2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--jar", required=True, type=Path)
parser.add_argument("--texture", default="assets/morefunquicksandmod/textures/blocks/quicksand.png")
parser.add_argument("--core", action="store_true", help="Map the three Task003 core models to their legacy textures")
args = parser.parse_args()
jar = args.jar.resolve()
before = hashlib.sha256(jar.read_bytes()).hexdigest()
if before != EXPECTED:
    parser.error("Input must match the researched original JAR SHA-256")
with (ROOT / "docs/texture_mapping_draft.csv").open(encoding="utf-8-sig") as handle:
    inventory = {row["original_path"]: row for row in csv.DictReader(handle)}
prefix = "assets/morefunquicksandmod/textures/blocks/"
selections = [("quicksand", prefix + "quicksand.png"), ("mud", prefix + "mud.png"),
              ("soft_quicksand", prefix + "SoftQuicksand1.png")] if args.core else [("dev_test_block", args.texture)]
if any(original not in inventory for _, original in selections):
    parser.error("Every selected texture must exist in the mapping draft")
output = ROOT / "private-resources" / ("core-legacy-test-pack.zip" if args.core else "legacy-test-pack.zip")
output.parent.mkdir(exist_ok=True)
records = []
original_bytes = {}
with zipfile.ZipFile(jar) as source, zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as pack:
    pack.writestr("pack.mcmeta", json.dumps({"pack": {"pack_format": 15,
        "description": "PRIVATE legacy MFQM local research pack - do not redistribute"}}))
    for model, original in selections:
        row = inventory[original]
        image = source.read(original)
        width, height = struct.unpack(">II", image[16:24])
        target = row["proposed_path"]
        original_bytes[target] = image
        pack.writestr(target, image)
        if row["mcmeta_exists"] == "true":
            metadata = source.read(row["original_mcmeta_path"])
            pack.writestr(target + ".mcmeta", metadata)
            original_bytes[target + ".mcmeta"] = metadata
        texture_id = "mfqm:" + target.split("/textures/", 1)[1][:-4]
        textures = {"all": texture_id, "particle": texture_id}
        block_model = {"parent": "minecraft:block/cube_all", "textures": textures}
        if model == "soft_quicksand":
            block_model = {"textures": textures, "elements": [{"from": [0, 0, 0], "to": [16, 13.6, 16],
                "faces": {face: {"texture": "#all"} for face in ["down", "up", "north", "south", "west", "east"]}}]}
        pack.writestr("assets/mfqm/models/block/" + model + ".json", json.dumps(block_model))
        records.append({"model": model, "original_path": original, "dimensions": [width, height],
            "sha256": hashlib.sha256(image).hexdigest(), "mcmeta_copied_verbatim": row["mcmeta_exists"] == "true"})
assert hashlib.sha256(jar.read_bytes()).hexdigest() == before
with zipfile.ZipFile(output) as pack:
    for target, original in original_bytes.items():
        assert pack.read(target) == original
print(json.dumps({"private_output": str(output), "original_jar_sha256": before, "core_mode": args.core,
    "image_bytes_unchanged": True, "selections": records,
    "warning": "Private local use only. No resizing/cropping/re-encoding or metadata rewriting. Unusual animation layouts require separate in-game verification."}, indent=2))
