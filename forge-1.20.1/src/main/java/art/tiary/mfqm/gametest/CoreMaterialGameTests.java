package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.*;
import art.tiary.mfqm.registry.ModBlocks;
import art.tiary.mfqm.state.*;
import com.mojang.authlib.GameProfile;
import java.util.UUID;
import net.minecraft.core.BlockPos;
import net.minecraft.gametest.framework.GameTest;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.ai.attributes.AttributeModifier;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.animal.Pig;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.GameType;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.storage.loot.LootParams;
import net.minecraft.world.level.storage.loot.parameters.LootContextParamSets;
import net.minecraft.world.level.storage.loot.parameters.LootContextParams;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.entity.player.PlayerEvent;
import net.minecraftforge.gametest.GameTestHolder;
import net.minecraftforge.gametest.PrefixGameTestTemplate;
import net.minecraftforge.registries.ForgeRegistries;

@GameTestHolder(MfqmReborn.MOD_ID)
@PrefixGameTestTemplate(false)
public final class CoreMaterialGameTests {
    private CoreMaterialGameTests() { }

    public static void pool(GameTestHelper helper, MaterialProfile profile) {
        for (int x = 2; x <= 14; x++) for (int z = 2; z <= 14; z++) {
            helper.setBlock(new BlockPos(x, 1, z), Blocks.BEDROCK);
            for (int y = 2; y <= 4; y++) helper.setBlock(new BlockPos(x, y, z),
                    x >= 4 && x <= 12 && z >= 4 && z <= 12 ? SinkCommands.materialState(profile) : Blocks.AIR.defaultBlockState());
        }
    }

    private static Pig pig(GameTestHelper helper, double x, double y, double z) {
        return helper.spawnWithNoFreeWill(EntityType.PIG, new Vec3(x, y, z));
    }

    private static Player playerFixture(GameTestHelper helper, boolean creative, boolean spectator) {
        // GameTestHelper.makeMockServerPlayerInLevel invokes Forge's login path with a null
        // Netty channel. These lifecycle fixtures need a Player, not a fake network login.
        return new Player(helper.getLevel(), BlockPos.ZERO, 0, new GameProfile(UUID.randomUUID(), "mfqm-fixture")) {
            @Override public boolean isSpectator() { return spectator; }
            @Override public boolean isCreative() { return creative; }
        };
    }

    @GameTest(template = "pool_test")
    public static void registeredMaterialsPlaceAndDrop(GameTestHelper helper) {
        for (var material : MaterialProfile.values()) {
            var state = SinkCommands.materialState(material);
            var id = new ResourceLocation("mfqm", material.id);
            helper.assertTrue(id.equals(ForgeRegistries.BLOCKS.getKey(state.getBlock())), "Stable block ID " + id);
            var item = Item.byBlock(state.getBlock());
            helper.assertTrue(id.equals(ForgeRegistries.ITEMS.getKey(item)), "Stable item ID " + id);
            var pos = new BlockPos(8, 2, 8);
            helper.setBlock(pos, state);
            helper.assertBlockPresent(state.getBlock(), pos);
            var params = new LootParams.Builder(helper.getLevel())
                    .withParameter(LootContextParams.BLOCK_STATE, state)
                    .withParameter(LootContextParams.ORIGIN, Vec3.atCenterOf(helper.absolutePos(pos)))
                    .withParameter(LootContextParams.TOOL, ItemStack.EMPTY).create(LootContextParamSets.BLOCK);
            var drops = helper.getLevel().getServer().getLootData().getLootTable(state.getBlock().getLootTable()).getRandomItems(params);
            helper.assertTrue(drops.size() == 1 && drops.get(0).is(item), "Correct material loot " + id);
        }
        helper.succeed();
    }

    @GameTest(template = "pool_test")
    public static void liveMudPoolGeometryAndShapes(GameTestHelper helper) {
        var origin = new BlockPos(8, 2, 8);
        var mud = ModBlocks.MUD.get().defaultBlockState();
        for (int x = -3; x <= 3; x++) for (int z = -3; z <= 3; z++) helper.setBlock(origin.offset(x, 0, z), mud);
        var abs = helper.absolutePos(origin);
        var grid = MudBlock.grid(helper.getLevel(), abs);
        helper.assertTrue(MudGeometry.poolDepth(grid) == 3, "radius3 center depth3");
        helper.assertTrue(mud.getCollisionShape(helper.getLevel(), abs).isEmpty(), "deep center has no support");
        for (int x = -1; x <= 1; x++) for (int z = -1; z <= 1; z++) if (x != 0 || z != 0) {
            helper.setBlock(origin.offset(x, 0, z), Blocks.AIR);
            helper.assertTrue(MudGeometry.poolDepth(grid) == 0, "each of8 neighbors required");
            helper.setBlock(origin.offset(x, 0, z), mud);
        }
        for (int[] axis : new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}) {
            var r2 = origin.offset(axis[0] * 2, 0, axis[1] * 2);
            helper.setBlock(r2, Blocks.AIR);
            helper.assertTrue(MudGeometry.poolDepth(grid) == 1, "radius2 gap gives1");
            helper.setBlock(r2, mud);
            var r3 = origin.offset(axis[0] * 3, 0, axis[1] * 3);
            helper.setBlock(r3, Blocks.AIR);
            helper.assertTrue(MudGeometry.poolDepth(grid) == 2, "radius3 gap gives2");
            helper.setBlock(r3, mud);
        }
        helper.setBlock(origin.east(), Blocks.AIR);
        helper.assertTrue(MudGeometry.safeEdge(grid) && MudGeometry.effectiveDepth(grid, 3) == 0, "open bank is safe");
        helper.setBlock(origin.above(), Blocks.WATER);
        helper.assertTrue(MudGeometry.poolDepth(grid) == 3 && !MudGeometry.safeEdge(grid), "water above overrides safe edge");
        helper.setBlock(origin.above(), mud);
        helper.setBlock(origin.above(2), Blocks.WATER);
        helper.assertTrue(MudGeometry.poolDepth(grid) == 3 && !MudGeometry.safeEdge(grid), "mud then water branch");
        helper.setBlock(origin.above(), Blocks.AIR); helper.setBlock(origin.above(2), Blocks.AIR);
        for (int x = -3; x <= 3; x++) for (int z = -3; z <= 3; z++) if (x != 0 || z != 0)
            helper.setBlock(origin.offset(x, 0, z), Blocks.STONE);
        double[] expected = {0.7, 0.5, 0.25, 0};
        for (int depth = 0; depth <= 3; depth++) {
            var variant = mud.setValue(MudBlock.DEPTH, depth);
            helper.setBlock(origin, variant);
            var shape = variant.getCollisionShape(helper.getLevel(), abs);
            helper.assertTrue(depth == 3 ? shape.isEmpty() : Math.abs(shape.max(net.minecraft.core.Direction.Axis.Y) - expected[depth]) < 1e-6,
                    "collision height state" + depth);
        }
        helper.succeed();
    }

    @GameTest(template = "pool_test", timeoutTicks = 80)
    public static void quicksandRealMobTrajectory(GameTestHelper helper) {
        pool(helper, MaterialProfile.QUICKSAND);
        Pig pig = pig(helper, 8.5, 5.01, 8.5);
        double initial = pig.getY();
        helper.runAfterDelay(35, () -> {
            var data = SinkCapability.get(pig);
            helper.assertTrue(data != null && data.active() && data.stuck > 0, "mob has authoritative sinking state");
            helper.assertTrue(pig.getY() < initial - 0.1, "quicksand actually sinks a ticking mob");
            helper.assertTrue(Double.isFinite(pig.getDeltaMovement().y), "finite trajectory");
            pig.discard(); helper.succeed();
        });
    }

    @GameTest(template = "pool_test", timeoutTicks = 80)
    public static void softQuicksandDeepCenterPull(GameTestHelper helper) {
        pool(helper, MaterialProfile.SOFT_QUICKSAND);
        Pig pig = pig(helper, 8.2, 3.7, 8.5);
        double target = helper.absoluteVec(new Vec3(8.5, 0, 8.5)).x;
        double initialDistance = Math.abs(pig.getX() - target);
        helper.runAfterDelay(12, () -> {
            var data = SinkCapability.get(pig);
            helper.assertTrue(data != null && data.material == MaterialProfile.SOFT_QUICKSAND, "soft profile selected");
            helper.assertTrue(Math.abs(pig.getX() - target) < initialDistance, "deep entity moves toward center");
            pig.discard(); helper.succeed();
        });
    }

    @GameTest(template = "pool_test", timeoutTicks = 140)
    public static void mudCenterAndSafeEdgeHaveDifferentSupport(GameTestHelper helper) {
        pool(helper, MaterialProfile.MUD);
        Pig center = pig(helper, 8.5, 5.01, 8.5);
        Pig edge = pig(helper, 12.7, 5.01, 8.5);
        helper.runAfterDelay(85, () -> {
            MfqmReborn.LOGGER.info("MFQM_TEST_MUD_SUPPORT centerY={} edgeY={} centerDepth={} edgeDepth={}",
                    center.getY(), edge.getY(), SinkCapability.get(center).mudDepth, SinkCapability.get(edge).mudDepth);
            helper.assertTrue(center.getY() < edge.getY() - 0.08, "deep center sinks below supported safe edge");
            helper.assertTrue(SinkCapability.get(center).mudDepth == 3, "center geometry selected depth3");
            helper.assertTrue(SinkCapability.get(edge).mudDepth == 0, "edge geometry selected depth0");
            center.discard(); edge.discard(); helper.succeed();
        });
    }

    @GameTest(template = "pool_test")
    public static void sameAndMixedCellsSettleOncePerEntityTick(GameTestHelper helper) {
        pool(helper, MaterialProfile.QUICKSAND);
        for (int y = 2; y <= 4; y++) helper.setBlock(new BlockPos(9, y, 8), ModBlocks.MUD.get());
        Pig pig = pig(helper, 9, 3.2, 8.5);
        var data = SinkCapability.get(pig);
        helper.assertTrue(data != null, "capability attached");
        data.air = 20;
        long before = data.settlements;
        SinkEngine.settle(helper.getLevel(), pig);
        helper.assertTrue(data.contacts >= 2 && data.eyeCovered, "multiple mixed contacts and independent covered eye");
        int air = data.air; double vy = pig.getDeltaMovement().y;
        SinkEngine.settle(helper.getLevel(), pig);
        helper.assertTrue(data.settlements == before + 1 && data.air == 19 && data.air == air,
                "one air deduction despite multiple cells and callbacks");
        helper.assertTrue(pig.getDeltaMovement().y == vy, "motion not applied twice");
        helper.setBlock(new BlockPos(9, 3, 8), ModBlocks.QUICKSAND.get());
        SinkEngine.settle(helper.getLevel(), pig);
        helper.assertTrue(data.settlements == before + 1, "same-material additional callback also ignored");
        pig.discard(); helper.succeed();
    }

    @GameTest(template = "pool_test", timeoutTicks = 50)
    public static void drowningDamageRequestCannotRepeatWithinOneTick(GameTestHelper helper) {
        pool(helper, MaterialProfile.QUICKSAND);
        Pig pig = pig(helper, 9, 3.2, 8.5);
        SinkCapability.get(pig).air = 0;
        helper.onEachTick(() -> {
            if (helper.getLevel().getGameTime() % 16 != 0) return;
            var data = SinkCapability.get(pig);
            SinkEngine.settle(helper.getLevel(), pig);
            long before = data.damageEvents;
            long settlements = data.settlements;
            SinkEngine.settle(helper.getLevel(), pig);
            helper.assertTrue(before == 1 && data.lastDamageTick == helper.getLevel().getGameTime()
                    && data.damageEvents == before && data.settlements == settlements,
                    "one damage request at the16tick clock, repeat callbacks do not change it");
            helper.assertTrue(pig.getHealth() < pig.getMaxHealth(), "damage reached actual living entity");
            pig.discard(); helper.succeed();
        });
    }

    @GameTest(template = "pool_test", timeoutTicks = 140)
    public static void oxygenDamageThenExitRecoversAndPreservesForeignModifier(GameTestHelper helper) {
        pool(helper, MaterialProfile.QUICKSAND);
        Pig pig = pig(helper, 8.5, 3.2, 8.5);
        var data = SinkCapability.get(pig);
        data.air = 1;
        UUID foreign = UUID.fromString("9c7bc098-e0e4-40c8-a8e7-77b28e330144");
        var speed = pig.getAttribute(Attributes.MOVEMENT_SPEED);
        speed.addTransientModifier(new AttributeModifier(foreign, "Foreign test effect", 0.1, AttributeModifier.Operation.ADDITION));
        helper.runAfterDelay(25, () -> {
            helper.assertTrue(data.damageEvents > 0 && pig.getHealth() < pig.getMaxHealth(), "covered eyes exhausted oxygen and took damage");
            helper.assertTrue(speed.getModifier(SinkEngine.SLOWNESS_ID) != null, "one owned slowdown modifier");
            var outside = helper.absoluteVec(new Vec3(2.5, 2, 2.5));
            pig.setPos(outside.x, outside.y, outside.z);
            pig.setDeltaMovement(Vec3.ZERO);
        });
        helper.runAfterDelay(27, () -> {
            helper.assertTrue(!data.active() && data.stuck == 0 && speed.getModifier(SinkEngine.SLOWNESS_ID) == null, "exit clears only own slowdown immediately");
            helper.assertTrue(speed.getModifier(foreign) != null, "foreign modifier preserved");
        });
        helper.runAfterDelay(95, () -> {
            helper.assertTrue(data.air == 300 && !data.eyeCovered, "air recovered at5/tick after exit");
            pig.discard(); helper.succeed();
        });
    }

    @GameTest(template = "pool_test")
    public static void actualEntityNBTStoresResidueButNoTransientState(GameTestHelper helper) {
        pool(helper, MaterialProfile.QUICKSAND);
        Pig pig = pig(helper, 8.5, 3.2, 8.5);
        SinkEngine.settle(helper.getLevel(), pig);
        var data = SinkCapability.get(pig);
        data.residueTicks = 100;
        CompoundTag saved = pig.saveWithoutId(new CompoundTag());
        var cap = saved.getCompound("ForgeCaps").getCompound("mfqm:sink_state");
        helper.assertTrue(cap.contains("schema") && !cap.contains("air") && !cap.contains("stuck"), "versioned persistent fields only");
        Pig restored = EntityType.PIG.create(helper.getLevel());
        restored.load(saved);
        var next = SinkCapability.get(restored);
        helper.assertTrue(next != null && next.residueTicks == 100 && next.residueType.equals("quicksand"), "actual entity NBT reload preserves residue");
        helper.assertTrue(!next.active() && next.air == 300 && next.stuck == 0, "reload never resumes transient trap state");
        helper.assertTrue(restored.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(SinkEngine.SLOWNESS_ID) == null, "transient attribute absent after NBT reload");
        var corrupt = new CompoundTag(); corrupt.putInt("schema", 1); corrupt.putString("residueType", "not_a_material"); corrupt.putInt("residueTicks", Integer.MAX_VALUE);
        next.load(corrupt);
        helper.assertTrue(next.residueTicks == 0 && next.residueType.isEmpty(), "invalid persistent input rejected");
        pig.discard(); restored.discard(); helper.succeed();
    }

    @GameTest(template = "pool_test")
    public static void deathAndRemovalInvalidateTransientState(GameTestHelper helper) {
        pool(helper, MaterialProfile.QUICKSAND);
        Pig dying = pig(helper, 8.5, 3.2, 8.5);
        SinkEngine.settle(helper.getLevel(), dying);
        var state = SinkCapability.get(dying);
        dying.kill();
        helper.assertTrue(!state.active() && state.air == 300 && state.residueTicks == 0, "real death clears all state");
        helper.assertTrue(dying.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(SinkEngine.SLOWNESS_ID) == null, "real death removes owned modifier");
        Pig removed = pig(helper, 8.5, 3.2, 8.5);
        SinkEngine.settle(helper.getLevel(), removed);
        var discarded = SinkCapability.get(removed);
        removed.discard();
        helper.assertTrue(!discarded.active() && discarded.air == 300, "removal/capability invalidation clears transient state");
        dying.discard(); helper.succeed();
    }

    @GameTest(template = "pool_test")
    public static void creativeSpectatorAndInvulnerableAreExempt(GameTestHelper helper) {
        pool(helper, MaterialProfile.QUICKSAND);
        var pos = helper.absoluteVec(new Vec3(8.5, 3.2, 8.5));
        for (var mode : new GameType[]{GameType.CREATIVE, GameType.SPECTATOR}) {
            var player = playerFixture(helper, mode == GameType.CREATIVE, mode == GameType.SPECTATOR);
            player.setPos(pos.x, pos.y, pos.z);
            var data = SinkCapability.get(player); data.lastTick = Long.MIN_VALUE;
            helper.assertTrue(SinkEngine.exempt(player), "mode must be exempt " + mode);
            SinkEngine.settle(helper.getLevel(), player);
            helper.assertTrue(!data.active() && data.air == 300, "mode does not trap or consume air " + mode);
            player.discard();
        }
        Pig pig = pig(helper, 8.5, 3.2, 8.5); pig.setInvulnerable(true);
        SinkEngine.settle(helper.getLevel(), pig);
        helper.assertTrue(!SinkCapability.get(pig).active(), "invulnerable mob exempt");
        pig.discard(); helper.succeed();
    }

    @GameTest(template = "pool_test")
    public static void nonFiniteVelocityNeverLeavesSolver(GameTestHelper helper) {
        pool(helper, MaterialProfile.SOFT_QUICKSAND);
        Pig pig = pig(helper, 8.5, 3.2, 8.5);
        pig.setDeltaMovement(Double.NaN, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
        SinkEngine.settle(helper.getLevel(), pig);
        var v = pig.getDeltaMovement();
        helper.assertTrue(Double.isFinite(v.x) && Double.isFinite(v.y) && Double.isFinite(v.z), "corrupt motion sanitized on real entity");
        pig.discard(); helper.succeed();
    }

    @GameTest(template = "pool_test")
    public static void playerCloneAndDimensionEventCleanup(GameTestHelper helper) {
        var original = playerFixture(helper, false, false);
        var next = playerFixture(helper, false, false);
        var old = SinkCapability.get(original);
        old.material = MaterialProfile.QUICKSAND; old.air = 0; old.stuck = 145;
        old.residueType = "quicksand"; old.residueTicks = 99;
        MinecraftForge.EVENT_BUS.post(new PlayerEvent.Clone(next, original, true));
        var clone = SinkCapability.get(next);
        helper.assertTrue(!clone.active() && clone.air == 300 && clone.residueTicks == 0, "death clone starts clean");
        clone.material = MaterialProfile.MUD; clone.air = 2; clone.stuck = 100;
        MinecraftForge.EVENT_BUS.post(new PlayerEvent.PlayerChangedDimensionEvent(next, Level.OVERWORLD, Level.NETHER));
        helper.assertTrue(!clone.active() && clone.stuck == 0 && clone.air == 300, "dimension event resets transient state");
        original.discard(); next.discard(); helper.succeed();
    }

    @GameTest(template = "pool_test")
    public static void invalidatedPlayerCapabilityCanReviveForDimensionTransfer(GameTestHelper helper) {
        pool(helper, MaterialProfile.QUICKSAND);
        var player = playerFixture(helper, false, false);
        var handle = player.getCapability(SinkCapability.CAP);
        var state = SinkCapability.get(player);
        state.material = MaterialProfile.QUICKSAND; state.air = 1; state.stuck = 145;
        state.residueType = "quicksand"; state.residueTicks = 80;
        player.invalidateCaps();
        helper.assertTrue(!handle.isPresent() && SinkCapability.get(player) == null, "invalid entity cannot expose old capability");
        player.reviveCaps();
        var revived = SinkCapability.get(player);
        helper.assertTrue(revived != null && !handle.isPresent(), "new valid handle after Forge revive, old handle stays invalid");
        helper.assertTrue(!revived.active() && revived.air == 300 && revived.residueTicks == 80, "only residue survives invalidation");
        var pos = helper.absoluteVec(new Vec3(8.5, 3.2, 8.5));
        player.setPos(pos.x, pos.y, pos.z);
        SinkEngine.settle(helper.getLevel(), player);
        helper.assertTrue(revived.active(), "player can sink again after revival");
        player.discard(); helper.succeed();
    }
}
