#!/usr/bin/env python3
"""Read-only original class inventory, actual JVM descriptors and bytecode edges. Requires jawa2.2.0."""
import argparse,zipfile,io,json,collections,re
from pathlib import Path
from common import *
from jawa.cf import ClassFile
from importlib.metadata import version
EXPECTED='2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
def ref(c):
 if hasattr(c,'class_')and hasattr(c,'name_and_type'):return (c.class_.name.value,c.name_and_type.name.value,c.name_and_type.descriptor.value)
 return None
def extract(jar,root,out):
 digest=sha(jar.read_bytes());assert digest==EXPECTED,'Original input differs; do not mix versions'
 files=[];classes=[];methods=[];fields=[];edges=[];resources=[];entry=[]
 with zipfile.ZipFile(jar)as z:
  names=[i.filename for i in z.infolist()if not i.is_dir()]
  assert len(names)==len(set(names)),'Duplicate archive entries'
  assert len(names)==len(set(n.lower()for n in names)),'Case collisions'
  for n in sorted(names):
   info=z.getinfo(n);b=z.read(n);fid=ident('file',n);kind='CLASS'if n.endswith('.class')else'PNG'if n.endswith('.png')else'ANIMATION'if n.endswith('.mcmeta')else'SOUND'if n.endswith('.ogg')else'LANGUAGE'if n.endswith('.lang')else'METADATA'if not n.startswith('assets/')else'OTHER'
   row=dict(original_file_id=fid,path=n,size=len(b),crc32=f'{info.CRC:08x}',sha256=sha(b),kind=kind,status='UNRESOLVED',input_sha256=digest);files.append(row)
   if n.startswith('assets/'):resources.append(row)
   if not n.endswith('.class'):continue
   c=ClassFile(io.BytesIO(b));name=c.this.name.value;cid=ident('class',name);ev='research/task-001/evidence/'+name.replace('/','__')+'.bytecode.txt'
   # Historical text is a locator, not the input to the class/member extraction.
   if not(root/ev).exists():ev='private:'+n
   attrs=lambda table:';'.join(c.constants.get(a[0]).value if isinstance(a,tuple)else a.name.value for a in table._table)
   classes.append(dict(class_id=cid,original_file_id=fid,class_name=name,super=c.super_.name.value,interfaces=';'.join(x.name.value for x in c.interfaces),sha256=sha(b),access=c.access_flags.value,attributes=attrs(c.attributes),evidence_ref=ev,status='BYTECODE_INDEXED_SEMANTICS_PARTIAL',archive_path=n,dossier_path='docs/reconstruction/original/classes/'+name+'.md'))
   for f in c.fields:
    symbol=name+'#'+f.name.value+':'+f.descriptor.value
    fields.append(dict(member_id=ident('field',symbol),class_id=cid,owner=name,name=f.name.value,descriptor=f.descriptor.value,access=f.access_flags.value,attributes=attrs(f.attributes),evidence_ref=ev,status='BYTECODE_CONFIRMED_SIGNATURE_ONLY'))
   for m in c.methods:
    symbol=name+'#'+m.name.value+m.descriptor.value;mid=ident('method',symbol);instructions=list(m.code.disassemble())if m.code else[]
    methods.append(dict(member_id=mid,class_id=cid,owner=name,name=m.name.value,descriptor=m.descriptor.value,access=m.access_flags.value,code_bytes=len(m.code._code)if m.code else 0,code_sha256=sha(m.code._code)if m.code else'',instruction_count=len(instructions),attributes=attrs(m.attributes),evidence_ref=ev,analysis_status='NOT_ANALYZED',evidence_type='BYTECODE_CONFIRMED_SIGNATURE_AND_EDGES'))
    for ins in instructions:
     for operand in ins.operands:
      if getattr(getattr(operand,'op_type',None),'name',None)!='CONSTANT_INDEX':continue
      constant=c.constants.get(operand.value);target=ref(constant)
      if target:
       owner,method,desc=target;tk='method'if desc.startswith('(')else'field';targetid=ident(tk,owner+'#'+method+(''if tk=='method'else':')+desc)
       edges.append(dict(edge_id=ident('edge',symbol+'@'+str(ins.pos)),caller_id=mid,offset=ins.pos,opcode=ins.mnemonic,target_id=targetid,target_owner=owner,target_name=method,target_descriptor=desc,evidence_ref=ev,scope='INTERNAL'if owner.startswith('MoreFunQuicksandMod/')else'EXTERNAL'))
    if any(x in attrs(m.attributes)for x in ['Annotations'])or m.name.value in ['preInit','init','postInit','generate']:
     entry.append(dict(entry_id=mid,class_id=cid,name=m.name.value,descriptor=m.descriptor.value,attributes=attrs(m.attributes),status='ENTRY_CANDIDATE_ANNOTATIONS_NOT_DECODED',evidence_ref=ev))
 for name,rows in [('ORIGINAL_JAR_FILES',files),('ORIGINAL_CLASSES',classes),('ORIGINAL_METHODS',methods),('ORIGINAL_FIELDS',fields),('ORIGINAL_RESOURCES',resources),('ORIGINAL_ENTRYPOINTS',entry)]:write(out/'manifest'/(name+'.csv'),rows)
 write(out/'mapping/CALL_GRAPH.csv',edges)
 assert sha(jar.read_bytes())==digest
 dump(out/'checks/ORIGINAL_INPUT.json',dict(JAR_INDEPENDENTLY_VERIFIED=True,sha256=digest,files=len(files),classes=len(classes),methods=len(methods),fields=len(fields),resources=len(resources),edges=len(edges),tool='jawa '+version('jawa'),directories_excluded=True,method_body_read_errors=0,unknown_semantics_not_excluded=True))
 return classes,methods,fields
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--input-jar',type=Path,required=True);p.add_argument('--repo-root',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();extract(a.input_jar,a.repo_root,a.out_dir)
