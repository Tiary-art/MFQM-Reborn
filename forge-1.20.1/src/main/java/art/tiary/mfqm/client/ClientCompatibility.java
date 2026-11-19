package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.*;
import net.minecraft.client.Minecraft;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.vehicle.Boat;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.ComputeFovModifierEvent;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

@Mod.EventBusSubscriber(modid=MfqmReborn.MOD_ID,value=Dist.CLIENT)
public final class ClientCompatibility {
    @SubscribeEvent public static void boat(TickEvent.ClientTickEvent e) {
        var p=Minecraft.getInstance().player;
        if(e.phase==TickEvent.Phase.START && p!=null && p.getVehicle() instanceof Boat b && b.isControlledByLocalInstance()) BoatMotion.prepare(b);
    }
    @SubscribeEvent public static void fov(ComputeFovModifierEvent e) {
        var p=e.getPlayer();
        if(p.isScoping()) return; // Vanilla scope has an explicit constant FOV.
        var speed=p.getAttribute(Attributes.MOVEMENT_SPEED);
        if(speed==null || p.getAbilities().getWalkingSpeed()==0) return;
        var own=speed.getModifier(SinkEngine.SLOWNESS_ID);
        if(own==null || own.getAmount()<=-1) return;
        // Recompute the attribute with only our UUID excluded, retaining all vanilla/foreign operations and clamps.
        var without=new net.minecraft.world.entity.ai.attributes.AttributeInstance(speed.getAttribute(), ignored -> {});
        without.setBaseValue(speed.getBaseValue());
        for(var modifier:speed.getModifiers()) if(!modifier.getId().equals(SinkEngine.SLOWNESS_ID)) without.addTransientModifier(modifier);
        double current=speed.getValue(), counterfactual=without.getValue();
        double walk=p.getAbilities().getWalkingSpeed();
        double ratio=(counterfactual/walk+1)/(current/walk+1);
        if(Double.isFinite(ratio)) e.setNewFovModifier((float)(e.getNewFovModifier()*ratio));
    }
}
