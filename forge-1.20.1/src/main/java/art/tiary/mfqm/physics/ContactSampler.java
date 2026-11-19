package art.tiary.mfqm.physics;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.Level;
import net.minecraft.util.Mth;
import net.minecraft.world.entity.LivingEntity;

public final class ContactSampler {
    public record Contact(MaterialProfile material, double surface, double immersion, double depthBlocks,
                          double centerX, double centerZ, boolean eyes, int cells, int mudDepth, double motionScale) {
        public Contact(MaterialProfile m,double s,double i,double d,double x,double z,boolean e,int c,int md) {
            this(m,s,i,d,x,z,e,c,md,1);
        }
    }
    private ContactSampler() { }

    /** Bounded downward sweep of the feet footprint; no chunk loads or collision edits. */
    public static Contact entry(Level level, LivingEntity entity, double fromY, double toY) {
        if (!Double.isFinite(fromY) || !Double.isFinite(toY) || toY >= fromY || fromY - toY > 16) return null;
        var box = entity.getBoundingBox();
        Contact best = null;
        for (int x = Mth.floor(Math.max(box.minX + 1e-6, entity.getX() - 4)); x <= Mth.floor(box.maxX - 1e-6) && x < entity.getX() + 5; x++)
            for (int z = Mth.floor(Math.max(box.minZ + 1e-6, entity.getZ() - 4)); z <= Mth.floor(box.maxZ - 1e-6) && z < entity.getZ() + 5; z++)
                for (int y = Mth.floor(fromY); y >= Mth.floor(toY) - 1; y--) {
                    var pos = new BlockPos(x, y, z);
                    if (!level.hasChunkAt(pos) || !(level.getBlockState(pos).getBlock() instanceof SinkingMedium b)) continue;
                    if (level.getBlockState(pos.above()).getBlock() == b) continue;
                    double surface = y + b.surfaceHeight(level.getBlockState(pos),level,pos);
                    if (fromY < surface - 0.05 || toY > surface + 0.05) continue;
                    if (best == null || surface > best.surface()) best = new Contact(b.profile(), surface, 0, 0,
                            x + 0.5 - entity.getX(), z + 0.5 - entity.getZ(), false, 1,
                            b instanceof MudBlock ? MudGeometry.effectiveDepth(MudBlock.grid(level, pos), level.getBlockState(pos).getValue(MudBlock.DEPTH)) : 0, b.motionScale());
                }
        return best;
    }

    public static Contact sample(Level level, LivingEntity entity) {
        var box = entity.getBoundingBox();
        MaterialProfile selected = null;
        double best = -1, surface = 0, cx = 0, cz = 0, scale = 1;
        int cells = 0, mudDepth = 0;
        // Bound atypically large entities; no chunk loads and no unbounded scans.
        int minX = Mth.floor(Math.max(box.minX + 1.0e-6, entity.getX() - 4));
        int maxX = Mth.floor(Math.min(box.maxX - 1.0e-6, entity.getX() + 4));
        int minZ = Mth.floor(Math.max(box.minZ + 1.0e-6, entity.getZ() - 4));
        int maxZ = Mth.floor(Math.min(box.maxZ - 1.0e-6, entity.getZ() + 4));
        int minY = Mth.floor(entity.getY() - 0.05);
        int maxY = Mth.floor(Math.min(box.maxY - 1.0e-6, entity.getY() + 4));
        for (int x = minX; x <= maxX; x++) for (int z = minZ; z <= maxZ; z++) {
            for (int y = maxY; y >= minY; y--) {
                BlockPos pos = new BlockPos(x, y, z);
                if (!level.hasChunkAt(pos)) continue;
                var state = level.getBlockState(pos);
                if (!(state.getBlock() instanceof SinkingMedium block)) continue;
                MaterialProfile profile = block.profile();
                double localSurface = y + profile.surfaceHeight;
                // Interior soft-sand cells fill to the cell above; only the top surface is 0.85.
                BlockPos top = pos;
                for (int step = 0; step < 16; step++) {
                    var above = top.above();
                    if (!level.hasChunkAt(above) || level.getBlockState(above).getBlock() != block) break;
                    top = above;
                }
                localSurface = top.getY() + block.surfaceHeight(level.getBlockState(top),level,top);
                if (entity.getY() > localSurface + 0.05 || box.maxY <= y) continue;
                cells++;
                double overlap = Math.min(box.maxX, x + 1) - Math.max(box.minX, x);
                overlap *= Math.min(box.maxZ, z + 1) - Math.max(box.minZ, z);
                double score = overlap * Math.min(entity.getBbHeight(), Math.max(0, localSurface - entity.getY()));
                if (score > best + 1.0e-9 || Math.abs(score - best) < 1.0e-9
                        && (selected == null || profile.priority > selected.priority)) {
                    selected = profile; scale = block.motionScale();
                    best = score;
                    surface = localSurface;
                    cx = x + 0.5;
                    cz = z + 0.5;
                    mudDepth = block instanceof MudBlock
                            ? MudGeometry.effectiveDepth(MudBlock.grid(level, pos), state.getValue(MudBlock.DEPTH)) : 0;
                }
            }
        }
        BlockPos eye = BlockPos.containing(entity.getEyePosition());
        var eyeState = level.getBlockState(eye);
        boolean covered = false;
        if (eyeState.getBlock() instanceof SinkingMedium eyeBlock) {
            double eyeSurface = eye.getY() + eyeBlock.surfaceHeight(eyeState,level,eye);
            if (level.getBlockState(eye.above()).getBlock() == eyeBlock) eyeSurface = eye.getY() + 1;
            covered = entity.getEyeY() < eyeSurface;
        }
        double depth = selected == null ? 0 : Math.max(0, surface - entity.getY());
        return new Contact(selected, surface, SinkMath.clamp(depth / Math.max(entity.getBbHeight(), 0.01), 0, 1),
                depth, cx - entity.getX(), cz - entity.getZ(), covered, cells, mudDepth, scale);
    }
}
