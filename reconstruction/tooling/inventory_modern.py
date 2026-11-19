#!/usr/bin/env python3
import argparse,re,json,io
from pathlib import Path
from common import *
from jawa.cf import ClassFile

def run(root,out):
 base=root/'forge-1.20.1';rows=[];members=[];regs=[];freeze=[];refs=[];edges=[]
 for path in sorted(base.rglob('*')):
  if not path.is_file()or any(x in path.relative_to(base).parts for x in ['build','run','.gradle','logs','docs']):continue
  if path.suffix not in['.java','.json','.toml','.properties','.gradle','.mcmeta','.png','.ogg']:continue
  rel=str(path.relative_to(root));kind='JAVA'if path.suffix=='.java'else'RESOURCE_CONFIG';text=path.read_text(encoding='utf-8')if path.suffix not in['.png','.ogg']else''
  role='DEV_ONLY'if'/gametest/'in rel or'/test/'in rel or'/diagnostic/'in rel or'Probe'in rel else'MODERN_BRIDGE'if any(x in rel for x in ['/network/','/registry/','/client/OriginalTextureBindings'])else'UNKNOWN'
  rows.append(dict(modern_id=ident('modern-file',rel),path=rel,kind=kind,sha256=sha(path.read_bytes()),role=role,original_refs='N/A'if role in['DEV_ONLY','MODERN_BRIDGE']else'UNKNOWN',status='INVENTORIED_NOT_PARITY_VERIFIED'))
  for i,line in enumerate(text.splitlines(),1):
   if any(x in line for x in ['registerMessage','messageBuilder','BooleanProperty.create','IntegerProperty.create','define(','putInt(','putBoolean(','putFloat(','getOrCreateTag','getPersistentData','ResourceLocation','CHANNEL_NAME','.define','putString(','getString(','getInt(','PROTOCOL']):
    freeze.append(dict(freeze_id=ident('freeze',rel+':'+str(i)),path=rel,line=i,expression=line.strip(),status='DO_NOT_RENAME_WITHOUT_MIGRATION',reason='Registry/state/config/save/network candidate; explicit review required'))
   for value in re.findall(r'"((?:minecraft|mfqm):[^"\s]+)"',line):refs.append(dict(reference_id=ident('ref',rel+':'+str(i)+value),path=rel,line=i,resource=value,status='EXTERNAL_VANILLA'if value.startswith('minecraft:')else'UNVERIFIED_USAGE',evidence_ref=rel))
 # Expand actual DeferredRegister loop source, not the catalog alone; dynamic event resolution remains separate.
 catalog=json.loads((base/'src/main/resources/data/mfqm/legacy_block_catalog.json').read_text(encoding='utf-8'))
 def reg(kind,id,source):
  regs.append(dict(modern_id=ident('registry',kind+':mfqm:'+id),kind=kind,registry_id='mfqm:'+id,source=source,status='SOURCE_RESOLVED_RUNTIME_ENUMERATION_NOT_RUN'))
  freeze.append(dict(freeze_id=ident('freeze',kind+':'+id),path=source,line='',expression=kind+' mfqm:'+id,status='FROZEN_EXISTING_ID',reason='Existing save compatibility'))
 for s in catalog:
  for kind,f in [('BLOCK','ModBlocks'),('ITEM','ModItems')]:reg(kind,s['id'],'forge-1.20.1/src/main/java/art/tiary/mfqm/registry/'+f+'.java')
  if s['fluid']:
   for kind,id in[('FLUID_TYPE',s['id']),('FLUID',s['id']),('FLUID','flowing_'+s['id']),('ITEM',s['id']+'_bucket')]:reg(kind,id,'forge-1.20.1/src/main/java/art/tiary/mfqm/content/LegacyFluids.java')
 for kind in['BLOCK','ITEM']:reg(kind,'dev_test_block','forge-1.20.1/src/main/java/art/tiary/mfqm/registry/Mod'+('Blocks'if kind=='BLOCK'else'Items')+'.java')
 reg('CREATIVE_TAB','materials','forge-1.20.1/src/main/java/art/tiary/mfqm/registry/ModTabs.java')
 for prefix in ['main','test']:
  for p in sorted((base/'build/classes/java'/prefix).rglob('*.class')):
   c=ClassFile(io.BytesIO(p.read_bytes()));owner=c.this.name.value
   for table,kind in[(c.methods,'METHOD'),(c.fields,'FIELD')]:
    for m in table:
     symbol=owner+'#'+m.name.value+(':'if kind=='FIELD'else'')+m.descriptor.value
     members.append(dict(modern_id=ident('modern-member',symbol),kind=kind,owner=owner,name=m.name.value,descriptor=m.descriptor.value,access=m.access_flags.value,build_scope=prefix,modern_path=str((base/'src'/prefix/'java'/(owner.split('$')[0]+'.java')).relative_to(root)),status='COMPILED_SIGNATURE_ONLY',original_refs='UNKNOWN'))
     if kind=='METHOD'and m.code:
      for ins in m.code.disassemble():
       for operand in ins.operands:
        if getattr(getattr(operand,'op_type',None),'name',None)!='CONSTANT_INDEX':continue
        value=c.constants.get(operand.value)
        if hasattr(value,'class_')and hasattr(value,'name_and_type'):
         target=value.class_.name.value+'#'+value.name_and_type.name.value+(''if value.name_and_type.descriptor.value.startswith('(')else':')+value.name_and_type.descriptor.value
         edges.append(dict(caller_id=ident('modern-member',symbol),offset=ins.pos,opcode=ins.mnemonic,target_symbol=target,status='COMPILED_DIRECT_REFERENCE_DYNAMIC_DISPATCH_UNKNOWN'))
 write(out/'mapping/MODERN_CALL_GRAPH.csv',edges)
 write(out/'manifest/NEW_PROJECT_INVENTORY.csv',rows);write(out/'manifest/MODERN_MEMBERS.csv',members);write(out/'manifest/MODERN_REGISTRY.csv',regs);write(out/'mapping/COMPATIBILITY_FREEZE.csv',freeze);write(out/'mapping/MODERN_RESOURCE_REFERENCES.csv',refs)
 return rows,regs
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo-root',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();run(a.repo_root.resolve(),a.out_dir)
