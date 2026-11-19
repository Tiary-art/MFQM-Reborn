package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.state.SinkCapability;
import net.minecraft.client.Minecraft;
import net.minecraft.client.renderer.*;
import net.minecraft.client.renderer.entity.player.PlayerRenderer;
import net.minecraft.client.renderer.texture.OverlayTexture;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.HumanoidArm;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.RenderArmEvent;
import net.minecraftforge.eventbus.api.*;
import net.minecraftforge.fml.common.Mod;

/** Draw the normal arm first, then an independent coating; respect already-cancelled custom hand renders. */
@Mod.EventBusSubscriber(modid=MfqmReborn.MOD_ID,value=Dist.CLIENT)
public final class CoatingHands {
    private static boolean drawingVanilla;
    @SubscribeEvent(priority=EventPriority.LOWEST) public static void arm(RenderArmEvent e) {
        if(drawingVanilla || e.getPlayer().isInvisible()) return;
        var d=SinkCapability.get(e.getPlayer());if(d==null || d.residueTicks<=0) return;
        var renderer=(PlayerRenderer)Minecraft.getInstance().getEntityRenderDispatcher().getRenderer(e.getPlayer());
        e.setCanceled(true);
        drawingVanilla=true;
        try {
            if(e.getArm()==HumanoidArm.RIGHT) renderer.renderRightHand(e.getPoseStack(),e.getMultiBufferSource(),e.getPackedLight(),e.getPlayer());
            else renderer.renderLeftHand(e.getPoseStack(),e.getMultiBufferSource(),e.getPackedLight(),e.getPlayer());
        } finally { drawingVanilla=false; }
        var model=renderer.getModel();var arm=e.getArm()==HumanoidArm.RIGHT?model.rightArm:model.leftArm;
        var sleeve=e.getArm()==HumanoidArm.RIGHT?model.rightSleeve:model.leftSleeve;
        String texture=d.residueType.equals("mud")?"mud":d.residueType.equals("soft_quicksand")?"red_sand":"sand";
        var consumer=e.getMultiBufferSource().getBuffer(RenderType.entityTranslucent(new ResourceLocation("minecraft","textures/block/"+texture+".png")));
        var poses=e.getPoseStack();poses.pushPose();poses.scale(1.008f,1.008f,1.008f);
        float alpha=Math.min(.65f,d.residueTicks/500f);
        arm.render(poses,consumer,e.getPackedLight(),OverlayTexture.NO_OVERLAY,1,1,1,alpha);
        sleeve.render(poses,consumer,e.getPackedLight(),OverlayTexture.NO_OVERLAY,1,1,1,alpha);
        poses.popPose();
    }
}
