package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.network.SinkNetwork;
import art.tiary.mfqm.physics.MaterialProfile;
import art.tiary.mfqm.physics.SinkMath;
import art.tiary.mfqm.state.SinkCapability;
import net.minecraft.client.Minecraft;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** Read-only physiological replicas and boolean input intents. Kinematics live in ClientMotionPrediction. */
@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID, value = Dist.CLIENT)
public final class ClientSinkState {
    private static boolean sentHeld;
    private ClientSinkState() { }

    public static void accept(SinkNetwork.Snapshot packet) {
        Minecraft mc = Minecraft.getInstance();
        if (mc.level == null || !mc.level.dimension().location().equals(packet.dimension())) return;
        var entity = mc.level.getEntity(packet.entityId());
        if (!(entity instanceof net.minecraft.world.entity.LivingEntity living) || !entity.getUUID().equals(packet.uuid())) return;
        var data = SinkCapability.get(living);
        if (data == null || packet.tick() < data.lastSnapshotTick || !Float.isFinite(packet.immersion())) return;
        data.lastSnapshotTick = packet.tick();
        data.material = MaterialProfile.byId(packet.material());
        data.immersion = SinkMath.clamp(packet.immersion(), 0, 1);
        data.stuck = (int) SinkMath.clamp(packet.stuck(), 0, 175);
        data.air = (int) SinkMath.clamp(packet.air(), -1, 300);
        data.eyeCovered = packet.eyes();
        data.residueType = MaterialProfile.byId(packet.residueType()) == null ? "" : packet.residueType();
        data.residueTicks = (int)SinkMath.clamp(packet.residueTicks(),0,10000);
        if(living==mc.player) living.setAirSupply(Math.max(0,data.air));
        data.settlements = Math.max(0, packet.settlements());
        if (Boolean.getBoolean("mfqm.traceSnapshots") && living == mc.player) {
            MfqmReborn.LOGGER.info("MFQM_SYNC_CLIENT {} {} {} {} {} {} {}", packet.uuid(), packet.tick(),
                    packet.material(), packet.immersion(), packet.air(), packet.stuck(), packet.settlements());
        }
    }

    @SubscribeEvent
    public static void tick(TickEvent.ClientTickEvent event) {
        if (event.phase != TickEvent.Phase.END) return;
        Minecraft mc = Minecraft.getInstance();
        if (mc.player == null || mc.getConnection() == null) { sentHeld = false; return; }
        var state = SinkCapability.get(mc.player);
        boolean active = state != null && state.active();
        boolean held = active && mc.screen == null && mc.options.keyJump.isDown();
        if (active && mc.player.tickCount % 5 == 0 || held != sentHeld) {
            SinkNetwork.CHANNEL.sendToServer(new SinkNetwork.Struggle(held));
            sentHeld = held;
        }
    }
}
