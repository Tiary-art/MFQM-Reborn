#!/usr/bin/env python3
import argparse,json,csv,gzip,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--jar',type=Path,required=True);a=p.parse_args();r=Path(__file__).resolve().parents[2];repo=r.parents[1]
names=['00_EXECUTIVE_SUMMARY.zh-CN.md','01_GARDENCIA_CLOSURE.md','02_SURFACE_25_BRANCH_CLOSURE.md','03_TOMBS_WLD_CLOSURE.md','04_MATERIAL_PHYSICS_PORT_SPEC.md','05_COATING_CAMERA_ASSET_PORT_SPEC.md','06_PORT_READINESS_MATRIX.csv','07_OPEN_QUESTIONS_AND_USER_ACTIONS.md','REPRODUCE.md'];assert all((r/n).is_file()and(r/n).stat().st_size for n in names)
sha=hashlib.sha256(a.jar.read_bytes()).hexdigest();assert sha=='2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
summary=json.loads((r/'evidence/results/summary.json').read_text());assert summary['cases']==65 and summary['completed_model_cases']==62 and summary['gardencia_model_executed_blocks']==99
assert summary['surface_whole_branches_semantically_closed']==0 and summary['tombs_remaining_helper_calls']==15
cases=json.loads((r/'evidence/results/cases.json').read_text());expect_fail={'liquid-invalid-bound','gard-moor-real','gard-moor-water-first'};assert {c['case']for c in cases if c['exit']!=0}==expect_fail
count=0;gz=0
for c in cases:
 path=repo/c['full_trace_path'];digest=hashlib.sha256();events={};last=None
 opener=gzip.open if path.suffix=='.gz'else open
 with opener(path,'rb')as f:
  for line in f:
   digest.update(line);e=json.loads(line);events[e['event']]=events.get(e['event'],0)+1;last=e
 assert events==c['events'],(c['case'],'event count mismatch')
 assert digest.hexdigest()==c['sha256'],(c['case'],'raw trace digest mismatch')
 assert last['event']==('ERROR'if c['exit']else'RESULT'),c['case']
 assert last.get('status')!='ORIGINAL_RUNTIME_TESTED'
 if c['exit']:
  assert last['type']==('java.lang.IllegalArgumentException'if c['case']=='liquid-invalid-bound'else'java.lang.ClassCastException'),c['case']
 count+=1;gz+=path.suffix=='.gz'
assert len(json.loads((r/'evidence/results/independent-mud-diff.json').read_text()))==14
rows=list(csv.DictReader((r/'evidence/results/gardencia-block-audit.csv').open()));assert len(rows)==100
assert sum(x['model_executed']=='True'for x in rows)==99
assert next(x for x in rows if x['block']=='B694')['closure']=='PROVED_UNREACHABLE'
assert len(list(csv.DictReader((r/'evidence/results/surface-25-audit.csv').open())))==25
assert len(list(csv.DictReader((r/'evidence/results/tombs-15-helper-audit.csv').open())))==15
assert len(json.loads((r/'evidence/results/ten-contact-inheritance.json').read_text())['objects'])==10
assert len(list(csv.DictReader((r/'evidence/results/original-asset-path-map.csv').open())))==247
assert len(list(csv.DictReader((r/'evidence/results/original-audio-path-map.csv').open())))==2
assert len(list(csv.DictReader((r/'evidence/results/physics-vectors.csv').open())))==112
forbidden={'.jar','.class','.png','.ogg','.zip','.pyc','.mca','.nbt'};bad=[str(f)for f in r.rglob('*')if f.is_file()and f.suffix.lower()in forbidden];assert not bad,bad
print(json.dumps({'status':'STATIC_VERIFIED_DELIVERY_AND_TRACE_INTEGRITY','trace_files_validated':count,'gzip_analysis_traces':gz,'registered_model_successes':62,'expected_negative_error':1,'unresolved_environment_errors':2,'independent_full_event_and_final_matches':14,'original_sha256':sha,'original_runtime':'NOT_RUN','scope':'integrity is not whole-method semantic proof'},ensure_ascii=False,indent=2))
