#!/usr/bin/env python3
"""Local-only private build; no upload/publish step. Requires the user's original JAR."""
import argparse,os,subprocess,sys,json,hashlib,shutil,zipfile
from pathlib import Path
R=Path(__file__).resolve().parents[3]
p=argparse.ArgumentParser();p.add_argument('--jar',type=Path,default=os.environ.get('MFQM_ORIGINAL_JAR'));p.add_argument('--offline',action='store_true');a=p.parse_args()
if not a.jar:p.error('BLOCKED_PRIVATE_INPUT: --jar or MFQM_ORIGINAL_JAR required')
assets=R/'local-original-assets/resources';out=R/'deliverables/phase9-private';out.mkdir(parents=True,exist_ok=True)
for args in [[],['--verify']]:subprocess.run([sys.executable,'-B',str(Path(__file__).with_name('asset_pipeline.py')),'--jar',str(a.jar),*args],check=True)
wrapper='gradlew.bat'if os.name=='nt'else'./gradlew'
cmd=[wrapper,'clean','test','build','-PmfqmOriginalAssets='+str(assets),'--console=plain']+(['--offline']if a.offline else[])
with(out/'private-build.log').open('w')as log:
 x=subprocess.run(cmd,cwd=R/'forge-1.20.1',stdout=log,stderr=subprocess.STDOUT)
if x.returncode:raise SystemExit(x.returncode)
jar=next((R/'forge-1.20.1/build/libs').glob('*.jar'));dest=out/'mfqm-reborn-phase9-original-textures-local.jar';shutil.copy(jar,dest)
with zipfile.ZipFile(dest)as z:
 files=json.loads((assets/'.mfqm-import-manifest.json').read_text())['files']
 for path,digest in files.items():assert hashlib.sha256(z.read(path)).hexdigest()==digest,path
meta={'mode':'PRIVATE_ORIGINAL_ASSETS_BUILD','distribution':'PRIVATE_ARTIFACT_NOT_DISTRIBUTED','path':str(dest.relative_to(R)),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'original_files_verified':len(files),'command':cmd,'exit':x.returncode}
(out/'ARTIFACTS.json').write_text(json.dumps(meta,indent=2)+'\n');(out/'SHA256SUMS').write_text(meta['sha256']+'  '+dest.name+'\n');print(json.dumps(meta,indent=2))
