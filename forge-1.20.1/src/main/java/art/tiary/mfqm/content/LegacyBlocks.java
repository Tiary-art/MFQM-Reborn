package art.tiary.mfqm.content;

import art.tiary.mfqm.physics.SinkingBlock;
import art.tiary.mfqm.registry.ModBlocks;
import java.util.ArrayDeque;
import java.util.HashSet;
import net.minecraft.core.BlockPos;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.LevelReader;
import net.minecraft.world.level.block.*;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.phys.Vec3;
import net.minecraft.world.phys.shapes.*;

/** Shared categories; special legacy dependencies remain explicitly PARTIAL in the catalog. */
public final class LegacyBlocks {
    private LegacyBlocks() { }
    public static Block create(LegacyCatalog.Spec s) {
        var p = BlockBehaviour.Properties.copy(Blocks.DIRT).strength(s.hardness()).lightLevel(state -> s.emission());
        if (s.drop().equals("EMPTY")) p.noLootTable();
        return switch (s.kind()) {
            case SINKING -> new MaterialBlock(s, p);
            case VISCOUS -> new LegacyFluids.MaterialLiquid(s,p);
            case TRAP -> new Trap(p);
            case SLAB -> new SlabBlock(p.noOcclusion());
            case PLANT -> new Plant(p.noCollission().noOcclusion().instabreak());
            case LILY -> new WaterlilyBlock(p.noOcclusion().instabreak());
            case LEAVES -> new Thin(p.noCollission().noOcclusion().instabreak(), s.height());
            case GAS -> new Thin(p.noCollission().noOcclusion().replaceable().instabreak(), 1);
            default -> new Solid(s, p);
        };
    }
    public static final class MaterialBlock extends SinkingBlock {
        private final LegacyCatalog.Spec spec;
        MaterialBlock(LegacyCatalog.Spec spec, BlockBehaviour.Properties p) { super(spec.profile(), p); this.spec = spec; }
        @Override public double motionScale() { return spec.motionScale(); }
        @Override public void entityInside(BlockState state, Level level, BlockPos pos, Entity entity) {
            if (!level.isClientSide && spec.damage() > 0 && entity instanceof LivingEntity living && living.tickCount % 20 == 0)
                living.hurt(level.damageSources().magic(), spec.damage());
        }
    }
    public static class Solid extends Block {
        private final LegacyCatalog.Spec spec;
        Solid(LegacyCatalog.Spec spec, BlockBehaviour.Properties p) { super(p); this.spec = spec; }
        @Override public VoxelShape getCollisionShape(BlockState s, BlockGetter l, BlockPos p, CollisionContext c) {
            return spec.id().equals("solid_honey") ? Block.box(.4, .4, .4, 15.6, 15.6, 15.6) : super.getCollisionShape(s,l,p,c);
        }
        @Override public void entityInside(BlockState s, Level l, BlockPos p, Entity e) {
            if (spec.id().equals("solid_honey")) e.makeStuckInBlock(s, new Vec3(.4,.7,.4));
        }
    }
    public static final class Thin extends Block {
        private final VoxelShape shape;
        Thin(BlockBehaviour.Properties p, double height) { super(p); shape=Block.box(0,0,0,16,height*16,16); }
        @Override public VoxelShape getShape(BlockState s, BlockGetter l, BlockPos p, CollisionContext c) { return shape; }
    }
    public static final class Plant extends BushBlock {
        Plant(BlockBehaviour.Properties p) { super(p); }
        @Override protected boolean mayPlaceOn(BlockState state, BlockGetter level, BlockPos pos) {
            return state.getBlock() instanceof art.tiary.mfqm.physics.SinkingMedium || super.mayPlaceOn(state,level,pos);
        }
    }
    /** Legacy horizontal powered conversion, bounded to64 cells instead of recursive world traversal. */
    public static final class Trap extends Block {
        Trap(BlockBehaviour.Properties p) { super(p); }
        @Override public void onPlace(BlockState s, Level l, BlockPos p, BlockState old, boolean moving) {
            if (old.getBlock()!=this) convert(l,p);
        }
        @Override public void neighborChanged(BlockState s, Level l, BlockPos p, Block b, BlockPos from, boolean moving) { convert(l,p); }
        private void convert(Level level, BlockPos pos) {
            if (level.isClientSide || !level.hasNeighborSignal(pos)) return;
            var queue=new ArrayDeque<BlockPos>(); var seen=new HashSet<BlockPos>(); queue.add(pos.immutable());
            while (!queue.isEmpty() && seen.size()<64) {
                var p=queue.remove(); if (!seen.add(p) || !level.hasChunkAt(p) || !level.getBlockState(p).is(this)) continue;
                level.setBlock(p, ModBlocks.QUICKSAND.get().defaultBlockState(), 2);
                queue.add(p.north());queue.add(p.south());queue.add(p.east());queue.add(p.west());
            }
        }
    }
}
