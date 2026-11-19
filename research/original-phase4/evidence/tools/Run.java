package audit;
import java.io.*;import java.nio.file.*;import java.lang.reflect.*;import java.util.*;import net.minecraft.world.*;import net.minecraft.block.*;import net.minecraft.block.material.*;import MoreFunQuicksandMod.main.MFQM;
public class Run {
 public static void main(String[]args)throws Exception {
 // jar offsets output method seed radius terrain targetBlock optionalMode
 boolean failed=false;Trace.out=new PrintWriter(Files.newBufferedWriter(Path.of(args[2])));String name=args[3];long seed=Long.parseLong(args[4]);int rad=Integer.parseInt(args[5]);World w=new World();w.fixture=args[6];Rng r=new Rng(seed,"passed");
 Trace.emit("HEADER","trace_kind","MODEL_TRACE","engine","original class bytes + in-memory logging + declared environment contracts","seed",seed,"method_requested",name,"fixture",w.fixture);
 try {Instrument loader=new Instrument(args[0],args[1]);Class<?>c=loader.loadClass("MoreFunQuicksandMod.main.CustomWorldGen");Object obj=c.getConstructor().newInstance();Method m;Object[]params;
  if(name.equals("generateSurface")){String cfg=args[7];if(!cfg.equals("NONE"))MFQM.class.getField(cfg).setBoolean(null,true);w.biome=new net.minecraft.world.biome.BiomeGenDesert();m=c.getDeclaredMethod(name,World.class,java.util.Random.class,int.class,int.class,int.class);params=new Object[]{w,r,-16,0,62};}
  else if(name.equals("generateAOADimGardencia")){String cfg=args[7];if(!cfg.equals("NONE"))MFQM.class.getField(cfg).setBoolean(null,true);m=c.getDeclaredMethod(name,World.class,java.util.Random.class,int.class,int.class);params=new Object[]{w,r,-16,0};}
  else if(name.equals("generateLiquidMire")){m=c.getDeclaredMethod(name,int.class,int.class,int.class,int.class,World.class,java.util.Random.class,Material.class,int.class);params=new Object[]{-16,70,0,rad,w,r,Material.field_151568_F,Integer.parseInt(args[7])};}
  else if(name.equals("generateMorass")){m=c.getDeclaredMethod(name,int.class,int.class,int.class,int.class,World.class,java.util.Random.class,float.class,int.class);params=new Object[]{-16,70,0,rad,w,r,1f,0};}
  else if(name.equals("generateMireOD")){m=c.getDeclaredMethod(name,int.class,int.class,int.class,int.class,World.class,java.util.Random.class,Material.class,Block.class,int.class);params=new Object[]{-16,70,0,rad,w,r,Material.field_151568_F,MFQM.JungleQuicksandBlock,0};}
  else {m=c.getDeclaredMethod(name,int.class,int.class,int.class,int.class,World.class,java.util.Random.class,Material.class,Block.class);params=new Object[]{-16,70,0,rad,w,r,Material.field_151568_F,MFQM.JungleQuicksandBlock};}
  m.setAccessible(true);m.invoke(obj,params);Trace.emit("RESULT","status","MODEL_TESTED","writes",w.blocks.size());
 } catch(Throwable e){Throwable cause=e instanceof InvocationTargetException?e.getCause():e;Trace.emit("ERROR","type",cause.getClass().getName(),"message",cause.toString());cause.printStackTrace();failed=true;}
 finally{Trace.out.flush();Trace.out.close();PrintWriter cover=new PrintWriter(Files.newBufferedWriter(Path.of(args[2]+".coverage.tsv")));for(var en:Trace.coverage.entrySet())for(int off:en.getValue())cover.println(en.getKey()+"\t"+off);cover.close();PrintWriter fin=new PrintWriter(Files.newBufferedWriter(Path.of(args[2]+".final.tsv")));for(var en:w.blocks.entrySet())fin.println(en.getKey()+"\t"+en.getValue()+"\t"+w.meta.getOrDefault(en.getKey(),0));fin.close();}
 if(failed)System.exit(1);
 }
}
