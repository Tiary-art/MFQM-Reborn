package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.*;
import art.tiary.mfqm.state.*;
import net.minecraft.gametest.framework.GameTest;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.gametest.GameTestHolder;
import net.minecraftforge.gametest.PrefixGameTestTemplate;

@GameTestHolder(MfqmReborn.MOD_ID)
@PrefixGameTestTemplate(false)
public final class MotionGameTests {
    @GameTest(template = "pool_test")
    public static void sweptThinLayerEntryDissipatesFastFall(GameTestHelper h) {
        CoreMaterialGameTests.pool(h, MaterialProfile.QUICKSAND);
        var pig = h.spawnWithNoFreeWill(EntityType.PIG, new Vec3(8.5, 7, 8.5));
        pig.setDeltaMovement(0, -4, 0); pig.fallDistance = 10;
        double y = pig.getY();
        var sweep = ContactSampler.entry(h.getLevel(), pig, y, y - 4);
        h.assertTrue(sweep != null, "sweep finds crossed top surface");
        MotionRuntime.prepare(pig, false);
        h.assertTrue(y + pig.getDeltaMovement().y >= sweep.surface() - SinkConfig.motionPolicy().entryDepth() - 1e-6,
                "first move cannot penetrate beyond candidate entry depth");
        h.assertTrue(pig.fallDistance == 0, "entry replaces free-fall history before move");
        pig.discard(); h.succeed();
    }
    @GameTest(template = "pool_test", timeoutTicks = 100)
    public static void actualMobDisplacementIsBoundedAfterContact(GameTestHelper h) {
        CoreMaterialGameTests.pool(h, MaterialProfile.QUICKSAND);
        var pig = h.spawnWithNoFreeWill(EntityType.PIG, new Vec3(8.5, 5.01, 8.5));
        final double[] previous = {pig.getY()};
        h.onEachTick(() -> {
            double delta = pig.getY() - previous[0]; previous[0] = pig.getY();
            h.assertTrue(Double.isFinite(delta) && delta >= -SinkConfig.motionPolicy().terminal() - 0.001,
                    "actual displacement, not solver velocity, bounded");
        });
        h.runAfterDelay(40, () -> { pig.discard(); h.succeed(); });
    }
    @GameTest(template = "pool_test")
    public static void exitAndLifecycleDoNotEraseOutsideFall(GameTestHelper h) {
        CoreMaterialGameTests.pool(h, MaterialProfile.MUD);
        var pig = h.spawnWithNoFreeWill(EntityType.PIG, new Vec3(8.5, 4.8, 8.5));
        MotionRuntime.prepare(pig, false);
        var d = SinkCapability.get(pig);
        h.assertTrue(d.controlledMotion, "inside contact controlled");
        pig.setPos(pig.getX() + 30, pig.getY() + 8, pig.getZ());
        pig.setDeltaMovement(0, -1, 0); pig.fallDistance = 6;
        MotionRuntime.prepare(pig, false);
        h.assertTrue(!d.controlledMotion && pig.fallDistance == 6 && pig.getDeltaMovement().y == -1,
                "outside motion and fall distance remain vanilla");
        d.motionAge = 20; d.motionPhase = MotionMath.Phase.SUBMERGED;
        SinkLifecycle.clear(pig, false);
        h.assertTrue(d.motionAge == 0 && d.motionPhase == MotionMath.Phase.OUTSIDE && !d.controlledMotion,
                "lifecycle clears candidate history");
        pig.discard(); h.succeed();
    }
    @GameTest(template = "pool_test")
    public static void controlledLandingDoesNotGrantOutsideFallImmunity(GameTestHelper h) {
        CoreMaterialGameTests.pool(h, MaterialProfile.QUICKSAND);
        var pig = h.spawnWithNoFreeWill(EntityType.PIG, new Vec3(8.5, 4.5, 8.5));
        MotionRuntime.prepare(pig, false);
        float health = pig.getHealth();
        pig.causeFallDamage(10, 1, pig.damageSources().fall());
        h.assertTrue(pig.getHealth() == health, "confirmed slow material landing discards old fall history");
        pig.setPos(pig.getX() + 30, pig.getY() + 10, pig.getZ());
        pig.setDeltaMovement(0, -1, 0);
        MotionRuntime.prepare(pig, false);
        pig.causeFallDamage(10, 1, pig.damageSources().fall());
        h.assertTrue(pig.getHealth() < health, "outside fall still causes real vanilla damage");
        pig.discard(); h.succeed();
    }
    @GameTest(template = "pool_test", timeoutTicks = 100)
    public static void naturalPigFallsAndEntersWithinDepthBudget(GameTestHelper h) {
        CoreMaterialGameTests.pool(h, MaterialProfile.QUICKSAND);
        var pig = h.spawnWithNoFreeWill(EntityType.PIG, new Vec3(8.5, 8, 8.5));
        pig.setNoAi(false);
        double start = pig.getY();
        final boolean[] contact = {false};
        h.onEachTick(() -> {
            var c = ContactSampler.sample(h.getLevel(), pig);
            if (!contact[0] && c.material() != null) {
                contact[0] = true;
                h.assertTrue(c.depthBlocks() <= SinkConfig.motionPolicy().entryDepth() + 0.001,
                        "natural real gravity entry has bounded first penetration");
            }
        });
        h.runAfterDelay(45, () -> {
            h.assertTrue(contact[0] && pig.getY() < start - 2, "pig actually fell; a floating fixture cannot pass");
            pig.discard(); h.succeed();
        });
    }
}
