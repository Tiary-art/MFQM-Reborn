package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.MotionRuntime;
import net.minecraft.client.Minecraft;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** Local kinematics only. No client oxygen, damage, settlement or remote-replica movement. */
@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID, value = Dist.CLIENT)
public final class ClientMotionPrediction {
    private ClientMotionPrediction() { }
    @SubscribeEvent public static void tick(TickEvent.PlayerTickEvent event) {
        var mc = Minecraft.getInstance();
        if (event.phase == TickEvent.Phase.START && event.player.level().isClientSide && event.player == mc.player) {
            MotionRuntime.prepare(event.player, mc.options.keyJump.isDown());
        }
    }
}
