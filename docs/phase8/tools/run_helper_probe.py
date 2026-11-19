#!/usr/bin/env python3
import argparse,subprocess,tempfile,json,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--jar',type=Path,required=True);p.add_argument('--java-home',type=Path,required=True);a=p.parse_args()
r=Path(__file__).resolve().parents[3];log=r/'docs/phase8/logs';commands=[]
with tempfile.TemporaryDirectory(prefix='mfqm-phase8-helper-')as d:
 root=Path(d);src=root/'src';classes=root/'classes';classes.mkdir()
 for name,text in {
 'net/minecraft/world/World.java':'package net.minecraft.world; public class World { public boolean field_72995_K; }',
 'net/minecraft/entity/Entity.java':'package net.minecraft.entity; public class Entity { public net.minecraft.world.World field_70170_p; }',
 'net/minecraft/entity/player/EntityPlayer.java':'package net.minecraft.entity.player; public class EntityPlayer extends net.minecraft.entity.Entity {}',
 }.items():
  f=src/name;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(text)
 commands.append([str(a.java_home/'bin/javac'),'--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED','-d',str(classes),str(r/'research/original-phase5/evidence/tools/BodyProof.java'),str(Path(__file__).with_name('HelperProbe.java')),*map(str,src.rglob('*.java'))])
 commands.append([str(a.java_home/'bin/java'),'--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED','-cp',str(classes),'audit.HelperProbe',str(a.jar),str(classes)])
 results=[]
 for n,cmd in enumerate(commands):
  x=subprocess.run(cmd,capture_output=True,text=True);(log/f'helper-probe-{n}.stdout').write_text(x.stdout);(log/f'helper-probe-{n}.stderr').write_text(x.stderr);results.append({'command':cmd,'exit':x.returncode});assert x.returncode==0,x.stderr
(log/'helper-probe.json').write_text(json.dumps({'results':results,'jar_sha256':hashlib.sha256(a.jar.read_bytes()).hexdigest(),'runtime':'unchanged selected original method body in explicit mocked type shell, not original Minecraft gameplay'},indent=2)+'\n')
