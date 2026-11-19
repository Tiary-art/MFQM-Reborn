package art.tiary.mfqm.diagnostic;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.MaterialProfile;
import art.tiary.mfqm.physics.SinkCommands;
import art.tiary.mfqm.state.SinkLifecycle;
import com.mojang.brigadier.arguments.IntegerArgumentType;
import com.mojang.brigadier.arguments.StringArgumentType;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;
import net.minecraft.commands.Commands;
import net.minecraft.core.BlockPos;
import net.minecraft.network.chat.Component;
import net.minecraft.network.protocol.game.ClientboundSetEntityMotionPacket;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.level.GameType;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.event.RegisterCommandsEvent;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** Destructive fixtures only in an operator's explicitly requested disposable test world. */
@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID)
public final class MotionTrials {
    private record Case(String material, int layers, int height, boolean pig) { }
    private record Suite(List<Case> cases, int index, long next, String prefix) { }
    private static final Map<UUID, Suite> SUITES = new HashMap<>();
    private static final Map<UUID, LivingEntity> FIXTURES = new HashMap<>();
    private MotionTrials() { }
    @SubscribeEvent public static void register(RegisterCommandsEvent event) {
        event.getDispatcher().register(Commands.literal("mfqm").then(Commands.literal("motion").requires(s -> s.hasPermission(2))
                .then(Commands.literal("diag").then(Commands.argument("ticks", IntegerArgumentType.integer(20, 1200))
                        .then(Commands.argument("label", StringArgumentType.word()).executes(c -> {
                            var player = c.getSource().getPlayerOrException();
                            String label = StringArgumentType.getString(c, "label");
                            if (validLabel(label)) MotionDiagnostics.start(player, player, IntegerArgumentType.getInteger(c, "ticks"), label);
                            return 1;
                        }))))
                .then(Commands.literal("stop").executes(c -> {
                    var p = c.getSource().getPlayerOrException(); SUITES.remove(p.getUUID()); MotionDiagnostics.stop(p);
                    var old = FIXTURES.remove(p.getUUID()); if (old != null && old != p) { MotionDiagnostics.stop(old); old.discard(); }
                    art.tiary.mfqm.network.SinkNetwork.startDiagnostic(p, p.getId(), 0, "stop", "00000000"); return 1;
                }))
                .then(Commands.literal("suite").then(Commands.argument("phase", StringArgumentType.word()).executes(c -> {
                    var p = c.getSource().getPlayerOrException(); String prefix = StringArgumentType.getString(c, "phase");
                    return startSuite(p, prefix, false);
                })))
                .then(Commands.literal("pigsuite").then(Commands.argument("phase", StringArgumentType.word()).executes(c ->
                        startSuite(c.getSource().getPlayerOrException(), StringArgumentType.getString(c, "phase"), true))))
                .then(Commands.literal("trial").then(Commands.argument("material", StringArgumentType.word())
                        .then(Commands.argument("layers", IntegerArgumentType.integer(1, 17))
                                .then(Commands.argument("height", IntegerArgumentType.integer(0, 10))
                                        .then(Commands.argument("subject", StringArgumentType.word()).executes(c -> {
                                            var p = c.getSource().getPlayerOrException(); SUITES.remove(p.getUUID());
                                            run(p, new Case(StringArgumentType.getString(c, "material"), IntegerArgumentType.getInteger(c, "layers"),
                                                    IntegerArgumentType.getInteger(c, "height"), StringArgumentType.getString(c, "subject").equals("pig")), "manual");
                                            return 1;
                                        }))))))));
    }
    private static int startSuite(ServerPlayer p, String prefix, boolean pigsOnly) {
        if (!validLabel(prefix) || prefix.length() > 20 || !p.isAlive()) return 0;
        var cases = new ArrayList<Case>();
        for (boolean pig : new boolean[]{false, true}) {
            if (pigsOnly && !pig) continue;
            for (var m : MaterialProfile.values()) for (int layers : new int[]{1, 3, 17})
                for (int height : new int[]{0, 3, 10}) cases.add(new Case(m.id, layers, height, pig));
        }
        SUITES.put(p.getUUID(), new Suite(cases, 0, p.level().getGameTime(), prefix));
        p.sendSystemMessage(Component.literal("MFQM motion suite: " + cases.size() + " real-tick fixtures; remain connected/unpaused. /mfqm motion stop"));
        return 1;
    }
    private static boolean validLabel(String label) { return label.matches("[A-Za-z0-9_-]{1,64}"); }
    private static void release(ServerPlayer player) {
        SUITES.remove(player.getUUID());
        var old = FIXTURES.remove(player.getUUID());
        if (old != null) {
            MotionDiagnostics.stop(old);
            if (old != player) old.discard();
        }
    }
    @SubscribeEvent public static void logout(net.minecraftforge.event.entity.player.PlayerEvent.PlayerLoggedOutEvent event) {
        if (event.getEntity() instanceof ServerPlayer player) release(player);
    }
    @SubscribeEvent public static void stopped(net.minecraftforge.event.server.ServerStoppedEvent event) {
        SUITES.clear(); FIXTURES.clear();
    }
    @SubscribeEvent public static void tick(TickEvent.LevelTickEvent event) {
        if (event.phase != TickEvent.Phase.END || event.level.isClientSide || SUITES.isEmpty()) return;
        for (var player : event.level.players()) {
            if (!(player instanceof ServerPlayer p)) continue;
            var suite = SUITES.get(p.getUUID());
            if (suite == null || event.level.getGameTime() < suite.next) continue;
            if (suite.index >= suite.cases.size()) {
                release(p);
                p.connection.teleport(8.5, 65, 0.5, 0, 30);
                p.sendSystemMessage(Component.literal("MFQM motion suite completed (records require analysis, not automatic acceptance)."));
                MfqmReborn.LOGGER.info("MFQM_B1_SUITE_END {}", suite.prefix); continue;
            }
            run(p, suite.cases.get(suite.index), suite.prefix);
            SUITES.put(p.getUUID(), new Suite(suite.cases, suite.index + 1, event.level.getGameTime() + 280, suite.prefix));
        }
    }
    private static void run(ServerPlayer player, Case c, String prefix) {
        if (!player.isAlive()) {
            player.sendSystemMessage(Component.literal("Respawn before starting a motion fixture; dead-player trials are invalid."));
            return;
        }
        boolean stone = c.material.equals("stone"), water = c.material.equals("water");
        var profile = MaterialProfile.byId(c.material);
        if (profile == null && !stone && !water) return;
        var previous = FIXTURES.remove(player.getUUID());
        if (previous != null) { MotionDiagnostics.stop(previous); if (previous != player) previous.discard(); }
        var level = player.serverLevel();
        for (int x = -5; x <= 5; x++) for (int z = -5; z <= 5; z++) {
            level.setBlockAndUpdate(new BlockPos(x, 64 - c.layers, z), Blocks.BEDROCK.defaultBlockState());
            for (int y = 65 - c.layers; y <= 80; y++) {
                var state = y > 64 ? Blocks.AIR.defaultBlockState() : stone ? Blocks.STONE.defaultBlockState()
                        : water ? Blocks.WATER.defaultBlockState() : SinkCommands.materialState(profile);
                level.setBlockAndUpdate(new BlockPos(x, y, z), state);
            }
        }
        for (int x = 6; x <= 10; x++) for (int z = -3; z <= 3; z++) level.setBlockAndUpdate(new BlockPos(x, 64, z), Blocks.STONE.defaultBlockState());
        SinkLifecycle.clear(player, true); player.setGameMode(GameType.SURVIVAL);
        player.setHealth(player.getMaxHealth()); player.getFoodData().setFoodLevel(20);
        player.setRespawnPosition(level.dimension(), new BlockPos(8, 65, 0), 0, true, false);
        double surface = 64 + (profile == null ? 1 : profile.surfaceHeight);
        LivingEntity target = player;
        if (c.pig) {
            player.connection.teleport(8.5, 65, 0.5, 90, 20);
            var pig = EntityType.PIG.create(level); if (pig == null) return;
            pig.setNoAi(false); pig.moveTo(0.5, surface + c.height + 0.01, 0.5, 0, 0); level.addFreshEntity(pig); target = pig;
        } else player.connection.teleport(0.5, surface + c.height + 0.01, 0.5, 0, 30);
        target.fallDistance = 0; target.setDeltaMovement(Vec3.ZERO);
        if (target == player) player.connection.send(new ClientboundSetEntityMotionPacket(player));
        art.tiary.mfqm.network.SinkNetwork.syncTo(player, player);
        FIXTURES.put(player.getUUID(), target);
        String label = prefix + "_" + (c.pig ? "pig" : "player") + "_" + c.material + "_L" + c.layers + "_H" + c.height;
        MotionDiagnostics.start(player, target, 260, label);
        MfqmReborn.LOGGER.info("MFQM_B1_TRIAL {} tick={} surface={}", label, level.getGameTime(), surface);
    }
}
