package art.tiary.mfqm.physics;

import net.minecraft.core.*;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.util.RandomSource;
import net.minecraft.world.item.context.BlockPlaceContext;
import net.minecraft.world.level.*;
import net.minecraft.world.level.block.*;
import net.minecraft.world.level.block.state.*;
import net.minecraft.world.level.block.state.properties.BooleanProperty;
import net.minecraft.world.level.material.Fluids;

/** Evidence: BlockQuicksand 350ff / BlockSoftQuicksand updateTick; no FallingBlock entities. */
public final class CoreSinkingBlock extends SinkingBlock {
    public static final BooleanProperty FILLED = BooleanProperty.create("filled");
    public CoreSinkingBlock(MaterialProfile profile, BlockBehaviour.Properties properties) {
        super(profile, properties.randomTicks());
        registerDefaultState(stateDefinition.any().setValue(FILLED, false));
    }
    @Override protected void createBlockStateDefinition(StateDefinition.Builder<Block,BlockState> b) { b.add(FILLED); }
    private BlockState filled(BlockState s, BlockGetter l, BlockPos p) { return s.setValue(FILLED, l.getBlockState(p.above()).is(this)); }
    @Override public BlockState getStateForPlacement(BlockPlaceContext c) { return filled(defaultBlockState(),c.getLevel(),c.getClickedPos()); }
    @Override public BlockState updateShape(BlockState s, Direction d, BlockState n, LevelAccessor l, BlockPos p, BlockPos np) {
        return d == Direction.UP ? s.setValue(FILLED, n.is(this)) : s;
    }
    @Override public double surfaceHeight(BlockState s, BlockGetter l, BlockPos p) {
        return profile() == MaterialProfile.SOFT_QUICKSAND && s.getValue(FILLED) ? 1 : profile().surfaceHeight;
    }
    @Override public void randomTick(BlockState state, ServerLevel l, BlockPos p, RandomSource random) {
        // Legacy: liquids adjacent inhibit movement; lava hardens sand. Never load a new chunk.
        for (Direction d : Direction.values()) {
            BlockPos n=p.relative(d);
            if (!l.hasChunkAt(n)) return;
            var f=l.getFluidState(n);
            if (f.is(net.minecraft.tags.FluidTags.LAVA)) {
                var target=profile()==MaterialProfile.SOFT_QUICKSAND ? Blocks.SAND.defaultBlockState()
                    : art.tiary.mfqm.registry.ModBlocks.LEGACY.get("dry_quicksand").get().defaultBlockState();
                l.setBlockAndUpdate(p,target); return;
            }
            if (f.is(net.minecraft.tags.FluidTags.WATER)) return;
        }
        if (random.nextInt(profile()==MaterialProfile.SOFT_QUICKSAND ? 2 : 5)!=0) return;
        BlockPos below=p.below();
        if (below.getY()<l.getMinBuildHeight() || !l.hasChunkAt(below)) return;
        var destination=l.getBlockState(below);
        if (!destination.canBeReplaced() || !destination.getFluidState().isEmpty() || l.getBlockEntity(below)!=null
                || !destination.getCollisionShape(l,below).isEmpty()) return;
        // Main-thread atomic relocation: one cell, no entity, no duplication, same stable registry ID.
        l.setBlock(below,filled(state,l,below),3);
        l.removeBlock(p,false);
    }
}
