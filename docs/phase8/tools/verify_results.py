#!/usr/bin/env python3
"""Verify distinct Gradle/assertion/shutdown/lock outcomes, not just an exit-success string."""
from pathlib import Path
import xml.etree.ElementTree as E
import subprocess,json,hashlib,shutil,fcntl,re
R=Path(__file__).resolve().parents[3];D=R/'docs/phase8';L=D/'logs';base='b1461ba'
def contents(name):return (L/name).read_text()
for name,n in [('baseline.log',36),('isolated-config-final.log',43),('final-verified-clean.log',43)]:
 text=contents(name)
 assert f'All {n} required tests passed' in text and 'BUILD SUCCESSFUL' in text and 'Game test server shutting down' in text,name
 assert 'Failed to start the minecraft server'not in text and 'required tests failed'not in text,name
assert 'enabled=false alive=true exempt=false' in contents('config-diagnostic.log')
assert 'trackedleasenotlostbeforeentityvisibility failed!'in contents('baseline-visibility-repro.log')
match=re.search(r'worldTick=(\d+) updated=(\d+) level=0',next(line for line in contents('baseline-visibility-repro.log').splitlines() if 'trackedleasenotlostbeforeentityvisibility failed!' in line));assert match and int(match[1])-int(match[2])==2
for name in ['player-server.log','player-server-session2.log']:
 text=contents(name);assert 'Done ('in text and 'All dimensions are saved'in text and 'BUILD SUCCESSFUL'in text,name
lock_checks=[]
for path in [R/'forge-1.20.1/run/phase8-candidate/world/session.lock',R/'forge-1.20.1/run/server/MFQM_PHASE8_PLAYERS/session.lock']:
 with path.open('r+b')as f:fcntl.lockf(f,fcntl.LOCK_EX|fcntl.LOCK_NB);fcntl.lockf(f,fcntl.LOCK_UN)
 lock_checks.append({'path':str(path.relative_to(R)),'exclusive_record_lock':'ACQUIRED_AND_RELEASED'})
rows=[]
for p in (R/'forge-1.20.1/build/test-results/test').glob('TEST-*.xml'):
 root=E.parse(p).getroot();rows.append({k:root.attrib[k]for k in ['name','tests','failures','errors','skipped']});shutil.copy(p,L/p.name)
assert sum(int(x['tests'])for x in rows)==46
assert all(int(x[k])==0 for x in rows for k in ['failures','errors','skipped'])
(L/'junit-summary.json').write_text(json.dumps(rows,indent=2)+'\n')
unchanged=[]
for rel in ['legacy/StuckLease.java','legacy/DryQuicksandCore.java','legacy/VoxelPort.java','legacy/LegacyRandom.java','legacy/LegacyBlock.java','physics/SinkEngine.java','physics/MotionRuntime.java','physics/MotionMath.java','physics/SinkMath.java','client/ClientMotionPrediction.java','client/ClientCompatibility.java']:
 p=R/'forge-1.20.1/src/main/java/art/tiary/mfqm'/rel
 assert p.read_bytes()==subprocess.check_output(['git','show',base+':'+str(p.relative_to(R))],cwd=R),rel
 unchanged.append(rel)
for p in (R/'forge-1.20.1/src/main/java/art/tiary/mfqm/network').glob('*.java'):
 assert p.read_bytes()==subprocess.check_output(['git','show',base+':'+str(p.relative_to(R))],cwd=R),p
for rel in subprocess.check_output(['git','diff',base,'--name-only'],cwd=R,text=True).splitlines():
 assert not rel.startswith('forge-1.20.1/src/main/resources/'),rel
assert 'new_modifier' in (R/'forge-1.20.1/src/main/java/art/tiary/mfqm/client/Phase8ClientTrace.java').read_text()
observations=json.loads((D/'observations.json').read_text());assert len(observations['clients'])==4
assert sum(x['lease_frames']for x in observations['clients'].values())==643
native=json.loads((L/'helper-probe.json').read_text());assert native['jar_sha256']=='2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
result={'overall':'PARTIAL','automatic_materials':['quicksand: non-player admitted Contact-output projection only'],'player_automation':'BLOCKED','baseline_GameTests':36,'final_GameTests':43,'JUnit':46,'static_contact_vectors':72,'native_helper_cases':4,'pure_and_vertical_files_unchanged':unchanged,'world_lock_checks':lock_checks,'actual_connected_clients':2,'client_snapshots':4,'natural_generation':'NOT_ENABLED','full_surface':'0/25','historical_failures_retained':True}
(D/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
