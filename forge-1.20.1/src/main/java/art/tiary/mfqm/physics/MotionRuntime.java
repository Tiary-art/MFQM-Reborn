package art.tiary.mfqm.physics;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.state.SinkCapability;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.event.entity.living.LivingEvent;
import net.minecraftforge.event.entity.living.LivingFallEvent;
import net.minecraftforge.eventbus.api.EventPriority;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** Kinematics before vanilla move; physiological settlement remains server-only. */
@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID)
public final class MotionRuntime {
    private MotionRuntime() { }
    public static boolean eligible(LivingEntity e) { return !SinkEngine.exempt(e) && !e.isPassenger(); }
    @SubscribeEvent public static void player(TickEvent.PlayerTickEvent event) {
        // Remote client replicas never predict; client-only caller handles local input.
        if (event.phase == TickEvent.Phase.START && !event.player.level().isClientSide) prepare(event.player, false);
    }
    @SubscribeEvent public static void mob(LivingEvent.LivingTickEvent event) {
        if (!(event.getEntity() instanceof Player) && !event.getEntity().level().isClientSide) prepare(event.getEntity(), false);
    }
    public static void prepare(LivingEntity e, boolean jumping) {
        if (!eligible(e)) return;
        var d = SinkCapability.get(e);
        if (d == null) return;
        var p = SinkConfig.motionPolicy();
        var c = ContactSampler.sample(e.level(), e);
        double incoming = e.getDeltaMovement().y;
        var entry = ContactSampler.entry(e.level(), e, e.getY(), e.getY() + Math.min(0, incoming));
        if (c.material() == null && entry == null) {
            d.controlledMotion = false;
            d.motionPhase = d.motionPhase == MotionMath.Phase.OUTSIDE || d.motionPhase == MotionMath.Phase.EXITING
                    ? MotionMath.Phase.OUTSIDE : MotionMath.Phase.EXITING;
            d.motionAge = 0;
            return;
        }
        boolean atSurface = c.material() != null;
        d.motionPhase = !atSurface || d.motionAge++ < 3 ? MotionMath.Phase.ENTERING : MotionMath.Phase.SUBMERGED;
        double vy = atSurface ? MotionMath.velocity(c.material(), c.depthBlocks(), e.getDeltaMovement().horizontalDistanceSqr() > 0.00000225,
                jumping || d.jumpHeld, p) * c.motionScale() : MotionMath.entryStep(e.getY(), entry.surface(), incoming, p);
        if (atSurface) vy = MotionMath.dampEntry(Math.max(-p.terminal(), vy), incoming, d.motionAge, p);
        // Shallow mud's solid half-height landing/jump remains vanilla geometry.
        if (atSurface && c.material() == MaterialProfile.MUD && c.mudDepth() == 0 && incoming > 0) return;
        double x = e.getDeltaMovement().x, z = e.getDeltaMovement().z;
        if (e.level().isClientSide && atSurface && !art.tiary.mfqm.integration.StuckAdapter.managed(e)) {
            var result = SinkMath.solve(c.material(), new SinkMath.Motion(x, vy, z), c.immersion(), c.depthBlocks(),
                    c.centerX(), c.centerZ(), Math.hypot(x, z) > 0.0015, jumping, e.onGround());
            x = result.motion().x(); z = result.motion().z();
        }
        e.setDeltaMovement(x, vy, z);
        d.controlledMotion = atSurface || entry != null;
        if (MotionMath.controlledLanding(true, false, vy, p) || entry != null) e.fallDistance = 0;
    }
    @SubscribeEvent public static void jump(LivingEvent.LivingJumpEvent event) {
        var e = event.getEntity();
        if (!eligible(e)) return;
        var c = ContactSampler.sample(e.level(), e);
        if (c.material() != null && !(c.material() == MaterialProfile.MUD && c.mudDepth() == 0)) {
            double y = MotionMath.velocity(c.material(), c.depthBlocks(), true, true, SinkConfig.motionPolicy());
            e.setDeltaMovement(e.getDeltaMovement().x, y, e.getDeltaMovement().z);
        }
    }
    @SubscribeEvent(priority = EventPriority.HIGH) public static void landing(LivingFallEvent event) {
        var e = event.getEntity();
        var d = SinkCapability.get(e);
        if (!eligible(e) || d == null || !d.controlledMotion) return;
        var c = ContactSampler.sample(e.level(), e);
        if (MotionMath.controlledLanding(c.material() != null, e.isPassenger(), e.getDeltaMovement().y, SinkConfig.motionPolicy())) {
            event.setDistance(0);
        }
    }
}
