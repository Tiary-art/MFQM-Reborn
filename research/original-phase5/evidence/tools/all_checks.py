#!/usr/bin/env python3
import argparse,subprocess,sys,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--phase1',type=Path,required=True);p.add_argument('--jar',type=Path,required=True);p.add_argument('--java-home',type=Path,required=True);p.add_argument('--work',type=Path,default=Path('/tmp/mfqm-phase5'));a=p.parse_args();r=Path(__file__).resolve().parents[2];tools=r/'evidence/tools';log=[]
def run(name,args,target):
 cmd=[sys.executable,'-B',str(tools/name),*list(map(str,args))];result=subprocess.run(cmd,capture_output=True,text=True);(r/target).write_text(result.stdout);log.append(dict(command=cmd,exit=result.returncode,stderr=result.stderr))
 if result.returncode:raise RuntimeError(result.stderr)
try:
 run('run_all.py',['--phase1',a.phase1,'--jar',a.jar,'--java-home',a.java_home,'--work',a.work,'--regress'],'evidence/logs/all-native.log')
 run('verify_saved.py',['--work',a.work],'evidence/results/oracle-rerun.json')
 run('test_guards_and_replay.py',['--work',a.work,'--java-home',a.java_home,'--jar',a.jar],'evidence/logs/guards.log')
 run('finalize.py',['--work',a.work],'evidence/logs/finalize.log')
 run('validate.py',['--jar',a.jar],'evidence/results/validation.json')
 print('PASS: 62 full native/oracle comparisons, 44 declarative crosschecks, 8 lifecycle callbacks, fixed-seed replay, fail-closed guards and Phase2–4 regression. Original Minecraft runtime NOT_RUN.')
finally:(r/'evidence/logs/all-checks-commands.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
