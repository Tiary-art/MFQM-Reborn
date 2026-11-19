package art.tiary.mfqm.legacy;

/** Original generateSoftSand transaction order; no worldgen registration or world callbacks. */
public final class DryQuicksandCore {
    private DryQuicksandCore() { }
    public static void generateDry(int x, int y, int z, int extent, VoxelPort world, LegacyRandom rng) {
        double cof = Math.max((double) extent / 10, 1);
        double a = rng.nextDouble() + 0.5;
        double b = ((1 - a) + 0.5) + 0.5;
        for (int i = 0; i <= extent; i++) {
            for (int j = 0; j <= extent; j++) {
                for (int e = 0; e <= extent; e++) {
                    int px = x + i - extent / 2, py = y - j, pz = z + e - extent / 2;
                    double dis = Math.sqrt(Math.pow(x - px, 2) * a + Math.pow(y - py, 2)
                            + Math.pow(z - pz, 2) * b);
                    double threshold = ((double) extent / 2) / (1 + Math.abs(a - b) / 3)
                            + (rng.nextDouble() * cof - cof / 2);
                    if (dis < threshold) {
                        world.write(px, py, pz, LegacyBlock.DRY_QUICKSAND, 0, 3);
                        world.write(px, py - 1, pz, LegacyBlock.DRY_QUICKSAND, 0, 3);
                        world.write(px, py - 2, pz, LegacyBlock.SANDSTONE, 0, 3);
                    }
                }
            }
        }
        if (extent > 4 && (extent < 10 || rng.nextInt(2 + extent / 2) == 0)) {
            for (int i = 0; i <= extent; i++) {
                for (int j = 0; j <= extent + 1; j++) {
                    for (int e = 0; e <= extent; e++) {
                        int px = x + i - extent / 2, py = y - j, pz = z + e - extent / 2;
                        if (j < extent / 3 && world.blockAt(px, py, pz) == LegacyBlock.DRY_QUICKSAND
                                && open(world, px - 1, py, pz)
                                && open(world, px + 1, py, pz)
                                && open(world, px, py, pz + 1)
                                && open(world, px, py, pz - 1)
                                && open(world, px, py - 1, pz)) {
                            world.write(px, py, pz, LegacyBlock.AIR, 0, 3);
                        }
                    }
                }
            }
        }
    }
    private static boolean open(VoxelPort world, int x, int y, int z) {
        // Preserve the second getBlock when the first result is not AIR.
        return world.blockAt(x, y, z) == LegacyBlock.AIR
                || world.blockAt(x, y, z) == LegacyBlock.DRY_QUICKSAND;
    }
}
