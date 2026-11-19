package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.*;
import art.tiary.mfqm.registry.ModBlocks;
import net.minecraft.core.BlockPos;
import net.minecraft.gametest.framework.*;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.vehicle.Boat;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.gametest.*;

@GameTestHolder(MfqmReborn.MOD_ID)
@PrefixGameTestTemplate(false)
public final class CompatibilityGameTests {
    @GameTest(template="pool_test") public static void softStackOutlineMatchesSurfaceAndHasNoCollision(GameTestHelper h) {
        var b=ModBlocks.SOFT_QUICKSAND.get();
        h.setBlock(5,2,5,b);h.setBlock(5,3,5,b);
        var lower=h.absolutePos(new BlockPos(5,2,5));var upper=lower.above();var l=h.getLevel();
        h.assertTrue(l.getBlockState(lower).getShape(l,lower).max(net.minecraft.core.Direction.Axis.Y)==1,"lower outline fills cell");
        h.assertTrue(Math.abs(l.getBlockState(upper).getShape(l,upper).max(net.minecraft.core.Direction.Axis.Y)-.85)<.00001,"top outline .85");
        h.assertTrue(l.getBlockState(lower).getCollisionShape(l,lower).isEmpty(),"outline is not solid collision");
        h.destroyBlock(new BlockPos(5,3,5));
        h.assertTrue(Math.abs(l.getBlockState(lower).getShape(l,lower).max(net.minecraft.core.Direction.Axis.Y)-.85)<.00001,"remove upper restores top");h.succeed();
    }
    @GameTest(template="pool_test",timeoutTicks=110) public static void boatsAndChestBoatsFloatAcrossAllCoreMaterials(GameTestHelper h) {
        Boat[] boats=new Boat[6];double[] surfaces=new double[6];
        for(int i=0;i<6;i++) {
            var block=new net.minecraft.world.level.block.Block[]{ModBlocks.QUICKSAND.get(),ModBlocks.SOFT_QUICKSAND.get(),ModBlocks.MUD.get()}[i%3];
            int x=3+(i%3)*5,z=i<3?4:11;
            for(int dx=-1;dx<=1;dx++)for(int dz=-1;dz<=1;dz++){
                h.setBlock(x+dx,1,z+dz,Blocks.STONE);for(int y=2;y<=4;y++)h.setBlock(x+dx,y,z+dz,block);
            }
            var type=i<3?EntityType.BOAT:EntityType.CHEST_BOAT;
            boats[i]=h.spawn(type,new Vec3(x+.5,5.1,z+.5));
            surfaces[i]=h.absolutePos(new BlockPos(x,4,z)).getY()+((SinkingBlock)block).profile().surfaceHeight;
        }
        h.runAfterDelay(80,()->{
            for(int i=0;i<6;i++){
                h.assertTrue(boats[i].isAlive(),"boat survives");
                double depth=surfaces[i]-boats[i].getY();
                h.assertTrue(depth>.15 && depth<.6,"hull floats near surface for material "+i+", depth="+depth);
                h.assertTrue(Math.abs(boats[i].getDeltaMovement().y)<.06,"settled vertical velocity");boats[i].discard();
            }h.succeed();
        });
    }
    @GameTest(template="pool_test") public static void conditionalDownmovePreservesOneCellAndMudDoesNotFall(GameTestHelper h) {
        var l=h.getLevel();var q=ModBlocks.QUICKSAND.get();var p=h.absolutePos(new BlockPos(4,5,4));
        h.setBlock(4,3,4,Blocks.STONE);h.setBlock(4,4,4,Blocks.AIR);h.setBlock(4,5,4,q);
        for(int i=0;i<100 && l.getBlockState(p).is(q);i++) q.randomTick(l.getBlockState(p),l,p,net.minecraft.util.RandomSource.create(i));
        h.assertTrue(l.getBlockState(p).isAir() && l.getBlockState(p.below()).is(q),"one-cell move without duplication");
        h.setBlock(7,5,4,ModBlocks.MUD.get());
        var m=h.absolutePos(new BlockPos(7,5,4));ModBlocks.MUD.get().randomTick(l.getBlockState(m),l,m,l.random);
        h.assertTrue(l.getBlockState(m).is(ModBlocks.MUD.get()),"mud is not a falling block");h.succeed();
    }
}
