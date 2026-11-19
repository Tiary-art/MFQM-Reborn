#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from common import *
p=argparse.ArgumentParser();p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();o=a.out_dir;metrics=[]
def add(name,total,verified=0,partial=0,blocked=0,notrun=0):
 metrics.append(dict(metric=name,N_total=total,N_verified=verified,N_partial=partial,N_unknown=total-verified-partial-blocked-notrun,N_blocked=blocked,N_not_run=notrun,N_not_applicable_with_proof=0,verified_percent=round(100*verified/total,4)if total else None))
for name,file in[('file_index','ORIGINAL_JAR_FILES'),('class_index','ORIGINAL_CLASSES'),('method_index','ORIGINAL_METHODS'),('field_index','ORIGINAL_FIELDS')]:
 n=len(read(o/'manifest'/(file+'.csv')));add(name,n,n)
add('deep_class_semantics',len(read(o/'manifest/ORIGINAL_CLASSES.csv')),partial=0)
add('registry_callsite_interpretation_not_complete_registry',len(read(o/'manifest/ORIGINAL_REGISTRY.csv')),partial=len(read(o/'manifest/ORIGINAL_REGISTRY.csv')))
for name,file in [('modern_registered_runtime','manifest/MODERN_REGISTRY.csv'),('creative_correct_on_identified_calls','manifest/ORIGINAL_REGISTRY.csv'),('asset_binding_on_original_resources','manifest/ORIGINAL_RESOURCES.csv'),('name_parity_on_identified_calls','manifest/ORIGINAL_REGISTRY.csv'),('behavior_parity_on_catalogued_cases','mapping/BEHAVIOR_CASES.csv'),('original_oracle_replay_r0_on_catalogued_cases','mapping/BEHAVIOR_CASES.csv'),('multiplayer_on_modern_registered_objects','manifest/MODERN_REGISTRY.csv')]:
 n=len(read(o/file))
 if name=='modern_registered_runtime' and (o/'manifest/MODERN_REGISTRY_RUNTIME.csv').exists():
  observed={(r['kind'],r['registry_id']) for r in read(o/'manifest/MODERN_REGISTRY_RUNTIME.csv')}
  add(name,n,verified=sum((r['kind'],r['registry_id']) in observed for r in read(o/file)))
 else:add(name,n,notrun=n)
add('modern_static_inventory',len(read(o/'manifest/NEW_PROJECT_INVENTORY.csv')),len(read(o/'manifest/NEW_PROJECT_INVENTORY.csv')))
add('modern_full_semantic_review',len(read(o/'manifest/NEW_PROJECT_INVENTORY.csv')),partial=len(read(o/'manifest/NEW_PROJECT_INVENTORY.csv')))
add('approximation_candidates',len(read(o/'mapping/AI_APPROXIMATION_AUDIT.csv')),partial=len(read(o/'mapping/AI_APPROXIMATION_AUDIT.csv')))
add('safe_replacements',len(read(o/'mapping/AI_APPROXIMATION_AUDIT.csv')))
add('actual_visual_acceptance_r0',len(read(o/'manifest/MODERN_REGISTRY.csv')),notrun=len(read(o/'manifest/MODERN_REGISTRY.csv')))
dump(o/'checks/COVERAGE.json',{'status':'PARTIAL','metrics':metrics,'unknown_universes':['complete runtime original registry','all metadata/creative variants','all behavior cases','integration pack universe'],'denominator_warning':'Rows are object units, not gameplay-completion percentages. Registry/variant total universe UNKNOWN; static callsites not substituted for full runtime registry. Unknowns retained. No prior-stage runtime imported as R0 PASS.'});write(o/'checks/COVERAGE.csv',metrics)
