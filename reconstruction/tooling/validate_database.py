#!/usr/bin/env python3
import argparse,json,collections
from pathlib import Path
from common import *
p=argparse.ArgumentParser();p.add_argument('--repo-root',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True);p.add_argument('--verify',action='store_true');a=p.parse_args();root=a.repo_root.resolve();out=a.out_dir;errors=[];tables={p.stem:read(p)for p in sorted((out/'manifest').glob('*.csv'))};maps={p.stem:read(p)for p in sorted((out/'mapping').glob('*.csv'))}
ids={}
for name,key in [('ORIGINAL_JAR_FILES','original_file_id'),('ORIGINAL_CLASSES','class_id'),('ORIGINAL_METHODS','member_id'),('ORIGINAL_FIELDS','member_id'),('NEW_PROJECT_INVENTORY','modern_id'),('MODERN_MEMBERS','modern_id'),('MODERN_REGISTRY','modern_id'),('ORIGINAL_REGISTRY','original_id')]:
 rows=tables[name];values=[r[key]for r in rows];ids[name]=set(values)
 if len(set(values))!=len(values):errors.append('duplicate '+name)
 if not rows:errors.append('empty '+name)
for r in tables['ORIGINAL_CLASSES']:
 if r['original_file_id']not in ids['ORIGINAL_JAR_FILES']:errors.append(r['class_id'])
 if not(root/'docs/reconstruction/original/classes'/(r['class_name']+'.md')).is_file():errors.append('dossier '+r['class_name'])
for name in['ORIGINAL_METHODS','ORIGINAL_FIELDS']:
 for r in tables[name]:
  if r['class_id']not in ids['ORIGINAL_CLASSES']:errors.append('orphan '+r['member_id'])
for r in tables['NEW_PROJECT_INVENTORY']:
 p=root/r['path']
 if not p.is_file()or sha(p.read_bytes())!=r['sha256']:errors.append('missing/changed '+r['path'])
original=set.union(*(ids[n]for n in['ORIGINAL_JAR_FILES','ORIGINAL_CLASSES','ORIGINAL_METHODS','ORIGINAL_FIELDS','ORIGINAL_REGISTRY']))
rows=maps['RESTORATION_MATRIX'];keys=[r['original_id']for r in rows]
if len(set(keys))!=len(keys)or set(keys)!=original:errors.append('matrix object coverage mismatch')
for r in maps['ORIGINAL_TO_MODERN']:
 if r['original_id']not in original or r['modern_id']not in ids['MODERN_REGISTRY']:errors.append('bad mapping '+r['original_id'])
for r in maps['CALL_GRAPH']:
 if r['caller_id']not in ids['ORIGINAL_METHODS']:errors.append('bad caller '+r['caller_id'])
for name,rows in [*tables.items(),*maps.items()]:
 for r in rows:
  ev=r.get('evidence_ref','')
  if ev and not ev.startswith('private:')and not(root/ev).is_file():errors.append('invalid evidence '+name+' '+ev)
for r in tables['MODERN_MEMBERS']:
 if not(root/r['modern_path']).is_file():errors.append('modern member source '+r['modern_path'])
for r in maps['MODERN_CALL_GRAPH']:
 if r['caller_id']not in ids['MODERN_MEMBERS']:errors.append('modern caller '+r['caller_id'])
for r in maps['BEHAVIOR_CASES']:
 for key in r['original_method_ids'].split(';'):
  if key not in ids['ORIGINAL_METHODS']:errors.append('behavior case method '+key)
if {r['new_path']for r in maps['AI_APPROXIMATION_AUDIT']}!={r['path']for r in tables['NEW_PROJECT_INVENTORY']}:errors.append('audit file coverage gap')
if 'ORIGINAL_ITEMSTACK_VARIANTS' in tables:
 variants=tables['ORIGINAL_ITEMSTACK_VARIANTS'];objects={r['original_object_id'] for r in tables['ORIGINAL_REGISTRY_OBJECTS']}
 keys_by_damage={(r['original_object_id'],r['old_damage']) for r in variants}
 stack_ids={r['original_stack_id'] for r in variants}
 if len(stack_ids)!=len(variants) or len(keys_by_damage)!=len(variants):errors.append('duplicate legacy stack identity')
 if any(r['original_object_id'] not in objects for r in variants):errors.append('legacy stack lacks object')
 if stack_ids!={r['original_stack_id'] for r in maps['CONTENT_PARITY_MATRIX']}:errors.append('stack parity coverage')
 if {(r['kind'],r['registry_id']) for r in tables['MODERN_REGISTRY']}!={(r['kind'],r['registry_id']) for r in tables['MODERN_REGISTRY_RUNTIME']}:errors.append('source/runtime registry mismatch')
unknown=[r for r in maps['CALL_GRAPH']if r['scope']=='INTERNAL'and r['target_id']not in ids['ORIGINAL_METHODS']|ids['ORIGINAL_FIELDS']]
write(out/'checks/UNRESOLVED_INTERNAL_EDGES.csv',unknown,fields=list(maps['CALL_GRAPH'][0]))
unmapped=[r for r in rows if not r.get('modern_ids')]if False else[r for r in maps['RESTORATION_MATRIX']if not r['modern_ids']]
write(out/'checks/UNMAPPED_ORIGINAL.csv',unmapped)
write(out/'checks/UNVERIFIED_MODERN.csv',tables['NEW_PROJECT_INVENTORY'])
dump(out/'checks/R0_VALIDATION.json',dict(status='PASS'if not errors else'FAIL',errors=errors,rows={k:len(v)for k,v in tables.items()},matrix_rows=len(keys),unresolved_internal_edges=len(unknown),unresolved_note='inherited/virtual dispatch/reference closure unknown; not called dead code',unmapped_original=len(unmapped),semantic_parity_verified=False))
print(json.dumps({'errors':errors,'matrix_rows':len(keys),'unmapped':len(unmapped)}));raise SystemExit(bool(errors))
