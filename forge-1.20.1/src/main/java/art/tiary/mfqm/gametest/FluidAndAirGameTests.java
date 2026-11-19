package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.content.LegacyFluids;
import art.tiary.mfqm.physics.*;
import art.tiary.mfqm.registry.ModBlocks;
import art.tiary.mfqm.state.SinkCapability;
import net.minecraft.core.BlockPos;
import net.minecraft.gametest.framework.*;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.item.BucketItem;
import net.minecraft.world.level.ClipContext;
import net.minecraft.world.level.block.*;
import net.minecraft.world.phys.*;
import net.minecraftforge.gametest.*;

@GameTestHolder(MfqmReborn.MOD_ID)
@PrefixGameTestTemplate(false)
public final class FluidAndAirGameTests {
    @GameTest(template="pool_test") public static void allThirteenNativeFluidBucketsPlaceAndPickUp(GameTestHelper h) {
        h.assertTrue(LegacyFluids.ALL.size()==13,"all thirteen fluid families");int i=0;
        for(var f:LegacyFluids.ALL.values()) {
            var p=h.absolutePos(new BlockPos(2+(i%4)*3,3,2+(i/4)*3));i++;
            h.getLevel().setBlockAndUpdate(p.below(),Blocks.STONE.defaultBlockState());
            h.getLevel().setBlockAndUpdate(p,Blocks.AIR.defaultBlockState());
            h.assertTrue(((BucketItem)f.bucket().get()).emptyContents(null,h.getLevel(),p,null),"bucket placement "+f.spec().id());
            var s=h.getLevel().getBlockState(p);
            h.assertTrue(s.is(ModBlocks.LEGACY.get(f.spec().id()).get()) && s.getFluidState().isSource(),"real source cell "+f.spec().id());
            h.assertTrue(s.getFluidState().getType().getFluidType()==f.type().get(),"real Forge FluidType");
            var pickup=((BucketPickup)s.getBlock()).pickupBlock(h.getLevel(),p,s);
            h.assertTrue(pickup.is(f.bucket().get()) && h.getLevel().getFluidState(p).isEmpty(),"pickup source exactly once");
        }h.succeed();
    }
    @GameTest(template="pool_test") public static void coreAirUsesNativeSupplyAndOneSettlement(GameTestHelper h) {
        CoreMaterialGameTests.pool(h,MaterialProfile.QUICKSAND);
        var pig=h.spawnWithNoFreeWill(EntityType.PIG,new Vec3(8.5,2,8.5));
        var d=SinkCapability.get(pig); d.air=10; pig.setAirSupply(7);
        SinkEngine.settle(h.getLevel(),pig);
        h.assertTrue(d.eyeCovered && d.air==6 && pig.getAirSupply()==6,"one shared air supply takes lower incoming water budget");
        SinkEngine.settle(h.getLevel(),pig);
        h.assertTrue(d.air==6 && pig.getAirSupply()==6,"duplicate callback cannot consume twice");
        pig.discard();h.succeed();
    }
    @GameTest(template="pool_test") public static void insideRaySkipsOnlyEnclosingCellAndStopsAtWall(GameTestHelper h) {
        h.setBlock(5,2,5,ModBlocks.QUICKSAND.get());h.setBlock(7,2,5,Blocks.STONE);
        var pig=h.spawnWithNoFreeWill(EntityType.PIG,new Vec3(5.5,2,5.5));
        Vec3 eye=pig.getEyePosition();
        var result=h.getLevel().clip(new ClipContext(eye,eye.add(5,0,0),ClipContext.Block.OUTLINE,ClipContext.Fluid.NONE,pig));
        h.assertTrue(result.getBlockPos().equals(h.absolutePos(new BlockPos(7,2,5))),"solid wall remains the first valid target");
        pig.discard();h.succeed();
    }
    @GameTest(template="pool_test",timeoutTicks=50) public static void exemptEntityStillWashesCosmeticResidue(GameTestHelper h) {
        h.setBlock(4,1,4,Blocks.STONE);h.setBlock(4,2,4,Blocks.WATER);h.setBlock(4,3,4,Blocks.WATER);
        var pig=h.spawnWithNoFreeWill(EntityType.PIG,new Vec3(4.5,2,4.5));pig.setInvulnerable(true);
        var d=SinkCapability.get(pig);d.residueType="mud";d.residueTicks=1000;
        h.runAfterDelay(5,()->{h.assertTrue(d.residueTicks<=800,"creative-like immunity must not bypass washing");pig.discard();h.succeed();});
    }

}
