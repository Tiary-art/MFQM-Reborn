#!/usr/bin/env python3
"""Private original-pixel importer. Public outputs are metadata/code only.
No resizing, recoloring or image re-encoding. Unmanaged/user-edited files are never overwritten/deleted.
"""
import argparse,csv,hashlib,json,os,re,struct,zipfile
from pathlib import Path,PurePosixPath
ROOT=Path(__file__).resolve().parents[3]
EXPECTED='2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
PREFIX='assets/morefunquicksandmod/'
def sha(data):return hashlib.sha256(data).hexdigest()
def jsonbytes(value):return (json.dumps(value,indent=2,ensure_ascii=False)+'\n').encode()
def alias(path):
 tail=path.split('textures/',1)[-1]
 return 'assets/mfqm/textures/'+('block/original/'+tail.split('/',1)[1] if tail.startswith('blocks/')else'original/'+tail).lower()
def png_info(data,sidecar=None):
 w,h,depth,color=struct.unpack('>IIBB',data[16:26]);offset=8;trns=False
 while offset<len(data):
  n=struct.unpack('>I',data[offset:offset+4])[0];kind=data[offset+4:offset+8];trns|=kind==b'tRNS';offset+=12+n
 anim=(sidecar or{}).get('animation');layout='STATIC_OR_SHEET_UNRESOLVED';frames=''
 if anim is not None:
  fw=anim.get('width',w);fh=anim.get('height',w);frames=str((w//fw)*(h//fh));layout=f'{fw}x{fh} frames; original sidecar copied verbatim'
 elif w==h:layout='STATIC_SQUARE';frames='1'
 return dict(width=w,height=h,png_color_type=color,alpha_channel=color in[4,6],palette_or_color_transparency=trns,frame_layout=layout,frame_count=frames)
def source_for(spec):
 p=ROOT/'research/original-phase3/evidence/source'/(spec['legacy_class']+'.cfr.txt')
 return p if p.exists()else None
def plan(jar):
 output={};mapping=[];inventory=[];bindings={};catalog=json.loads((ROOT/'forge-1.20.1/src/main/resources/data/mfqm/legacy_block_catalog.json').read_text(encoding='utf-8'))
 with zipfile.ZipFile(jar)as z:
  names=set(z.namelist());target_sources={}
  for name in sorted(names):
   if not name.startswith(PREFIX)or name.endswith('/'):continue
   data=z.read(name);cat='other'
   if '/textures/blocks/'in name:cat='block'
   elif '/textures/items/'in name:cat='item'
   elif '/textures/entity/'in name:cat='entity_overlay'if 'mud' in name.lower()else'entity'
   elif any(x in name.lower()for x in ['gui','logo','icons']):cat='GUI'
   elif '/sounds/'in name:cat='sound'
   row=dict(original_path=name,original_sha256=sha(data),bytes=len(data),category=cat,original_case_preserved=True)
   if name.endswith('.png'):
    meta=json.loads(z.read(name+'.mcmeta'))if name+'.mcmeta'in names else None;row.update(png_info(data,meta));row['sidecar']=name+'.mcmeta'if meta is not None else''
    row['sidecar_json']=json.dumps(meta,separators=(',',':'))if meta is not None else''
   inventory.append(row)
  def texture(spec,old,usage,evidence,status='CONFIRMED',blocker=''):
   original=PREFIX+'textures/blocks/'+old+'.png';target=alias(original)
   if original not in names:raise ValueError('Missing exact-case original texture '+original)
   if target in target_sources and target_sources[target]!=original:raise ValueError('Case-fold target collision')
   target_sources[target]=original
   mapping.append(dict(original_path=original,original_sha256=sha(z.read(original)),new_registry_id='mfqm:'+spec['id'],target_resource_path=target,usage=usage,mapping_evidence=evidence,status=status,blocker=blocker))
   if status=='CONFIRMED':
    output[target]=z.read(original)
    if original+'.mcmeta'in names:output[target+'.mcmeta']=z.read(original+'.mcmeta')
   return 'mfqm:'+target.split('/textures/',1)[1][:-4]
  for spec in catalog:
   p=source_for(spec);text=p.read_text(encoding='utf-8')if p else'';lines=text.splitlines();icons=[]
   for i,line in enumerate(lines,1):
    if 'func_94245_a('in line:
     for old in re.findall(r'func_94245_a\("morefunquicksandmod:([^"+]+)"\)',line):icons.append((old,f'{p.relative_to(ROOT)}:{i} registerIcon + original getIcon reviewed'))
   ident=spec['id'];confirmed=False;model=ROOT/f'forge-1.20.1/src/main/resources/assets/mfqm/models/block/{ident}.json'
   if ident=='soft_quicksand':
    assert 'Math.min(Math.max(par2, 0), 2)'in text
    chosen=next(t for t in icons if t[0]=='SoftQuicksand1');tex=texture(spec,*[chosen[0],'block/default-metadata0-and-inventory',chosen[1]])
    for name in ['soft_quicksand','soft_quicksand_full']:
     m=json.loads((model.parent/(name+'.json')).read_text(encoding='utf-8'));m['textures']={'all':tex,'particle':tex};output[f'assets/mfqm/models/block/{name}.json']=jsonbytes(m)
    for old,evidence in icons:
     if old!='SoftQuicksand1':texture(spec,old,'metadata1-or2',evidence,'UNRESOLVED','Modern block has FILLED, no original metadata1/2 selector; not flattened into default')
    confirmed=True
   elif spec['fluid'] and len(icons)==2 and icons[0][0].endswith('_Still')and icons[1][0].endswith('_Flowing'):
    still=texture(spec,icons[0][0],'fluid-still',icons[0][1]);flow=texture(spec,icons[1][0],'fluid-flowing',icons[1][1]);bindings[ident]={'still':still,'flowing':flow,'tint':-1};confirmed=True
    # Original getIcon uses still for top/bottom and flowing for sides; modern item geometry stays provisional.
    output[f'assets/mfqm/models/block/{ident}.json']=jsonbytes({'parent':'minecraft:block/cube_bottom_top','textures':{'bottom':still,'top':still,'side':flow,'particle':still}})
    mapping.append(dict(original_path=PREFIX+'textures/blocks/'+icons[0][0]+'.png',original_sha256=sha(z.read(PREFIX+'textures/blocks/'+icons[0][0]+'.png')),new_registry_id='mfqm:'+ident,target_resource_path=f'assets/mfqm/models/block/{ident}.json',usage='block-item-and-particle-model',mapping_evidence=icons[0][1]+'; original getIcon top/bottom still, side flowing',status='PARTIAL_RENDER_GEOMETRY',blocker='Textures bound; modern cube inventory geometry is not claimed original item rendering'))
   elif len(icons)==1 and spec['kind']in['SINKING','SOLID','LEAVES'] and ident not in['temp_vore','temp_meat']:
    tex=texture(spec,icons[0][0],'block/default-and-inventory',icons[0][1]);m=json.loads(model.read_text(encoding='utf-8'));m['textures']={'all':tex,'particle':tex}
    # Original transparent pixels remain unchanged; JSON render layer is a modern compatibility choice.
    if ident=='leaves_pile':m['render_type']='minecraft:cutout'
    output[f'assets/mfqm/models/block/{ident}.json']=jsonbytes(m);confirmed=True
   if not confirmed:
    for old,evidence in icons:texture(spec,old,'multi-face/metadata/special-renderer',evidence,'UNRESOLVED','Face/variant/custom-render selection not closed; existing placeholder retained')
    if not icons:mapping.append(dict(original_path='',original_sha256='',new_registry_id='mfqm:'+ident,target_resource_path='',usage='inherited-vanilla'if ident in['sandstone_trap','sinking_rug','custom_lily_pad']else'block/item',mapping_evidence=str(p.relative_to(ROOT))if p else'catalog only',status='VANILLA_INTENTIONAL_PARTIAL'if ident in['sandstone_trap','sinking_rug','custom_lily_pad']else'UNRESOLVED',blocker='Original inherits BlockSandStone/BlockColored/BlockLilyPad; keep vanilla design; metadata/face/geometry parity still partial'if ident in['sandstone_trap','sinking_rug','custom_lily_pad']else'Dynamic/custom registration requires explicit proof; no guessed texture'))
   if spec['fluid']:mapping.append(dict(original_path='',original_sha256='',new_registry_id='mfqm:'+ident+'_bucket',target_resource_path='',usage='bucket-item',mapping_evidence='LegacyFluids/modern item model + original item renderer not closed',status='UNRESOLVED',blocker='Still/flowing mapping does not prove bucket item appearance'))
  import sys
  sys.path.insert(0,str(ROOT/'reconstruction/tooling/r1'))
  from private_models import overlay
  catalog_path=ROOT/'forge-1.20.1/src/main/resources/data/mfqm/r1_content.json'
  overlay(z,json.loads(catalog_path.read_text(encoding='utf-8')),output)
  output['assets/mfqm/original_texture_bindings.json']=jsonbytes({'mode':'PRIVATE_ORIGINAL_ASSETS_BUILD','original_jar_sha256':EXPECTED,'fluids':bindings})
 for row in inventory:
  original=row['original_path'];base=original[:-7]if original.endswith('.mcmeta')else original
  uses=[m for m in mapping if m['original_path']==base]
  row.update(new_registry_id=';'.join(sorted({m['new_registry_id']for m in uses})),target_resource_path=';'.join(sorted({m['target_resource_path']for m in uses})),usage=';'.join(sorted({m['usage']for m in uses})),mapping_evidence=';'.join(sorted({m['mapping_evidence']for m in uses})),status=('CONFIRMED'if all(m['status']=='CONFIRMED'for m in uses)else'PARTIAL_MULTIPLE_USAGES')if uses else'UNRESOLVED',blocker=';'.join(sorted({m['blocker']for m in uses if m['blocker']}))if uses else'No confirmed current renderer/registry binding; metadata only')
 return output,inventory,mapping

def output_root(path):
 p=path.resolve();private=(ROOT/'local-original-assets').resolve()
 if p==ROOT or ROOT in p.parents:
  if p!=private and private not in p.parents:raise ValueError('In-repo private output must be under ignored local-original-assets/')
 else:
  if any((x/'.git').exists()for x in[p,*p.parents]):raise ValueError('Outside output cannot target another Git worktree')
 return p
def write_csv(path,rows):
 keys=list(dict.fromkeys(k for row in rows for k in row));path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('w',newline='',encoding='utf-8')as f:w=csv.DictWriter(f,fieldnames=keys,lineterminator='\n');w.writeheader();w.writerows(rows)
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--jar',type=Path,default=os.environ.get('MFQM_ORIGINAL_JAR'));ap.add_argument('--output',type=Path,default=ROOT/'local-original-assets/resources');ap.add_argument('--dry-run',action='store_true');ap.add_argument('--verify',action='store_true');ap.add_argument('--clean-generated',action='store_true');ap.add_argument('--audit',action='store_true');a=ap.parse_args();dest=output_root(a.output);manifest=dest/'.mfqm-import-manifest.json';prior=json.loads(manifest.read_text(encoding='utf-8'))if manifest.exists()else{'files':{}}
 # Validate every registered path before reading or deleting any generated file.
 for rel in prior['files']:
  p=PurePosixPath(rel)
  if p.is_absolute()or'..'in p.parts or'\\'in rel or not str(p).startswith('assets/mfqm/'):raise ValueError('Unsafe ownership manifest path')
 for rel in [*prior['files'],'.mfqm-import-manifest.json']:
  target=(dest/rel).resolve()
  if dest not in target.parents:raise ValueError('SYMLINK_ESCAPE_PRESERVED: '+rel)
 if a.clean_generated:
  conflicts=[rel for rel,h in prior['files'].items()if(dest/rel).exists()and sha((dest/rel).read_bytes())!=h]
  if conflicts:raise ValueError('USER_EDITED_FILES_PRESERVED: '+str(conflicts))
  if not a.dry_run:
   for rel in prior['files']:
    p=dest/rel
    if p.exists():p.unlink()
   if manifest.exists():manifest.unlink()
  print(json.dumps({'mode':'CLEAN_PLAN'if a.dry_run else'CLEAN_GENERATED','owned_files':len(prior['files']),'unmanaged_files':'untouched'}));return
 if a.jar is None:ap.error('BLOCKED_PRIVATE_INPUT: supply --jar or MFQM_ORIGINAL_JAR')
 jar=Path(a.jar).resolve();before=sha(jar.read_bytes())
 if before!=EXPECTED:raise ValueError('Original JAR SHA mismatch; no substitute assets accepted')
 files,inventory,mapping=plan(jar)
 if a.audit:
  write_csv(ROOT/'docs/phase9/ORIGINAL_ASSET_INVENTORY.csv',inventory);write_csv(ROOT/'docs/phase9/TEXTURE_MAPPING.csv',mapping)
 # All target IDs must use modern lowercase paths, and every generated mfqm texture reference must resolve.
 for rel in files:
  if rel!=rel.lower()or'..'in PurePosixPath(rel).parts:raise ValueError('Invalid modern resource path')
 for rel,data in files.items():
  if rel.endswith('.json')and'/models/'in rel:
   for value in json.loads(data).get('textures',{}).values():
    if value.startswith('mfqm:'):
     target='assets/mfqm/textures/'+value.split(':',1)[1]+'.png'
     if target not in files:raise ValueError('Missing generated model texture '+target)
 if a.verify:
  if not manifest.exists():raise ValueError('No owned import manifest')
  if prior['files']!={k:sha(v)for k,v in files.items()}:raise ValueError('Manifest differs from deterministic original plan')
  for rel,data in files.items():
   if not(dest/rel).is_file()or(dest/rel).read_bytes()!=data:raise ValueError('Generated bytes changed/missing: '+rel)
  print(json.dumps({'status':'VERIFIED_ORIGINAL_BYTES_AND_REFERENCES','files':len(files),'original_jar_unchanged':sha(jar.read_bytes())==before}));return
 for rel in files:
  if dest not in (dest/rel).resolve().parents:raise ValueError('SYMLINK_ESCAPE_PRESERVED: '+rel)
 conflicts=[rel for rel,data in files.items()if(dest/rel).exists()and(dest/rel).read_bytes()!=data and(rel not in prior['files']or sha((dest/rel).read_bytes())!=prior['files'][rel])]
 if conflicts:raise ValueError('UNMANAGED_OR_USER_EDITED_FILES_PRESERVED: '+str(conflicts))
 if not a.dry_run:
  for rel,data in files.items():
   p=dest/rel;p.parent.mkdir(parents=True,exist_ok=True)
   if not p.exists()or p.read_bytes()!=data:p.write_bytes(data)
  manifest.write_bytes(jsonbytes({'mode':'PRIVATE_ORIGINAL_ASSETS_BUILD','original_jar_sha256':before,'files':{k:sha(v)for k,v in sorted(files.items())}}))
 assert sha(jar.read_bytes())==before
 print(json.dumps({'mode':'DRY_RUN'if a.dry_run else'PRIVATE_IMPORT','files':len(files),'pngs':sum(k.endswith('.png')for k in files),'confirmed_registry_ids':len({x['new_registry_id']for x in mapping if x['status']=='CONFIRMED'}),'output':str(dest),'private_artifact':'NOT_FOR_PUBLIC_DISTRIBUTION'},indent=2))
if __name__=='__main__':main()
