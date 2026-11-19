#!/usr/bin/env python3
"""Verify observed pass markers, immutable pure cores, and no new natural entry points.
Gradle BUILD SUCCESSFUL alone is deliberately insufficient (see retained lock failure).
"""
from pathlib import Path
import json,subprocess,xml.etree.ElementTree as E,hashlib,shutil
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'docs/phase7';L=D/'logs'
base='9eda883';core='forge-1.20.1/src/main/java/art/tiary/mfqm/legacy'
for p in (ROOT/core).glob('*.java'):
 assert p.read_bytes()==subprocess.check_output(['git','show',base+':'+str(p.relative_to(ROOT))],cwd=ROOT),p
for name,n in [('baseline-gametest.log',29),('timing-diagnostic-run.log',36)]:
 text=(L/name).read_text();assert f'All {n} required tests passed' in text and 'BUILD SUCCESSFUL' in text and 'Game test server shutting down'in text,name
 assert 'Failed to start the minecraft server'not in text and 'DirectoryLock$LockException'not in text,name
text=(L/'dedicated-server-console.log').read_text()
assert 'Done ('in text and 'Stopping server'in text and 'All dimensions are saved'in text and 'BUILD SUCCESSFUL'in text
results=[]
for p in (ROOT/'forge-1.20.1/build/test-results/test').glob('TEST-*.xml'):
 r=E.parse(p).getroot();results.append({k:r.attrib[k]for k in ['name','tests','failures','errors','skipped']});shutil.copy(p,L/p.name)
assert sum(int(r['tests'])for r in results)==45
assert all(int(r[k])==0 for r in results for k in ['failures','errors','skipped'])
(L/'junit-summary.json').write_text(json.dumps(results,indent=2)+'\n')
# These sensitive subsystems are byte-identical. SinkEngine's integration diff is separately reviewed.
for folder in ['client','network']:
 for p in (ROOT/'forge-1.20.1/src/main/java/art/tiary/mfqm'/folder).glob('*.java'):
  assert p.read_bytes()==subprocess.check_output(['git','show',base+':'+str(p.relative_to(ROOT))],cwd=ROOT),p
for name in ['MotionMath.java','SinkMath.java']:
 p=ROOT/'forge-1.20.1/src/main/java/art/tiary/mfqm/physics'/name
 assert p.read_bytes()==subprocess.check_output(['git','show',base+':'+str(p.relative_to(ROOT))],cwd=ROOT)
for p in (ROOT/'forge-1.20.1/src/main/java/art/tiary/mfqm/integration').glob('*.java'):
 text=p.read_text();assert 'net.minecraft.client.'not in text and 'PlacedFeature'not in text and 'BiomeModifier'not in text
for rel in subprocess.check_output(['git','diff',base,'--name-only'],cwd=ROOT,text=True).splitlines():
 assert not rel.startswith('forge-1.20.1/src/main/resources/'),rel
(D/'RESULTS.json').write_text(json.dumps({'overall':'PARTIAL','baseline_GameTests':29,'candidate_GameTests':36,'JUnit':45,'pure_cores_unchanged':True,'natural_generation':'NOT_REGISTERED','automatic_material_Level':'BLOCKED','connected_client':'NOT_RUN','full_surface_closed':'0/25','dedicated_start_console_stop':'PASS','historical_intermittent_fixture_failures':['two-fixture-tick release check','two-tick hold early snapshot'],'registered_release_trace':[line for line in (L/'timing-diagnostic-run.log').read_text().splitlines() if 'PHASE7_REGISTERED_LEASE_' in line]},indent=2)+'\n')
print('PASS: observed36 candidate /29 baseline GameTests,45 JUnit, dedicated console stop/save; overall integration PARTIAL')
