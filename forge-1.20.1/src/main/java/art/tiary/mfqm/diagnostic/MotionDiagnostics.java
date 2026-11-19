package art.tiary.mfqm.diagnostic;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.network.SinkNetwork;
import art.tiary.mfqm.state.SinkCapability;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelDuplexHandler;
import io.netty.channel.ChannelPromise;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.Map;
import java.util.IdentityHashMap;
import java.util.UUID;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.atomic.AtomicLong;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.LivingEntity;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.event.entity.living.LivingHurtEvent;
import net.minecraftforge.event.entity.living.LivingFallEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.loading.FMLPaths;

/** Explicit, operator-owned, bounded observation. Never changes entity state or packets. */
@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID)
public final class MotionDiagnostics {
    private static final Map<LivingEntity, Session> SESSIONS = new IdentityHashMap<>();
    private MotionDiagnostics() { }
    public static void start(ServerPlayer owner, LivingEntity target, int ticks, String label) {
        stop(target);
        if (SESSIONS.size() >= 16) return;
        String token = UUID.randomUUID().toString().substring(0, 8);
        try {
            var session = new Session(target, ticks, label, token);
            SESSIONS.put(target, session);
            SinkNetwork.startDiagnostic(owner, target.getId(), ticks, label, token);
            if (target instanceof ServerPlayer player && SinkNetwork.connected(player)) session.observePackets(player);
            MfqmReborn.LOGGER.info("MFQM_B1_DIAG {} {} {}", label, token, session.path);
        } catch (IOException ex) { MfqmReborn.LOGGER.warn("Cannot open bounded motion diagnostic", ex); }
    }
    public static void stop(LivingEntity target) {
        var session = SESSIONS.remove(target);
        if (session != null) session.close();
    }
    public static boolean enabled(LivingEntity target) { return SESSIONS.containsKey(target); }
    @SubscribeEvent public static void leave(net.minecraftforge.event.entity.EntityLeaveLevelEvent event) {
        if (!event.getLevel().isClientSide && event.getEntity() instanceof LivingEntity living) stop(living);
    }
    @SubscribeEvent public static void logout(net.minecraftforge.event.entity.player.PlayerEvent.PlayerLoggedOutEvent event) {
        if (!event.getEntity().level().isClientSide) stop(event.getEntity());
    }
    @SubscribeEvent public static void stopped(net.minecraftforge.event.server.ServerStoppedEvent event) {
        for (var session : SESSIONS.values()) session.close();
        SESSIONS.clear();
    }
    public static void point(LivingEntity target, String point) {
        var session = SESSIONS.get(target);
        if (session != null) session.sample(target, point);
    }
    @SubscribeEvent public static void playerTick(TickEvent.PlayerTickEvent event) {
        if (!event.player.level().isClientSide && event.phase == TickEvent.Phase.START) point(event.player, "player_tick_start");
    }
    @SubscribeEvent public static void fall(LivingFallEvent event) {
        if (event.getEntity().level().isClientSide) return;
        var s = SESSIONS.get(event.getEntity());
        if (s != null) s.event("fall_event", "distance=" + event.getDistance() + ";multiplier=" + event.getDamageMultiplier());
    }
    @SubscribeEvent public static void hurt(LivingHurtEvent event) {
        if (event.getEntity().level().isClientSide) return;
        var s = SESSIONS.get(event.getEntity());
        if (s != null) s.event("hurt_event", event.getSource().getMsgId() + ";amount=" + event.getAmount());
    }
    @SubscribeEvent public static void level(TickEvent.LevelTickEvent event) {
        if (event.level.isClientSide || SESSIONS.isEmpty()) return;
        var iterator = SESSIONS.entrySet().iterator();
        while (iterator.hasNext()) {
            var entry = iterator.next(); var entity = entry.getKey(); var s = entry.getValue();
            if (entity.level() != event.level) continue;
            if (entity.isRemoved() || event.level.getGameTime() >= s.until) { s.close(); iterator.remove(); continue; }
            if (event.phase == TickEvent.Phase.START) s.sample(entity, "level_tick_start");
            else s.drain();
        }
    }
    public static String anonymous(UUID uuid, String token) {
        return UUID.nameUUIDFromBytes((token + uuid).getBytes(StandardCharsets.UTF_8)).toString();
    }
    private static final class Session {
        final Path path;
        final BufferedWriter writer;
        boolean writeFailed;
        final long until;
        final LivingEntity target;
        final String token;
        double lastY;
        long lastTick = Long.MIN_VALUE;
        boolean previousActive;
        final ConcurrentLinkedQueue<String> packets = new ConcurrentLinkedQueue<>();
        final AtomicLong sequence = new AtomicLong();
        ServerPlayer connectionOwner;
        Session(LivingEntity entity, int ticks, String label, String token) throws IOException {
            this.target = entity; this.token = token; this.until = entity.level().getGameTime() + Math.min(1200, ticks);
            path = FMLPaths.GAMEDIR.get().resolve("mfqm-motion").resolve(label + "_" + token + "_server.jsonl");
            Files.createDirectories(path.getParent()); writer = Files.newBufferedWriter(path);
            event("session", "build=" + MfqmReborn.class.getPackage().getImplementationVersion()
                    + ";sourceRevision=" + System.getProperty("mfqm.sourceRevision", "unavailable")
                    + ";sound_event=unavailable_on_server;packet_point=netty_arrival_or_write_before_delegate");
        }
        void observePackets(ServerPlayer player) {
            connectionOwner = player;
            var channel = player.connection.connection.channel();
            channel.eventLoop().execute(() -> {
                if (!channel.isActive()) return;
                channel.pipeline().addBefore("packet_handler", "mfqm_diag_" + token, new ChannelDuplexHandler() {
                    @Override public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
                        String kind = msg.getClass().getSimpleName();
                        if ((msg instanceof net.minecraft.network.protocol.game.ServerboundMovePlayerPacket
                                || msg instanceof net.minecraft.network.protocol.game.ServerboundAcceptTeleportationPacket)
                                && packets.size() < 128) {
                            String fields = "";
                            if (msg instanceof net.minecraft.network.protocol.game.ServerboundMovePlayerPacket movement)
                                fields = ",\"packet_y\":" + (movement.hasPosition() && Double.isFinite(movement.getY(0)) ? movement.getY(0) : "null")
                                        + ",\"packet_ground\":" + movement.isOnGround();
                            if (msg instanceof net.minecraft.network.protocol.game.ServerboundAcceptTeleportationPacket ack)
                                fields = ",\"teleport_id\":" + ack.getId();
                            packets.add("{\"point\":\"packet_arrival\",\"side\":\"server_netty\",\"nano\":"
                                    + System.nanoTime() + ",\"sequence\":" + sequence.incrementAndGet() + ",\"kind\":\"" + kind + "\"" + fields + "}");
                        }
                        super.channelRead(ctx, msg);
                    }
                    @Override public void write(ChannelHandlerContext ctx, Object msg, ChannelPromise promise) throws Exception {
                        if (msg instanceof net.minecraft.network.protocol.game.ClientboundPlayerPositionPacket position && packets.size() < 128)
                            packets.add("{\"point\":\"teleport_write\",\"side\":\"server_netty\",\"nano\":" + System.nanoTime()
                                    + ",\"teleport_id\":" + position.getId() + ",\"packet_y\":" + position.getY() + "}");
                        super.write(ctx, msg, promise);
                    }
                });
            });
        }
        void sample(LivingEntity entity, String point) {
            var data = SinkCapability.get(entity);
            if (data == null) return;
            var observed = art.tiary.mfqm.physics.ContactSampler.sample((net.minecraft.server.level.ServerLevel)entity.level(), entity);
            long tick = entity.level().getGameTime();
            boolean post = point.equals("settle_end");
            double dy = lastTick == Long.MIN_VALUE ? 0 : entity.getY() - lastY;
            String line = String.format(java.util.Locale.ROOT,
                    "{\"point\":\"%s\",\"side\":\"server\",\"tick\":%d,\"nano\":%d,\"entity\":\"%s\",\"dimension\":\"%s\",\"y\":%.9f,\"dy\":%.9f,\"vy\":%.9f,\"fall\":%.6f,\"ground\":%s,\"horizontal_collision\":%s,\"vertical_collision\":%s,\"material\":\"%s\",\"cells\":%d,\"immersion\":%.6f,\"first_contact\":%s,\"jump\":%s,\"health\":%.3f,\"air\":%d,\"settlements\":%d,\"corrections\":%d,\"correction_reason\":\"%s\"}",
                    point, tick, System.nanoTime(), anonymous(entity.getUUID(), token), entity.level().dimension().location(),
                    entity.getY(), dy, entity.getDeltaMovement().y, entity.fallDistance, entity.onGround(), entity.horizontalCollision,
                    entity.verticalCollision, data.active() ? data.material.id : "none", data.contacts, data.immersion,
                    post && data.active() && !previousActive, data.jumpHeld, entity.getHealth(), data.air, data.settlements,
                    data.motionCorrections, data.correctionReason);
            write(line.substring(0, line.length() - 1) + String.format(java.util.Locale.ROOT,
                    ",\"surface\":%.6f,\"depth\":%.6f,\"observed_material\":\"%s\"}",
                    observed.surface(), observed.depthBlocks(), observed.material() == null ? "none" : observed.material().id));
            event("motion_phase", data.motionPhase.name() + ";controlled=" + data.controlledMotion + ";age=" + data.motionAge);
            if (post) { lastY = entity.getY(); lastTick = tick; previousActive = data.active(); }
        }
        void event(String kind, String detail) {
            write("{\"point\":\"" + kind + "\",\"side\":\"server\",\"tick\":" + target.level().getGameTime()
                    + ",\"nano\":" + System.nanoTime() + ",\"detail\":\"" + detail.replace("\\", "\\\\").replace("\"", "\\\"") + "\"}");
        }
        void drain() { for (int i = 0; i < 64; i++) { var p = packets.poll(); if (p == null) break; write(p); } }
        void write(String line) {
            if (writeFailed) return;
            try { writer.write(line); writer.newLine(); writer.flush(); }
            catch (IOException ex) { writeFailed = true; MfqmReborn.LOGGER.warn("Diagnostic write stopped", ex); }
        }
        void close() {
            drain();
            if (connectionOwner != null) {
                var channel = connectionOwner.connection.connection.channel();
                try {
                    channel.eventLoop().execute(() -> { if (channel.pipeline().get("mfqm_diag_" + token) != null) channel.pipeline().remove("mfqm_diag_" + token); });
                } catch (java.util.concurrent.RejectedExecutionException ignored) {
                    // A closed channel has no future packet traffic to observe.
                }
            }
            try { writer.close(); } catch (IOException ignored) { }
        }
    }
}
