package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.registry.ModTabs;
import com.google.gson.*;
import net.minecraft.client.Minecraft;
import net.minecraft.client.Screenshot;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.inventory.InventoryMenu;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.RenderGuiEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.registries.ForgeRegistries;
import java.nio.file.*;
import java.util.List;

/** Opt-in verification of creative stacks through the in-game GUI item renderer. */
@Mod.EventBusSubscriber(modid=MfqmReborn.MOD_ID,value=Dist.CLIENT)
public final class R1AtlasProbe {
    private static List<ItemStack> stacks;
    private static int frames;
    private static boolean reloading;
    @SubscribeEvent public static void afterHud(RenderGuiEvent.Post event) throws Exception {
        String dir = System.getProperty("mfqm.r1Atlas");
        if (dir == null || reloading) return;
        var mc = Minecraft.getInstance();
        if (mc.level == null || mc.player == null) return;
        if (stacks == null) {
            var tab = ModTabs.CONTENT.get();
            tab.buildContents(new CreativeModeTab.ItemDisplayParameters(mc.level.enabledFeatures(),true,mc.level.registryAccess()));
            stacks = List.copyOf(tab.getDisplayItems());
        }
        var graphics = event.getGuiGraphics();
        int columns = Math.max(1,(graphics.guiWidth()-8)/18);
        for (int i=0;i<stacks.size();i++) graphics.renderItem(stacks.get(i),4+(i%columns)*18,4+(i/columns)*18);
        graphics.flush();
        frames++;
        if (frames != 40 && frames != 100) return;
        Path output=Path.of(dir);
        Files.createDirectories(output);
        var report=new JsonArray();
        for(var stack:stacks) {
            var model=mc.getItemRenderer().getModel(stack,mc.level,mc.player,0);
            var row=new JsonObject();
            row.addProperty("id",ForgeRegistries.ITEMS.getKey(stack.getItem()).toString());
            row.addProperty("name",stack.getHoverName().getString());
            row.addProperty("particle",model.getParticleIcon().contents().name().toString());
            row.addProperty("missing_model",model==mc.getModelManager().getMissingModel());
            report.add(row);
        }
        var sprite=mc.getTextureAtlas(InventoryMenu.BLOCK_ATLAS).apply(new ResourceLocation("mfqm","block/original/mucus_flowing"));
        MfqmReborn.LOGGER.info("R1 GUI stacks={} mucus sprite={} size={}x{} frames={} capture={}",stacks.size(),
                sprite.contents().name(),sprite.contents().width(),sprite.contents().height(),sprite.contents().getUniqueFrames().count(),frames);
        Files.writeString(output.resolve("atlas-"+frames+".json"),new Gson().toJson(report));
        Screenshot.grab(output.toFile(),mc.getMainRenderTarget(),ignored->{});
        if(frames==40) {
            reloading=true;
            mc.reloadResourcePacks().thenRun(()->mc.execute(()->reloading=false));
        } else mc.execute(mc::stop);
    }
}
