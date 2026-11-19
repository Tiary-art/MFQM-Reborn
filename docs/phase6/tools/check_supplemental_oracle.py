#!/usr/bin/env python3
import sys,json,gzip,argparse
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/original-phase5/evidence/tools'))
from oracle_vm import Oracle
class SupplementalOracle(Oracle):
 # Original Phase5 VM has no deny voxel fixture (only its write-rejection predicate).
 # Declare the same y66-water/AIR fixture as Phase5 World.java, without changing old evidence.
 def peek(self,x,y,z):
  if self.fixture=='deny':return self.blocks.get((x,y,z),'field_150355_j'if y==66 else'field_150350_a')
  return super().peek(x,y,z)
p=argparse.ArgumentParser();p.add_argument('--methods',required=True);a=p.parse_args()
ms=json.loads(Path(a.methods).read_text());out=[]
for fixture in ['desert-refuse','deny','protected']:
 o=SupplementalOracle(ms,0,fixture,'0');key=next(m['class']+'#'+m['name']+m['descriptor']for m in ms if m['name']=='generateSoftSand');o.run(key,[o.this,-16,70,0,5,'WORLD',o.passed])
 with gzip.open(ROOT/f'docs/phase6/evidence/supplement-{fixture}.jsonl.gz','rt')as f:actual=[json.loads(l)for l in f]
 actual=[e for e in actual if e['event']not in ('HEADER','RESULT')]
 assert actual==o.events,(fixture,len(actual),len(o.events))
 out.append({'fixture':fixture,'full_native_vm_events':len(actual),'status':'PASS'})
print(json.dumps(out,indent=2))
