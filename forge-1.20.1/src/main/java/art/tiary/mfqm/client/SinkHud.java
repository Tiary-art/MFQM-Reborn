package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.state.SinkCapability;
import java.util.Locale;
import net.minecraft.client.Minecraft;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.RegisterGuiOverlaysEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID, value = Dist.CLIENT, bus = Mod.EventBusSubscriber.Bus.MOD)
public final class SinkHud {
    private SinkHud() { }
    @SubscribeEvent public static void register(RegisterGuiOverlaysEvent event) {
        event.registerBelowAll("material_camera", (gui, graphics, partialTick, width, height) -> {
            var mc=Minecraft.getInstance();
            if(mc.level==null) return;
            var eye=mc.gameRenderer.getMainCamera().getPosition();
            var pos=net.minecraft.core.BlockPos.containing(eye);
            var state=mc.level.getBlockState(pos);
            if(!(state.getBlock() instanceof art.tiary.mfqm.physics.SinkingMedium b) || eye.y>=pos.getY()+b.surfaceHeight(state,mc.level,pos)) return;
            String texture=b.profile()==art.tiary.mfqm.physics.MaterialProfile.MUD ? "mud" : b.profile()==art.tiary.mfqm.physics.MaterialProfile.SOFT_QUICKSAND ? "red_sand" : "sand";
            com.mojang.blaze3d.systems.RenderSystem.enableBlend();
            com.mojang.blaze3d.systems.RenderSystem.setShaderColor(.4f,.4f,.4f,.78f);
            graphics.blit(new net.minecraft.resources.ResourceLocation("minecraft","textures/block/"+texture+".png"),0,0,width,height,0,0,16,16,16,16);
            com.mojang.blaze3d.systems.RenderSystem.setShaderColor(1,1,1,1);
            com.mojang.blaze3d.systems.RenderSystem.disableBlend();
        });
        event.registerAboveAll("sink_status", (gui, graphics, partialTick, width, height) -> {
            var mc = Minecraft.getInstance();
            if (mc.player == null || mc.options.hideGui) return;
            var data = SinkCapability.get(mc.player);
            if (data == null || !data.active() && data.air >= 300) return;
            String text = String.format(Locale.ROOT, "MFQM %s | depth %.0f%% | air %d/300",
                    data.active() ? data.material.id : "clear", data.immersion * 100, Math.max(0, data.air));
            graphics.drawString(mc.font, text, 6, 6, 0xFFFFFF, true);
        });
    }
}
