#!/usr/bin/env python3
"""Recompute oracle streams against saved native evidence; not native self-replay."""
import argparse,json,gzip,hashlib,math
from pathlib import Path
from oracle_vm import Oracle,Random,f32
from declarative_oracles import verify
ap=argparse.ArgumentParser();ap.add_argument('--work',type=Path,required=True);a=ap.parse_args();r=Path(__file__).resolve().parents[2];methods=json.loads((a.work/'oracle-methods.json').read_text());cases=json.loads((r/'evidence/results/cases.json').read_text());verified=[]
for c in cases:
 o=Oracle(methods,c['seed'],c['fixture'],c['config']);name=c['method'].split('#')[1].split('(')[0];key=c['method'];rad=c['radius']
 if name in ['generateSpawner','generateChest']:o.worldrng=Random(c['seed'],'world');args=[o.this,'WORLD',-16,70,0]+([2]if name=='generateChest'else[])
 elif name=='generateWLD':o.config='GenQS';args=[o.this,'WORLD',o.passed,-16,0]
 elif name=='PlantingThis':args=['MorassBlock','WORLD',o.passed,-16,70,0]
 elif name=='generateSurface':args=[o.this,'WORLD',o.passed,-16,0,62]
 elif name=='generateSoftSand':args=[o.this,-16,70,0,rad,'WORLD',o.passed]
 else:args=[o.this,-16,70,0,rad,'WORLD',o.passed,'material:field_151586_h'if c['config']=='water-only'else'material:field_151568_F','MudBlock'if c['config']=='MudBlock'else'JungleQuicksandBlock']
 o.run(key,args)
 with gzip.open(r/'evidence/results'/(c['tag']+'.jsonl.gz'),'rt')as f:actual=[json.loads(x)for x in f]
 actual=[x for x in actual if x['event']not in ['HEADER','RESULT','TILE_FINAL']];assert len(actual)==len(o.events)
 for idx,(x,y)in enumerate(zip(actual,o.events)):
  if x.get('api')=='nextFloat':x=dict(x);x['value']=f32(x['value'])
  assert x==y,(c['tag'],idx,x,y)
 assert {k:(v,o.meta[k])for k,v in o.blocks.items()}=={tuple(map(int,p.split(','))):(b,int(m))for p,b,m in [x.split('\t')for x in (r/'evidence/results'/(c['tag']+'.jsonl.final.tsv')).read_text().splitlines()]}
 verify(actual,o,name,rad,c['seed'],c['fixture'],c['config']);verified.append(c['tag'])
print(json.dumps({'status':'MODEL_TESTED','saved_native_vs_independent_oracle_rerun':len(verified),'unsupported_types':'fail closed; checked array/tile casts and Java array bounds','original_runtime':'NOT_RUN'},indent=2))
