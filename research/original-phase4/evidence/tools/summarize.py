#!/usr/bin/env python3
import csv,json,re,collections,hashlib,gzip
from pathlib import Path
r=Path(__file__).resolve().parents[2];repo=r.parents[1];results=r/'evidence/results';cases=json.loads((results/'cases.json').read_text());caseby={x['case']:x for x in cases}
def table(name,rows):
 with(r/name).open('w',newline='')as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
# Historical 10 misses remain explicit; do not remove unreachable/error-path blocks.
cfg=json.loads((repo/'research/original-phase2/evidence/cfg/CustomWorldGen__generateAOADimGardencia.json').read_text());seen=set();sources=collections.defaultdict(set)
for path in results.glob('*.coverage.tsv'):
 for line in path.read_text().splitlines():
  name,off=line.split('\t')
  if '#generateAOADimGardencia('in name:seen.add(int(off));sources[int(off)].add(path.name)
misses={254:'Flat=true, passed seed/gate; old fixtures only used Flat=false',387:'valid solid ground but isAboveFreeSpace=false; ceiling fixture',393:'Tar early break; tar fixture',406:'solid/free rejection countBlock>10; ceiling fixture',459:'Flat path executes generateMireO; seed114',684:'MucBl ground valid but space blocked; sand-ceiling',694:'UNREACHABLE: ten Y positions, countBlock<=10, guard>10',1014:'Moor nextInt100==0 executes generateWater; seed2132',1246:'LiquidMire water but overhead blocks; alternating water/solid',1256:'LiquidMire scan rejects >10 water layers; alternating fixture'}
blockrows=[]
for b in cfg['blocks']:
 key=b['start'];conditional=key<193
 blockrows.append({'method':cfg['class']+'#'+cfg['method']+cfg['descriptor'],'block':'B'+str(key),'end':b['end'],'model_executed':key in seen,'closure':'CONTRACT_BOUND_GenMud'if conditional else'PROVED_UNREACHABLE'if key==694 else'UNRESOLVED','closure_scope':'only declared API/fixture contract; not full Gardencia proof'if conditional else'normal JVM local loop bound'if key==694 else'actual execution does not prove helper equivalence','previous_phase3_miss':key in misses,'condition_or_counterexample':misses.get(key,''),'fixture_evidence':' ; '.join(sorted(sources[key])),'cfg':'../original-phase2/evidence/cfg/CustomWorldGen__generateAOADimGardencia.json'})
table('evidence/results/gardencia-block-audit.csv',blockrows)
# Surface: 25 separate audits, not just a larger index.
ins_surface=[i for m in json.loads((r/'evidence/results/methods-selected.json').read_text()) if m['name']=='generateSurface' for i in m['instructions']]
anchors=[];cursor=-1
source_chains=list(csv.DictReader((repo/'research/original-phase3/evidence/indexes/surface-all-chains.csv').open()))[1:]
for ch in source_chains:
 cfgname=re.search(r'MFQM\.(Gen\w+)',ch['condition']).group(1)
 hit=next(i for i in ins_surface if i['offset']>cursor and i['opcode']=='getstatic' and 'MFQM.'+cfgname+':'in i['args'])
 cursor=hit['offset'];anchors.append(cursor)
surface_calls=list(csv.DictReader((repo/'research/original-phase2/evidence/indexes/worldgen-call-edges.csv').open()))

chains=list(csv.DictReader((repo/'research/original-phase3/evidence/indexes/surface-all-chains.csv').open()))[1:];materials=[x for x in csv.DictReader((repo/'research/original-phase3/01_ALL_SINKABLE_MATERIALS.csv').open())if x['record_kind']=='BLOCK_SCOPE'];fieldids={f:x['legacy_registration']for x in materials for f in x['block_fields'].split(';')};surface=[]
for num,ch in enumerate(chains,1):
 c=caseby[f'surface-{num:02d}-seed0'];p=results/(c['case']+'.jsonl');events=[json.loads(x)for x in p.read_text().splitlines()];writes=[e for e in events if e['event']=='WORLD_WRITE'];products=sorted({str(e['block'])+':'+str(e['metadata'])for e in writes});helpers=sorted({e['method']for e in events if e['event']=='HELPER_ENTER'});cfgs=[e['name']for e in events if e['event']=='CONFIG_GATE'and e['value']];staticmap=[]
 for field in ch['direct_product_fields'].split(';'):
  if field in fieldids:staticmap.append(field+' -> '+fieldids[field])
 anchor=anchors[num-1];stop=anchors[num] if num<len(anchors)else ins_surface[-1]['offset']+1
 pending_calls=[x['target_class']+'#'+x['target_method']+x['target_descriptor']+'@'+x['offset'] for x in surface_calls if x['caller_method']=='generateSurface' and anchor<=int(x['offset'])<stop]
 positive='surface-qs-positive'if 'GenQS' in ch['condition'] else'surface-softsand-positive'if'GenSSand'in ch['condition']else''
 surface.append({'branch':num,'original_condition':ch['condition'],'original_method':ch['entry'],'config_offsets':ch['config_bytecode_offsets'],'anchor_interval_not_semantic_ownership':str(anchor)+'..'+str(stop-1),'callee_dependencies_with_offsets':';'.join(pending_calls),'static_source':'../original-phase3/'+ch['source'],'parameter_expressions':ch['parameters_and_effects'],'declared_material_mapping':';'.join(staticmap)or'UNRESOLVED/helper-derived; no invented ID','seed0_enabled_config':';'.join(cfgs),'seed0_exit':c['exit'],'seed0_write_calls':len(writes),'seed0_actual_block_meta':';'.join(products)or'NONE in this fixture','actual_helpers_instrumented':';'.join(helpers),'positive_fixture':positive or'UNRESOLVED','negative_or_gate_fixture':c['full_trace_path'],'boundary_fixture':'surface-qs-no-ground'if positive=='surface-qs-positive'else'UNRESOLVED','code_found':True,'branch_explained':'PARTIAL: full source expressions retained; all biome/compat semantics not closed','model_executed':c['exit']==0,'independent_cross_validation':False,'original_runtime':'NOT_RUN','PORT_READY':'BLOCKED','blocker':'UNRESOLVED anchor interval '+str(anchor)+'..'+str(stop-1)+'; independent path/final-state equivalence for listed callees; static source retains biome/config/meta conditions'})
table('evidence/results/surface-25-audit.csv',surface)
# Do not recopy Tombs direct writes; add the 15 omitted helper sites with precise parent offsets.
methods=json.loads((repo/'research/original-phase3/evidence/indexes/trace-methods.json').read_text());tombsites=[]
for k,m in methods.items():
 if not k.startswith('GenerateDesertTombs#'):continue
 for i in m['instructions']:
  if i['opcode'].startswith('invoke')and any('Method '+n+':'in i['args']for n in ['generateSpawner','generateChest','generateChest2']):tombsites.append({'caller':m['class']+'#'+m['name']+m['descriptor'],'offset':i['offset'],'helper':i['args'],'execution_this_phase':'NOT_RUN','status':'UNRESOLVED','next_dependency':'TileEntity/NBT/ChestGenHooks/WeightedRandom mocks; independent loot/RNG oracle'})
assert len(tombsites)==15;table('evidence/results/tombs-15-helper-audit.csv',tombsites)
# Shared formula affects the actual setStuck callers, not a fixed three-material list.
stuck=list(csv.DictReader((repo/'research/original-phase3/evidence/indexes/material-instruction-sites.csv').open()));stuck=[x for x in stuck if x['signal']=='stuck'];table('evidence/results/stuck-kernel-callers.csv',stuck)
ready=[{'mechanism':'Gardencia GenMud fragment B0..190','evidence':'independent-mud-diff.json; gardencia-block-audit.csv','status':'SEMANTICALLY_CLOSED','PORT_READY':'CONDITIONAL_FRAGMENT_ONLY','scope':'14 blocks; all ordered events and final state under declared pure/native World contract; not complete generator','blocker':'Gardencia-only original route (MFQM.AOADimGardencia), modern dimension/API mapping, caller RNG protocol and world scheduling must be reviewed; not an Overworld rule'}, {'mechanism':'Gardencia B694','evidence':'b694-unreachable-proof.json','status':'SEMANTICALLY_CLOSED','PORT_READY':'NOT_A_FEATURE','scope':'normal JVM local bound proof; cannot count as executed coverage','blocker':'none within proof assumptions'}, {'mechanism':'MireO / MireOD / LiquidMire / Morass / Water','evidence':'cases.json; full traces','status':'MODEL_TESTED','PORT_READY':'BLOCKED','scope':'actual original method bodies in declared mock world; errors preserved','blocker':'independent full helper oracle; Morass PlantingThis native type/environment'}, {'mechanism':'CustomPotionEvent stuck numerical kernel','evidence':'physics-vectors.csv; physics-vector-check.json; stuck-kernel-callers.csv','status':'MODEL_TESTED','PORT_READY':'FORMULA_SPEC_ONLY','scope':'112 numeric vectors; no final net motion/world event equivalence','blocker':'full original event/property lifecycle and all material caller branches'}, {'mechanism':'10 no-own-contact Vanilla chains','evidence':'ten-contact-inheritance.json; vanilla javap','status':'STATIC_VERIFIED','PORT_READY':'BLOCKED','scope':'Vanilla Block contact offset0 return, inherited through checked parents','blocker':'old Forge patches and other events; not proof of no gameplay effects'}, {'mechanism':'Original MFQM asset path/hash map','evidence':'original-asset-path-map.csv','status':'STATIC_VERIFIED','PORT_READY':'PRIVATE_IMPORT_PLAN_ONLY','scope':'247 names/hash/dimensions; no pixels copied','blocker':'modern UV/state/render validation and public redistribution authorization'}]
for x in surface:ready.append({'mechanism':'Surface branch '+str(x['branch'])+': '+x['original_condition'],'evidence':'surface-25-audit.csv; '+x['negative_or_gate_fixture'],'status':'MODEL_TESTED'if x['model_executed']else'UNRESOLVED','PORT_READY':'BLOCKED','scope':x['branch_explained'],'blocker':x['blocker']})
for name in ['Tombs all 15 helper calls','WLD structure end-to-end','49-object complete physical families']:
 ready.append({'mechanism':name,'evidence':'tombs-15-helper-audit.csv'if name.startswith('Tombs')else'../original-phase3/09_OPEN_QUESTIONS_AND_PORT_READINESS.md','status':'UNRESOLVED','PORT_READY':'BLOCKED','scope':'not completed in this phase','blocker':'see exact retained Phase2/3 method/offset evidence; no fake runtime'})
table('06_PORT_READINESS_MATRIX.csv',ready)
summary={'baseline':'37d18a1 (Phase3 merged main)','cases':len(cases),'completed_model_cases':sum(c['exit']==0 for c in cases),'expected_invalid_bound_error':sum(c.get('expected_error',False)for c in cases),'unresolved_environment_errors':[c['case']for c in cases if c['exit']!=0 and not c.get('expected_error',False)],'independent_complete_event_final_state_comparisons':len(json.loads((results/'independent-mud-diff.json').read_text())),'gardencia_total_blocks':len(cfg['blocks']),'gardencia_model_executed_blocks':sum(b['model_executed']for b in blockrows),'gardencia_contract_bound_fragment_blocks':14,'gardencia_unconditional_unreachable_proof_blocks':1,'gardencia_whole_method_semantically_closed':False,'surface_branches_audited':len(surface),'surface_whole_branches_semantically_closed':0,'tombs_remaining_helper_calls':15,'original_runtime':'NOT_RUN'}
(results/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary,ensure_ascii=False,indent=2))
