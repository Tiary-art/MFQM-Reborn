package art.tiary.mfqm.integration;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.SinkConfig;
import com.mojang.brigadier.arguments.IntegerArgumentType;
import com.mojang.brigadier.arguments.LongArgumentType;
import net.minecraft.commands.Commands;
import net.minecraft.commands.CommandSourceStack;
import net.minecraft.commands.arguments.coordinates.BlockPosArgument;
import net.minecraft.network.chat.Component;
import net.minecraftforge.event.RegisterCommandsEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID)
public final class Phase7Commands {
    private Phase7Commands() { }
    private static boolean safe(CommandSourceStack s) {
        return !StuckAdapter.forcedDisabled() && SinkConfig.PHASE7_TEST_WORLD.get()
                && (s.getServer().getWorldData().getLevelName().startsWith("MFQM_PHASE7_") || s.getServer().getWorldData().getLevelName().startsWith("MFQM_PHASE8_"));
    }
    @SubscribeEvent public static void register(RegisterCommandsEvent e) {
        e.getDispatcher().register(Commands.literal("mfqm_phase7").requires(s -> s.hasPermission(2))
            .then(Commands.literal("disable").executes(c -> {
                StuckAdapter.disableAll();
                c.getSource().sendSuccess(() -> Component.literal("Experimental contact/lease/test-world entries disabled; owned leases cleared. Existing terrain is not rolled back."), true); return 1;
            }))
            .then(Commands.literal("release").executes(c -> {
                StuckAdapter.clear(c.getSource().getPlayerOrException()); return 1;
            }))
            .then(Commands.literal("contact").then(Commands.argument("level", IntegerArgumentType.integer(0, 255))
                .executes(c -> {
                    var s = c.getSource();
                    if (!safe(s) || !StuckAdapter.enabled()) {
                        s.sendFailure(Component.literal("Requires phase7.testWorld=true, stuckLease=true and MFQM_PHASE7_ test world name.")); return 0;
                    }
                    StuckAdapter.contact(s.getPlayerOrException(), IntegerArgumentType.getInteger(c, "level"));
                    s.sendSuccess(() -> Component.literal("One ordered test contact queued. No automatic material producer. Creative/spectator/riders exempt."), false);
                    return 1;
                })))
            .then(Commands.literal("hold").then(Commands.argument("level", IntegerArgumentType.integer(0, 255))
                .then(Commands.argument("ticks", IntegerArgumentType.integer(1, 200)).executes(c -> {
                    var s = c.getSource();
                    if (!safe(s) || !StuckAdapter.enabled()) { s.sendFailure(Component.literal("Test-world guards and stuckLease must be enabled.")); return 0; }
                    StuckAdapter.holdForTest(s.getPlayerOrException(), IntegerArgumentType.getInteger(c, "level"), IntegerArgumentType.getInteger(c, "ticks"));
                    s.sendSuccess(() -> Component.literal("Bounded injected contacts started; release cancels immediately."), false); return 1;
                }))))
            .then(Commands.literal("dry").then(Commands.argument("pos", BlockPosArgument.blockPos())
                .then(Commands.argument("extent", IntegerArgumentType.integer(-1, 18))
                    .then(Commands.argument("seed", LongArgumentType.longArg()).executes(c -> {
                        var s = c.getSource();
                        if (!safe(s)) { s.sendFailure(Component.literal("Back up a disposable MFQM_PHASE7_ world and set phase7.testWorld=true first.")); return 0; }
                        try {
                            DryWorldAdapter.generate(s.getLevel(), BlockPosArgument.getLoadedBlockPos(c, "pos"),
                                IntegerArgumentType.getInteger(c, "extent"), LongArgumentType.getLong(c, "seed"),
                                line -> { if (SinkConfig.PHASE7_DIAGNOSTICS.get()) MfqmReborn.LOGGER.info("PHASE7_DRY {}", line); });
                            s.sendSuccess(() -> Component.literal("Controlled Dry transaction complete; not natural generation."), false); return 1;
                        } catch (IllegalArgumentException | IllegalStateException ex) {
                            s.sendFailure(Component.literal(ex.getMessage())); return 0;
                        }
                    }))))));
    }
}
