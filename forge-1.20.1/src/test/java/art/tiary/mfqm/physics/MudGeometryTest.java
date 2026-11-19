package art.tiary.mfqm.physics;

import java.util.HashMap;
import java.util.Map;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

final class MudGeometryTest {
    private static final class Grid implements MudGeometry.Grid {
        final Map<String, MudGeometry.Cell> cells = new HashMap<>();
        int upperState;
        String key(int x, int y, int z) { return x + "/" + y + "/" + z; }
        void set(int x, int y, int z, MudGeometry.Cell value) { cells.put(key(x, y, z), value); }
        void square(int radius) { for (int x = -radius; x <= radius; x++) for (int z = -radius; z <= radius; z++) set(x, 0, z, MudGeometry.Cell.MUD); }
        @Override public MudGeometry.Cell cell(int x, int y, int z) { return cells.getOrDefault(key(x, y, z), MudGeometry.Cell.OPEN); }
        @Override public int depthState(int x, int y, int z) { return upperState; }
    }

    @Test void allEightNeighborsAndBothAxisRingsAreRequired() {
        var grid = new Grid();
        grid.square(1);
        assertEquals(1, MudGeometry.poolDepth(grid));
        grid.square(2);
        assertEquals(2, MudGeometry.poolDepth(grid));
        grid.square(3);
        assertEquals(3, MudGeometry.poolDepth(grid));
        for (int x = -1; x <= 1; x++) for (int z = -1; z <= 1; z++) if (x != 0 || z != 0) {
            grid.set(x, 0, z, MudGeometry.Cell.OPEN);
            assertEquals(0, MudGeometry.poolDepth(grid), "missing neighbor " + x + "," + z);
            grid.set(x, 0, z, MudGeometry.Cell.MUD);
        }
        for (int[] axis : new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}) {
            grid.set(axis[0] * 2, 0, axis[1] * 2, MudGeometry.Cell.OPEN);
            assertEquals(1, MudGeometry.poolDepth(grid));
            grid.set(axis[0] * 2, 0, axis[1] * 2, MudGeometry.Cell.MUD);
            grid.set(axis[0] * 3, 0, axis[1] * 3, MudGeometry.Cell.OPEN);
            assertEquals(2, MudGeometry.poolDepth(grid));
            grid.set(axis[0] * 3, 0, axis[1] * 3, MudGeometry.Cell.MUD);
        }
    }

    @Test void liquidAboveOverridesGeometryAndDisablesSafeEdge() {
        var grid = new Grid();
        grid.set(0, 1, 0, MudGeometry.Cell.LIQUID);
        assertEquals(3, MudGeometry.poolDepth(grid));
        assertFalse(MudGeometry.safeEdge(grid));
        grid.set(0, 1, 0, MudGeometry.Cell.MUD);
        grid.set(0, 2, 0, MudGeometry.Cell.LIQUID);
        assertEquals(3, MudGeometry.poolDepth(grid));
        assertFalse(MudGeometry.safeEdge(grid));
    }

    @Test void airEdgeDowngradesDepthButSolidBankDoesNot() {
        var grid = new Grid(); grid.square(3);
        grid.set(1, 0, 0, MudGeometry.Cell.OPEN);
        assertTrue(MudGeometry.safeEdge(grid));
        assertEquals(0, MudGeometry.effectiveDepth(grid, 3));
        grid.set(1, 0, 0, MudGeometry.Cell.SOLID);
        assertFalse(MudGeometry.safeEdge(grid));
        assertEquals(3, MudGeometry.effectiveDepth(grid, 3));
    }

    @Test void collisionHeightsAndStackedBranchMatchDiscreteEvidence() {
        var grid = new Grid();
        for (int[] axis : new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}})
            grid.set(axis[0], 0, axis[1], MudGeometry.Cell.SOLID);
        assertEquals(0.7, MudGeometry.collisionHeight(grid, 0), 1e-9);
        assertEquals(0.5, MudGeometry.collisionHeight(grid, 1), 1e-9);
        assertEquals(0.25, MudGeometry.collisionHeight(grid, 2), 1e-9);
        assertEquals(0, MudGeometry.collisionHeight(grid, 3));
        grid.set(0, 1, 0, MudGeometry.Cell.MUD);
        assertEquals(0.7, MudGeometry.collisionHeight(grid, 3), 1e-9);
        grid.upperState = 3;
        assertEquals(0, MudGeometry.collisionHeight(grid, 3));
    }
}
