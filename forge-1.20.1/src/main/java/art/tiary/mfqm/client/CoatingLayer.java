package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.state.SinkCapability;
import com.mojang.blaze3d.vertex.PoseStack;
import net.minecraft.client.model.PlayerModel;
import net.minecraft.client.player.AbstractClientPlayer;
import net.minecraft.client.renderer.*;
import net.minecraft.client.renderer.entity.player.PlayerRenderer;
import net.minecraft.client.renderer.entity.layers.RenderLayer;
import net.minecraft.client.renderer.texture.OverlayTexture;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.EntityRenderersEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** Independent translucent layer; never replaces the player's skin or resource pack. Standard armor is covered separately; custom mod armor geometry is not reproduced. */
@Mod.EventBusSubscriber(modid=MfqmReborn.MOD_ID,value=Dist.CLIENT,bus=Mod.EventBusSubscriber.Bus.MOD)
public final class CoatingLayer extends RenderLayer<AbstractClientPlayer,PlayerModel<AbstractClientPlayer>> {
    private final net.minecraft.client.model.HumanoidModel<AbstractClientPlayer> inner,outer;
    public CoatingLayer(PlayerRenderer parent,net.minecraft.client.model.geom.EntityModelSet models) {
        super(parent);
        inner=new net.minecraft.client.model.HumanoidModel<>(models.bakeLayer(net.minecraft.client.model.geom.ModelLayers.PLAYER_INNER_ARMOR));
        outer=new net.minecraft.client.model.HumanoidModel<>(models.bakeLayer(net.minecraft.client.model.geom.ModelLayers.PLAYER_OUTER_ARMOR));
    }
    @SubscribeEvent public static void layers(EntityRenderersEvent.AddLayers e) {
        for(String skin:e.getSkins()) { PlayerRenderer r=e.getSkin(skin); if(r!=null) r.addLayer(new CoatingLayer(r,e.getEntityModels())); }
    }
    @Override public void render(PoseStack poses,MultiBufferSource buffers,int light,AbstractClientPlayer p,float swing,float amount,float partial,float age,float yaw,float pitch) {
        var d=SinkCapability.get(p);
        if(d==null || d.residueTicks<=0 || p.isInvisible()) return;
        String texture=d.residueType.equals("mud") ? "mud" : d.residueType.equals("soft_quicksand") ? "red_sand" : "sand";
        float alpha=Math.min(.65f,d.residueTicks/500f);
        poses.pushPose(); poses.scale(1.008f,1.008f,1.008f);
        getParentModel().renderToBuffer(poses,buffers.getBuffer(RenderType.entityTranslucent(new ResourceLocation("minecraft","textures/block/"+texture+".png"))),light,OverlayTexture.NO_OVERLAY,1,1,1,alpha);
        poses.popPose();
        for(var slot:net.minecraft.world.entity.EquipmentSlot.values()) {
            if(!(p.getItemBySlot(slot).getItem() instanceof net.minecraft.world.item.ArmorItem armor) || armor.getEquipmentSlot()!=slot) continue;
            var model=slot==net.minecraft.world.entity.EquipmentSlot.LEGS?inner:outer;
            getParentModel().copyPropertiesTo(model);model.setAllVisible(false);
            switch(slot) {
                case HEAD -> { model.head.visible=true;model.hat.visible=true; }
                case CHEST -> { model.body.visible=true;model.rightArm.visible=true;model.leftArm.visible=true; }
                case LEGS -> { model.body.visible=true;model.leftLeg.visible=true;model.rightLeg.visible=true; }
                case FEET -> { model.leftLeg.visible=true;model.rightLeg.visible=true; }
                default -> {}
            }
            poses.pushPose();poses.scale(1.008f,1.008f,1.008f);
            model.renderToBuffer(poses,buffers.getBuffer(RenderType.entityTranslucent(new ResourceLocation("minecraft","textures/block/"+texture+".png"))),light,OverlayTexture.NO_OVERLAY,1,1,1,alpha);
            poses.popPose();
        }
    }
}
