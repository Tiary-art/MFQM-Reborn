package net.minecraft.world;
import java.util.*;import net.minecraft.block.*;import net.minecraft.init.*;import net.minecraft.block.material.*;import net.minecraft.world.biome.*;import audit.*;
public class World {
 public java.util.Random field_73012_v=new Rng(9,"world");public WorldProvider field_73011_w=new WorldProvider();public BiomeGenBase biome=new BiomeGenBase();
 public net.minecraft.tileentity.TileEntity lastTile;
 public net.minecraft.tileentity.TileEntity func_147438_o(int x,int y,int z){if(fixture.equals("null-tile")||(peek(x,y,z)!=Blocks.field_150474_ac&&peek(x,y,z)!=Blocks.field_150486_ae)){audit.Trace.emit("TILE_GET","kind","null");return null;}lastTile=peek(x,y,z)==Blocks.field_150474_ac?new net.minecraft.tileentity.TileEntityMobSpawner():new net.minecraft.tileentity.TileEntityChest();audit.Trace.emit("TILE_GET","kind",lastTile.getClass().getSimpleName());return lastTile;}
 public static Block fixtureLava=new Block("fixture_lava");static {fixtureLava.material=Material.field_151587_i;fixtureLava.material.solid=false;fixtureLava.material.liquid=true;fixtureLava.material.blocksMovement=false;}
 public String fixture="mud";public Map<String,Block> blocks=new TreeMap<>();public Map<String,Integer>meta=new TreeMap<>();
 String key(int x,int y,int z){return x+","+y+","+z;}
 public Block peek(int x,int y,int z){Block b=blocks.get(key(x,y,z));if(b!=null)return b;
 if(fixture.equals("protected"))return y<=70?MoreFunQuicksandMod.main.MFQM.SoftQuicksandBlock:Blocks.field_150350_a;
 if(fixture.equals("wld-positive")){if(x==-64&&y==63&&z==-48)return fixtureLava;if(x==-69&&y==63&&z==-47)return Blocks.field_150354_m;if(x==-64&&y==61&&z==-48)return Blocks.field_150348_b;return Blocks.field_150350_a;}
 if(fixture.startsWith("plant-"))return y<=70?MoreFunQuicksandMod.main.MFQM.MorassBlock:Blocks.field_150350_a;
 if(fixture.equals("all-layouts")){int code=(x+16)*16+z;if(y==66)return (code&64)!=0?Blocks.field_150355_j:Blocks.field_150350_a;if(y==65)return (code&32)!=0?Blocks.field_150348_b:Blocks.field_150350_a;if(y>=60&&y<=64)return (code&(1<<(y-60)))!=0?Blocks.field_150348_b:Blocks.field_150350_a;return Blocks.field_150350_a;}
 if(fixture.equals("tar"))return MoreFunQuicksandMod.main.MFQM.TarBlock;
 if(fixture.equals("ceiling"))return Blocks.field_150348_b;
 if(fixture.equals("sand-ceiling"))return Blocks.field_150354_m;
 if(fixture.equals("water-alternating"))return y%2==0?Blocks.field_150355_j:Blocks.field_150348_b;
 if(fixture.equals("ground65"))return y<=65?Blocks.field_150354_m:Blocks.field_150350_a;
 if(fixture.equals("water-island")){if(y>70)return Blocks.field_150350_a;if(y==70)return x%4==0?Blocks.field_150355_j:Blocks.field_150354_m;return Blocks.field_150354_m;}
 if(fixture.equals("pond")){if(y>66)return Blocks.field_150350_a;if(y==66)return x%4==0?Blocks.field_150355_j:Blocks.field_150354_m;return Blocks.field_150354_m;}
 if(fixture.startsWith("wld-reject"))return Blocks.field_150350_a;
 if(fixture.equals("empty"))return Blocks.field_150350_a;
 if(fixture.equals("mixed")){if(y==66)return (x+z)%3==0?Blocks.field_150348_b:Blocks.field_150355_j;if(y==65&&(x+z)%2==0||y==62)return Blocks.field_150348_b;return Blocks.field_150350_a;}
 if((fixture.equals("desert")||fixture.equals("desert-refuse")))return y<=70?Blocks.field_150354_m:Blocks.field_150350_a;
 if(fixture.equals("mud")||fixture.equals("deny"))return y==66?Blocks.field_150355_j:Blocks.field_150350_a;
 if(fixture.equals("water"))return y<=70?Blocks.field_150355_j:Blocks.field_150350_a;
 return y<=70?Blocks.field_150348_b:Blocks.field_150350_a;}
 public Block func_147439_a(int x,int y,int z){Block b=peek(x,y,z);Trace.emit("WORLD_READ","api","getBlock","x",x,"y",y,"z",z,"block",b);return b;}
 public boolean func_147465_d(int x,int y,int z,Block b,int m,int f){boolean applied=!fixture.equals("desert-refuse")&&(!fixture.equals("deny")||y!=63)&&(!fixture.equals("all-layouts")||(((x+16)*16+z)&128)==0);if(applied){blocks.put(key(x,y,z),b);meta.put(key(x,y,z),m);}Trace.emit("WORLD_WRITE","api","setBlock","x",x,"y",y,"z",z,"block",b,"metadata",m,"flags",f,"applied",applied);return applied;}
 public boolean func_147449_b(int x,int y,int z,Block b){return func_147465_d(x,y,z,b,0,3);}
 public boolean func_147468_f(int x,int y,int z){return func_147465_d(x,y,z,Blocks.field_150350_a,0,3);}
 public int func_72805_g(int x,int y,int z){int m=meta.getOrDefault(key(x,y,z),0);Trace.emit("WORLD_READ","api","metadata","x",x,"y",y,"z",z,"value",m);return m;}
 public BiomeGenBase func_72807_a(int x,int z){biome.flowerName=fixture.equals("plant-null")?"none":"fixture_flower";Trace.emit("WORLD_READ","api","biome","x",x,"z",z,"id",biome.field_76756_M);return biome;}
 public boolean func_147437_c(int x,int y,int z){return func_147439_a(x,y,z)==Blocks.field_150350_a;}
 public boolean func_72899_e(int x,int y,int z){Trace.emit("WORLD_READ","api","chunkExists","x",x,"y",y,"z",z);if(fixture.startsWith("wld-reject"))return false;if(fixture.equals("wld-positive"))return x==-56&&z==-40;Trace.unresolved("chunk existence unspecified");return false;}
 public net.minecraft.world.storage.WorldInfo func_72912_H(){return new net.minecraft.world.storage.WorldInfo();}
}
