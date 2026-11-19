package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import com.google.gson.JsonParser;
import net.minecraft.client.Minecraft;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.RegisterClientReloadListenersEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Map;
import java.util.HashMap;

/** Client rendering only. Missing private marker keeps the exact public water/tint fallback. */
@Mod.EventBusSubscriber(modid=MfqmReborn.MOD_ID,bus=Mod.EventBusSubscriber.Bus.MOD,value=Dist.CLIENT)
public final class OriginalTextureBindings {
    private static volatile Map<String,ResourceLocation[]> cached;
    private static Map<String,ResourceLocation[]> bindings() {
        var current=cached;if(current!=null)return current;
        var result=new HashMap<String,ResourceLocation[]>();
        var resource=Minecraft.getInstance().getResourceManager().getResource(new ResourceLocation("mfqm","original_texture_bindings.json"));
        if(resource.isPresent())try(var reader=new InputStreamReader(resource.get().open(),StandardCharsets.UTF_8)){
            var root=JsonParser.parseReader(reader).getAsJsonObject();
            for(var e:root.getAsJsonObject("fluids").entrySet()){
                var o=e.getValue().getAsJsonObject();result.put(e.getKey(),new ResourceLocation[]{new ResourceLocation(o.get("still").getAsString()),new ResourceLocation(o.get("flowing").getAsString())});
            }
        }catch(Exception ex){MfqmReborn.LOGGER.warn("Invalid private texture bindings; using public placeholders",ex);}
        return cached=Map.copyOf(result);
    }
    public static boolean hasFluid(String id){return bindings().containsKey(id);}
    public static ResourceLocation fluid(String id,boolean flowing){
        var pair=bindings().get(id);
        return pair==null?new ResourceLocation("minecraft",flowing?"block/water_flow":"block/water_still"):pair[flowing?1:0];
    }
    @SubscribeEvent public static void reload(RegisterClientReloadListenersEvent event){
        event.registerReloadListener((net.minecraft.server.packs.resources.ResourceManagerReloadListener)manager->cached=null);
    }
}
