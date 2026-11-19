#!/usr/bin/env python3
import argparse,csv,json,hashlib
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('--original-jar',type=Path,required=True);a=ap.parse_args();r=a.root
names=['00_EXECUTIVE_SUMMARY.zh-CN.md','01_ALL_SINKABLE_MATERIALS.csv','02_MECHANISM_FAMILIES.md','03_SURFACE_WORLDGEN_ALL_MATERIALS.md','04_GARDENCIA_WLD_STRUCTURES.md','05_DESERT_TOMBS_BLUEPRINT.md','06_RNG_WRITE_TRACE_SPEC.md','07_MATERIAL_MOTION_SPEC.md','08_COATING_CAMERA_TEXTURE_SPEC.md','09_OPEN_QUESTIONS_AND_PORT_READINESS.md','REPRODUCE.md']
assert all((r/n).is_file()and(r/n).stat().st_size for n in names)
rows=list(csv.DictReader((r/names[1]).open()));base=[x for x in rows if x['record_kind']=='BLOCK_SCOPE'];assert len(base)==49 and len({x['legacy_registration']for x in base})==49
assert len([x for x in rows if x['record_kind']=='FLUID_DEFINITION'])==12
assert len([x for x in rows if x['record_kind']=='LITERAL_METADATA_WRITE'])==47
for x in rows:
 assert x['runtime']=='NOT_RUN'
 for e in x['evidence'].split(';'):assert (r/e.strip()).is_file(),e
assert len(list(csv.DictReader((r/'evidence/indexes/metadata-domain-coverage.csv').open())))==784
assert len(list(csv.DictReader((r/'evidence/indexes/surface-all-chains.csv').open())))==26
summ=list(csv.DictReader((r/'evidence/indexes/five-method-summary.csv').open()));assert len(summ)==5
assert all(x['semantic_closed_blocks']=='0'for x in summ)
blocks=list(csv.DictReader((r/'evidence/indexes/five-method-block-status.csv').open()));assert len(blocks)==1886
traces=0;eventcount=0
for f in (r/'evidence/traces').glob('*.jsonl'):
 es=[json.loads(x)for x in f.read_text().splitlines()];assert es[0]['trace_kind']=='MODEL_TRACE';assert [e['seq']for e in es]==list(range(len(es)));traces+=1;eventcount+=len(es)
assert traces==6
forbidden={'.jar','.class','.png','.ogg','.zip','.pyc','.nbt','.mca'};bad=[str(f)for f in r.rglob('*')if f.is_file()and f.suffix.lower()in forbidden];assert not bad,bad
sha=hashlib.sha256(a.original_jar.read_bytes()).hexdigest();assert sha=='2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
print(json.dumps({'status':'STATIC_VERIFIED_DELIVERY_CHECK','original_sha256':sha,'required_deliverables':len(names),'registered_blocks':49,'metadata_write_evidence_rows':47,'fluid_definitions':12,'metadata_domain_only':784,'surface_outer_regions':26,'unresolved_semantic_blocks':1886,'model_trace_files':traces,'trace_events':eventcount,'forbidden_binaries':0,'original_runtime':'NOT_RUN'},ensure_ascii=False,indent=2))
