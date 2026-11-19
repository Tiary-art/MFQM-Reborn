#!/usr/bin/env python3
"""Build mock-only JVM harness in /tmp and execute reproducible cases. No game build."""
from pathlib import Path
import argparse,subprocess,json,hashlib,shutil,sys,csv,gzip
ap=argparse.ArgumentParser();ap.add_argument('--phase1',type=Path,required=True);ap.add_argument('--jar',type=Path,required=True);ap.add_argument('--java-home',type=Path,required=True);ap.add_argument('--work',type=Path,default=Path('/tmp/mfqm-phase4'));ap.add_argument('--extended',action='store_true');a=ap.parse_args();repo=Path(__file__).resolve().parents[4];r=repo/'research/original-phase4';tools=r/'evidence/tools';work=a.work
assert hashlib.sha256(a.jar.read_bytes()).hexdigest()=='2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
log=[]
def command(cmd,stdout=None):
 p=subprocess.run(list(map(str,cmd)),capture_output=True,text=True);log.append({'command':list(map(str,cmd)),'exit':p.returncode,'stderr':p.stderr})
 if stdout:Path(stdout).write_text(p.stdout)
 if p.returncode:raise RuntimeError(p.stderr)
 return p
command([sys.executable,'-B',tools/'prepare.py','--phase1',a.phase1,'--out',work],r/'evidence/logs/prepare.log');(work/'src/audit').mkdir(parents=True,exist_ok=True);(work/'classes').mkdir(exist_ok=True)
for n in ['Trace','Instrument','Rng','Run']:shutil.copy(tools/(n+'.java'),work/'src/audit'/(n+'.java'))
shutil.copy(tools/'World.java',work/'src/net/minecraft/world/World.java')
export=['--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED']
command([a.java_home/'bin/javac',*export,'-d',work/'classes',*sorted((work/'src').rglob('*.java'))])
base=[a.java_home/'bin/java',*export,'-cp',work/'classes','audit.Run',a.jar,work/'offsets.tsv'];cases=[]
def run(tag,method,seed=0,rad=4,fixture='stone',arg='0',private=False,expected_error=False):
 path=(work/'private-traces'if private else r/'evidence/results')/(tag+'.jsonl');path.parent.mkdir(parents=True,exist_ok=True)
 cmd=list(map(str,base+[path,method,seed,rad,fixture,arg]))
 try:p=subprocess.run(cmd,capture_output=True,text=True,timeout=90)
 except subprocess.TimeoutExpired as e:
  rec={'case':tag,'exit':'TIMEOUT','path':str(path),'verdict':'UNRESOLVED','error':'90s model budget; not a passing trace'};cases.append(rec);return
 log.append({'command':cmd,'exit':p.returncode,'stderr':p.stderr});errpath=r/'evidence/logs'/(tag+'.stderr')
 if p.stderr:errpath.write_text(p.stderr)
 elif errpath.exists():errpath.unlink()
 counts={};last=None;worldwrites=0
 with path.open()as f:
  for line in f:
   e=json.loads(line);counts[e['event']]=counts.get(e['event'],0)+1;last=e
 rec={'case':tag,'method':method,'seed':seed,'radius':rad,'fixture':fixture,'arg':arg,'exit':p.returncode,'events':counts,'status':'MODEL_TESTED'if p.returncode==0 else'UNRESOLVED','expected_error':expected_error,'full_trace_path':str(path)if private else str(path.relative_to(repo)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'last':last}
 cases.append(rec)
 if private:
  compressed=r/'evidence/results'/(tag+'.jsonl.gz')
  with path.open('rb') as fin,compressed.open('wb') as fout:
   with gzip.GzipFile(fileobj=fout,mode='wb',mtime=0) as z:shutil.copyfileobj(fin,z)
  rec['full_trace_path']=str(compressed.relative_to(repo));rec['raw_local_path']=str(path);rec['compression']='gzip; decompress for complete ordered MODEL_TRACE'
  # Full ordered output retained privately; public result is an explicitly labeled digest, not a full trace.
  (r/'evidence/results'/(tag+'.digest.json')).write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
  shutil.copy(path.with_name(path.name+'.coverage.tsv'),r/'evidence/results'/(tag+'.coverage.tsv'))
 if bool(p.returncode)!=expected_error:print('UNEXPECTED_RESULT',tag,p.returncode,p.stderr[:500])
for terrain in ['mud','empty','mixed','deny']:
 for seed in [0,1,-1]:run(f'gard-mud-{terrain}-{seed}','generateAOADimGardencia',seed,4,terrain,'GenMud')
run('gard-mud-all-layouts','generateAOADimGardencia',0,4,'all-layouts','GenMud')
run('gard-mud-disabled','generateAOADimGardencia',0,4,'mud','NONE')
for method in ['generateMireO','generateMireOD','generateLiquidMire','generateMorass']:
 for rad in [0,1,4]:run(f'{method}-r{rad}',method,0,rad,'water'if method in ['generateLiquidMire','generateMorass']else'stone','1'if method=='generateLiquidMire'else'0')
run('liquid-invalid-bound','generateLiquidMire',0,4,'water','76',expected_error=True)
# Existing material-wide Surface branch table: each top-level region gets an actual disabled/negative execution.
chains=list(csv.DictReader((repo/'research/original-phase3/evidence/indexes/surface-all-chains.csv').open()))[1:]
import re
for i,ch in enumerate(chains,1):
 config=re.search(r'MFQM\.(Gen\w+)',ch['condition']).group(1)
 run(f'surface-{i:02d}-seed0','generateSurface',0,4,'desert',config)
run('surface-qs-positive','generateSurface',10,4,'desert','GenQS')
run('surface-qs-no-ground','generateSurface',10,4,'empty','GenQS')
run('surface-softsand-positive','generateSurface',38,4,'desert','GenSSand')
# Missing-block counterexamples: no parent/helper body is silently bypassed.
for tag,seed,terrain,cfg in [('jqs-ceiling',10,'ceiling','GenJQS'),('jqs-tar',10,'tar','GenJQS'),('blossom-ceiling',384,'sand-ceiling','GenMucBl'),('liqmire-ceiling',1,'water-alternating','GenLiqMire')]:run(tag,'generateAOADimGardencia',seed,4,terrain,cfg)
if a.extended:
 run('jqs-od-real','generateAOADimGardencia',10,4,'stone','GenJQS',private=True)
 run('gard-liqmire-real','generateAOADimGardencia',1,4,'water-island','GenLiqMire',private=True)
 run('gard-moor-water-first','generateAOADimGardencia',2132,4,'pond','GenMoor',private=True)
 run('jqs-flat-real', 'generateAOADimGardencia',114,4,'stone','GenJQS',private=True)
 run('gard-blossom-real','generateAOADimGardencia',384,4,'ground65','GenMucBl',private=True)
 run('gard-moor-real','generateAOADimGardencia',10,4,'pond','GenMoor',private=True)
(r/'evidence/results/cases.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2)+'\n');(r/'evidence/logs/commands.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
sys.path.insert(0,str(tools));from reference_mud import compare
comparisons=[compare(r/'evidence/results'/(f'gard-mud-{terrain}-{seed}.jsonl'),seed,terrain)for terrain in ['mud','empty','mixed','deny']for seed in [0,1,-1]]
comparisons.append(compare(r/'evidence/results/gard-mud-disabled.jsonl',0,'mud',False))
comparisons.append(compare(r/'evidence/results/gard-mud-all-layouts.jsonl',0,'all-layouts'))
(r/'evidence/results/independent-mud-diff.json').write_text(json.dumps(comparisons,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'cases':len(cases),'model_success':sum(c['exit']==0 for c in cases),'unresolved_errors':sum(c['exit']!=0 for c in cases),'independent_full_event_and_final_state_matches':len(comparisons),'original_runtime':'NOT_RUN'},indent=2))
