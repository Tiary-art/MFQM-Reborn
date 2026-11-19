#!/usr/bin/env python3
from pathlib import Path
import argparse,subprocess,sys,json,re
ap=argparse.ArgumentParser();ap.add_argument('--phase1',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();repo=Path(__file__).resolve().parents[4];base=repo/'research/original-phase4/evidence/tools/prepare.py';p=subprocess.run([sys.executable,'-B',str(base),'--phase1',str(a.phase1),'--out',str(a.out)],capture_output=True,text=True);assert p.returncode==0,p.stderr
src=a.out/'src'
def write(cls,body):
 path=src/(cls.replace('.','/')+'.java');path.parent.mkdir(parents=True,exist_ok=True);path.write_text('package '+cls.rsplit('.',1)[0]+';\n'+body+'\n')
# Compile-time placeholder is overwritten before any test JVM starts by DeriveType.
write('MoreFunQuicksandMod.main.blocks.BlockMorass','public class BlockMorass extends net.minecraft.block.Block {public BlockMorass(String id){super(id);}public void PlantingThis(net.minecraft.world.World w,java.util.Random r,int x,int y,int z){throw new AssertionError("placeholder must never execute");}}')
f=src/'MoreFunQuicksandMod/main/MFQM.java';s=f.read_text().replace('MorassBlock=new net.minecraft.block.Block("MorassBlock")','MorassBlock=new MoreFunQuicksandMod.main.blocks.BlockMorass("MorassBlock")');assert 'new MoreFunQuicksandMod.main.blocks.BlockMorass'in s;f.write_text(s)
mat=src/'net/minecraft/block/material/Material.java';text=mat.read_text();mat.write_text(text.rsplit('}',1)[0]+'public static Material field_151583_m=new Material("field_151583_m");}')
f=src/'net/minecraft/block/Block.java';s=f.read_text().replace('public String toString()', 'public boolean func_149721_r(){return material.solid;}public String toString()');f.write_text(s)
write('net.minecraft.block.BlockFlower','''public class BlockFlower extends Block {public static BlockFlower flower=new BlockFlower("fixture_flower");public BlockFlower(String n){super(n);material=net.minecraft.block.material.Material.field_151585_k;}public boolean func_149721_r(){return false;}public static BlockFlower func_149857_e(String name){audit.Trace.emit("FLOWER_LOOKUP","name",name);return name.equals("none")?null:flower;}public static int func_149856_f(String name){return 2;}public boolean func_149718_j(net.minecraft.world.World w,int x,int y,int z){boolean ok=!w.fixture.equals("plant-refuse");audit.Trace.emit("PLANT_CHECK","x",x,"y",y,"z",z,"allowed",ok);return ok;}}''')
f=src/'net/minecraft/world/biome/BiomeGenBase.java';s=f.read_text().replace('public int field_', 'public String func_150572_a(java.util.Random r,int x,int y,int z){audit.Trace.emit("BIOME_FLOWER","x",x,"y",y,"z",z);return "fixture_flower";}public int field_',1);f.write_text(s.replace('public String func_150572_a','public String flowerName="fixture_flower";public String func_150572_a').replace('return "fixture_flower";','return flowerName;'))
# Original method offset list includes the exact original PlantingThis body.
ms=json.loads((a.phase1/'indexes/methods-with-instructions.json').read_text());selected=json.loads((a.out/'methods-selected.json').read_text());lines=(a.out/'offsets.tsv').read_text().splitlines()
for m in ms:
 if m['class'].endswith('.blocks.BlockMorass')and m['name']=='PlantingThis':
  selected.append(m)
  for i in m['instructions']:
   target=i['args'].split()[0]if i['opcode'].startswith('if')or i['opcode']in ['goto','goto_w']else'';lines.append(m['class']+'#'+m['name']+m['descriptor']+'\t'+str(i['offset'])+('\t'+target if target else''))
from extra_env import add
add(src,ms,selected,lines)
(a.out/'offsets.tsv').write_text('\n'.join(lines)+'\n');(a.out/'methods-selected.json').write_text(json.dumps(selected,indent=1)+'\n');print('Phase5 typed Morass shell + original PlantingThis input prepared')

raw=(a.phase1/'evidence/fresh-javap-all.txt').read_text().splitlines()
for m in selected:
 m['switches']={}
 for i in m['instructions']:
  if i['opcode'] not in ['tableswitch','lookupswitch']:continue
  cases={}
  for line in raw[i['javap_line']:]:
   if '}'in line:break
   mt=re.match(r'\s+(default|-?\d+):\s+(\d+)',line)
   if mt:cases[mt[1]]=int(mt[2])
  m['switches'][str(i['offset'])]=cases
(a.out/'oracle-methods.json').write_text(json.dumps(selected,indent=1)+'\n')
