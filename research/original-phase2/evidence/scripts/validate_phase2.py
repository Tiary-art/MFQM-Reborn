#!/usr/bin/env python3
"""Static artifact checks only; never launch Minecraft or simulate gameplay."""
from pathlib import Path
import argparse,json,csv,hashlib
ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);a=ap.parse_args();r=a.root
names=['00_EXECUTIVE_SUMMARY.zh-CN.md','01_WORLDGEN_ENTRY_CALLGRAPH.md','02_WORLDGEN_GENERATOR_MATRIX.csv','03_WORLDGEN_ALGORITHMS.md','04_WORLDGEN_PORT_SPEC_1_20_1.md','05_MOTION_EXECUTABLE_SPEC.md','06_COATING_VISUAL_AUDIO_SPEC.md','07_FULL_MECHANISM_GAP_MATRIX.csv','08_ORIGINAL_RUNTIME_TEST_PLAN.md','09_IMPLEMENTATION_ROADMAP.md']
assert all((r/n).is_file() and (r/n).stat().st_size for n in names)
count=blocks=edges=0
for f in (r/'evidence/cfg').glob('*.json'):
 d=json.loads(f.read_text()); heads={b['start'] for b in d['blocks']}; offsets={x['offset'] for b in d['blocks'] for x in b['instructions']}
 assert len(heads)==len(d['blocks']),f
 for e in d['edges']:assert e['from'] in heads and e['to'] in heads,(f,e)
 for b in d['blocks']:assert b['instructions'] and b['start']==b['instructions'][0]['offset'] and b['end']==b['instructions'][-1]['offset'],f
 count+=1;blocks+=len(heads);edges+=len(d['edges'])
assert count==213
forbidden={'.jar','.class','.png','.ogg','.zip','.nbt','.mca'}
assert not [str(f) for f in r.rglob('*') if f.is_file() and f.suffix.lower() in forbidden]
coat=list(csv.DictReader((r/'evidence/indexes/coating-applicability-49.csv').open()));assert len(coat)==49
assert all(x['runtime']=='NOT_RUN' for x in coat)
gaps=list(csv.DictReader((r/'07_FULL_MECHANISM_GAP_MATRIX.csv').open()));assert len(gaps)==161
unresolved=list(csv.DictReader((r/'evidence/indexes/unresolved-five-method-blocks.csv').open()))
assert len({x['method'] for x in unresolved})==5
manifest=json.loads((r/'evidence/manifest.json').read_text());assert manifest['original_sha256']=='2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
print(json.dumps({'status':'PASS_STATIC_ARTIFACT_CHECKS_ONLY','required_documents':len(names),'cfg_methods':count,'blocks':blocks,'edges':edges,'unresolved_five_method_blocks':len(unresolved),'coating_materials':len(coat),'class_gap_inventory':len(gaps),'forbidden_binary_assets':0,'original_runtime':'NOT_RUN'},ensure_ascii=False,indent=2))
