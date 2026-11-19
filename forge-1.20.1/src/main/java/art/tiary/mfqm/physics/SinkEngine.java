package art.tiary.mfqm.physics;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.network.SinkNetwork;
import art.tiary.mfqm.state.SinkCapability;
import art.tiary.mfqm.state.SinkState;
import java.util.UUID;
import net.minecraft.network.protocol.game.ClientboundSetEntityMotionPacket;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.ai.attributes.AttributeModifier;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID)
public final class SinkEngine {
    public static final UUID SLOWNESS_ID = UUID.fromString("035c9be5-623c-4d21-8145-67c31f5ac309");
    private SinkEngine() { }

    @SubscribeEvent
    public static void tick(TickEvent.LevelTickEvent event) {
        if (event.phase != TickEvent.Phase.END || !(event.level instanceof ServerLevel level)) return;
        for (var entity : level.getAllEntities()) {
            if (entity instanceof LivingEntity living && !living.isRemoved()) settle(level, living);
        }
    }

    public static boolean exempt(LivingEntity entity) {
        return !entity.isAlive() || entity.isSpectator() || entity.isInvulnerable()
                || entity instanceof Player p && (p.isCreative() || p.getAbilities().invulnerable);
    }

    /** Public for integration tests; the guard also protects against accidental repeated callbacks. */
    public static void settle(ServerLevel level, LivingEntity entity) {
        SinkState data = SinkCapability.get(entity);
        if (data == null) return;
        long time = level.getGameTime();
        String dimension = level.dimension().location().toString();
        if (data.lastTick == time && data.lastDimension.equals(dimension)) return;
        data.lastTick = time;
        data.lastDimension = dimension;
        data.settlements++;
        boolean before = data.active() || data.wasActive;
        if (!finitePosition(entity)) {
            cleanup(entity, data, true);
            // Never emit a non-finite coordinate. Vanilla normally rejects these before this point.
            var spawn = level.getSharedSpawnPos();
            entity.setPos(spawn.getX() + 0.5, spawn.getY() + 1, spawn.getZ() + 0.5);
            entity.setDeltaMovement(Vec3.ZERO);
            MfqmReborn.LOGGER.warn("Recovered non-finite entity coordinates for {}", entity.getUUID());
            return;
        }
        if (exempt(entity)) {
            cleanup(entity, data, true);
            decayResidue(entity,data);
            finish(entity, data, before, time);
            return;
        }
        if (data.hasPrevious && !entity.isPassenger() && entity instanceof ServerPlayer player && SinkNetwork.connected(player)) {
            reconcilePlayer(player, data);
        } else if (data.active() && data.hasPrevious && entity.isPassenger() && !(entity.getVehicle() instanceof net.minecraft.world.entity.vehicle.Boat)
                && entity instanceof ServerPlayer player && SinkNetwork.connected(player)) {
            reconcileMountedLegacy(player, data);
        }
        var contact = ContactSampler.sample(level, entity);
        if (entity.getVehicle() instanceof net.minecraft.world.entity.vehicle.Boat)
            contact = new ContactSampler.Contact(null, 0, 0, 0, 0, 0, contact.eyes(), 0, 0);
        if (contact.material() == null) {
            data.leaveContact();
            removeModifier(entity);
        } else {
            data.material = contact.material();
            data.immersion = contact.immersion();
            data.contacts = contact.cells();
            data.mudDepth = contact.mudDepth();
            data.residueType = data.material.id;
            data.residueTicks = Math.min(10000, data.residueTicks + 5);
            if (data.inputTick == Long.MIN_VALUE || time - data.inputTick > 10) data.jumpHeld = false;
            boolean struggle = data.jumpHeld && (data.lastStruggleTick == Long.MIN_VALUE || time - data.lastStruggleTick >= 8);
            if (struggle) data.lastStruggleTick = time;
            boolean moving = data.hasPrevious && Math.hypot(entity.getX() - data.previousX, entity.getZ() - data.previousZ) > 0.0015;
            var velocity = entity.getDeltaMovement();
            var result = SinkMath.solve(data.material, new SinkMath.Motion(velocity.x, velocity.y, velocity.z),
                    data.immersion, contact.depthBlocks(), contact.centerX(), contact.centerZ(), moving, struggle, entity.onGround());
            data.stuck = result.stuck();
            var v = result.motion();
            double vertical = entity.isPassenger() ? v.y() : Math.max(-SinkConfig.motionPolicy().terminal(), MotionMath.velocity(data.material, contact.depthBlocks(), moving, struggle, SinkConfig.motionPolicy()) * contact.motionScale());
            data.lastVertical = vertical;
            boolean legacyLease = art.tiary.mfqm.integration.StuckAdapter.managed(entity);
            entity.setDeltaMovement(legacyLease ? velocity.x : v.x(), vertical, legacyLease ? velocity.z : v.z());
            entity.hasImpulse = !(entity instanceof ServerPlayer) || entity.isPassenger();
            // Preserve Task 003's mounted LivingEntity fallback; B1 makes no boat/rider fix.
            if (entity.isPassenger()) entity.fallDistance = 0;
            if (legacyLease) removeModifier(entity);
            else setModifier(entity, result.speedFactor());
            if (entity.isPassenger() && entity instanceof ServerPlayer player && player.connection != null) {
                player.connection.send(new ClientboundSetEntityMotionPacket(entity));
            }
        }
        data.eyeCovered = contact.eyes();
        boolean oxygen = entity instanceof Player ? SinkConfig.PLAYER_OXYGEN.get() : SinkConfig.MOB_OXYGEN.get();
        data.air = (int) SinkMath.clamp(data.air, -1, 300);
        boolean protectedBreathing = net.minecraft.world.effect.MobEffectUtil.hasWaterBreathing(entity);
        if (data.eyeCovered && oxygen) {
            data.air = Math.min(data.air, entity.getAirSupply());
            int respiration = net.minecraft.world.item.enchantment.EnchantmentHelper.getRespiration(entity);
            if (!protectedBreathing && (respiration == 0 || entity.getRandom().nextInt(respiration+1)==0)) data.air = Math.max(-1,data.air-1);
            entity.setAirSupply(Math.max(0,data.air));
        } else if (entity.isEyeInFluid(net.minecraft.tags.FluidTags.WATER)) {
            data.air = Math.max(-1,entity.getAirSupply());
        } else {
            boolean recovering = data.air < 300;
            data.air = oxygen ? Math.min(300,data.air+5) : 300;
            if (recovering) entity.setAirSupply(Math.max(0,data.air));
        }
        if (data.eyeCovered && !protectedBreathing && (!oxygen || data.air < 0) && time % 16 == 0 && data.lastDamageTick != time) {
            data.lastDamageTick = time;
            if (oxygen) data.air = 0;
            float damage = (float) (Math.max(entity.getMaxHealth() * 0.1, 2) * SinkConfig.DAMAGE_MULTIPLIER.get());
            if (Float.isFinite(damage) && damage > 0 && !entity.isInvulnerableTo(entity.damageSources().drown())) {
                data.damageEvents++;
                entity.hurt(entity.damageSources().drown(), damage);
            }
        }
        decayResidue(entity,data);
        art.tiary.mfqm.content.MaterialEffects.tick(level,entity,data,before,time);
        finish(entity, data, before, time);
    }

    private static void decayResidue(LivingEntity entity,SinkState data) {
        // Creative/invulnerable physiology exemptions must not disable cosmetic washing or expiry.
        if(entity.isInWaterOrRain()) data.residueTicks=Math.max(0,data.residueTicks-50);
        else if(!data.active() && data.residueTicks>0) data.residueTicks--;
    }

    private static boolean finitePosition(LivingEntity entity) {
        return Double.isFinite(entity.getX()) && Double.isFinite(entity.getY()) && Double.isFinite(entity.getZ());
    }

    private static void reconcileMountedLegacy(ServerPlayer player, SinkState data) {
        double dx = player.getX() - data.previousX, dy = player.getY() - data.previousY, dz = player.getZ() - data.previousZ;
        if (dx * dx + dy * dy + dz * dz > 16 * 16) {
            data.leaveContact(); data.hasPrevious = false; removeModifier(player); return;
        }
        var limit = SinkMath.limitPlayerStep(new SinkMath.Motion(dx, dy, dz), data.lastVertical,
                player.getAttributeValue(Attributes.MOVEMENT_SPEED), data.material == MaterialProfile.MUD && data.mudDepth == 0);
        if (Math.abs(dx - limit.x()) + Math.abs(dy - limit.y()) + Math.abs(dz - limit.z()) > 0.001) {
            data.motionCorrections++; data.correctionReason = "legacy_mounted_step_budget";
            player.connection.teleport(data.previousX + limit.x(), data.previousY + limit.y(), data.previousZ + limit.z(),
                    player.getYRot(), player.getXRot());
        }
    }

    private static void reconcilePlayer(ServerPlayer player, SinkState data) {
        double dx = player.getX() - data.previousX, dy = player.getY() - data.previousY, dz = player.getZ() - data.previousZ;
        // Unknown server-side teleports from other mods must not drag an entity back into a pit.
        // Forge teleport events are handled explicitly; this is a fallback for direct position APIs.
        if (dx * dx + dy * dy + dz * dz > 16 * 16) {
            data.leaveContact();
            data.hasPrevious = false;
            removeModifier(player);
            return;
        }
        var policy = SinkConfig.motionPolicy();
        long now = System.nanoTime();
        double elapsed = data.motionNano == 0 ? 1 : (now - data.motionNano) / 50_000_000.0;
        data.motionNano = now;
        var swept = ContactSampler.entry(player.level(), player, data.previousY, player.getY());
        double minY = Double.NEGATIVE_INFINITY;
        String reason = "none";
        if (!data.active() && swept != null) {
            minY = swept.surface() - policy.entryDepth();
            reason = "entry_penetration";
        } else if (data.active() && ContactSampler.sample(player.level(), player).material() != null) {
            minY = data.previousY - MotionMath.downwardBudget(elapsed, policy);
            reason = "terminal_budget";
        }
        // Exceptional server correction only. Ordinary accepted client steps are not teleported.
        if (player.getY() < minY - 0.001) {
            data.motionCorrections++;
            data.correctionReason = reason;
            player.connection.teleport(player.getX(), minY, player.getZ(), player.getYRot(), player.getXRot());
        }
    }

    private static void finish(LivingEntity entity, SinkState data, boolean before, long time) {
        data.previousX = entity.getX(); data.previousY = entity.getY(); data.previousZ = entity.getZ();
        data.hasPrevious = true;
        if (before != data.active() || (data.active() || data.air < 300) && time % 5 == 0
                || data.air == 300 && data.lastSyncedAir != 300 || (data.residueTicks > 0 || data.lastSyncedResidue > 0) && time % 20 == 0) {
            SinkNetwork.sync(entity, data);
            data.lastSyncedAir = data.air;
            data.lastSyncedResidue = data.residueTicks;
        }
        data.wasActive = data.active();
        if (data.trace != null) data.trace.record(entity, data, time);
        art.tiary.mfqm.diagnostic.MotionDiagnostics.point(entity, "settle_end");
    }

    public static void removeModifier(LivingEntity entity) {
        var speed = entity.getAttribute(Attributes.MOVEMENT_SPEED);
        if (speed != null) speed.removeModifier(SLOWNESS_ID);
    }

    private static void setModifier(LivingEntity entity, double factor) {
        var speed = entity.getAttribute(Attributes.MOVEMENT_SPEED);
        if (speed == null) return;
        var existing = speed.getModifier(SLOWNESS_ID);
        double amount = SinkMath.clamp(factor, 0.02, 1) - 1;
        if (existing != null && Math.abs(existing.getAmount() - amount) < 0.0001) return;
        speed.removeModifier(SLOWNESS_ID);
        speed.addTransientModifier(new AttributeModifier(SLOWNESS_ID, "MFQM temporary stuck", amount,
                AttributeModifier.Operation.MULTIPLY_TOTAL));
    }

    public static void cleanup(LivingEntity entity, SinkState data, boolean refillAir) {
        removeModifier(entity);
        data.leaveContact();
        if (refillAir) data.air = 300;
    }
}
