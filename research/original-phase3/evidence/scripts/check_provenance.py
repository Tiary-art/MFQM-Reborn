#!/usr/bin/env python3
import argparse,json,csv
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('--phase1',type=Path,required=True);a=p.parse_args();r=a.root
ms=json.loads((a.phase1/'indexes/methods-with-instructions.json').read_text());lookup={(m['class']+'#'+m['name']+m['descriptor']):m for m in ms};selected=json.loads((r/'evidence/indexes/trace-methods.json').read_text())
for m in selected.values():assert m==lookup[m['class']+'#'+m['name']+m['descriptor']]
sites=list(csv.DictReader((r/'evidence/indexes/material-instruction-sites.csv').open()))
for s in sites:
 m=lookup[s['method']];i=next(x for x in m['instructions']if x['offset']==int(s['offset']));assert i['args']==s['target']and i['opcode']==s['opcode']
print(json.dumps({'status':'STATIC_VERIFIED','selected_methods_identical_to_phase1':len(selected),'material_instruction_sites_exactly_matched':len(sites),'scope':'source provenance only; no gameplay semantic proof'},indent=2))
