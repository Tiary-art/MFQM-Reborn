package art.tiary.mfqm.integration;

import art.tiary.mfqm.legacy.*;
import art.tiary.mfqm.registry.ModBlocks;
import java.util.Random;
import java.util.function.Consumer;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.level.block.Blocks;

/** Synchronous loaded-chunk-only port. Event trace is API activity, not all neighbor side effects. */
public final class DryWorldAdapter implements VoxelPort {
    private final ServerLevel level;
    private final Consumer<String> trace;
    public DryWorldAdapter(ServerLevel level, Consumer<String> trace) { this.level = level; this.trace = trace; }
    public LegacyBlock blockAt(int x, int y, int z) {
        BlockPos pos = new BlockPos(x, y, z);
        if (!level.hasChunkAt(pos)) throw new IllegalStateException("Unloaded read: " + pos);
        var block = level.getBlockState(pos).getBlock();
        LegacyBlock b = block == ModBlocks.LEGACY.get("dry_quicksand").get() ? LegacyBlock.DRY_QUICKSAND
                : block == Blocks.SANDSTONE ? LegacyBlock.SANDSTONE
                : block == Blocks.AIR || block == Blocks.CAVE_AIR || block == Blocks.VOID_AIR ? LegacyBlock.AIR
                : block == Blocks.SAND ? LegacyBlock.SAND
                : block == Blocks.STONE ? LegacyBlock.STONE
                : block == ModBlocks.SOFT_QUICKSAND.get() ? LegacyBlock.SOFT_QUICKSAND : LegacyBlock.OTHER;
        trace.accept("Q\t" + x + "\t" + y + "\t" + z + "\t" + b);
        return b;
    }
    public boolean write(int x, int y, int z, LegacyBlock b, int metadata, int flags) {
        if (metadata != 0 || flags != 3) throw new IllegalArgumentException("Unsupported legacy state/flags");
        BlockPos pos = new BlockPos(x, y, z);
        var block = switch (b) {
            case DRY_QUICKSAND -> ModBlocks.LEGACY.get("dry_quicksand").get();
            case SANDSTONE -> Blocks.SANDSTONE;
            case AIR -> Blocks.AIR;
            default -> throw new IllegalArgumentException("Unsupported write identity: " + b);
        };
        boolean applied = level.hasChunkAt(pos) && !level.isOutsideBuildHeight(pos)
                && level.setBlock(pos, block.defaultBlockState(), flags);
        trace.accept("W\t" + x + "\t" + y + "\t" + z + "\t" + b + "\t" + metadata + "\t" + flags + "\t" + applied);
        return applied;
    }
    public static LegacyRandom random(long seed, Consumer<String> trace) {
        Random rng = new Random(seed);
        return new LegacyRandom() {
            public int nextInt(int bound) { int v = rng.nextInt(bound); trace.accept("R\tnextInt\t" + bound + "\t" + v); return v; }
            public double nextDouble() { double v = rng.nextDouble(); trace.accept("R\tnextDouble\t-\t" + v); return v; }
        };
    }
    public static void generate(ServerLevel level, BlockPos origin, int extent, long seed, Consumer<String> trace) {
        if (extent < -1 || extent > 18) throw new IllegalArgumentException("Test extent must be -1..18");
        // Preflight complete read/write volume; never force-load chunks or partially start an unloaded transaction.
        int half = extent / 2;
        for (int x = origin.getX() - half - 1; x <= origin.getX() + extent - half + 1; x++)
            for (int z = origin.getZ() - half - 1; z <= origin.getZ() + extent - half + 1; z++) {
                if (!level.hasChunkAt(new BlockPos(x, origin.getY(), z))) throw new IllegalStateException("Unloaded test volume");
            }
        if (origin.getY() - Math.max(extent, 0) - 2 < level.getMinBuildHeight()
                || origin.getY() >= level.getMaxBuildHeight()) throw new IllegalArgumentException("Outside test build height");
        DryQuicksandCore.generateDry(origin.getX(), origin.getY(), origin.getZ(), extent,
                new DryWorldAdapter(level, trace), random(seed, trace));
    }
}
