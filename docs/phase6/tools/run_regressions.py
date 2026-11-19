#!/usr/bin/env python3
"""Historical tests that write evidence run in a disposable isolated copy."""
from pathlib import Path
import argparse,subprocess,shutil,tempfile,json,sys
ROOT=Path(__file__).resolve().parents[3]
p=argparse.ArgumentParser();p.add_argument('--methods-work',default='/tmp/mfqm-phase5');a=p.parse_args()
out=ROOT/'docs/phase6/logs';results=[]
with tempfile.TemporaryDirectory(prefix='mfqm-phase6-regression-')as temp:
 repo=Path(temp);shutil.copytree(ROOT/'research',repo/'research');(repo/'.git').mkdir()
 commands=[
 ('phase2-static',[sys.executable,'-B',str(repo/'research/original-phase2/evidence/scripts/validate_phase2.py'),str(repo/'research/original-phase2')]),
 ('phase3-trace',[sys.executable,'-B',str(repo/'research/original-phase3/evidence/scripts/test_trace.py'),str(repo/'research/original-phase3')]),
 ('phase4-math',[sys.executable,'-B',str(repo/'research/original-phase4/evidence/tools/check_vectors.py')]),
 ('phase5-saved-native',[sys.executable,'-B',str(repo/'research/original-phase5/evidence/tools/verify_saved.py'),'--work',a.methods_work]),
 ]
 for name,cmd in commands:
  r=subprocess.run(cmd,capture_output=True,text=True);(out/(name+'.stdout')).write_text(r.stdout);(out/(name+'.stderr')).write_text(r.stderr)
  results.append(dict(name=name,command=cmd,exit=r.returncode))
(out/'historical-regressions.json').write_text(json.dumps(results,indent=2)+'\n')
assert all(r['exit']==0 for r in results),results
print('PASS: Phase2 static, Phase3 trace, Phase4 112 numeric vectors, Phase5 62 saved native/independent VM cases; isolated evidence unchanged')
