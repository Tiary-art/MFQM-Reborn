#!/usr/bin/env python3
import argparse,tempfile,shutil,subprocess,sys,os,json
from pathlib import Path
from common import *
p=argparse.ArgumentParser();p.add_argument('--repo-root',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True);p.add_argument('--input-jar',type=Path,required=True);a=p.parse_args();r=a.repo_root.resolve();o=a.out_dir.resolve();results=[]
def call(name,args,expected=0):
 cmd=[sys.executable,'-B',str(r/'reconstruction/tooling'/name),*map(str,args)];x=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=os.environ|{'PYTHONIOENCODING':'utf-8'});assert (x.returncode==0)==(expected==0),(cmd,x.stdout,x.stderr);results.append(dict(command=cmd,exit=x.returncode,stdout=x.stdout,stderr=x.stderr,expected_success=expected==0))
before={p.name:sha(p.read_bytes())for p in(o/'manifest').glob('ORIGINAL_*.csv')}
call('inventory_original.py',['--repo-root',r,'--out-dir',o,'--input-jar',a.input_jar]);after={p.name:sha(p.read_bytes())for p in(o/'manifest').glob('ORIGINAL_*.csv')};assert before==after
call('inventory_original.py',['--repo-root',r,'--out-dir',o],1)
with tempfile.TemporaryDirectory(prefix='mfqm-r0-')as d:
 t=Path(d)
 for sub in ['manifest','mapping']:shutil.copytree(o/sub,t/sub)
 rows=read(t/'mapping/ORIGINAL_TO_MODERN.csv');rows[0]['original_id']='intentionally-invalid';write(t/'mapping/ORIGINAL_TO_MODERN.csv',rows)
 call('validate_database.py',['--repo-root',r,'--out-dir',t,'--verify'],1)
call('validate_database.py',['--repo-root',r,'--out-dir',o,'--verify'])
dump(o/'checks/TOOL_TESTS.json',dict(status='PASS',checks=['same original input deterministic manifests','missing input fails explicitly','invalid original foreign key rejected','live full database valid'],runs=results))
