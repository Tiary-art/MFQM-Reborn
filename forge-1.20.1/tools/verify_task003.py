#!/usr/bin/env python3
"""Additional Task003 resource checks; keep Task002's auditor unchanged."""
import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / 'src/main/resources'
checks = []

def check(ok, label):
    if not ok:
        raise AssertionError(label)
    checks.append(label)

def read(path):
    return json.loads((R / path).read_text())

for name, texture in [('quicksand', 'sand'), ('mud', 'mud'), ('soft_quicksand', 'red_sand')]:
    states = read(f'assets/mfqm/blockstates/{name}.json')['variants']
    check(all(s['model'] == f'mfqm:block/{name}' for s in states.values()), name + ' blockstate chain')
    check(set(states) == ({f'depth={i}' for i in range(4)} if name == 'mud' else {''}), name + ' independent states')
    model = read(f'assets/mfqm/models/block/{name}.json')
    check(model['textures']['all'] == f'minecraft:block/{texture}', name + ' vanilla external texture')
    if name == 'soft_quicksand':
        check(model['elements'][0]['to'][1] == 13.6, 'SoftQuicksand 0.85 top')
    check(read(f'assets/mfqm/models/item/{name}.json')['parent'] == f'mfqm:block/{name}', name + ' item model')
    check(read(f'data/mfqm/loot_tables/blocks/{name}.json')['pools'][0]['entries'][0]['name'] == f'mfqm:{name}', name + ' own drop')
    for locale in ['en_us', 'zh_cn']:
        check(bool(read(f'assets/mfqm/lang/{locale}.json')[f'block.mfqm.{name}']), name + ' ' + locale)
check(not list(R.rglob('*.png')) and not list(R.rglob('*.ogg')), 'No bundled PNG/OGG')
if len(sys.argv) > 1:
    jarpath = Path(sys.argv[1])
    with zipfile.ZipFile(jarpath) as jar:
        check(not any(n.endswith(('.png', '.ogg')) for n in jar.namelist()), 'JAR contains no PNG/OGG')
        for n in jar.namelist():
            if n.endswith('.class'):
                check(int.from_bytes(jar.read(n)[6:8], 'big') == 61, 'Java17 ' + n)
    digest = hashlib.sha256(jarpath.read_bytes()).hexdigest()
else:
    digest = None
print(json.dumps({'status': 'PASS', 'checks': checks, 'jar_sha256': digest}, ensure_ascii=False, indent=2))
