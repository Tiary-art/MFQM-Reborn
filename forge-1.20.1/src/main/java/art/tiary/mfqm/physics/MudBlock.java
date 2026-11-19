package art.tiary.mfqm.physics;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.IntegerProperty;
import net.minecraft.world.phys.shapes.CollisionContext;
import net.minecraft.world.phys.shapes.Shapes;
import net.minecraft.world.phys.shapes.VoxelShape;

public final class MudBlock extends SinkingBlock {
    public static final IntegerProperty DEPTH = IntegerProperty.create("depth", 0, 3);

    public MudBlock(BlockBehaviour.Properties properties) {
        super(MaterialProfile.MUD, properties);
        registerDefaultState(stateDefinition.any().setValue(DEPTH, 0));
    }

    @Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> builder) {
        builder.add(DEPTH);
    }

    public static MudGeometry.Grid grid(BlockGetter level, BlockPos origin) {
        return new MudGeometry.Grid() {
            @Override public MudGeometry.Cell cell(int x, int y, int z) {
                var pos = origin.offset(x, y, z);
                var state = level.getBlockState(pos);
                if (state.getBlock() instanceof MudBlock) return MudGeometry.Cell.MUD;
                if (!level.getFluidState(pos).isEmpty()) return MudGeometry.Cell.LIQUID;
                return state.isSolid() ? MudGeometry.Cell.SOLID : MudGeometry.Cell.OPEN;
            }
            @Override public int depthState(int x, int y, int z) {
                var state = level.getBlockState(origin.offset(x, y, z));
                return state.hasProperty(DEPTH) ? state.getValue(DEPTH) : 0;
            }
        };
    }

    @Override
    public VoxelShape getCollisionShape(BlockState state, BlockGetter level, BlockPos pos, CollisionContext context) {
        double height = MudGeometry.collisionHeight(grid(level, pos), state.getValue(DEPTH));
        return height == 0 ? Shapes.empty() : Block.box(0, 0, 0, 16, height * 16, 16);
    }
}
