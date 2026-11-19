#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from common import *
p=argparse.ArgumentParser();p.add_argument('--repo-root',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();r=a.repo_root.resolve();assets=r/'forge-1.20.1/src/main/resources/assets';rows=[]
private={x['target_resource_path']for x in read(r/'docs/phase9/TEXTURE_MAPPING.csv')if x['status']=='CONFIRMED'}
def add(p,key,value,kind):
 if not isinstance(value,str)or value.startswith('#'):return
 ns,sep,path=value.partition(':')
 if not sep:ns='minecraft';path=value
 target='assets/'+ns+'/'+('textures/'+path+'.png'if kind=='texture'else'models/'+path+'.json')
 present=(assets.parent/target).is_file()
 rows.append(dict(reference_id=ident('resource-ref',str(p.relative_to(r))+key+value),source=str(p.relative_to(r)),json_key=key,resource=value,kind=kind,target_path=target,status='EXTERNAL_VANILLA'if ns!='mfqm'else'PRESENT_NOT_RENDER_VERIFIED'if present else'PRIVATE_IMPORT_REQUIRED_NOT_PACKAGING_PROOF'if target in private else'MISSING_OR_DYNAMIC_UNRESOLVED',evidence_ref=str(p.relative_to(r))))
for p in sorted((assets/'mfqm').rglob('*.json')):
 doc=json.loads(p.read_text(encoding='utf-8'))
 def walk(obj,path=''):
  if isinstance(obj,dict):
   for k,v in obj.items():
    if k in['parent','model']:add(p,path+'/'+k,v,'model')
    if k=='textures'and isinstance(v,dict):
     for tk,tv in v.items():add(p,path+'/textures/'+tk,tv,'texture')
    walk(v,path+'/'+k)
  elif isinstance(obj,list):
   for i,v in enumerate(obj):walk(v,path+'/'+str(i))
 walk(doc)
write(a.out_dir/'mapping/RESOURCE_REFERENCE_GRAPH.csv',rows)
