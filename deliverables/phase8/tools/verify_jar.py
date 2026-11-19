#!/usr/bin/env python3
"""Verify the delivered reobfuscated artifact, not an obsolete filename or a dev class folder."""
from pathlib import Path
import argparse,hashlib,json,zipfile,subprocess
p=argparse.ArgumentParser();p.add_argument('--java-home',type=Path,required=True);a=p.parse_args()
R=Path(__file__).resolve().parents[3];D=R/'deliverables/phase8';jar=D/'mfqm-reborn-phase8-controlled.jar';record=json.loads((R/'docs/phase8/ARTIFACTS.json').read_text())
digest=hashlib.sha256(jar.read_bytes()).hexdigest();assert digest==record['sha256']
base='art/tiary/mfqm/'
required=['integration/OriginalContactBridge.class','legacy/QuicksandContacts.class','integration/StuckAdapter.class','integration/DryWorldAdapter.class','integration/Phase7Commands.class','client/Phase8ClientTrace.class','gametest/Phase8GameTests.class','gametest/Phase8TestIsolation.class']
with zipfile.ZipFile(jar)as z:
 names=set(z.namelist());assert all(base+n in names for n in required)
 assert not any(n.lower().endswith(('.png','.ogg'))for n in names)
 assert all(int.from_bytes(z.read(n)[6:8],'big')==61 for n in names if n.endswith('.class'))
 resources=['META-INF/mods.toml','data/mfqm/legacy_block_catalog.json','assets/mfqm/lang/zh_cn.json']
 assert all(n in names for n in resources)
 manifest=z.read('META-INF/MANIFEST.MF').decode();mods=z.read('META-INF/mods.toml').decode();assert 'mfqm'in mods
with zipfile.ZipFile(R/'deliverables/task-0035-b2/mfqm-reborn-0.0.3.5-b2-candidate.jar')as z:
 old=set(z.namelist());assert all(base+n not in old for n in required)
old_digest=hashlib.sha256((R/'deliverables/task-0035-b2/mfqm-reborn-0.0.3.5-b2-candidate.jar').read_bytes()).hexdigest();assert digest!=old_digest
classes=['physics.SinkingBlock','integration.OriginalContactBridge','integration.StuckAdapter','integration.Phase7Commands','physics.CoreSinkingBlock','legacy.QuicksandContacts']
disassembly={}
for name in classes:
 cmd=[str(a.java_home/'bin/javap'),'-classpath',str(jar),'-c','-p','art.tiary.mfqm.'+name]
 r=subprocess.run(cmd,capture_output=True,text=True);assert r.returncode==0,r.stderr;disassembly[name]=r.stdout
assert 'OriginalContactBridge.inside' in disassembly['physics.SinkingBlock']
assert 'QuicksandContacts.emit' in disassembly['integration.OriginalContactBridge']
assert 'StuckAdapter.automaticContact' in disassembly['integration.OriginalContactBridge']
assert 'StuckLease.update' in disassembly['integration.StuckAdapter']
assert 'StuckAdapter.disableAll' in disassembly['integration.Phase7Commands']
assert 'forcedDisabled' in disassembly['integration.StuckAdapter']
shape=disassembly['physics.CoreSinkingBlock'].split('public double surfaceHeight',1)[1].split('public void randomTick',1)[0]
assert 'FILLED' in shape and 'InterfaceMethod net/minecraft/world/level/BlockGetter.' not in shape
(D/'logs/phase8-delivered-jar.javap.txt').write_text('\n\n'.join(disassembly.values()))
result={'status':'PASS_PACKAGED_BYTECODE_AND_RESOURCE_VERIFICATION','sha256':digest,'required_phase8_classes':required,'hook_chain':['SinkingBlock -> OriginalContactBridge.inside','OriginalContactBridge -> QuicksandContacts.emit -> StuckAdapter.automaticContact','StuckAdapter -> StuckLease.update','Phase7Commands -> StuckAdapter.disableAll'],'shader_shape':'FILLED-state read without BlockGetter query','java_class_version':61,'old_b2_sha256':old_digest,'old_b2_missing_all_required_phase8_classes':True,'manifest':manifest,'packaged_jar_gameplay_runtime_this_delivery':'NOT_RUN; rebuild/JUnit/bytecode inspection only'}
(D/'jar-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
