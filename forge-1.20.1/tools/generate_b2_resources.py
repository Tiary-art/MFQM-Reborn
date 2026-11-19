#!/usr/bin/env python3
"""Generate legal vanilla-only fallback resources from immutable legacy ID evidence."""
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1];res=root/'src/main/resources'
entries=json.loads((res/'data/mfqm/legacy_block_catalog.json').read_text())
def write(path,data):
 path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
langs={code:json.loads((res/f'assets/mfqm/lang/{code}.json').read_text()) for code in ['en_us','zh_cn']}
for s in entries:
 id=s['id'];key='block.mfqm.'+id
 if id not in ['quicksand','mud','soft_quicksand']:
  langs['en_us'][key]=s['legacy_id']+' (vanilla placeholder)'
  langs['zh_cn'][key]=s['legacy_id']+'（暂用原版材质）'
  texture='minecraft:block/'+s['texture'];kind=s['kind']
  model={'parent':'minecraft:block/cube_all','textures':{'all':texture}}
  if kind in ['PLANT','LILY']:model={'parent':'minecraft:block/cross','textures':{'cross':texture}}
  if kind=='LEAVES':model={'textures':{'all':texture,'particle':texture},'elements':[{'from':[0,0,0],'to':[16,s['height']*16,16],'faces':{d:{'texture':'#all'} for d in ['down','up','north','south','west','east']}}]}
  variants={'':{'model':'mfqm:block/'+id}}
  if kind=='SLAB':
   model={'parent':'minecraft:block/slab','textures':{'bottom':texture,'top':texture,'side':texture}}
   write(res/f'assets/mfqm/models/block/{id}_top.json',{'parent':'minecraft:block/slab_top','textures':{'bottom':texture,'top':texture,'side':texture}})
   write(res/f'assets/mfqm/models/block/{id}_double.json',{'parent':'minecraft:block/cube_all','textures':{'all':texture}})
   variants={f'type={t}':{'model':'mfqm:block/'+id+suffix} for t,suffix in [('bottom',''),('top','_top'),('double','_double')]}
  write(res/f'assets/mfqm/models/block/{id}.json',model)
  write(res/f'assets/mfqm/blockstates/{id}.json',{'variants':variants})
  write(res/f'assets/mfqm/models/item/{id}.json',{'parent':'mfqm:block/'+id})
  loot={'type':'minecraft:block','pools':[]}
  if s['drop']=='SELF':loot['pools']=[{'rolls':1,'entries':[{'type':'minecraft:item','name':'mfqm:'+id}],'conditions':[{'condition':'minecraft:survives_explosion'}]}]
  write(res/f'data/mfqm/loot_tables/blocks/{id}.json',loot)
for code,data in langs.items():data['itemGroup.mfqm']='MFQM — Materials' if code=='en_us' else 'MFQM — 材料';write(res/f'assets/mfqm/lang/{code}.json',data)
write(res/'data/minecraft/tags/blocks/mineable/shovel.json',{'replace':False,'values':['mfqm:'+s['id'] for s in entries if s['kind'] in ['SINKING','VISCOUS']]})
print(f'Generated resource references for {len(entries)} verified legacy Block IDs; no PNG/OGG copied.')
