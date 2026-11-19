#!/usr/bin/env python3
from pathlib import Path
import argparse,subprocess,sys,json
p=argparse.ArgumentParser();p.add_argument('--jar',type=Path,required=True);a=p.parse_args();r=Path(__file__).resolve().parents[2];dest=r/'should-not-extract';assert not dest.exists()
cmd=[sys.executable,'-B',str(r/'evidence/tools/private_assets.py'),'--jar',str(a.jar),'--extract','--out',str(dest)];result=subprocess.run(cmd,capture_output=True,text=True)
assert result.returncode!=0 and 'private extraction cannot target a Git worktree'in result.stderr
assert not dest.exists()
print(json.dumps({'status':'MODEL_TESTED_TOOL_GUARD','command':cmd,'expected_nonzero_exit':result.returncode,'stderr':result.stderr,'out_directory_created':False,'original_pixels_or_audio_extracted':False},indent=2))
