#!/usr/bin/env python3
import argparse,csv,json,re,subprocess,hashlib
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--phase1-work',type=Path,required=True);ap.add_argument('--java-home',type=Path,required=True);a=ap.parse_args();root=Path(__file__).resolve().parents[2];repo=root.parents[1];rows=list(csv.DictReader((repo/'research/original-phase3/01_ALL_SINKABLE_MATERIALS.csv').open()));rows=[x for x in rows if x['record_kind']=='BLOCK_SCOPE'and x['sinkability'].startswith('UNKNOWN')]
srg=a.phase1_work/'joined.srg';jar=a.phase1_work/'minecraft-1.7.10-client.jar';maps={}
for line in srg.read_text().splitlines():
 if line.startswith('CL: '):_,obf,named=line.split();maps[named.replace('/','.')]=obf
cache={}
def read(named):
 if named in cache:return cache[named]
 obf=maps[named];p=subprocess.run([str(a.java_home/'bin/javap'),'-p','-c','-s','-classpath',str(jar),obf],text=True,capture_output=True);assert p.returncode==0,p.stderr;text=p.stdout;(root/'evidence/results'/('vanilla-'+obf+'.javap.txt')).write_text(text)
 decl=next(l for l in text.splitlines()if re.match(r'public (?:abstract )?class ',l));m=re.search(r' extends ([\w.$]+)',decl);parent=m[1]if m else'java.lang.Object';parent=next((n for n,o in maps.items()if o==parent),parent)
 hit=re.search(r'public void a\(ahb, int, int, int, sa\);\s+descriptor: \(Lahb;IIILsa;\)V\s+Code:\s+0: return',text)
 descriptor_exists='descriptor: (Lahb;IIILsa;)V'in text
 result={'class':named,'obfuscated':obf,'parent':parent,'contact_declared':descriptor_exists,'contact_verified_empty':bool(hit),'evidence':'evidence/results/vanilla-'+obf+'.javap.txt'};cache[named]=result;return result
out=[]
for x in rows:
 chain=[];name=x['parent'];terminal=None
 while name in maps:
  t=read(name);chain.append(t)
  if t['contact_declared']:terminal=t;break
  name=t['parent']
 assert terminal and terminal['contact_verified_empty'],(x['legacy_registration'],chain)
 out.append({'object':x['legacy_registration'],'mod_class':x['legacy_class'],'vanilla_parent_chain':chain,'contact_fact':'inherits Vanilla Block contact method: offset0 return','boundary':'Forge1.7.10 patch and external event/callback effects not verified; not a declaration that the block has no gameplay effects','status':'STATIC_VERIFIED_VANILLA_CHAIN; full Forge environment UNRESOLVED'})
(root/'evidence/results/ten-contact-inheritance.json').write_text(json.dumps({'objects':out,'vanilla_client_sha256':hashlib.sha256(jar.read_bytes()).hexdigest(),'srg_sha256':hashlib.sha256(srg.read_bytes()).hexdigest(),'original_mod_runtime':'NOT_RUN'},ensure_ascii=False,indent=2)+'\n');print('10 Vanilla contact inheritance paths verified; Forge patches remain unresolved')
