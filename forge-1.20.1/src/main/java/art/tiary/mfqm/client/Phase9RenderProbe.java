package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.registry.ModBlocks;
import net.minecraft.client.Minecraft;
import net.minecraft.client.Screenshot;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import java.nio.file.*;
import java.util.*;
import com.google.gson.Gson;

/** Opt-in local render evidence; private screenshots stay in the explicitly supplied local folder. */
@Mod.EventBusSubscriber(modid=MfqmReborn.MOD_ID,value=Dist.CLIENT)
public final class Phase9RenderProbe {
    private static int ticks,captures;
    private static boolean reloaded, reloadRequested;
    @SubscribeEvent public static void tick(TickEvent.ClientTickEvent event) {
        String dir=System.getProperty("mfqm.phase9ProbeDir");
        if(dir==null || event.phase!=TickEvent.Phase.END)return;
        var mc=Minecraft.getInstance();if(mc.player==null)return;
        ticks++;
        if(ticks%80!=0 || captures>=12 || reloadRequested && !reloaded)return;
        Path out=Path.of(dir);
        try {
            Files.createDirectories(out);Map<String,Object> evidence=new LinkedHashMap<>();
            evidence.put("tick",mc.level.getGameTime());evidence.put("position",mc.player.position().toString());
            Map<String,Object> sprites=new LinkedHashMap<>();
            for(String id:List.of("quicksand","mud","soft_quicksand","leaves_pile","acid","bog")) {
                var block=ModBlocks.LEGACY.get(id).get();var state=block.defaultBlockState();
                var model=mc.getBlockRenderer().getBlockModelShaper().getBlockModel(state);
                Map<String,Object> item=new LinkedHashMap<>();
                item.put("particle",model.getParticleIcon().contents().name().toString());
                Set<String> faces=new TreeSet<>();
                for(var q:model.getQuads(state,null,net.minecraft.util.RandomSource.create(0)))faces.add(q.getSprite().contents().name().toString());
                for(var face:net.minecraft.core.Direction.values())for(var q:model.getQuads(state,face,net.minecraft.util.RandomSource.create(0)))faces.add(q.getSprite().contents().name().toString());
                item.put("face_sprites",faces);
                if(art.tiary.mfqm.content.LegacyFluids.ALL.containsKey(id)) {
                    item.put("still",OriginalTextureBindings.fluid(id,false).toString());item.put("flowing",OriginalTextureBindings.fluid(id,true).toString());
                    var atlas=mc.getTextureAtlas(net.minecraft.world.inventory.InventoryMenu.BLOCK_ATLAS);
                    var stillSprite=atlas.apply(OriginalTextureBindings.fluid(id,false));
                    var flowingSprite=atlas.apply(OriginalTextureBindings.fluid(id,true));
                    item.put("still_atlas_name",stillSprite.contents().name().toString());item.put("flowing_atlas_name",flowingSprite.contents().name().toString());
                    item.put("still_unique_frames",stillSprite.contents().getUniqueFrames().count());item.put("flowing_unique_frames",flowingSprite.contents().getUniqueFrames().count());
                }
                sprites.put(id,item);
            }
            evidence.put("sprites",sprites);evidence.put("after_programmatic_F3T_equivalent",reloaded);
            Files.writeString(out.resolve("probe-"+captures+".json"),new Gson().toJson(evidence));
            // Framebuffer capture is private and is not embedded in public test fixtures/reports.
            Screenshot.grab(out.toFile(),mc.getMainRenderTarget(),ignored->{});
            MfqmReborn.LOGGER.info("PHASE9_RENDER_PROBE capture={} after_reload={} sprites={}",captures,reloaded,sprites);
            captures++;
            if(captures==4 && !reloadRequested){reloadRequested=true;mc.reloadResourcePacks().thenRun(()->reloaded=true);}
        }catch(Exception ex){MfqmReborn.LOGGER.warn("Phase9 render probe failed",ex);}
    }
}
