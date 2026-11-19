#!/usr/bin/env python3
"""Check catalog/asset completeness and prohibit bundled legacy binary art in this source set."""
from pathlib import Path
import json
r=Path(__file__).resolve().parents[1];res=r/'src/main/resources';a=json.loads((res/'data/mfqm/legacy_block_catalog.json').read_text())
assert len(a)==49 and len({s['id'] for s in a})==49
assert sum(bool(s['fluid']) for s in a)==13
langs=[json.loads((res/f'assets/mfqm/lang/{n}.json').read_text())for n in ['en_us','zh_cn']]
for s in a:
 for sub in ['blockstates','models/block','models/item']:
  assert (res/f"assets/mfqm/{sub}/{s['id']}.json").is_file(),(s['id'],sub)
 assert (res/f"data/mfqm/loot_tables/blocks/{s['id']}.json").is_file(),s['id']
 assert all('block.mfqm.'+s['id'] in l for l in langs),s['id']
 if s['fluid']:
  assert (res/f"assets/mfqm/models/item/{s['id']}_bucket.json").is_file()
  assert all('item.mfqm.'+s['id']+'_bucket' in l for l in langs)
for p in res.rglob('*'):
 if p.is_file():
  assert p.suffix.lower()not in ['.png','.ogg','.jar'],p
  if p.suffix=='.json':json.loads(p.read_text())
print('PASS: 49 unique legacy Block IDs, 13 fluid bucket resource sets, block/item/model/lang/loot JSON coverage; no PNG/OGG/JAR in main resources.')
