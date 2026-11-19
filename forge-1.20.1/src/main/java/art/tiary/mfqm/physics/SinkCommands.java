package art.tiary.mfqm.physics;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.registry.ModBlocks;
import art.tiary.mfqm.state.SinkCapability;
import art.tiary.mfqm.state.TraceSession;
import com.mojang.brigadier.arguments.StringArgumentType;
import java.io.IOException;
import java.util.Locale;
import net.minecraft.commands.Commands;
import net.minecraft.commands.SharedSuggestionProvider;
import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import net.minecraft.network.protocol.game.ClientboundSetEntityMotionPacket;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.level.GameType;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.event.RegisterCommandsEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.loading.FMLPaths;

/** Explicit operator-only test pad/measurement commands; never natural world generation. */
@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID)
public final class SinkCommands {
    private SinkCommands() { }
    @SubscribeEvent public static void register(RegisterCommandsEvent event) {
        event.getDispatcher().register(Commands.literal("mfqm")
                .then(Commands.literal("status").executes(ctx -> {
                    var player = ctx.getSource().getPlayerOrException();
                    var data = SinkCapability.get(player);
                    if (data != null) ctx.getSource().sendSuccess(() -> Component.literal(String.format(Locale.ROOT,
                            "MFQM server material=%s depth=%.4f air=%d stuck=%d eye=%s contacts=%d settlements=%d tick=%d",
                            data.active() ? data.material.id : "none", data.immersion, data.air, data.stuck,
                            data.eyeCovered, data.contacts, data.settlements, data.lastTick)), false);
                    return 1;
                }))
                .then(Commands.literal("trace").requires(s -> s.hasPermission(2))
                        .then(Commands.literal("stop").executes(ctx -> {
                            var data = SinkCapability.get(ctx.getSource().getPlayerOrException());
                            if (data != null) data.closeTrace();
                            return 1;
                        }))
                        .then(Commands.literal("start").then(Commands.argument("label", StringArgumentType.word()).executes(ctx -> {
                            startTrace(ctx.getSource().getPlayerOrException(), StringArgumentType.getString(ctx, "label"), 400);
                            return 1;
                        }))))
                .then(Commands.literal("trial").requires(s -> s.hasPermission(2))
                        .then(Commands.argument("material", StringArgumentType.word()).suggests((ctx, b) ->
                                SharedSuggestionProvider.suggest(new String[]{"quicksand", "mud", "soft_quicksand"}, b))
                                .then(Commands.argument("scenario", StringArgumentType.word()).suggests((ctx, b) ->
                                        SharedSuggestionProvider.suggest(new String[]{"still", "walk", "jump", "hold_jump", "fast_fall", "edge", "single_layer", "multi_layer", "deep_oxygen"}, b))
                                        .executes(ctx -> trial(ctx.getSource().getPlayerOrException(),
                                                StringArgumentType.getString(ctx, "material"), StringArgumentType.getString(ctx, "scenario")))))));
    }

    public static BlockState materialState(MaterialProfile material) {
        return switch (material) {
            case QUICKSAND -> ModBlocks.QUICKSAND.get().defaultBlockState();
            case MUD -> ModBlocks.MUD.get().defaultBlockState();
            case SOFT_QUICKSAND -> ModBlocks.SOFT_QUICKSAND.get().defaultBlockState();
        };
    }

    private static int trial(ServerPlayer player, String id, String scenario) {
        var material = MaterialProfile.byId(id);
        if (material == null) { player.sendSystemMessage(Component.literal("Unknown core material")); return 0; }
        var level = player.serverLevel();
        int top = Math.max(level.getMinBuildHeight() + 8, 64);
        int layers = scenario.equals("single_layer") ? 1 : 3;
        for (int x = -5; x <= 5; x++) for (int z = -5; z <= 5; z++) {
            level.setBlockAndUpdate(new BlockPos(x, top - layers, z), Blocks.BEDROCK.defaultBlockState());
            for (int y = top - layers + 1; y <= top + 5; y++) {
                var state = y <= top ? materialState(material) : Blocks.AIR.defaultBlockState();
                level.setBlockAndUpdate(new BlockPos(x, y, z), state);
            }
        }
        // Open-air edge and an independent safe exit platform.
        for (int z = -5; z <= 5; z++) level.setBlockAndUpdate(new BlockPos(5, top, z), Blocks.AIR.defaultBlockState());
        for (int x = 6; x <= 10; x++) for (int z = -3; z <= 3; z++)
            level.setBlockAndUpdate(new BlockPos(x, top, z), Blocks.STONE.defaultBlockState());
        var state = SinkCapability.get(player);
        SinkLifecycleBridge.reset(player);
        player.setGameMode(GameType.SURVIVAL);
        player.setHealth(player.getMaxHealth());
        player.getFoodData().setFoodLevel(20);
        double surface = top + material.surfaceHeight;
        double y = scenario.equals("deep_oxygen") ? surface - player.getEyeHeight() - 0.1
                : surface + (scenario.equals("fast_fall") ? 3 : 0.01);
        double x = scenario.equals("edge") ? 4.75 : 0.5;
        player.connection.teleport(x, y, 0.5, 0, 35);
        player.setDeltaMovement(scenario.equals("fast_fall") ? new Vec3(0, -1, 0) : Vec3.ZERO);
        player.connection.send(new ClientboundSetEntityMotionPacket(player));
        startTrace(player, id + "_" + scenario, scenario.equals("deep_oxygen") ? 420 : 200);
        player.sendSystemMessage(Component.literal("MFQM trial " + id + " / " + scenario + ": apply the named input; /mfqm status"));
        MfqmReborn.LOGGER.info("MFQM_TRIAL {} {} {} layers={} surface={} player={}", id, scenario,
                level.dimension().location(), layers, surface, player.getUUID());
        return state != null ? 1 : 0;
    }

    private static void startTrace(ServerPlayer player, String label, int ticks) {
        if (!label.matches("[A-Za-z0-9_-]{1,48}")) { player.sendSystemMessage(Component.literal("Invalid trace label")); return; }
        var data = SinkCapability.get(player);
        if (data == null) return;
        data.closeTrace();
        var path = FMLPaths.GAMEDIR.get().resolve("mfqm-traces")
                .resolve(label + "_" + player.level().getGameTime() + "_" + player.getId() + ".csv");
        try {
            data.trace = new TraceSession(path, ticks);
            MfqmReborn.LOGGER.info("MFQM_TRACE {}", path);
        } catch (IOException e) { player.sendSystemMessage(Component.literal("Cannot create trace: " + e.getMessage())); }
    }

    private static final class SinkLifecycleBridge {
        static void reset(ServerPlayer player) { art.tiary.mfqm.state.SinkLifecycle.clear(player, true); }
    }
}
