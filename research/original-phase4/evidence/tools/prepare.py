#!/usr/bin/env python3
import argparse,json,re,collections,shutil
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--phase1',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();root=a.out;src=root/'src';src.mkdir(parents=True,exist_ok=True)
ms=json.loads((a.phase1/'indexes/methods-with-instructions.json').read_text());cwg=[m for m in ms if m['class'].endswith('.CustomWorldGen')];refs=collections.defaultdict(set)
for m in [m for m in ms if m['class'].split('.')[-1] in ['CustomWorldGen','GenerateMucusBlossom']]:
 for i in m['instructions']:
  if i['opcode']in ['getfield','getstatic','putfield','putstatic']and '// Field 'in i['args']:
   k,d=i['args'].split('// Field ',1)[1].split(':');refs[k].add(d)
def write(cls,body):
 p=src/(cls.replace('.','/')+'.java');p.parent.mkdir(parents=True,exist_ok=True);p.write_text('package '+cls.rsplit('.',1)[0]+';\n'+body+'\n')
# These are declared environment contracts, NOT copies of Minecraft implementation.
matfields=sorted({k.split('.')[-1]for k in refs if k.startswith('net/minecraft/block/material/Material.')})
write('net.minecraft.block.material.Material','''public class Material {
 public final String id;public boolean solid,liquid,blocksMovement;public Material(String id){this.id=id;solid=!id.equals("field_151579_a")&&!id.equals("field_151586_h");liquid=id.equals("field_151586_h");blocksMovement=solid;}
 public boolean func_76220_a(){return solid;}public boolean func_76224_d(){return liquid;}public boolean func_76218_k(){return blocksMovement;}
 public String toString(){return id;}
'''+ '\n'.join('public static Material '+f+'=new Material("'+f+'");'for f in matfields)+'}')
write('net.minecraft.block.Block','''public class Block {
 public final String id;public net.minecraft.block.material.Material material;
 public Block(String id){this.id=id;material=net.minecraft.block.material.Material.field_151576_e;}
 public net.minecraft.block.material.Material func_149688_o(){return material;}
 public boolean func_149662_c(){return material.solid;}public boolean func_149716_u(){return false;}
 public String toString(){return id;}
}''')
# Preserve exact field descriptors (BlockGrass/BlockSand/etc) for linkage.
types={'net.minecraft.block.Block'}
for k,ds in refs.items():
 if k.startswith('net/minecraft/init/Blocks.'):
  for d in ds:types.add(d[1:-1].replace('/','.'))
for t in types-{'net.minecraft.block.Block'}:write(t,'public class '+t.split('.')[-1]+' extends Block {public '+t.split('.')[-1]+'(String id){super(id);}}')
def typename(d):return {'I':'int','Z':'boolean','[I':'int[]','F':'float','D':'double'}.get(d,d[1:-1].replace('/','.')if d.startswith('L')else'UNSUPPORTED')
blockdecl=[]
for k,ds in refs.items():
 if k.startswith('net/minecraft/init/Blocks.'):
  f=k.split('.')[-1];t=typename(next(iter(ds)));blockdecl.append('public static '+t+' '+f+'=new '+t+'("'+f+'");')
write('net.minecraft.init.Blocks','public class Blocks {'+'\n'.join(blockdecl)+'''
 static {field_150350_a.material=net.minecraft.block.material.Material.field_151579_a;field_150355_j.material=net.minecraft.block.material.Material.field_151586_h;field_150358_i.material=net.minecraft.block.material.Material.field_151586_h;field_150354_m.material=net.minecraft.block.material.Material.field_151595_p;}
}''')
mdecl=[]
for k,ds in refs.items():
 if 'MFQM.'in k:
  f=k.split('.')[-1];d=next(iter(ds));t=typename(d)
  val='false'if d=='Z'else'0'if d=='I'else'new int[256]'if d=='[I'else'new net.minecraft.block.Block("'+f+'")'if t=='net.minecraft.block.Block'else'null'
  mdecl.append('public static '+t+' '+f+'='+val+';')
write('MoreFunQuicksandMod.main.MFQM','public class MFQM {'+'\n'.join(mdecl)+'}')
write('net.minecraft.inventory.IInventory','public interface IInventory {}')
write('net.minecraft.world.gen.feature.WorldGenerator','public abstract class WorldGenerator {public abstract boolean func_76484_a(net.minecraft.world.World w,java.util.Random r,int x,int y,int z);}')
write('net.minecraft.world.chunk.IChunkProvider','public interface IChunkProvider {}')
write('cpw.mods.fml.common.IWorldGenerator','public interface IWorldGenerator {void generate(java.util.Random r,int x,int z,net.minecraft.world.World w,net.minecraft.world.chunk.IChunkProvider a,net.minecraft.world.chunk.IChunkProvider b);}')
write('net.minecraft.world.WorldProvider','public class WorldProvider {public int field_76574_g;}')
write('net.minecraft.world.biome.BiomeGenBase','''public class BiomeGenBase {public int field_76756_M=1;public net.minecraft.block.Block field_76752_A=net.minecraft.init.Blocks.field_150349_c,field_76753_B=net.minecraft.init.Blocks.field_150346_d;}''')
for name in ['BiomeGenSwamp','BiomeGenJungle','BiomeGenForest','BiomeGenDesert','BiomeGenSnow','BiomeGenHills','BiomeGenPlains','BiomeGenMesa','BiomeGenSavanna','BiomeGenTaiga','BiomeGenOcean','BiomeGenRiver','BiomeGenBeach','BiomeGenStoneBeach']:
 write('net.minecraft.world.biome.'+name,'public class '+name+' extends BiomeGenBase {}')
# Support types used during JVM verification; none of these are silent generator stubs.
write('net.minecraftforge.common.BiomeDictionary','public class BiomeDictionary {public enum Type {SWAMP,FOREST,FROZEN,COLD,HOT,SAVANNA,DRY,PLAINS,SPOOKY,RIVER,OCEAN,WET,JUNGLE,BEACH,DESERT,SANDY} public static boolean isBiomeOfType(net.minecraft.world.biome.BiomeGenBase b,Type t){audit.Trace.unresolved("BiomeDictionary mock not specified");return false;}}')
write('net.minecraft.world.WorldType','public class WorldType {public static WorldType field_77135_d=new WorldType(),field_77137_b=new WorldType();}')
write('net.minecraft.world.storage.WorldInfo','public class WorldInfo {public net.minecraft.world.WorldType func_76067_t(){return net.minecraft.world.WorldType.field_77135_d;}}')
write('net.minecraft.util.Vec3','public class Vec3 {public double field_72450_a,field_72448_b,field_72449_c;}')
# Actual helper source is not replaced: missing ecology callback fails explicitly.
for name in ['BlockMorass','BlockBog','BlockSlurry']:
 write('MoreFunQuicksandMod.main.liquids.'+name,'public class '+name+' extends net.minecraft.block.Block {public '+name+'(){super("'+name+'");}public void PlantingThis(net.minecraft.world.World w,java.util.Random r,int x,int y,int z){audit.Trace.unresolved("'+name+'.PlantingThis");}}')
# Only selected methods instrumented; rest of original class remains unchanged in memory.
selected={'generateSurface','generateMire','generateSoftSand','validSandMaterial','getDesertType','generateAOADimGardencia','generateMireO','generateMireOD','generateLiquidMire','generateMorass','generateWater','soilBlock','fillerBlock','validWaterMaterial','validSolidMaterial','validLiqMaterial','validPlantMaterial','validGroundMaterial','isAboveFreeSpace','genIsFlat','genIsFlatSolid','isGroundQS','isGroundNear','spawnMorass','generateLeavesAround'}
# Instrument the complete within-class call closure so nested World/RNG events
# retain the true original callee location rather than the parent callsite.
import csv
calls=list(csv.DictReader((a.phase1/'indexes/calls.csv').open()))
changed=True
while changed:
 changed=False
 for edge in calls:
  if edge['caller_class']=='MoreFunQuicksandMod.main.CustomWorldGen' and edge['caller_method']in selected and edge['target_class']=='MoreFunQuicksandMod.main.CustomWorldGen' and edge['target_method']not in selected:
   selected.add(edge['target_method']);changed=True
(root/'instrumented-method-names.json').write_text(json.dumps(sorted(selected),indent=2)+'\n')
lines=[]
for m in [m for m in ms if m['class'].split('.')[-1]in ['CustomWorldGen','GenerateMucusBlossom']]:
 if m['name']not in selected and not(m['class'].endswith('GenerateMucusBlossom')and m['name']!='<init>'):continue
 key=m['class']+'#'+m['name']+m['descriptor']
 for i in m['instructions']:
  target=i['args'].split()[0]if i['opcode'].startswith('if')or i['opcode']in ['goto','goto_w']else''
  lines.append(key+'\t'+str(i['offset'])+('\t'+target if target else''))
(root/'offsets.tsv').write_text('\n'.join(lines)+'\n');(root/'methods-selected.json').write_text(json.dumps([m for m in cwg if m['name']in selected],indent=1)+'\n');print('prepared environment contracts and',len(lines),'original offset mappings')
