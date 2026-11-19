#!/usr/bin/env python3
"""Compare every pre-existing game file with baseline using Git checkout normalization."""
import subprocess,json,hashlib,argparse,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
p=argparse.ArgumentParser();p.add_argument('--javac',required=True);a=p.parse_args()
baseline='184eacb';existing=subprocess.check_output(['git','ls-tree','-r','--name-only',baseline,'forge-1.20.1'],cwd=ROOT,text=True).splitlines()
for rel in existing:
 actual=subprocess.check_output(['git','hash-object','--path='+rel,rel],cwd=ROOT,text=True).strip()
 expected=subprocess.check_output(['git','rev-parse',baseline+':'+rel],cwd=ROOT,text=True).strip()
 assert actual==expected,rel
core=ROOT/'forge-1.20.1/src/main/java/art/tiary/mfqm/legacy'
for path in core.glob('*.java'):
 text=path.read_text();assert 'import net.minecraft' not in text and 'import net.minecraftforge' not in text
outside=[]
for path in (ROOT/'forge-1.20.1/src/main/java').rglob('*.java'):
 if path.parent==core:continue
 text=path.read_text()
 assert not any(s in text for s in ['art.tiary.mfqm.legacy','DryQuicksandCore','StuckLease','LegacyRandom','VoxelPort']),path
 outside.append(path)
with tempfile.TemporaryDirectory(prefix='mfqm-phase6-javac-')as t:
 r=subprocess.run([a.javac,'--release','17','-d',t,*map(str,sorted(core.glob('*.java')))],capture_output=True,text=True);assert r.returncode==0,r.stderr
print(json.dumps({'status':'PASS','baseline':baseline,'existing_forge_files_unchanged':len(existing),'outside_core_java_files_scanned':len(outside),'comparison':'Git clean-filter normalized blobs (gradlew.bat checkout uses CRLF)', 'pure_core_compiles_with_empty_classpath':True,'game_calls_core':False,'runtime_test':'NOT_RUN'},indent=2))
