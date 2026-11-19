package art.tiary.mfqm.diagnostic;

import art.tiary.mfqm.MfqmReborn;
import com.mojang.brigadier.arguments.IntegerArgumentType;
import java.util.IdentityHashMap;
import java.util.Map;
import net.minecraft.commands.Commands;
import net.minecraft.server.MinecraftServer;
import net.minecraftforge.event.RegisterCommandsEvent;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.event.server.ServerStoppedEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** Explicit timing perturbation for disposable operator tests. NEVER part of diagnostics. */
@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID)
public final class MotionLoadFixture {
    private record Load(int remaining, int delay) { }
    private static final Map<MinecraftServer, Load> ACTIVE = new IdentityHashMap<>();
    private MotionLoadFixture() { }
    @SubscribeEvent public static void register(RegisterCommandsEvent event) {
        event.getDispatcher().register(Commands.literal("mfqm").then(Commands.literal("motionload")
                .requires(s -> s.hasPermission(4)).then(Commands.argument("ticks", IntegerArgumentType.integer(1, 200))
                .then(Commands.argument("delayMs", IntegerArgumentType.integer(0, 200)).executes(c -> {
                    int ticks = IntegerArgumentType.getInteger(c, "ticks"), delay = IntegerArgumentType.getInteger(c, "delayMs");
                    ACTIVE.put(c.getSource().getServer(), new Load(ticks, delay));
                    MfqmReborn.LOGGER.info("MFQM_LOAD_BEGIN ticks={} sleepMs={} (explicit timing fixture, not observation)", ticks, delay);
                    return 1;
                })))));
    }
    @SubscribeEvent public static void tick(TickEvent.ServerTickEvent event) {
        if (event.phase != TickEvent.Phase.END || ACTIVE.isEmpty()) return;
        var server = event.getServer();
        var load = ACTIVE.get(server);
        if (load == null) return;
        try { Thread.sleep(load.delay); } catch (InterruptedException ex) { Thread.currentThread().interrupt(); ACTIVE.remove(server); return; }
        if (load.remaining <= 1) {
            ACTIVE.remove(server);
            MfqmReborn.LOGGER.info("MFQM_LOAD_END nano={}", System.nanoTime());
        } else ACTIVE.put(server, new Load(load.remaining - 1, load.delay));
    }
    @SubscribeEvent public static void stop(ServerStoppedEvent event) { ACTIVE.remove(event.getServer()); }
}
