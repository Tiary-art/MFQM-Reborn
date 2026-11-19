#!/usr/bin/env python3
"""Read-only compare against Task001 inventory; do not export original archive bytes."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import zipfile

p = argparse.ArgumentParser()
p.add_argument('--original-jar', required=True, type=Path)
p.add_argument('--built-jar', required=True, type=Path)
a = p.parse_args()
root = Path(__file__).resolve().parents[2]
sha = lambda b: hashlib.sha256(b).hexdigest()
original_hash = sha(a.original_jar.read_bytes())
assert original_hash == '2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
with (root/'research/task-001/evidence/archive_entries.csv').open(encoding='utf-8-sig') as f:
    inventory = {row['path']:row for row in csv.DictReader(f)}
with zipfile.ZipFile(a.original_jar) as jar:
    images = [n for n in jar.namelist() if n.endswith('.png')]
    assert len(images) == 247
    assert all(sha(jar.read(n)) == inventory[n]['sha256'] for n in images)
    all_original_hashes = {row['sha256'] for row in inventory.values() if row['sha256']}
with zipfile.ZipFile(a.built_jar) as jar:
    assert not any(n.endswith(('.png','.ogg')) for n in jar.namelist())
    assert not any(sha(jar.read(n)) in all_original_hashes for n in jar.namelist() if not n.endswith('/'))
assert sha(a.original_jar.read_bytes()) == original_hash
print(json.dumps(dict(status='PASS', original_jar_sha256=original_hash, png_verified_against_task001=247,
    original_jar_modified=False, built_jar_sha256=sha(a.built_jar.read_bytes()),
    built_jar_bytes=a.built_jar.stat().st_size, bundled_png_ogg=0,
    built_entries_matching_original_file_hashes=0), indent=2))
