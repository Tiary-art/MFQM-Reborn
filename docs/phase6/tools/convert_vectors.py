#!/usr/bin/env python3
"""Deterministic projection of all API events; never synthesize expected core outputs."""
import gzip,json,hashlib,csv,struct
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'forge-1.20.1/src/test/resources/phase6'
OUT.mkdir(parents=True,exist_ok=True)
P=ROOT/'research/original-phase5/evidence/results'
sources=[]
def load(path):
 sources.append({'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
 return [json.loads(l) for l in gzip.open(path,'rt')]
def identity(b):return {'field_150350_a':'AIR','SandBlock':'DRY_QUICKSAND','field_150322_A':'SANDSTONE','field_150354_m':'SAND','field_150348_b':'STONE','SoftQuicksandBlock':'SOFT_QUICKSAND'}.get(b,'OTHER')
def project(e):
 k=e['event']
 if k=='RNG_CALL':
  return 'R\t'+e['api']+'\t'+str(e.get('bound','-'))+'\t'+str(e['value'])
 if k=='WORLD_READ' and e.get('api')=='getBlock':return '\t'.join(map(str,['Q',e['x'],e['y'],e['z'],identity(e['block'])]))
 if k=='WORLD_WRITE':return '\t'.join(map(str,['W',e['x'],e['y'],e['z'],identity(e['block']),e['metadata'],e['flags'],str(e['applied']).lower()]))
cases=json.loads((P/'cases.json').read_text());manifest=[]
for c in cases:
 if '#generateSoftSand(' not in c['method']:continue
 events=load(P/(c['tag']+'.jsonl.gz'))
 lines=[v for e in events if (v:=project(e)) is not None]
 (OUT/(c['tag']+'.tsv')).write_text('\n'.join(lines)+'\n')
 manifest.append('\t'.join(map(str,[c['tag'],c['seed'],c['radius'],c['fixture']])))
(OUT/'dry-cases.tsv').write_text('\n'.join(manifest)+'\n')
events=load(P/'stuck-lifecycle.jsonl.gz');lines=[]
original=[e for e in events if e['event']!='HEADER'];reference=load(P/'stuck-lifecycle.oracle.jsonl.gz')
assert len(original)==len(reference)==123
for x,y in zip(original,reference):
 assert x.keys()==y.keys()
 for k in x:
  if k=='jump':assert struct.pack('>f',x[k])==struct.pack('>f',y[k])
  elif k=='amount':assert abs(x[k]-y[k])<=1e-14
  else:assert x[k]==y[k]

for e in events:
 k=e['event']
 if k=='TICK':lines.append('T\t'+str(e['tick']))
 elif k=='LEVEL_SET':lines.append('L\t'+str(e['value']))
 elif k in ('ATTR_QUERY','PROP_GET'):lines.append(('A' if k=='ATTR_QUERY' else 'P')+'\t'+str(e['present']).lower())
 elif k=='ATTR_REMOVE':lines.append('D\t'+e['uuid'])
 elif k=='ATTR_ADD':lines.append('\t'.join(map(str,['N',e['uuid'],e['amount'],e['operation'],str(e['saved']).lower()])))
(OUT/'stuck.tsv').write_text('\n'.join(lines)+'\n');stuck_count=len(lines)
p=ROOT/'research/original-phase4/evidence/results/physics-vectors.csv'
(OUT/'physics-vectors.csv').write_bytes(p.read_bytes());sources.append({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'docs/phase6/vector-sources.json').write_text(json.dumps({'sources':sources,'native_lifecycle_events':len([e for e in events if e['event']!='HEADER']),'projection':'all RNG_CALL, getBlock WORLD_READ, WORLD_WRITE; all lifecycle port/Level events; excludes bytecode flow and out-of-scope jump/snapshot'},indent=2)+'\n')
print('converted',len(manifest),'Dry native traces; 123 lifecycle events projected; 112 math vectors')
# Existing supplementary raw traces are replayable without the private JAR.
for path in sorted((ROOT/'docs/phase6/evidence').glob('supplement-*.jsonl.gz')):
 fixture=path.name.removeprefix('supplement-').removesuffix('.jsonl.gz');tag='supplement-'+fixture
 lines=[v for e in load(path) if(v:=project(e))is not None]
 (OUT/(tag+'.tsv')).write_text('\n'.join(lines)+'\n')
 manifest.append(f'{tag}\t0\t5\t{fixture}')
# Exact child slice of the seed38 natural parent; earlier RNG calls warm the SAME stream.
es=load(P/'dry-positive.jsonl.gz');method='MoreFunQuicksandMod.main.CustomWorldGen#generateSoftSand('
start=next(i for i,e in enumerate(es) if e['event']=='HELPER_ENTER' and e.get('method','').startswith(method))
end=next(i for i in range(start+1,len(es)) if es[i]['event']=='HELPER_EXIT' and es[i].get('method','').startswith(method))
prefix=[project(e) for e in es[:start] if e['event']=='RNG_CALL' and e.get('rng')=='passed']
(OUT/'parent38-prefix.tsv').write_text('\n'.join(prefix)+'\n')
(OUT/'parent38.tsv').write_text('\n'.join(v for e in es[start:end+1] if(v:=project(e))is not None)+'\n')
manifest.append('parent38\t38\t5\tdesert')
(OUT/'dry-cases.tsv').write_text('\n'.join(manifest)+'\n')
(ROOT/'docs/phase6/vector-sources.json').write_text(json.dumps({'sources':sources,'native_lifecycle_events':123,'dry_cases':len(manifest),'projection':'all RNG API, block reads/writes (including failure); lifecycle attribute/property/Level API; excludes bytecode branch events and out-of-scope jump/snapshot','parent38_args':'(-16,70,0,5), corroborated via Phase5 independent VM invocation; RNG warmed from every prior passed-stream call'},indent=2)+'\n')

for p in [P/'cases.json',P/'stuck-diff.json',P/'method-provenance.csv',ROOT/'research/original-phase5/PORT_READY_COMPONENTS.md']:
 sources.append({'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
index=ROOT/'docs/phase6/vector-sources.json';data=json.loads(index.read_text());data['sources']=sources;data['projected_stuck_events']=stuck_count;index.write_text(json.dumps(data,indent=2)+'\n')
