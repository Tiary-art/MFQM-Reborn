#!/usr/bin/env python3
"""Actual-input guard tests; no original pixels embedded in public fixtures."""
from pathlib import Path
import argparse,subprocess,sys,tempfile,json,hashlib
R=Path(__file__).resolve().parents[3];tool=Path(__file__).with_name('asset_pipeline.py');p=argparse.ArgumentParser();p.add_argument('--jar',type=Path,required=True);a=p.parse_args();results=[]
private=R/'local-original-assets';private.mkdir(exist_ok=True)
def run(args,success=True):
 r=subprocess.run([sys.executable,'-B',str(tool),'--jar',str(a.jar),*map(str,args)],capture_output=True,text=True)
 assert (r.returncode==0)==success,(args,r.stdout,r.stderr)
 results.append({'args':list(map(str,args)),'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr});return r
with tempfile.TemporaryDirectory(prefix='guard-',dir=private)as d:
 dest=Path(d)/'resources';opts=['--output',dest]
 run([*opts,'--dry-run']);assert not dest.exists()
 run(opts);before={str(p.relative_to(dest)):hashlib.sha256(p.read_bytes()).hexdigest()for p in dest.rglob('*')if p.is_file()}
 run(opts);assert before=={str(p.relative_to(dest)):hashlib.sha256(p.read_bytes()).hexdigest()for p in dest.rglob('*')if p.is_file()}
 run([*opts,'--verify'])
 custom=dest/'user-custom.txt';custom.write_text('user-owned marker')
 owned=dest/'assets/mfqm/models/block/quicksand.json';original=owned.read_bytes();owned.write_text('user-edited model')
 run(opts,False);run([*opts,'--clean-generated'],False);assert owned.read_text()=='user-edited model'and custom.read_text()=='user-owned marker'
 owned.write_bytes(original);run([*opts,'--clean-generated']);assert custom.is_file()and not owned.exists()
 run(['--output',R/'forge-1.20.1/src/main/resources','--dry-run'],False)
 run(opts);owned=dest/'assets/mfqm/models/block/quicksand.json';owned.unlink();outside=Path(d)/'outside.txt';outside.write_text('never touch');owned.symlink_to(outside)
 run(opts,False);run([*opts,'--clean-generated'],False);assert outside.read_text()=='never touch'
print(json.dumps({'status':'PASS','checks':['dry-run no output','idempotent full hashes','verify original bytes/references','edited-file import refusal','edited-file atomic cleanup refusal','unmanaged file preserved','source-tree output denied','symlink escape import/cleanup denied'],'commands':results},indent=2))
