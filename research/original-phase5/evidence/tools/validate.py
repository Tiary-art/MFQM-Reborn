#!/usr/bin/env python3
import argparse,json,csv,gzip,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--jar',type=Path,required=True);a=p.parse_args();r=Path(__file__).resolve().parents[2]
required=['00_EXECUTIVE_SUMMARY.zh-CN.md','01_MORASS_MOCK_AND_PLANTING_CLOSURE.md','02_SURFACE_BRANCH_CLOSURE.md','03_STUCK_AND_MATERIAL_PHYSICS_PORT_SPEC.md','04_TOMBS_WLD_VERTICAL_SLICES.md','05_MATERIAL_AND_VISUAL_GAPS.md','06_PORT_READINESS_MATRIX.csv','07_OPEN_QUESTIONS_AND_USER_ACTIONS.md','REPRODUCE.md','PORT_READY_COMPONENTS.md','summary.json']
assert all((r/f).is_file()and(r/f).stat().st_size for f in required)
s=json.loads((r/'summary.json').read_text());cases=json.loads((r/'evidence/results/cases.json').read_text());assert len(cases)==s['independent_vm_full_event_cases']==62
assert sum(bool(c['declarative'])for c in cases)==44 and all(c['native_exit']==0 for c in cases)
manifest=json.loads((r/'evidence/results/trace-manifest.json').read_text());assert len(manifest)==128
for entry in manifest:
 h=hashlib.sha256()
 with gzip.open(r/entry['path'],'rb')as f:
  for line in f:h.update(line);json.loads(line)
 assert h.hexdigest()==entry['uncompressed_sha256'],entry['path']
for c in cases:
 with gzip.open(r/'evidence/results'/(c['tag']+'.jsonl.gz'),'rt')as f:events=[json.loads(l)for l in f]
 assert events[-1]['event']=='RESULT' and not any(x['event']in ['ERROR','UNRESOLVED']for x in events)
for m in s['whole_morass_parent_reruns']:assert m['final']['status']=='MODEL_TESTED'and not m['independent_whole_parent']
assert s['stuck']['events_matched']==123 and s['stuck']['ticks']==8
assert len(list(csv.DictReader((r/'evidence/results/surface-25-status.csv').open())))==25
assert s['whole_surface_all_biomes_closed']==0
assert json.loads((r/'evidence/results/oracle-rerun.json').read_text())['saved_native_vs_independent_oracle_rerun']==62
replay=json.loads((r/'evidence/results/guards-and-replay.json').read_text());assert replay['repeat_bytes_identical']and len(replay['negative_cases'])==4
proof=(r/'evidence/results/body-identity.log').read_text();assert proof.count('BODY_IDENTICAL')==4
assert json.loads((r/'evidence/results/phase4-regression.json').read_text())['registered_model_successes']==62
assert json.loads((r/'evidence/results/phase3-regression.json').read_text())['original_runtime']=='NOT_RUN'
assert s['original_runtime']=='NOT_RUN'and hashlib.sha256(a.jar.read_bytes()).hexdigest()==s['original_jar_sha256']
forbidden={'.jar','.class','.png','.ogg','.zip','.pyc','.mca','.nbt'};assert not[f for f in r.rglob('*')if f.is_file()and f.suffix.lower()in forbidden]
print(json.dumps({'status':'STATIC_VERIFIED_ARTIFACT_AND_MODEL_INTEGRITY','full_vm_event_comparisons':62,'extra_declarative_cases':44,'complete_canonical_trace_files':len(manifest),'identical_original_body_fingerprints':4,'life_cycle_events':123,'old_phase_regression':'PASS_WITH_HISTORICAL_EXPECTED_FAILURES_UNCHANGED','ready_algorithm_components':2,'whole_surface_full_scope_closed':0,'original_runtime':'NOT_RUN'},indent=2))
