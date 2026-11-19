#!/usr/bin/env python3
"""Baseline runner; Windows branch is provided but NOT_RUN in R0."""
import argparse,subprocess,os
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--repo-root',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True);p.add_argument('--offline',action='store_true');a=p.parse_args();out=a.out_dir/'evidence/logs';out.mkdir(parents=True,exist_ok=True)
cmd=(['cmd.exe','/d','/c','gradlew.bat']if os.name=='nt'else['./gradlew'])+['clean','test','build','runGameTestServer','--console=plain']+(['--offline']if a.offline else[])
with(out/'clean-build-gametest.log').open('wb')as log:x=subprocess.run(cmd,cwd=a.repo_root/'forge-1.20.1',stdout=log,stderr=subprocess.STDOUT)
raise SystemExit(x.returncode)
