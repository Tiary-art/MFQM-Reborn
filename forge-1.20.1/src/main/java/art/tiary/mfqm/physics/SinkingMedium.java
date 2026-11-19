package art.tiary.mfqm.physics;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.BlockGetter;
import net.minecraft.world.level.block.state.BlockState;

/** Shared material contact for granular blocks and true Forge liquids. */
public interface SinkingMedium {
    MaterialProfile profile();
    double motionScale();
    double surfaceHeight(BlockState state,BlockGetter level,BlockPos pos);
}
