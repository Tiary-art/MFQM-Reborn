#!/usr/bin/env python3
import argparse,csv,json,re,sys,hashlib
from pathlib import Path
from trace_vm import JavaRandom,VM
ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);a=ap.parse_args();r=a.root;methods=json.loads((r/'evidence/indexes/trace-methods.json').read_text());passed=[];negative=[]
# Official java.util.Random reference including nextInt1, rejection paths, negative seeds.
refs=list(csv.reader((r/'evidence/tests/java-rng-reference.csv').open()));current=None;rng=None;draws=[]
for seed,repeat,bound,value in refs:
 if seed!=current:current=seed;rng=JavaRandom(int(seed),lambda **k:draws.append(k))
 assert rng.nextInt(int(bound))==int(value),(seed,repeat,bound,value)
assert any(d['draws']>1 for d in draws)
passed.append(f'java.util.Random differential: {len(refs)} results exact; rejection and nextInt(1) included')
r1=JavaRandom(0);before=r1.state;assert r1.nextInt(1)==0 and r1.state!=before
r2=JavaRandom(0);assert r1.nextInt(100)!=r2.nextInt(100);passed.append('removing nextInt(1) changes subsequent RNG value')
for b in [0,-1,2147483648]:
 try:JavaRandom(0).nextInt(b);raise AssertionError('expected invalid bound')
 except ValueError:negative.append('invalid bound rejected: '+str(b))
v=VM(methods,0,(-16,0),'mud');v.run('generateAOADimGardencia',['THIS','WORLD','RNG',-16,0]);writes=[e for e in v.events if e['event']=='WRITE'];assert len(writes)==1536
assert len({(e['x'],e['y'],e['z'])for e in writes})==1536
assert {e['y'] for e in writes}==set(range(60,66));assert all(e['metadata']==(0 if e['y']==65 else 3)for e in writes)
assert len([e for e in v.events if e['event']=='RNG'])==2
assert any(e['x']<0 and e['chunk_x']==-1 for e in writes);passed.append('Gardencia Mud fixture: 1536 exact writes; metadata; negative chunk coordinates; two entry RNG calls')
v2=VM(methods,0,(-16,0),'mud');v2.run('generateAOADimGardencia',['THIS','WORLD','RNG',-16,0]);assert v.events==v2.events;passed.append('deterministic replay: all events identical')
# This fixture forces Blossom generator to return false. Original caller still sets blockGen true.
v=VM(methods,384,(-16,0),'blossom');v.run('generateAOADimGardencia',['THIS','WORLD','RNG',-16,0]);assert v.stub_count==1;assert [e['value']for e in v.events if e['event']=='BLOCKGEN_STORE']==[0,1];passed.append('Blossom false-return fixture still stores blockGen=1')
# Fail closed, never silently ignore unsupported instruction or external helper.
bad=dict(methods);bad['CustomWorldGen#generateAOADimGardencia']={'instructions':[{'offset':0,'opcode':'unsupported_test_opcode','args':''}]}
try:VM(bad).run('generateAOADimGardencia',[]);raise AssertionError('expected unsupported failure')
except NotImplementedError:negative.append('unsupported opcode fails closed')
try:VM(methods).invoke('unknownHelper','()V',[],None);raise AssertionError('expected unresolved helper failure')
except NotImplementedError:negative.append('undeclared helper fails closed')
# Independent CFR literal decoder vs bytecode-driven trace of entire ordered Tombs chain.
v=VM(methods);v.run('func_76484_a',['THIS','WORLD','RNG',0,0,0],'GenerateDesertTombs');actual=[(e['method'].split('#')[1],e['x'],e['y'],e['z'],e['block'],e['metadata'])for e in v.events if e['event']=='BLUEPRINT_WRITE'];expected=[]
p2=r.parent/'original-phase2/evidence/source-methods'
pat=re.compile(r'this\.setBlock\(world, i\s*\+\s*(-?\d+), j\s*\+\s*(-?\d+), k\s*\+\s*(-?\d+), (?:\(Block\))?(Blocks|MFQM)\.(\w+), (-?\d+)\);')
for name in ['func_76484_a','generate2','generate3','generate4','generate5','generate6']:
 src=(p2/('GenerateDesertTombs__'+name+'.cfr.txt')).read_text()
 for m in pat.finditer(src):
  x,y,z,owner,block,meta=m.groups();field=('net/minecraft/init/Blocks.'if owner=='Blocks'else'MoreFunQuicksandMod/main/MFQM.')+block;expected.append((name,int(x),int(y),int(z),field,int(meta)))
assert len(expected)==8489,(len(expected),len(actual));assert expected==actual
passed.append('Tombs independent CFR literal coordinate/metadata/order decoder equals all 8489 bytecode direct writes')
blue=[]
for e in v.events:
 if e['event']=='BLUEPRINT_WRITE':blue.append({k:e[k]for k in ['seq','method','offset','x','y','z','block','metadata','flags','chunk_x','chunk_z']})
with (r/'evidence/indexes/tombs-direct-write-blueprint.csv').open('w',newline='')as f:
 w=csv.DictWriter(f,fieldnames=list(blue[0]));w.writeheader();w.writerows(blue)
print(json.dumps({'status':'MODEL_TESTED','passed':passed,'expected_negative_cases':negative,'original_runtime':'NOT_RUN','warning':'fixture semantics and leaf generator bodies are not original game equivalence proofs'},ensure_ascii=False,indent=2))
