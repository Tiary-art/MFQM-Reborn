#!/usr/bin/env python3
from pathlib import Path
import argparse,csv,json,re,collections
ap=argparse.ArgumentParser();ap.add_argument('repo',type=Path);ap.add_argument('--phase1',type=Path,required=True);a=ap.parse_args();r=a.repo/'research/original-phase3';p2=a.repo/'research/original-phase2'
def csvout(name,rows):
 with(r/name).open('w',newline='')as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
# No fixture coverage is promoted to semantic closure.
coverage=collections.defaultdict(set)
for f in (r/'evidence/traces').glob('*.summary.json'):
 d=json.loads(f.read_text())
 for k,v in d['instruction_offsets_exercised'].items():coverage[k]|=set(v)
rows=[];summary=[]
for n in ['generateSurface','generateAOADimGardencia','generateWLD','generateNether','generateABC2']:
 path=p2/'evidence/cfg'/('CustomWorldGen__'+n+'.json');d=json.loads(path.read_text());seen=coverage['CustomWorldGen#'+n];ex=0
 for b in d['blocks']:
  exercised=b['start']in seen;ex+=exercised;rows.append({'class':'MoreFunQuicksandMod.main.CustomWorldGen','method':n,'descriptor':d['descriptor'],'block':'B'+str(b['start']),'end':b['end'],'semantic_closure':'UNRESOLVED','model_exercised':exercised,'evidence':'../original-phase2/evidence/cfg/'+path.name,'next_step':'stack/RNG/write semantics and all helper paths differential proof; fixture coverage is not equivalence'})
 summary.append({'method':n,'semantic_closed_blocks':0,'total_blocks':len(d['blocks']),'model_exercised_blocks':ex,'remaining_semantic_blocks':len(d['blocks'])})
csvout('evidence/indexes/five-method-block-status.csv',rows);csvout('evidence/indexes/five-method-summary.csv',summary)
# Constant metadata writes proved by contiguous stack operands, not source-variable guesses.
ms=json.loads((a.phase1/'indexes/methods-with-instructions.json').read_text());lits=[]
def const(i):
 op=i['opcode']
 if op.startswith('iconst_'):return -1 if op.endswith('m1')else int(op[-1])
 if op in ['bipush','sipush']:return int(i['args'])
 return None
for m in ms:
 ins=m['instructions']
 for j,i in enumerate(ins):
  if 'World.func_147465_d:'not in i['args']or j<3:continue
  block,meta,flags=ins[j-3:j]
  if block['opcode']!='getstatic' or 'MFQM.'not in block['args']or const(meta)is None or const(flags)is None:continue
  field=block['args'].split('MFQM.',1)[1].split(':',1)[0];lits.append({'block_field':field,'metadata':const(meta),'flags':const(flags),'method':m['class']+'#'+m['name']+m['descriptor'],'field_offset':block['offset'],'metadata_offset':meta['offset'],'write_offset':i['offset'],'status':'STATIC_VERIFIED_LITERAL_OPERANDS; path reachability not claimed'})
csvout('evidence/indexes/literal-metadata-writes.csv',lits)
materials=[x for x in csv.DictReader((r/'01_ALL_SINKABLE_MATERIALS.csv').open()) if x['metadata_variants'].startswith('PARTIAL:')];variants=[]
for mat in materials:
 writes=[x for x in lits if x['block_field']in mat['block_fields'].split(';')];vals=sorted({x['metadata']for x in writes})
 mat['observed_metadata_write_values']=';'.join(map(str,vals))or'UNKNOWN'
 for val in vals:
  v=dict(mat);v['metadata_variants']=str(val)+' (literal write provenance, not proof of distinct behavior)';sites=[x for x in writes if x['metadata']==val];v['metadata_evidence']=';'.join(x['method']+'@'+str(x['write_offset'])for x in sites);variants.append(v)
# Main CSV includes one block-scope row and concrete constant-metadata evidence rows. No claim all 16 states exist.
# Fluid definitions are additional material descriptors, not extra Block mechanisms.
fluidrows=[];fluids=[]
for m in ms:
 if not m['class'].split('.')[-1].endswith('Fluid') or '.liquids.' not in m['class'] or m['name']!='<init>':continue
 name=m['class'].split('.')[-1];src=a.phase1/'evidence/bytecode'/(m['class'].replace('.','__')+'.txt');dst=r/'evidence/bytecode'/src.name;dst.write_bytes(src.read_bytes());params=[];fluidname='UNKNOWN'
 for j,i in enumerate(m['instructions']):
  if i['opcode'].startswith('ldc') and '// String 'in i['args']:fluidname=i['args'].split('// String ',1)[1]
  if any(q in i['args']for q in ['setDensity:','setViscosity:','setTemperature:']):params.append(str(i['offset'])+':'+i['args']+'; preceding='+str(m['instructions'][j-1]))
 f={k:'UNKNOWN' for k in materials[0]};f.update(legacy_registration=fluidname,legacy_class=m['class'],parent='net.minecraftforge.fluids.Fluid',metadata_variants='NOT_APPLICABLE: Fluid descriptor; associated Block metadata unresolved',sinkability='NOT_ENTITY_COLLISION_CLASS; associated Block behavior required',formula_entry=m['class']+'#<init>'+m['descriptor']+'@0..'+str(m['instructions'][-1]['offset']),evidence='evidence/bytecode/'+src.name,confidence='STATIC_VERIFIED_DEFINITION; Block association PARTIAL',runtime='NOT_RUN');fluidrows.append(f)
 fluids.append({'fluid_class':m['class'],'fluid_name_literal':fluidname,'constructor':f['formula_entry'],'parameter_call_offsets_and_operands':';'.join(params),'evidence':f['evidence'],'status':'STATIC_VERIFIED_CALLS; no independent entity physics assumed'})
csvout('evidence/indexes/fluid-definitions.csv',fluids)
for x in materials:x['record_kind']='BLOCK_SCOPE'
for x in variants:x['record_kind']='LITERAL_METADATA_WRITE'
for x in fluidrows:x['record_kind']='FLUID_DEFINITION'
csvout('01_ALL_SINKABLE_MATERIALS.csv',materials+variants+fluidrows)
blue=list(csv.DictReader((r/'evidence/indexes/tombs-direct-write-blueprint.csv').open()));stats={}
for n in ['func_76484_a','generate2','generate3','generate4','generate5','generate6']:
 b=[x for x in blue if x['method'].endswith('#'+n)];stats[n]={'writes':len(b),'bbox':[[min(int(x[k])for x in b),max(int(x[k])for x in b)]for k in ['x','y','z']],'metadata':sorted({int(x['metadata'])for x in b})}
(r/'evidence/indexes/tombs-blueprint-summary.json').write_text(json.dumps({'direct_writes':len(blue),'unique_positions':len({(x['x'],x['y'],x['z'])for x in blue}),'methods':stats,'excluded':'15 chest/spawner helper invocations, their RNG/TE writes; final whole-world state not reconstructed','rotation':'no input rotation transform in these six straight-line methods; fixed literal offsets and metadata'},indent=2)+'\n')
print(json.dumps({'block_rows':len(materials),'constant_metadata_rows':len(variants),'literal_metadata_write_sites':len(lits),'five_methods':summary,'tombs':stats},ensure_ascii=False,indent=2))
