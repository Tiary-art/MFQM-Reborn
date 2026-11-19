package audit;
import java.nio.file.*;import java.io.*;import java.lang.reflect.*;import net.minecraft.entity.*;import net.minecraftforge.event.entity.living.LivingEvent.LivingUpdateEvent;
public class StuckRun {
 public static void main(String[]a)throws Exception{Trace.out=new PrintWriter(Files.newBufferedWriter(Path.of(a[0])));Class<?>c=Class.forName("MoreFunQuicksandMod.main.CustomPotionEvent");Object o=c.getConstructor().newInstance();Method m=c.getMethod("onLivingUpdateEvent",LivingUpdateEvent.class);EntityLivingBase e=new EntityLivingBase();
 Trace.emit("HEADER","trace_kind","MODEL_TRACE","contract","original LivingUpdate body; attribute/property API mocks");
 int[][]callbacks={{145},{},{},{145,128},{50},{255},{0}};
 for(int tick=0;tick<callbacks.length;tick++){Trace.emit("TICK","tick",tick);for(int level:callbacks[tick])e.props.setStuckLevel(level);e.field_70747_aH=.02f;e.field_70124_G=tick%2==0;m.invoke(o,new LivingUpdateEvent(e));Trace.emit("SNAPSHOT","tick",tick,"level",e.props.getLevel(),"jump",e.field_70747_aH,"modifiers",e.attrs.map.size());}
 e.props=null;Trace.emit("TICK","tick",7);m.invoke(o,new LivingUpdateEvent(e));Trace.emit("SNAPSHOT","tick",7,"level","no-property","jump",e.field_70747_aH,"modifiers",e.attrs.map.size());Trace.out.close();}
}
