#!/usr/bin/env python3
"""Evidence extraction, never infer behavior from translated material names."""
import argparse,csv,json,re,hashlib,collections,shutil
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--phase1',type=Path,required=True);ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--cfr',type=Path,required=True);a=ap.parse_args();r=a.repo/'research/original-phase3';p=a.phase1;p2=a.repo/'research/original-phase2'
for d in ['evidence/indexes','evidence/source','evidence/bytecode']:(r/d).mkdir(parents=True,exist_ok=True)
def csvout(name,rows):
 with (r/name).open('w',newline='')as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
ms=json.loads((p/'indexes/methods-with-instructions.json').read_text());classes={c['class']:c for c in csv.DictReader((p/'indexes/classes.csv').open())};byclass=collections.defaultdict(list)
for m in ms:byclass[m['class']].append(m)
materials=list(csv.DictReader((p/'indexes/material-behaviors.csv').open()));coats={x['class']:x for x in csv.DictReader((p2/'evidence/indexes/coating-applicability-49.csv').open())}
# Identify member fields assigned a NEW Block object in preInit using bytecode-local evidence.
fields=collections.defaultdict(set);registration=[]
for m in ms:
 if m['class'].endswith('.MFQM'):
  ins=m['instructions']
  for j,i in enumerate(ins):
   if i['opcode']=='new' and re.search(r'// class MoreFunQuicksandMod/main/(?:blocks|liquids)/',i['args']):
    clazz=i['args'].split('// class ',1)[1].replace('/','.')
    for k in ins[j+1:j+100]:
     if k['opcode']=='putstatic' and 'Lnet/minecraft/block/Block;'in k['args']:
      field=k['args'].split('// Field ',1)[1].split(':')[0];fields[clazz.split('.')[-1]].add(field);registration.append({'class':clazz,'constructor_new_offset':i['offset'],'field_assignment_offset':k['offset'],'field':field,'entry':m['class']+'#'+m['name']+m['descriptor'],'status':'STATIC_VERIFIED_ASSIGNMENT_PATTERN; constructor args see bytecode'});break
csvout('evidence/indexes/block-field-assignments.csv',registration)
worldms=[m for m in ms if m['class'].split('.')[-1]in ['CustomWorldGen','CustomWorldGenLakes','CustomGenerationEvent','GenerateMucusBlossom','GenerateDesertTombs']]
site_rows=[];meta=[];rows=[];motion=[]
patterns={'motion_x':'field_70159_w','motion_y':'field_70181_x','motion_z':'field_70179_y','ground':'field_70122_E','web':'func_70110_aj','hurt':'func_70097_a','air':'func_70050_g','stuck':'setStuckEffect','coating':'checkPlayerMuddy','bubble':'Bubble','sound':'func_72908_a','metadata':'func_72805_g','flow_or_world_write':'func_147465_d'}
for mat in materials:
 cls=next(c for c in classes if c.split('.')[-1]==mat['class']);own=byclass[cls];contact=next((m for m in own if m['name']=='func_149670_a'),None);lookup=classes[cls]['parent'];inherited='NONE_DECLARED; external inherited semantics UNKNOWN'
 while not contact and lookup in classes:
  contact=next((m for m in byclass[lookup]if m['name']=='func_149670_a'),None);lookup=classes[lookup]['parent']
  if contact:inherited='INHERITED_FROM '+contact['class']
 evidence={k:[]for k in patterns}
 for m in own:
  for j,i in enumerate(m['instructions']):
   for k,tok in patterns.items():
    if tok in i['args']:
     loc=m['class']+'#'+m['name']+m['descriptor']+'@'+str(i['offset']);evidence[k].append(loc)
     site_rows.append(dict(legacy_id=mat['legacy_id'],signal=k,method=m['class']+'#'+m['name']+m['descriptor'],offset=i['offset'],opcode=i['opcode'],target=i['args'],evidence='evidence/bytecode/'+cls.replace('.','__')+'.txt',status='STATIC_VERIFIED_INSTRUCTION_ONLY'))
     if k=='metadata':
      after=m['instructions'][j+1:j+24];meta.append(dict(legacy_id=mat['legacy_id'],method=m['class']+'#'+m['name']+m['descriptor'],offset=i['offset'],following_ir=' | '.join(str(q['offset'])+':'+q['opcode']+' '+q['args']for q in after),meaning='PARTIAL; read-to-branch dataflow not yet proven'))
   if i['opcode']=='putfield' and any(v in i['args']for v in ['field_70159_w','field_70181_x','field_70179_y']):
    prev=m['instructions'][max(0,j-20):j+1];motion.append(dict(legacy_id=mat['legacy_id'],method=m['class']+'#'+m['name']+m['descriptor'],offset=i['offset'],target=i['args'],preceding_ir=' | '.join(str(q['offset'])+':'+q['opcode']+' '+q['args']for q in prev),status='STATIC_VERIFIED_WRITE; full expression PARTIAL'))
 src=a.cfr/('/'.join(cls.split('.')[2:])+'.java')
 if src.exists():shutil.copy(src,r/'evidence/source'/(mat['class']+'.cfr.txt'))
 bc=p/'evidence/bytecode'/(cls.replace('.','__')+'.txt');shutil.copy(bc,r/'evidence/bytecode'/bc.name)
 flds=fields[mat['class']];wg=[]
 for m in worldms:
  for i in m['instructions']:
   if any(('MFQM.'+f+':')in i['args']for f in flds):wg.append(m['class'].split('.')[-1]+'#'+m['name']+'@'+str(i['offset']))
 c=coats[mat['class']];body=''if not contact else '\n'.join(i['opcode']+' '+re.sub(r'#\d+\s*','',i['args'])for i in contact['instructions'])
 rows.append(dict(legacy_registration=mat['legacy_id'],legacy_class=cls,parent=classes[cls]['parent'],block_fields=';'.join(sorted(flds))or'UNKNOWN',metadata_variants='PARTIAL: all reads indexed in metadata-read-sites.csv; no assumption every 0..15 is valid variant',sinkability='CONTACT_HANDLER_PRESENT; actual sinking paths PARTIAL'if contact else'UNKNOWN_INHERITED_OR_NO_CONTACT',formula_entry=(contact['class']+'#'+contact['name']+contact['descriptor']+'@0..'+str(contact['instructions'][-1]['offset']))if contact else inherited,depth_stuck=';'.join(evidence['stuck'])or'UNKNOWN',horizontal_jump=';'.join(evidence['motion_x']+evidence['motion_z'])or'UNKNOWN',suffocation_damage=';'.join(evidence['air']+evidence['hurt'])or'UNKNOWN',coating=c['applicability'],coating_type=c['type_expression'],cleaning='MuddyEvent shared conditional cleaning; applicability inherited/external UNKNOWN',overlay='PARTIAL; direct eye/opaque paths require individual review',bubble=';'.join(evidence['bubble'])or'UNKNOWN',sound=';'.join(evidence['sound'])or'UNKNOWN',flow_fall='PARTIAL; '+classes[cls]['parent'],worldgen=';'.join(wg)or'UNKNOWN (field mapping or generation route unresolved)',metadata_evidence=';'.join(evidence['metadata'])or'NO_DIRECT_READ; inherited/external UNKNOWN',contact_algorithm_hash=hashlib.sha256(body.encode()).hexdigest()if body else'NONE',modern_id=mat['b2_id'],modern_gap='Registration only does not prove mechanism; no grouping into three profiles',evidence='evidence/bytecode/'+bc.name+'; evidence/source/'+mat['class']+'.cfr.txt',confidence='PARTIAL_SEMANTICS; instruction sites STATIC_VERIFIED',runtime='NOT_RUN'))
csvout('01_ALL_SINKABLE_MATERIALS.csv',rows);csvout('evidence/indexes/material-instruction-sites.csv',site_rows);csvout('evidence/indexes/metadata-read-sites.csv',meta);csvout('evidence/indexes/motion-component-writes.csv',motion)
# Every storage metadata value gets an explicit coverage row, not an assertion it is a reachable original variant.
grid=[]
for mat in rows:
 for value in range(16):grid.append({'legacy_registration':mat['legacy_registration'],'class':mat['legacy_class'],'storage_metadata':value,'reachable_variant':'UNKNOWN','behavior':'UNKNOWN unless per-read branch dataflow resolved','evidence':mat['metadata_evidence'],'status':'COVERAGE_DOMAIN_ONLY_NOT_VARIANT_PROOF'})
csvout('evidence/indexes/metadata-domain-coverage.csv',grid)
# Full Surface ordered outer blocks, complete original text per block for faithful expressions.
vf=(p2/'evidence/pseudocode/CustomWorldGen.vineflower.txt').read_text();lines=vf.splitlines();start=next(i for i,l in enumerate(lines)if 'private void generateSurface('in l);end=next((i for i in range(start+1,len(lines))if re.match(r'^   (?:private|public|protected) ',lines[i])),len(lines));body=lines[start:end];starts=[i for i,l in enumerate(body)if re.match(r'^      if \(',l)];chains=[]
sm=next(m for m in worldms if m['name']=='generateSurface');ins=sm['instructions']
for order,k in enumerate(starts):
 stop=starts[order+1]if order+1<len(starts)else len(body);chunk='\n'.join(body[k:stop]);config=sorted(set(re.findall(r'MFQM\.(Gen\w+)',chunk)));products=sorted(set(re.findall(r'MFQM\.(\w+Block)',chunk)));helpers=sorted(set(re.findall(r'(?:this\.)?(generate\w+|gen\w+)\(',chunk)));slug=f'surface-{order+1:02d}';path='evidence/source/'+slug+'.vineflower.txt';(r/path).write_text('// Decompiled inference, NOT original source; semantic closure PARTIAL\n'+chunk+'\n');offsets=[i['offset']for i in ins if any('MFQM.'+c+':'in i['args']for c in config)];expr=[l.strip()for l in chunk.splitlines()if any(q in l for q in ['nextInt','nextFloat','genCount','genPos','genRad','firstBlockYCoord','blockGen','return','break;',' = ','while (','for ('])]
 chains.append(dict(order=order+1,entry='CustomWorldGen#generateSurface'+sm['descriptor'],condition=body[k].strip(),configs=';'.join(config),direct_product_fields=';'.join(products)or'UNKNOWN/helper-produced',helpers=';'.join(helpers),config_bytecode_offsets=';'.join(map(str,offsets))or'NONE',source=path,vineflower_lines=f'{start+k+1}..{start+stop}',parameters_and_effects=' | '.join(expr),status='PARTIAL; literal expressions indexed, branch equivalence not proved',runtime='NOT_RUN'))
csvout('evidence/indexes/surface-all-chains.csv',chains)
# Branch-domain evidence (not automatic metadata-value inference).
print(json.dumps({'materials':len(rows),'metadata_domain_rows':len(grid),'metadata_reads':len(meta),'motion_component_writes':len(motion),'material_instruction_sites':len(site_rows),'surface_outer_blocks':len(chains),'mapped_block_classes':len(fields)}))
