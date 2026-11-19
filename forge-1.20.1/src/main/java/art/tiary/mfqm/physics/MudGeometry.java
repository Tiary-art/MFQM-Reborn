package art.tiary.mfqm.physics;

/** Discrete geometry recovered from BlockMud.getMudDepth/getMudSafe/collision AABB. */
public final class MudGeometry {
    public enum Cell { MUD, LIQUID, SOLID, OPEN }
    public interface Grid {
        Cell cell(int x, int y, int z);
        int depthState(int x, int y, int z);
    }
    private static final int[][] AXES = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    private MudGeometry() { }

    public static boolean liquidAbove(Grid grid) {
        return grid.cell(0, 1, 0) == Cell.LIQUID
                || grid.cell(0, 1, 0) == Cell.MUD && grid.cell(0, 2, 0) == Cell.LIQUID;
    }

    public static int poolDepth(Grid grid) {
        if (liquidAbove(grid)) return 3;
        for (int x = -1; x <= 1; x++) for (int z = -1; z <= 1; z++) {
            if ((x != 0 || z != 0) && grid.cell(x, 0, z) != Cell.MUD) return 0;
        }
        for (var axis : AXES) if (grid.cell(axis[0] * 2, 0, axis[1] * 2) != Cell.MUD) return 1;
        for (var axis : AXES) if (grid.cell(axis[0] * 3, 0, axis[1] * 3) != Cell.MUD) return 2;
        return 3;
    }

    public static boolean safeEdge(Grid grid) {
        if (liquidAbove(grid)) return false;
        for (var axis : AXES) if (grid.cell(axis[0], 0, axis[1]) == Cell.OPEN) return true;
        return false;
    }

    public static int effectiveDepth(Grid grid, int stateDepth) {
        int depth = Math.max(Math.max(0, Math.min(3, stateDepth)), poolDepth(grid));
        return depth > 0 && safeEdge(grid) ? 0 : depth;
    }

    public static double collisionHeight(Grid grid, int stateDepth) {
        int depth = effectiveDepth(grid, stateDepth);
        if (depth > 0 && (grid.cell(0, 1, 0) != Cell.MUD || grid.depthState(0, 1, 0) > 2)) {
            return switch (depth) { case 1 -> 0.5; case 2 -> 0.25; default -> 0; };
        }
        return 0.7;
    }
}
