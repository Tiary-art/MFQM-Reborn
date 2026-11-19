#!/usr/bin/env python3
import json,sys,subprocess,hashlib,math
from pathlib import Path
from oracle_vm import Oracle,f32
r=Path(__file__).resolve().parents[2]
methods=[];base=[]
def configure(work,java_home,jar):
 global methods,base
 methods=json.loads((work/'oracle-methods.json').read_text());base=[str(java_home/'bin/java'),'--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED','-cp',str(work/'classes'),'audit.Run',str(jar),str(work/'offsets.tsv')]

def case(tag,name,seed=0,rad=4,fixture='stone',config='0'):
 path=r/'evidence/results'/(tag+'.jsonl');p=subprocess.run(base+[str(path),name,str(seed),str(rad),fixture,config],capture_output=True,text=True);(r/'evidence/logs'/(tag+'.stderr')).write_text(p.stderr)
 if p.returncode:raise RuntimeError(p.stderr)
 o=Oracle(methods,seed,fixture,config);clazz='MoreFunQuicksandMod.main.blocks.BlockMorass'if name=='PlantingThis'else'MoreFunQuicksandMod.main.GenerateDesertTombs'if name in ['generateSpawner','generateChest']else'MoreFunQuicksandMod.main.CustomWorldGen';m=next(m for m in methods if m['class']==clazz and m['name']==name);key=clazz+'#'+name+m['descriptor']
 if name in ['generateSpawner','generateChest']:
  from oracle_vm import Random
  o.worldrng=Random(seed,'world');args=[o.this,'WORLD',-16,70,0]+([2]if name=='generateChest'else[])
 elif name=='generateWLD':o.config='GenQS';args=[o.this,'WORLD',o.passed,-16,0]
 elif name=='PlantingThis':args=['MorassBlock','WORLD',o.passed,-16,70,0]
 elif name=='generateSurface':args=[o.this,'WORLD',o.passed,-16,0,62]
 elif name=='generateSoftSand':args=[o.this,-16,70,0,rad,'WORLD',o.passed]
 else:args=[o.this,-16,70,0,rad,'WORLD',o.passed,'material:field_151586_h'if config=='water-only'else'material:field_151568_F','MudBlock'if config=='MudBlock'else'JungleQuicksandBlock']
 o.run(key,args);actual=[json.loads(l)for l in path.read_text().splitlines()];actual=[e for e in actual if e['event']not in ['HEADER','RESULT','TILE_FINAL']];path.with_suffix('.oracle.jsonl').write_text(''.join(json.dumps(e)+'\n'for e in o.events));assert len(actual)==len(o.events),(tag,len(actual),len(o.events))
 for idx,(a,b)in enumerate(zip(actual,o.events)):
  if a.get('api')=='nextFloat'and b.get('api')=='nextFloat':a=dict(a);a['value']=f32(a['value'])
  assert a==b,(tag,idx,a,b)
 final={tuple(map(int,xyz.split(','))):(block,int(meta))for xyz,block,meta in (line.split('\t')for line in path.with_name(path.name+'.final.tsv').read_text().splitlines())}
 assert final=={k:(b,o.meta[k])for k,b in o.blocks.items()},tag
 from declarative_oracles import verify
 semantic=verify(actual,o,name,rad,seed,fixture,config)
 if hasattr(o,'tile') and o.tile is not None:
  finals=[json.loads(l)for l in path.read_text().splitlines()if '"TILE_FINAL"'in l]
  assert len(finals)==1
  field='slots'if name=='generateChest'else'data';assert finals[0][field]==o.java_map(o.tile[field]),(tag,finals,o.tile)
 return dict(jvm_command=base+[str(path),name,str(seed),str(rad),fixture,config],declarative=semantic,tag=tag,method=key,seed=seed,radius=rad,fixture=fixture,config=config,status='MODEL_TESTED_INDEPENDENT_VM_FULL_EVENT_DIFF',events=len(actual),final_cells=len(final),native_exit=p.returncode,oracle_steps=o.steps)
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--work',type=Path,required=True);p.add_argument('--java-home',type=Path,required=True);p.add_argument('--jar',type=Path,required=True);a=p.parse_args();configure(a.work,a.java_home,a.jar)
 results=[]
 for tag,n,seed,rad,terrain,cfg in [('spawner','generateSpawner',0,4,'stone','0'),('spawner-null','generateSpawner',0,4,'null-tile','0'),('chest','generateChest',0,4,'stone','0'),('wld-reject','generateWLD',0,4,'wld-reject','GenQS'),('wld-positive','generateWLD',0,4,'wld-positive','GenQS')]:
  print(tag,flush=True);results.append(case(tag,n,seed,rad,terrain,cfg))
 (r/'evidence/results/vertical-diffs.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
