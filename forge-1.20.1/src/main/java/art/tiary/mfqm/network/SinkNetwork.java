package art.tiary.mfqm.network;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.client.ClientSinkState;
import art.tiary.mfqm.physics.MaterialProfile;
import art.tiary.mfqm.state.SinkCapability;
import art.tiary.mfqm.state.SinkState;
import java.util.UUID;
import java.util.function.Supplier;
import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.LivingEntity;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.fml.DistExecutor;
import net.minecraftforge.network.NetworkDirection;
import net.minecraftforge.network.NetworkEvent;
import net.minecraftforge.network.NetworkRegistry;
import net.minecraftforge.network.PacketDistributor;
import net.minecraftforge.network.simple.SimpleChannel;

public final class SinkNetwork {
    private static final String VERSION = "3-b2";
    public static final SimpleChannel CHANNEL = NetworkRegistry.newSimpleChannel(
            new ResourceLocation(MfqmReborn.MOD_ID, "sink"), () -> VERSION, VERSION::equals, VERSION::equals);
    private SinkNetwork() { }

    public static void register() {
        CHANNEL.messageBuilder(Diagnostic.class, 2, NetworkDirection.PLAY_TO_CLIENT)
                .encoder((m, b) -> { b.writeVarInt(m.entity); b.writeVarInt(m.ticks); b.writeUtf(m.label, 64); b.writeUtf(m.token, 8); })
                .decoder(b -> new Diagnostic(b.readVarInt(), b.readVarInt(), b.readUtf(64), b.readUtf(8)))
                .consumerMainThread((m, ctx) -> {
                    DistExecutor.unsafeRunWhenOn(Dist.CLIENT, () -> () -> art.tiary.mfqm.client.ClientMotionDiagnostics.start(m.entity, m.ticks, m.label, m.token));
                    ctx.get().setPacketHandled(true);
                }).add();
        CHANNEL.messageBuilder(Snapshot.class, 0, NetworkDirection.PLAY_TO_CLIENT)
                .encoder(Snapshot::encode).decoder(Snapshot::decode).consumerMainThread(Snapshot::handle).add();
        CHANNEL.messageBuilder(Struggle.class, 1, NetworkDirection.PLAY_TO_SERVER)
                .encoder((msg, buf) -> buf.writeBoolean(msg.held))
                .decoder(buf -> new Struggle(buf.readBoolean())).consumerMainThread(Struggle::handle).add();
    }

    public record Snapshot(int entityId, UUID uuid, ResourceLocation dimension, long tick, String material,
                           float immersion, int stuck, int air, boolean eyes, long settlements, String residueType, int residueTicks) {
        static void encode(Snapshot msg, FriendlyByteBuf buf) {
            buf.writeVarInt(msg.entityId); buf.writeUUID(msg.uuid); buf.writeResourceLocation(msg.dimension);
            buf.writeLong(msg.tick); buf.writeUtf(msg.material, 32); buf.writeFloat(msg.immersion);
            buf.writeVarInt(msg.stuck); buf.writeVarInt(msg.air); buf.writeBoolean(msg.eyes); buf.writeLong(msg.settlements); buf.writeUtf(msg.residueType,32); buf.writeVarInt(msg.residueTicks);
        }
        static Snapshot decode(FriendlyByteBuf buf) {
            return new Snapshot(buf.readVarInt(), buf.readUUID(), buf.readResourceLocation(), buf.readLong(),
                    buf.readUtf(32), buf.readFloat(), buf.readVarInt(), buf.readVarInt(), buf.readBoolean(), buf.readLong(), buf.readUtf(32), buf.readVarInt());
        }
        static void handle(Snapshot msg, Supplier<NetworkEvent.Context> ctx) {
            DistExecutor.unsafeRunWhenOn(Dist.CLIENT, () -> () -> ClientSinkState.accept(msg));
            ctx.get().setPacketHandled(true);
        }
    }

    private record Diagnostic(int entity, int ticks, String label, String token) { }
    public static void startDiagnostic(ServerPlayer owner, int entity, int ticks, String label, String token) {
        if (connected(owner)) CHANNEL.send(PacketDistributor.PLAYER.with(() -> owner), new Diagnostic(entity, ticks, label, token));
    }

    public record Struggle(boolean held) {
        static void handle(Struggle msg, Supplier<NetworkEvent.Context> ctx) {
            ServerPlayer player = ctx.get().getSender();
            if (player == null || !player.isAlive()) return;
            SinkState state = SinkCapability.get(player);
            long now = player.level().getGameTime();
            // Intent only. No client-provided motion, location, damage, oxygen or material IDs.
            if (state != null && state.active() && state.inputTick != now) {
                state.jumpHeld = msg.held;
                state.inputTick = now;
            }
            ctx.get().setPacketHandled(true);
        }
    }

    public static Snapshot snapshot(LivingEntity entity, SinkState state) {
        return new Snapshot(entity.getId(), entity.getUUID(), entity.level().dimension().location(),
                entity.level().getGameTime(), state.active() ? state.material.id : "none", (float) state.immersion,
                state.stuck, state.air, state.eyeCovered, state.settlements, state.residueType, state.residueTicks);
    }

    public static void sync(LivingEntity entity, SinkState state) {
        Snapshot packet = snapshot(entity, state);
        // GameTest/fake players can have a listener with no real Netty channel. Never send
        // custom packets through those connections. Replicas are bounded to nearby players;
        // the receiver also checks actual entity presence/UUID before accepting a snapshot.
        if (entity.level() instanceof net.minecraft.server.level.ServerLevel level) {
            for (var player : level.players()) if (connected(player) &&
                    (player == entity || player.distanceToSqr(entity) <= 128 * 128)) {
                CHANNEL.send(PacketDistributor.PLAYER.with(() -> player), packet);
            }
        }
        if (Boolean.getBoolean("mfqm.traceSnapshots") && entity instanceof ServerPlayer) {
            MfqmReborn.LOGGER.info("MFQM_SYNC_SERVER {} {} {} {} {} {} {}", packet.uuid, packet.tick,
                    packet.material, packet.immersion, packet.air, packet.stuck, packet.settlements);
        }
    }

    public static void syncTo(ServerPlayer player, LivingEntity target) {
        SinkState state = SinkCapability.get(target);
        if (state != null && connected(player)) {
            CHANNEL.send(PacketDistributor.PLAYER.with(() -> player), snapshot(target, state));
        }
    }

    public static boolean connected(ServerPlayer player) {
        return player.connection != null && player.connection.connection.channel() != null
                && player.connection.connection.isConnected();
    }
}
