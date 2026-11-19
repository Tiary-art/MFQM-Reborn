package art.tiary.mfqm.integration;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.legacy.QuicksandContacts;
import art.tiary.mfqm.physics.SinkConfig;
import art.tiary.mfqm.registry.ModBlocks;
import net.minecraft.core.BlockPos;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.state.BlockState;

/** Preserve actual callback arrival order. Never use overlap score/max/dedup. */
public final class OriginalContactBridge {
    private OriginalContactBridge() { }
    public static void inside(BlockState state, Level level, BlockPos pos, Entity entity) {
        if (level.isClientSide || !SinkConfig.ORIGINAL_CONTACTS.get() || !StuckAdapter.enabled()
                || !(entity instanceof LivingEntity living) || entity instanceof Player
                || state.getBlock() != ModBlocks.QUICKSAND.get()) return;
        if (art.tiary.mfqm.physics.SinkEngine.exempt(living) || living.isPassenger()) return;
        if (!admittedVolume(level, living)) { StuckAdapter.cancelAutomatic(living); return; }
        // Players require the old posY/yOffset + side-authority mapping; keep BLOCKED.
        // The legacy SandBlob/WLD special entity/dimension do not exist in this runtime.
        if (!level.hasChunkAt(pos.above()) || !level.hasChunkAt(pos.above(2))) return;
        boolean a = level.getBlockState(pos.above()).getBlock() == state.getBlock();
        boolean b = a && level.getBlockState(pos.above(2)).getBlock() == state.getBlock();
        QuicksandContacts.emit(living.getY(), pos.getY(), a, b, true, value -> {
            if (SinkConfig.PHASE7_DIAGNOSTICS.get()) MfqmReborn.LOGGER.info(
                    "PHASE8_AUTO entity={} tick={} material=quicksand pos={} entityY={} km={} metadata=not-used above={} twoAbove={} rng=contact-projection-independent level={}",
                    living.getUUID(), level.getGameTime(), pos.toShortString(), living.getY(), Math.max(living.getY() - pos.getY() + .5, 0), a, b, value);
            StuckAdapter.automaticContact(living, value);
        });
    }
    private static boolean admittedVolume(Level level, LivingEntity entity) {
        var b = entity.getBoundingBox();
        if (!Double.isFinite(entity.getX()) || !Double.isFinite(entity.getY()) || !Double.isFinite(entity.getZ())
                || !Float.isFinite(entity.getBbWidth()) || !Float.isFinite(entity.getBbHeight())
                || entity.getBbWidth() > 4 || entity.getBbHeight() > 4) return false;
        for (int x=net.minecraft.util.Mth.floor(b.minX+.001);x<=net.minecraft.util.Mth.floor(b.maxX-.001);x++)
            for (int y=net.minecraft.util.Mth.floor(b.minY+.001);y<=net.minecraft.util.Mth.floor(b.maxY-.001);y++)
                for (int z=net.minecraft.util.Mth.floor(b.minZ+.001);z<=net.minecraft.util.Mth.floor(b.maxZ-.001);z++) {
                    var p=new BlockPos(x,y,z);
                    if (!level.hasChunkAt(p)) return false;
                    var block=level.getBlockState(p).getBlock();
                    if (block instanceof art.tiary.mfqm.physics.SinkingMedium && block!=ModBlocks.QUICKSAND.get()) return false;
                }
        return true;
    }
}
