#!/usr/bin/env python3
"""Read-only original asset mapping/private import. No resizing, drawing or publication."""
import argparse,csv,json,hashlib,zipfile
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--jar',type=Path,required=True);ap.add_argument('--out',type=Path);ap.add_argument('--extract',action='store_true');a=ap.parse_args();r=Path(__file__).resolve().parents[2];repo=r.parents[1];assert hashlib.sha256(a.jar.read_bytes()).hexdigest()=='2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
rows=list(csv.DictReader((repo/'research/original-phase3/evidence/indexes/phase1-textures.csv').open()));mapping=[];seen=set()
for x in rows:
 path=x['path'];tail=path.split('assets/morefunquicksandmod/',1)[1];tail=tail[len('textures/'):]if tail.startswith('textures/')else'ui/'+tail
 alias='legacy/'+tail[:-4].lower();assert alias not in seen,alias;seen.add(alias);mapping.append({'original_path':path,'original_sha256':x['sha256'],'modern_resource_id_proposal':'mfqm:'+alias,'modern_target_proposal':'assets/mfqm/textures/'+alias+'.png','width':x['width'],'height':x['height'],'animation_sidecar':x['animated_metadata'],'status':'PROPOSED_PATH_MAPPING; original pixels unchanged; modern UV/animation compatibility not validated'})
(r/'evidence/results/original-asset-path-map.csv').parent.mkdir(parents=True,exist_ok=True)
with(r/'evidence/results/original-asset-path-map.csv').open('w',newline='')as f:
 w=csv.DictWriter(f,fieldnames=list(mapping[0]),lineterminator="\n");w.writeheader();w.writerows(mapping)
audio=[]
with zipfile.ZipFile(a.jar) as z:
 for name in sorted(z.namelist()):
  if not name.endswith('.ogg'):continue
  tail=name.split('/sounds/',1)[1];alias='legacy/'+tail[:-4].lower();audio.append({'original_path':name,'sha256':hashlib.sha256(z.read(name)).hexdigest(),'modern_sound_file_proposal':'assets/mfqm/sounds/'+alias+'.ogg','modern_sound_resource_proposal':'mfqm:'+alias,'status':'Original-JAR-packaged audio path mapping; rights unconfirmed; event registration/playback not implemented'})
with(r/'evidence/results/original-audio-path-map.csv').open('w',newline='')as f:
 w=csv.DictWriter(f,fieldnames=list(audio[0]),lineterminator="\n");w.writeheader();w.writerows(audio)
if a.extract:
 assert a.out is not None,'--extract requires --out';dest=a.out.resolve()
 assert not any((p/'.git').exists()for p in [dest,*dest.parents]),'private extraction cannot target a Git worktree'
 with zipfile.ZipFile(a.jar)as z:
  for x in mapping:
   data=z.read(x['original_path']);assert hashlib.sha256(data).hexdigest()==x['original_sha256'];target=dest/x['modern_target_proposal'];target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
   if x['original_path']+'.mcmeta'in z.namelist():Path(str(target)+'.mcmeta').write_bytes(z.read(x['original_path']+'.mcmeta'))
  for x in audio:
   data=z.read(x['original_path']);assert hashlib.sha256(data).hexdigest()==x['sha256'];target=dest/x['modern_sound_file_proposal'];target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
print(json.dumps({'status':'STATIC_VERIFIED_ASSET_PATH_HASH_MAPPING','textures':len(mapping),'self_audio_files':len(audio),'duplicate_modern_targets':0,'pixels_extracted':bool(a.extract),'runtime_render_validation':'NOT_RUN'},indent=2))
