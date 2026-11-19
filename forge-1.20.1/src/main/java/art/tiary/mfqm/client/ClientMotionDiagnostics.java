package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.diagnostic.MotionDiagnostics;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import net.minecraft.client.Minecraft;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.client.event.sound.PlaySoundEvent;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.loading.FMLPaths;

@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID, value = Dist.CLIENT)
public final class ClientMotionDiagnostics {
    private static BufferedWriter writer;
    private static int targetId, remaining;
    private static String token;
    private static double previousY;
    private static long previousTick;
    private ClientMotionDiagnostics() { }
    public static void start(int entityId, int ticks, String label, String sessionToken) {
        close();
        if (ticks <= 0) return;
        if (!label.matches("[A-Za-z0-9_-]{1,64}") || !sessionToken.matches("[a-f0-9]{8}")) return;
        try {
            var path = FMLPaths.GAMEDIR.get().resolve("mfqm-motion").resolve(label + "_" + sessionToken + "_client.jsonl");
            Files.createDirectories(path.getParent()); writer = Files.newBufferedWriter(path);
            targetId = entityId; remaining = Math.min(1200, Math.max(1, ticks)); token = sessionToken; previousTick = Long.MIN_VALUE;
            write("{\"point\":\"session\",\"side\":\"client\",\"detail\":\"packet_confirmation_send_time=unavailable;sound_backend_success=unavailable\"}");
        } catch (IOException ex) { MfqmReborn.LOGGER.warn("Client motion diagnostic unavailable", ex); }
    }
    @SubscribeEvent public static void tick(TickEvent.ClientTickEvent event) {
        if (writer == null) return;
        var mc = Minecraft.getInstance();
        if (mc.level == null || mc.player == null) { close(); return; }
        var entity = mc.level.getEntity(targetId);
        if (entity == null) { if (event.phase == TickEvent.Phase.END && --remaining <= 0) close(); return; }
        long tick = mc.level.getGameTime();
        double dy = previousTick == Long.MIN_VALUE ? 0 : entity.getY() - previousY;
        write(String.format(java.util.Locale.ROOT,
                "{\"point\":\"client_tick_%s\",\"side\":\"client\",\"tick\":%d,\"nano\":%d,\"entity\":\"%s\",\"dimension\":\"%s\",\"local_player\":%s,\"y\":%.9f,\"dy\":%.9f,\"vy\":%.9f,\"fall\":%.6f,\"ground\":%s,\"horizontal_collision\":%s,\"vertical_collision\":%s,\"jump\":%s}",
                event.phase.name().toLowerCase(java.util.Locale.ROOT), tick, System.nanoTime(), MotionDiagnostics.anonymous(entity.getUUID(), token),
                mc.level.dimension().location(), entity == mc.player, entity.getY(), dy, entity.getDeltaMovement().y,
                entity.fallDistance, entity.onGround(), entity.horizontalCollision, entity.verticalCollision, mc.options.keyJump.isDown()));
        if (entity instanceof net.minecraft.world.entity.LivingEntity living) {
            var contact = art.tiary.mfqm.physics.ContactSampler.sample(mc.level, living);
            write(String.format(java.util.Locale.ROOT,
                    "{\"point\":\"client_contact_%s\",\"side\":\"client\",\"tick\":%d,\"surface\":%.6f,\"depth\":%.6f,\"material\":\"%s\",\"cells\":%d}",
                    event.phase.name().toLowerCase(java.util.Locale.ROOT), tick, contact.surface(), contact.depthBlocks(),
                    contact.material() == null ? "none" : contact.material().id, contact.cells()));
        }
        if (event.phase == TickEvent.Phase.END) {
            previousY = entity.getY(); previousTick = tick;
            if (--remaining <= 0) close();
        }
    }
    @SubscribeEvent public static void sound(PlaySoundEvent event) {
        if (writer != null && event.getSound() != null) {
            var sound = event.getSound();
            var mc = Minecraft.getInstance();
            if (mc.player != null && mc.player.distanceToSqr(sound.getX(), sound.getY(), sound.getZ()) <= 144)
                write("{\"point\":\"sound_requested\",\"side\":\"client\",\"nano\":" + System.nanoTime()
                        + ",\"sound\":\"" + sound.getLocation() + "\"}");
        }
    }
    private static void write(String value) {
        if (writer == null) return;
        try { writer.write(value); writer.newLine(); writer.flush(); } catch (IOException ex) { close(); }
    }
    private static void close() {
        if (writer != null) try { writer.close(); } catch (IOException ignored) { }
        writer = null;
    }
}
