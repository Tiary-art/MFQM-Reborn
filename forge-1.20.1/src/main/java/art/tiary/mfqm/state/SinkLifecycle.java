package art.tiary.mfqm.state;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.network.SinkNetwork;
import art.tiary.mfqm.physics.SinkEngine;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.LivingEntity;
import net.minecraftforge.event.entity.EntityLeaveLevelEvent;
import net.minecraftforge.event.entity.EntityTeleportEvent;
import net.minecraftforge.event.entity.living.LivingDeathEvent;
import net.minecraftforge.event.entity.living.LivingEvent;
import net.minecraftforge.event.entity.player.PlayerEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID)
public final class SinkLifecycle {
    private SinkLifecycle() { }

    public static void clear(LivingEntity entity, boolean all) {
        SinkEngine.removeModifier(entity);
        var state = SinkCapability.get(entity);
        if (state != null) {
            if (all) state.clearAll(); else state.resetTransient();
        }
    }

    @SubscribeEvent public static void death(LivingDeathEvent event) {
        if (!event.getEntity().level().isClientSide) clear(event.getEntity(), true);
    }
    @SubscribeEvent public static void jump(LivingEvent.LivingJumpEvent event) {
        if (event.getEntity().level().isClientSide) return;
        var state = SinkCapability.get(event.getEntity());
        if (state != null && state.active()) {
            state.jumpHeld = true;
            state.inputTick = event.getEntity().level().getGameTime();
        }
    }
    @SubscribeEvent public static void leave(EntityLeaveLevelEvent event) {
        if (event.getEntity() instanceof LivingEntity living) clear(living, false);
    }
    @SubscribeEvent public static void clone(PlayerEvent.Clone event) {
        event.getOriginal().reviveCaps();
        try {
            var old = SinkCapability.get(event.getOriginal());
            var next = SinkCapability.get(event.getEntity());
            if (next != null) {
                if (!event.isWasDeath() && old != null) next.load(old.save()); else next.clearAll();
            }
            clear(event.getOriginal(), false);
        } finally { event.getOriginal().invalidateCaps(); }
    }
    @SubscribeEvent public static void login(PlayerEvent.PlayerLoggedInEvent event) {
        clear(event.getEntity(), false);
        if (event.getEntity() instanceof ServerPlayer player) SinkNetwork.syncTo(player, player);
    }
    @SubscribeEvent public static void respawn(PlayerEvent.PlayerRespawnEvent event) {
        clear(event.getEntity(), !event.isEndConquered());
        if (event.getEntity() instanceof ServerPlayer player) SinkNetwork.syncTo(player, player);
    }
    @SubscribeEvent public static void dimension(PlayerEvent.PlayerChangedDimensionEvent event) {
        clear(event.getEntity(), false);
        if (event.getEntity() instanceof ServerPlayer player) SinkNetwork.syncTo(player, player);
    }
    @SubscribeEvent public static void logout(PlayerEvent.PlayerLoggedOutEvent event) { clear(event.getEntity(), false); }
    @SubscribeEvent public static void teleport(EntityTeleportEvent event) {
        if (event.getEntity() instanceof LivingEntity living && !living.level().isClientSide) {
            var data = SinkCapability.get(living);
            if (data != null) {
                data.leaveContact();
                data.hasPrevious = false;
                SinkEngine.removeModifier(living);
            }
        }
    }
    @SubscribeEvent public static void tracking(PlayerEvent.StartTracking event) {
        if (event.getEntity() instanceof ServerPlayer player && event.getTarget() instanceof LivingEntity target) {
            SinkNetwork.syncTo(player, target);
        }
    }
}
