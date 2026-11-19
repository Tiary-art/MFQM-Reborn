#!/usr/bin/env python3
import argparse,subprocess,sys,json,shutil,hashlib,gzip,csv
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--phase1',type=Path,required=True);ap.add_argument('--jar',type=Path,required=True);ap.add_argument('--java-home',type=Path,required=True);ap.add_argument('--work',type=Path,default=Path('/tmp/mfqm-phase5'));ap.add_argument('--regress',action='store_true');a=ap.parse_args();r=Path(__file__).resolve().parents[2];repo=r.parents[1];tools=r/'evidence/tools';results=r/'evidence/results';log=[]
assert hashlib.sha256(a.jar.read_bytes()).hexdigest()=='2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
def run(cmd,out):
 p=subprocess.run(list(map(str,cmd)),capture_output=True,text=True);log.append(dict(command=list(map(str,cmd)),exit=p.returncode,stderr=p.stderr));(r/out).write_text(p.stdout)
 if p.returncode:raise RuntimeError(p.stderr)
 return p
try:
 run([sys.executable,'-B',tools/'prepare.py','--phase1',a.phase1,'--out',a.work],'evidence/logs/prepare.log');(a.work/'src/audit').mkdir(parents=True,exist_ok=True);(a.work/'classes').mkdir(exist_ok=True)
 for src in tools.glob('*.java'):shutil.copy(src,a.work/'src/audit'/src.name)if src.name!='World.java'else shutil.copy(src,a.work/'src/net/minecraft/world/World.java')
 export=['--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED'];run([a.java_home/'bin/javac',*export,'-d',a.work/'classes',*sorted((a.work/'src').rglob('*.java'))],'evidence/logs/compile.log')
 run([a.java_home/'bin/java',*export,'-cp',a.work/'classes','audit.DeriveType',a.jar,a.work/'offsets.tsv',a.work/'classes'],'evidence/results/body-identity.log')
 import compare
 compare.configure(a.work,a.java_home,a.jar);cases=[]
 for fixture in ['plant-ok','plant-refuse','plant-null']:
  for seed in [0,1,-1]:cases.append(compare.case(f'{fixture}-{seed}','PlantingThis',seed,4,fixture))
 for name in ['generateMire','generateSoftSand']:
  for rad in [-1,0,1,4,5,10,18]:
   for seed in [0,1]:cases.append(compare.case(f'{name}-r{rad}-s{seed}',name,seed,rad,'stone'if name=='generateMire'else'desert'))
 cases.append(compare.case('mire-protected','generateMire',0,4,'protected'))
 cases.append(compare.case('mire-mud','generateMire',0,4,'stone','MudBlock'))
 cases.append(compare.case('mire-material-reject','generateMire',0,4,'stone','water-only'))
 for name,cfg,seed in [('qs','GenQS',10),('dry','GenSSand',38)]:
  for tag,terrain,sd in [('positive','desert',seed),('no-ground','empty',seed),('probability-reject','desert',0),('refused-writes','desert-refuse',seed)]:cases.append(compare.case(f'{name}-{tag}','generateSurface',sd,4,terrain,cfg))
 cases.append(compare.case('surface-composed','generateSurface',10,4,'desert','GenSSand,GenQS'))
 cases.append(compare.case('surface-composed-dry-wins','generateSurface',38,4,'desert','GenSSand,GenQS'))
 cases.append(compare.case('dry-helper-air-boundary','generateSoftSand',0,10,'empty'))
 for name in ['generateSpawner','generateChest']:
  for seed in [0,4096,-1]:cases.append(compare.case(f'{name}-s{seed}',name,seed,4,'stone'))
  cases.append(compare.case(name+'-null',name,0,4,'null-tile'))
 for fixture in ['wld-reject','wld-reject-overlap','wld-positive']:cases.append(compare.case(fixture,'generateWLD',0,4,fixture,'GenQS'))
 # Full parent Morass reruns retain real callback bodies; no oracle claim for whole parent.
 parent=[]
 for seed in [10,2132]:
  tag=f'morass-parent-{seed}';path=results/(tag+'.jsonl');p=subprocess.run(compare.base+[str(path),'generateAOADimGardencia',str(seed),'4','pond','GenMoor'],capture_output=True,text=True);log.append(dict(command=compare.base+[str(path),'generateAOADimGardencia',str(seed),'4','pond','GenMoor'],exit=p.returncode,stderr=p.stderr));assert p.returncode==0,p.stderr;events=[json.loads(l)for l in path.read_text().splitlines()];assert not any(e['event']in ['ERROR','UNRESOLVED']for e in events);parent.append(dict(seed=seed,status='MODEL_TESTED',events=len(events),final=events[-1],independent_whole_parent=False))
 run([a.java_home/'bin/java','-cp',a.work/'classes','audit.StuckRun',results/'stuck-lifecycle.jsonl'],'evidence/logs/stuck.log');run([sys.executable,'-B',tools/'lifecycle_oracle.py'],'evidence/logs/stuck-oracle.log')
 if a.regress:
  # Keep all historical evidence untouched: regress in a disposable repository-shaped copy.
  reg=a.work/'regression';(reg/'research').mkdir(parents=True,exist_ok=True);(reg/'.git').mkdir(exist_ok=True)
  for phase in ['original-phase2','original-phase3','original-phase4']:shutil.copytree(repo/'research'/phase,reg/'research'/phase,dirs_exist_ok=True)
  run([sys.executable,'-B',reg/'research/original-phase2/evidence/scripts/validate_phase2.py',reg/'research/original-phase2'],'evidence/results/phase2-regression.json')
  run([sys.executable,'-B',reg/'research/original-phase4/evidence/tools/all_checks.py','--phase1',a.phase1,'--jar',a.jar,'--java-home',a.java_home,'--work',a.work/'regression-build'],'evidence/logs/phase4-regression.log')
  shutil.copy(reg/'research/original-phase4/evidence/results/validation.json',results/'phase4-regression.json');shutil.copy(reg/'research/original-phase4/evidence/results/phase3-regression.json',results/'phase3-regression.json')
 (results/'cases.json').write_text(json.dumps(cases,indent=2)+'\n');(results/'morass-parent.json').write_text(json.dumps(parent,indent=2)+'\n')
 # Complete native and oracle logs are compressed, not sampled/cropped. SHA is for uncompressed content.
 traces=[]
 for path in list(results.glob('*.jsonl')):
  datahash=hashlib.sha256(path.read_bytes()).hexdigest();gz=path.with_suffix(path.suffix+'.gz')
  with path.open('rb')as fin,gz.open('wb')as fout:
   with gzip.GzipFile(fileobj=fout,mode='wb',mtime=0)as z:shutil.copyfileobj(fin,z)
  traces.append(dict(path=str(gz.relative_to(r)),uncompressed_sha256=datahash));path.unlink()
 (results/'trace-manifest.json').write_text(json.dumps(traces,indent=2)+'\n')
 summary=dict(independent_vm_full_event_cases=len(cases),declarative_geometry_walk_cases=sum(bool(c['declarative'])for c in cases),whole_morass_parent_reruns=parent,stuck=json.loads((results/'stuck-diff.json').read_text()),regression_run=a.regress,original_runtime='NOT_RUN',whole_surface_all_biomes_closed=0)
 (r/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:v for k,v in summary.items()if k not in ['stuck','whole_morass_parent_reruns']},indent=2))
finally:(r/'evidence/logs/commands.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
