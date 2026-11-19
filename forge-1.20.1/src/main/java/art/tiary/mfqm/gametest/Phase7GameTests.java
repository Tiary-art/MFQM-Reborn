package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.integration.*;
import art.tiary.mfqm.legacy.StuckLease;
import art.tiary.mfqm.physics.*;
import java.util.*;
import java.nio.file.*;
import net.minecraft.core.BlockPos;
import net.minecraft.gametest.framework.GameTest;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.ai.attributes.AttributeModifier;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.gametest.GameTestHolder;
import net.minecraftforge.gametest.PrefixGameTestTemplate;

@GameTestHolder(MfqmReborn.MOD_ID)
@PrefixGameTestTemplate(false)
public final class Phase7GameTests {
    @GameTest(template = "pool_test", timeoutTicks = 100, batch = "phase7_lease")
    public static void leaseLifecycleAndMutualExclusion(GameTestHelper h) {
        SinkConfig.EXPERIMENTAL_STUCK.set(true);
        var pig = h.spawnWithNoFreeWill(EntityType.PIG, new Vec3(8.5, 7, 8.5));
        var speed = pig.getAttribute(Attributes.MOVEMENT_SPEED);
        UUID foreign = UUID.fromString("00000000-0000-0000-0000-000000000123");
        speed.addTransientModifier(new AttributeModifier(foreign, "foreign control", .2, AttributeModifier.Operation.MULTIPLY_TOTAL));
        var frames = StuckAdapter.observeForTest(pig);
        long initialTick = h.getLevel().getGameTime();
        MfqmReborn.LOGGER.info("PHASE8_LEASE_SETUP enabled={} alive={} exempt={}",StuckAdapter.enabled(),pig.isAlive(),SinkEngine.exempt(pig));
        StuckAdapter.contact(pig, 145);
        StuckAdapter.contact(pig, 128);
        StuckAdapter.update(pig);
        double p = 128 - 5, c = pig.horizontalCollision ? 0 : 1;
        double expected = Math.max(1 / Math.pow(1 + p * (1 + c / 2) / 50, 2), .02) - 1;
        h.assertTrue(Math.abs(speed.getModifier(StuckLease.UUID_KEY).getAmount() - expected) < 1e-12, "last contact wins");
        h.assertTrue(speed.getModifier(SinkEngine.SLOWNESS_ID) == null, "no old UUID stacking");
        h.assertTrue(!speed.save().toString().contains(StuckLease.UUID_KEY.toString()), "lease not persisted");
        h.runAfterDelay(2, () -> {
            h.assertTrue(frames.stream().anyMatch(f -> f.tick() == initialTick + 1 && f.level() == -1 && !f.modifierPresent()), "exact next world END release history");
            h.assertTrue(speed.getModifier(StuckLease.UUID_KEY) == null, "no-contact release via real level END: " + StuckAdapter.diagnosticState(pig));
            h.assertTrue(speed.getModifier(foreign) != null, "foreign UUID retained");
            StuckAdapter.contact(pig, 255);
            StuckAdapter.update(pig);
            SinkConfig.EXPERIMENTAL_STUCK.set(false);
        });
        h.runAfterDelay(6, () -> {
            h.assertTrue(speed.getModifier(StuckLease.UUID_KEY) == null, "config disable cleans lease");
            SinkConfig.EXPERIMENTAL_STUCK.set(true);
            StuckAdapter.contact(pig, 145);
            // Direct lifecycle callbacks verify server adapter cleanup, not real player reconnect.
            StuckAdapter.update(pig);
            h.assertTrue(speed.getModifier(StuckLease.UUID_KEY) != null, "active lease before unload");
            StuckAdapter.leave(new net.minecraftforge.event.entity.EntityLeaveLevelEvent(pig, h.getLevel()));
            h.assertTrue(!StuckAdapter.managed(pig), "unload clears state");
            StuckAdapter.contact(pig, 145);
            StuckAdapter.update(pig);
            h.assertTrue(speed.getModifier(StuckLease.UUID_KEY) != null, "active lease before death");
            StuckAdapter.death(new net.minecraftforge.event.entity.living.LivingDeathEvent(pig, pig.damageSources().generic()));
            h.assertTrue(!StuckAdapter.managed(pig), "death clears state");
            h.assertTrue(speed.getModifier(foreign) != null, "foreign modifier survives lifecycle");
            SinkConfig.EXPERIMENTAL_STUCK.set(false);
            pig.discard(); h.succeed();
        });
    }

    @GameTest(template = "pool_test", batch = "phase7_player")
    public static void playerLifecycleHandlerFixtures(GameTestHelper h) {
        SinkConfig.EXPERIMENTAL_STUCK.set(true);
        var player = new net.minecraft.world.entity.player.Player(h.getLevel(), BlockPos.ZERO, 0,
                new com.mojang.authlib.GameProfile(UUID.randomUUID(), "phase7-fixture")) {
            public boolean isSpectator() { return false; }
            public boolean isCreative() { return getAbilities().instabuild; }
        };
        var next = new net.minecraft.world.entity.player.Player(h.getLevel(), BlockPos.ZERO, 0,
                new com.mojang.authlib.GameProfile(UUID.randomUUID(), "phase7-clone")) {
            public boolean isSpectator() { return false; }
            public boolean isCreative() { return false; }
        };
        var speed = player.getAttribute(Attributes.MOVEMENT_SPEED);
        Runnable active = () -> {
            StuckAdapter.clear(player); StuckAdapter.contact(player, 145); StuckAdapter.update(player);
            h.assertTrue(speed.getModifier(StuckLease.UUID_KEY) != null, "active fixture lease");
        };
        Runnable clean = () -> h.assertTrue(speed.getModifier(StuckLease.UUID_KEY) == null && !StuckAdapter.managed(player), "handler clears owned state");
        active.run(); StuckAdapter.logout(new net.minecraftforge.event.entity.player.PlayerEvent.PlayerLoggedOutEvent(player)); clean.run();
        active.run(); StuckAdapter.login(new net.minecraftforge.event.entity.player.PlayerEvent.PlayerLoggedInEvent(player)); clean.run();
        active.run(); StuckAdapter.respawn(new net.minecraftforge.event.entity.player.PlayerEvent.PlayerRespawnEvent(player, false)); clean.run();
        active.run(); StuckAdapter.dimension(new net.minecraftforge.event.entity.player.PlayerEvent.PlayerChangedDimensionEvent(player,
                net.minecraft.world.level.Level.OVERWORLD, net.minecraft.world.level.Level.NETHER)); clean.run();
        active.run(); StuckAdapter.clone(new net.minecraftforge.event.entity.player.PlayerEvent.Clone(next, player, true)); clean.run();
        active.run(); player.getAbilities().instabuild = true; StuckAdapter.update(player); clean.run();
        player.getAbilities().instabuild = false;
        SinkConfig.EXPERIMENTAL_STUCK.set(false); player.discard(); next.discard(); h.succeed();
    }

    @GameTest(template = "pool_test", timeoutTicks = 100, batch = "phase7_registered")
    public static void registeredEntityLeaseReleaseTiming(GameTestHelper h) {
        SinkConfig.EXPERIMENTAL_STUCK.set(true);
        var pig = h.spawnWithNoFreeWill(EntityType.PIG, new Vec3(8.5, 7, 8.5));
        h.runAfterDelay(5, () -> {
            h.assertTrue(h.getLevel().getEntity(pig.getUUID()) == pig, "entity registered before lease timing begins");
            StuckAdapter.contact(pig, 145); StuckAdapter.contact(pig, 128); StuckAdapter.update(pig);
            MfqmReborn.LOGGER.info("PHASE7_REGISTERED_LEASE_START {}", StuckAdapter.diagnosticState(pig));
            h.assertTrue(pig.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(StuckLease.UUID_KEY) != null, "registered entity receives lease");
        });
        h.runAfterDelay(7, () -> {
            MfqmReborn.LOGGER.info("PHASE7_REGISTERED_LEASE_END {}", StuckAdapter.diagnosticState(pig));
            h.assertTrue(pig.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(StuckLease.UUID_KEY) == null, "registered no-contact release within two fixture ticks: " + StuckAdapter.diagnosticState(pig));
            StuckAdapter.clear(pig); SinkConfig.EXPERIMENTAL_STUCK.set(false); pig.discard(); h.succeed();
        });
    }

    @GameTest(template = "pool_test", timeoutTicks = 100, batch = "phase7_hold")
    public static void boundedInjectedContactScript(GameTestHelper h) {
        SinkConfig.PHASE7_DIAGNOSTICS.set(true);
        SinkConfig.EXPERIMENTAL_STUCK.set(true);
        var pig = h.spawnWithNoFreeWill(EntityType.PIG, new Vec3(8.5, 7, 8.5));
        MfqmReborn.LOGGER.info("PHASE7_HOLD_TEST_ENTITY {}", pig.getUUID());
        var holdFrames = StuckAdapter.observeForTest(pig);
        long holdStart = h.getLevel().getGameTime();
        StuckAdapter.holdForTest(pig, 145, 2);
        StuckAdapter.update(pig);
        // Check actual END snapshots, not an ambiguously phased intermediate GameTest callback.

        h.runAfterDelay(4, () -> {
            h.assertTrue(pig.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(StuckLease.UUID_KEY) == null, "script expires without persistent data");
            h.assertTrue(holdFrames.stream().anyMatch(f -> f.tick() == holdStart && f.remaining() == 1 && f.modifierPresent()), "first hold update");
            h.assertTrue(holdFrames.stream().anyMatch(f -> f.tick() == holdStart + 1 && f.remaining() == 0 && f.modifierPresent()), "second hold update at next world tick");
            h.assertTrue(holdFrames.stream().anyMatch(f -> f.tick() == holdStart + 2 && f.level() == -1 && !f.modifierPresent()), "release at exact following world tick");
            StuckAdapter.clear(pig); SinkConfig.EXPERIMENTAL_STUCK.set(false); pig.discard(); h.succeed();
        });
    }

    @GameTest(template = "pool_test", timeoutTicks = 100, batch = "phase7_motion")
    public static void measuredMotionWithAndWithoutInjectedLease(GameTestHelper h) {
        CoreMaterialGameTests.pool(h, MaterialProfile.QUICKSAND);
        SinkConfig.EXPERIMENTAL_STUCK.set(true);
        var baseline = h.spawnWithNoFreeWill(EntityType.PIG, new Vec3(6.5, 5.01, 8.5));
        var candidate = h.spawnWithNoFreeWill(EntityType.PIG, new Vec3(10.5, 5.01, 8.5));
        var pigs = List.of(baseline, candidate);
        List<String> trace = new ArrayList<>();
        trace.add("tick,mode,y,dy,vy,old_modifier,legacy_modifier");
        double[] previous = {baseline.getY(), candidate.getY()};
        int[] tick = {0};
        h.onEachTick(() -> {
            tick[0]++;
            for (int i = 0; i < pigs.size(); i++) {
                var pig = pigs.get(i); var speed = pig.getAttribute(Attributes.MOVEMENT_SPEED);
                double dy = pig.getY() - previous[i]; previous[i] = pig.getY();
                h.assertTrue(Double.isFinite(dy) && dy >= -.1, "observed displacement finite and bounded");
                trace.add(tick[0] + "," + (i == 0 ? "old" : "injected") + "," + pig.getY() + "," + dy + ","
                        + pig.getDeltaMovement().y + "," + (speed.getModifier(SinkEngine.SLOWNESS_ID) != null) + ","
                        + (speed.getModifier(StuckLease.UUID_KEY) != null));
                if (i == 1 && tick[0] <= 25) StuckAdapter.contact(pig, 145);
            }
        });
        h.runAfterDelay(40, () -> {
            try {
                Path out = Path.of("phase7-traces"); Files.createDirectories(out);
                Files.write(out.resolve("paired-mob-motion.csv"), trace);
            } catch (java.io.IOException ex) { throw new RuntimeException(ex); }
            h.assertTrue(candidate.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(StuckLease.UUID_KEY) == null, "release after contact sequence stops");
            StuckAdapter.clear(candidate); SinkConfig.EXPERIMENTAL_STUCK.set(false);
            baseline.discard(); candidate.discard(); h.succeed();
        });
    }

    @GameTest(template = "pool_test")
    public static void dryGuardAndAirAliases(GameTestHelper h) {
        var level = h.getLevel(); var origin = h.absolutePos(new BlockPos(8, 8, 8));
        List<String> events = new ArrayList<>(); var port = new DryWorldAdapter(level, events::add);
        for (var air : List.of(Blocks.AIR, Blocks.CAVE_AIR, Blocks.VOID_AIR)) {
            level.setBlock(origin, air.defaultBlockState(), 3);
            h.assertTrue(port.blockAt(origin.getX(), origin.getY(), origin.getZ()) == art.tiary.mfqm.legacy.LegacyBlock.AIR, "explicit modern AIR alias");
        }
        events.clear();
        try { DryWorldAdapter.generate(level, new BlockPos(20000000, 64, 20000000), 5, 0, events::add); throw new AssertionError("unloaded accepted"); }
        catch (IllegalStateException expected) { h.assertTrue(events.isEmpty(), "unloaded preflight produces no partial writes/RNG"); }
        h.assertTrue(!port.write(origin.getX(), level.getMaxBuildHeight(), origin.getZ(), art.tiary.mfqm.legacy.LegacyBlock.AIR, 0, 3), "out-of-height write false");
        h.assertTrue(events.get(0).endsWith("false"), "rejected write remains observable");
        h.succeed();
    }

    @GameTest(template = "pool_test")
    public static void dryRealWorldOrderedNativeSlice(GameTestHelper h) {
        try {
            BlockPos origin = h.absolutePos(new BlockPos(8, 8, 8));
            // Solid supported sand fixture; generation and comparison are synchronous before scheduled falling ticks.
            for (int x = -4; x <= 5; x++) for (int z = -4; z <= 5; z++) {
                h.getLevel().setBlock(origin.offset(x, -8, z), Blocks.STONE.defaultBlockState(), 3);
                for (int y = -7; y <= 0; y++) h.getLevel().setBlock(origin.offset(x, y, z), Blocks.SAND.defaultBlockState(), 3);
                for (int y = 1; y <= 2; y++) h.getLevel().setBlock(origin.offset(x, y, z), Blocks.AIR.defaultBlockState(), 3);
            }
            List<String> actual = new ArrayList<>();
            DryWorldAdapter.generate(h.getLevel(), origin, 5, 0, actual::add);
            Path fixture = Path.of(System.getProperty("mfqm.phase7Vectors"), "generateSoftSand-r5-s0.tsv");
            List<String> expected = Files.readAllLines(fixture);
            h.assertTrue(actual.size() == expected.size(), "complete native event count " + actual.size() + "/" + expected.size());
            int sameStateRejected = 0;
            Map<BlockPos, String> finalCells = new HashMap<>();
            List<String> translated = new ArrayList<>();
            for (int i = 0; i < actual.size(); i++) {
                String[] a = actual.get(i).split("\t"), b = expected.get(i).split("\t");
                if (a[0].equals("R")) {
                    if (a[1].equals("nextDouble")) b[3] = Double.toString(Double.parseDouble(b[3]));
                } else {
                    b[1] = Integer.toString(Integer.parseInt(b[1]) + origin.getX() + 16);
                    b[2] = Integer.toString(Integer.parseInt(b[2]) + origin.getY() - 70);
                    b[3] = Integer.toString(Integer.parseInt(b[3]) + origin.getZ());
                    if (a[0].equals("W")) {
                        BlockPos pos = new BlockPos(Integer.parseInt(a[1]), Integer.parseInt(a[2]), Integer.parseInt(a[3]));
                        if (!a[7].equals(b[7])) {
                            h.assertTrue(a[7].equals("false") && a[4].equals(finalCells.get(pos)), "only same-state setBlock false is expected");
                            sameStateRejected++; b[7] = a[7];
                        }
                        finalCells.put(pos, a[4]);
                    }
                }
                h.assertTrue(Arrays.equals(a, b), "ordered event mismatch " + i + ": " + actual.get(i));
                translated.add(String.join("\t", b));
            }
            DryWorldAdapter check = new DryWorldAdapter(h.getLevel(), ignored -> {});
            for (var e : finalCells.entrySet()) {
                BlockPos pos = e.getKey();
                h.assertTrue(check.blockAt(pos.getX(), pos.getY(), pos.getZ()).name().equals(e.getValue()), "final state matches native at " + pos);
            }
            Path out = Path.of("phase7-traces"); Files.createDirectories(out);
            Files.write(out.resolve("dry-real-world.tsv"), actual);
            Files.writeString(out.resolve("dry-summary.txt"), "events=" + actual.size() + " same_state_false=" + sameStateRejected + " cells=" + finalCells.size() + "\n");
            MfqmReborn.LOGGER.info("PHASE7_DRY_NATIVE events={} same_state_false={} final_cells={}", actual.size(), sameStateRejected, finalCells.size());
            h.succeed();
        } catch (Exception ex) { throw new RuntimeException(ex); }
    }
}
