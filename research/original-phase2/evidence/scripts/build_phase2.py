#!/usr/bin/env python3
"""Phase2 static evidence index + conservative CFG. Does NOT run original gameplay."""
from pathlib import Path
import argparse,json,csv,re,hashlib,collections,shutil
p=argparse.ArgumentParser();p.add_argument('--phase1',type=Path,required=True);p.add_argument('--cfr',type=Path,required=True);p.add_argument('--work',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();r=a.out
for d in ['evidence/cfg','evidence/bytecode','evidence/source-methods','evidence/indexes','evidence/logs','evidence/pseudocode']:(r/d).mkdir(parents=True,exist_ok=True)
methods=json.loads((a.phase1/'indexes/methods-with-instructions.json').read_text());calls=list(csv.DictReader((a.phase1/'indexes/calls.csv').open()));allraw=(a.phase1/'evidence/fresh-javap-all.txt').read_text().splitlines()
core={'CustomWorldGen','CustomWorldGenLakes','CustomGenerationEvent','GenerateDesertTombs','GenerateMucusBlossom'}
selected=[m for m in methods if m['class'].split('.')[-1]in core]
def writecsv(path,rows,fields=None):
 rows=list(rows)
 with (r/path).open('w',newline='')as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def saved(path,x):(r/path).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
# Split readable CFR methods by a declaration starting in column4; braces are balanced lexically.
source={};source_meta={}
for c in core:
 text=(a.cfr/(c+'.java')).read_text();lines=text.splitlines();matches=list(re.finditer(r'^    (?:public|private|protected) (?:static )?[^\n;=]+\([^\n]*\) \{',text,re.M))
 for i,m in enumerate(matches):
  start=m.start();j=m.end();depth=1;quote=None;escape=False
  while j<len(text)and depth:
   ch=text[j]
   if quote:
    if escape:escape=False
    elif ch=='\\':escape=True
    elif ch==quote:quote=None
   elif ch in ['"',"'"]:quote=ch
   elif ch=='{':depth+=1
   elif ch=='}':depth-=1
   j+=1
  name=re.search(r'(\w+)\(',m.group()).group(1);body=text[start:j];key=(c,name)
  if key not in source:source[key]=body;source_meta[key]=text[:start].count('\n')+1
  else:source[key]+='\n// OVERLOAD\n'+body
# verbose bytecode retains exception/local variable tables. Store a complete targeted copy.
v=(a.work/'worldgen-javap-v.txt').read_text();(r/'evidence/bytecode/worldgen-javap-v.txt').write_text(v)
# Parse exception tables by class/method descriptor; exact declaration names match the phase1 inventory.
exc=collections.defaultdict(list);curclass=None;name=None;desc=None;inexc=False
for line in v.splitlines():
 cm=re.match(r'public class ([\w.$]+)',line)
 if cm:curclass=cm.group(1);name=None
 if re.match(r'^  (?:public|private|protected) ',line) and '('in line and line.strip().endswith(';'):
  x=re.search(r'(\S+)\(',line.strip());name=x.group(1);name='<init>'if name==curclass else name;desc=None;inexc=False
 if name and line.strip().startswith('descriptor:'):desc=line.split('descriptor:',1)[1].strip()
 if line.strip()=='Exception table:':inexc=True;continue
 if inexc:
  x=re.match(r'\s+(\d+)\s+(\d+)\s+(\d+)\s+(.+)',line)
  if x and curclass and name and desc:exc[(curclass,name,desc)].append({'from':int(x[1]),'to':int(x[2]),'target':int(x[3]),'type':x[4]})
  elif line.strip()and not line.strip().startswith('from'):inexc=False
index=[];constants=[];rng=[];dispatch=[];writes=[];parameters=[];cfgsummary=[]
for m in selected:
 c=m['class'].split('.')[-1];n=m['name'];ins=m['instructions'];slug=c+'__'+n.replace('<','').replace('>','');safe=slug
 if any(x['slug']==slug for x in index):safe+='__'+hashlib.sha1(m['descriptor'].encode()).hexdigest()[:8]
 end=ins[-1]['offset']if ins else 0;leaders={ins[0]['offset']}if ins else set();targets={};offsets={x['offset']for x in ins};handlers=exc[(m['class'],n,m['descriptor'])]
 for idx,i in enumerate(ins):
  op=i['opcode'];to=[]
  if op.startswith('if')or op in ['goto','goto_w','jsr','jsr_w']:to=[int(i['args'].split()[0])]
  elif op in ['tableswitch','lookupswitch']:
   for line in allraw[i['javap_line']:]:
    if '}'in line:break
    mt=re.match(r'\s+(?:-?\d+|default):\s+(\d+)',line)
    if mt:to.append(int(mt.group(1)))
  if to:
   assert all(t in offsets for t in to),(c,n,i,to)
   targets[i['offset']]=sorted(set(to));leaders.update(to)
  if (to or op.endswith('return')or op in ['return','athrow'])and idx+1<len(ins):leaders.add(ins[idx+1]['offset'])
  if any(s in i['args']for s in ['// int ','// double ','// float ','// long ']):constants.append({'class':m['class'],'method':n,'descriptor':m['descriptor'],'offset':i['offset'],'literal':i['args'].split('//',1)[1].strip(),'status':'VERIFIED_STATIC_LITERAL_ONLY'})
  if i['opcode'].startswith('invoke')and 'java/util/Random.'in i['args']:
   rng.append({'class':m['class'],'method':n,'descriptor':m['descriptor'],'offset':i['offset'],'operation':i['args'],'prior_instructions':' | '.join(f"{x['offset']}:{x['opcode']} {x['args']}"for x in ins[max(0,idx-12):idx]),'status':'VERIFIED_CALLSITE; bound/dataflow PARTIAL'})
  if i['opcode'].startswith('invoke')and any(s in i['args']for s in ['func_147465_d','func_147468_f','func_150818_a','func_76654_b','func_76484_a','setBlock:','generateSpawner','generateChest']):
   writes.append({'class':m['class'],'method':n,'descriptor':m['descriptor'],'offset':i['offset'],'operation':i['args'],'prior_instructions':' | '.join(f"{x['offset']}:{x['opcode']} {x['args']}"for x in ins[max(0,idx-18):idx]),'status':'VERIFIED_CALLSITE; coordinates/metadata require dataflow or source crosscheck'})
 for h in handlers:
  leaders.add(h['from']);leaders.add(h['target'])
  if h['to']in offsets:leaders.add(h['to'])
 heads=sorted(leaders);blocks=[];edges=[]
 for j,head in enumerate(heads):
  last=heads[j+1]if j+1<len(heads)else end+1;items=[x for x in ins if head<=x['offset']<last];tail=items[-1];op=tail['opcode'];block={'start':head,'end':tail['offset'],'instructions':items};blocks.append(block)
  for target in targets.get(tail['offset'],[]):edges.append({'from':head,'to':target,'kind':op})
  if not(op in ['goto','goto_w','return','athrow','tableswitch','lookupswitch']or op.endswith('return'))and j+1<len(heads):edges.append({'from':head,'to':heads[j+1],'kind':'fallthrough'})
  for h in handlers:
   if any(h['from']<=x['offset']<h['to']for x in items):edges.append({'from':head,'to':h['target'],'kind':'exception:'+h['type']})
 back=[e for e in edges if e['to']<=e['from']and not e['kind'].startswith('exception')]
 data={'class':m['class'],'method':n,'descriptor':m['descriptor'],'blocks':blocks,'edges':edges,'exception_handlers':handlers,'backward_edges':back,'scope':'Conservative static CFG; exception edges over-approximate; backward edges are not a proof of natural-loop nesting. No Minecraft execution.'};saved('evidence/cfg/'+safe+'.json',data)
 if n in ['generateAOADimGardencia','generateWLD','generateABC2','generateNether','generateSurface']:
  dot=['digraph cfg {','node [shape=box];']+[f'b{b["start"]} [label="B{b["start"]}..{b["end"]}"];'for b in blocks]+[f'b{e["from"]} -> b{e["to"]} [label="{e["kind"].replace(chr(34),chr(39))}"];'for e in edges]+['}'];(r/'evidence/cfg'/(safe+'.dot')).write_text('\n'.join(dot)+'\n')
  # Explicit label-level lowering, with exact opcodes retained instead of inventing high-level equivalence.
  ir=[f'# {m["class"]}.{n}{m["descriptor"]}','# Stack-machine pseudocode/IR; goto targets and exception ranges exact; API effects external.']
  for b in blocks:
   ir.append(f'B{b["start"]}:')
   ir.extend(f'  {x["offset"]}: {x["opcode"]} {x["args"]}'for x in b['instructions'])
  (r/'evidence/pseudocode'/(safe+'.vm-ir.txt')).write_text('\n'.join(ir)+'\n')
 body=source.get((c,n),'');srcpath=''
 if body:
  srcpath='evidence/source-methods/'+safe+'.cfr.txt';(r/srcpath).write_text(f'// CFR0.152; original decompiler line {source_meta[(c,n)]}; NOT original source; inspect **/goto artifacts if present.\n'+body+'\n')
  # Every assignment/loop/probability/Y branch relevant expression, not guessed numeric defaults.
  for li,line in enumerate(body.splitlines(),1):
   if re.search(r'genCount|genPos|genRad|firstBlockYCoord|rad_cof|nextInt|nextDouble|for \(|while \(',line):
    if len(line)>2000:line=line[:2000]+' [truncated; full source file retained]'
    parameters.append({'class':m['class'],'method':n,'descriptor':m['descriptor'],'parameter_or_gate':line.strip(),'source_file':srcpath,'source_body_line':li,'bytecode_scope':'0-'+str(end),'status':'PARTIAL_DECOMPILED_EXPRESSION; full control/dataflow not yet proved','runtime':'NOT_RUN'})
 refs=sorted({re.search(r'MFQM\.(\w+)',x['args'])[1]for x in ins if re.search(r'MFQM\.(\w+)',x['args'])});row={'slug':safe,'class':m['class'],'method':n,'descriptor':m['descriptor'],'instruction_count':len(ins),'last_offset':end,'basic_blocks':len(blocks),'edges':len(edges),'backward_edges':len(back),'exception_handlers':len(handlers),'mfqm_fields':';'.join(refs),'source_file':srcpath,'algorithm_status':'PARTIAL','runtime':'NOT_RUN'};index.append(row);cfgsummary.append({k:row[k]for k in ['class','method','descriptor','basic_blocks','edges','backward_edges','exception_handlers']})
writecsv('evidence/indexes/generator-methods.csv',index);writecsv('evidence/indexes/cfg-summary.csv',cfgsummary);writecsv('evidence/indexes/numeric-constants.csv',constants);writecsv('evidence/indexes/rng-call-sites.csv',rng);writecsv('evidence/indexes/write-and-subgenerator-sites.csv',writes);writecsv('02_WORLDGEN_GENERATOR_MATRIX.csv',parameters)
selectednames={m['class']for m in selected};edges=[c for c in calls if c['caller_class']in selectednames or c['target_class']in selectednames];writecsv('evidence/indexes/worldgen-call-edges.csv',edges)
# Config declarations from MFQM, paired with exact preInit bytecode string/field offsets.
mfqm=(a.cfr/'MFQM.java').read_text();config=[]
pre=next(m for m in methods if m['class'].endswith('.MFQM')and m['name']=='preInit')
for li,line in enumerate(mfqm.splitlines(),1):
 if 'config.get('in line and any(s in line for s in ['Gen','CWG','Altitude','Biomes','world','biome']):
  field=re.search(r'(\w+)\s*=\s*config.get',line);offset=[x['offset']for x in pre['instructions']if field and x['opcode']=='putstatic'and ('MFQM.'+field.group(1)+':')in x['args']]
  config.append({'field':field.group(1)if field else'UNKNOWN','declaration':line.strip(),'cfr_line':li,'preInit_putstatic_offsets':';'.join(map(str,offset)),'status':'VERIFIED_FIELD_BINDING'if offset else'PARTIAL','runtime':'NOT_RUN'})
writecsv('evidence/indexes/worldgen-config.csv',config)
# Cross-check all required phase1 inputs rather than assuming the package was complete.
required=['COMPLETION_REPORT.zh-CN.md']+[str(p.relative_to(a.phase1))for p in (a.phase1/'reports').glob('*.md')]+['indexes/classes.csv','indexes/methods.csv','indexes/calls.csv','indexes/branches.csv','indexes/material-behaviors.csv','indexes/original-runtime-cases.csv']
assert all((a.phase1/p).exists()for p in required);assert len(list(csv.DictReader((a.phase1/'indexes/original-runtime-cases.csv').open())))==90
saved('evidence/indexes/phase1-input-check.json',{'files_checked':required,'runtime_cases':90,'status':'PASS_INPUTS_PRESENT'})
print(json.dumps({'classes':len(core),'methods':len(selected),'cfg_blocks':sum(x['basic_blocks']for x in index),'generator_matrix_rows':len(parameters),'rng_sites':len(rng),'write_or_subgenerator_sites':len(writes),'call_edges':len(edges),'config_rows':len(config)},ensure_ascii=False))
