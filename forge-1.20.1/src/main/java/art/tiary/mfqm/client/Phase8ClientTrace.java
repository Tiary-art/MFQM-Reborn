package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.legacy.StuckLease;
import net.minecraft.client.Minecraft;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.ComputeFovModifierEvent;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.EventPriority;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import java.io.*;
import java.nio.file.*;
import java.util.Locale;

/** Explicit dev-launch observation only. No key injection, attribute writes or FOV changes. */
@Mod.EventBusSubscriber(modid=MfqmReborn.MOD_ID,value=Dist.CLIENT)
public final class Phase8ClientTrace {
    private static BufferedWriter out;
    private static int remaining=3600;
    private static boolean failed;
    private static void write(String line) {
        if(!Boolean.getBoolean("mfqm.phase8ClientTrace") || failed || remaining<=0)return;
        try {
            if(out==null)out=Files.newBufferedWriter(Path.of("phase8-client.jsonl"));
            out.write(line);out.newLine();out.flush();
        }catch(IOException ex){failed=true;MfqmReborn.LOGGER.warn("Phase8 client trace failed",ex);}
    }
    @SubscribeEvent public static void tick(TickEvent.ClientTickEvent e){
        if(e.phase!=TickEvent.Phase.END || !Boolean.getBoolean("mfqm.phase8ClientTrace"))return;
        var p=Minecraft.getInstance().player;if(p==null)return;
        var speed=p.getAttribute(Attributes.MOVEMENT_SPEED);
        write(String.format(Locale.ROOT,"{\"event\":\"client_tick\",\"millis\":%d,\"tick\":%d,\"dimension\":\"%s\",\"y\":%.9f,\"speed\":%.15g,\"lease\":%s,\"creative\":%s}",
                System.currentTimeMillis(),p.level().getGameTime(),p.level().dimension().location(),p.getY(),speed==null?0:speed.getValue(),speed!=null&&speed.getModifier(StuckLease.UUID_KEY)!=null,p.isCreative()));
        remaining--;
        if(remaining==0 && out!=null)try{out.close();}catch(IOException ignored){}
    }
    @SubscribeEvent(priority=EventPriority.LOWEST) public static void fov(ComputeFovModifierEvent e){
        if(!Boolean.getBoolean("mfqm.phase8ClientTrace"))return;
        var p=e.getPlayer();var speed=p.getAttribute(Attributes.MOVEMENT_SPEED);
        write(String.format(Locale.ROOT,"{\"event\":\"fov_observed\",\"millis\":%d,\"tick\":%d,\"new_modifier\":%.9f,\"lease\":%s}",System.currentTimeMillis(),p.level().getGameTime(),e.getNewFovModifier(),speed!=null&&speed.getModifier(StuckLease.UUID_KEY)!=null));
    }
}
