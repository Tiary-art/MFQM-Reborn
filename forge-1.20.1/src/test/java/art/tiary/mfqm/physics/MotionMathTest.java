package art.tiary.mfqm.physics;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class MotionMathTest {
    private final MotionMath.Policy p = new MotionMath.Policy(0.08, 0.055, 0.020);
    @Test void entryLimitsPenetrationButRetainsAirTravel() {
        for (double speed : new double[]{-0.01, -0.1, -1, -4, -100}) {
            double step = MotionMath.entryStep(65.01, 65, speed, p);
            assertTrue(65.01 + step >= 64.92 - 1e-9);
            assertTrue(step <= 0);
        }
        assertEquals(-3.08, MotionMath.entryStep(68, 65, -5, p), 1e-9);
    }
    @Test void materialDepthAndStruggleRemainDistinctAndBounded() {
        assertTrue(MotionMath.velocity(MaterialProfile.MUD, 0, false, false, p)
                > MotionMath.velocity(MaterialProfile.QUICKSAND, 0, false, false, p));
        assertTrue(MotionMath.velocity(MaterialProfile.QUICKSAND, 0, false, false, p)
                > MotionMath.velocity(MaterialProfile.SOFT_QUICKSAND, 0, false, false, p));
        for (var material : MaterialProfile.values()) for (double depth : new double[]{-1, 0, 0.01, 1, 3, 17, Double.NaN}) {
            double still = MotionMath.velocity(material, depth, false, false, p);
            double active = MotionMath.velocity(material, depth, true, true, p);
            assertTrue(Double.isFinite(active) && active >= -p.terminal() && active < 0);
            assertTrue(active <= still);
        }
    }
    @Test void latencyWindowIsBoundedAndDoesNotGrowWithoutLimit() {
        assertEquals(0.135, MotionMath.downwardBudget(1, p), 1e-9);
        assertEquals(0.30, MotionMath.downwardBudget(6, p), 1e-9);
        assertEquals(MotionMath.downwardBudget(4, p), MotionMath.downwardBudget(1000, p));
    }
    @Test void outsideFastFallPassengersAndUpwardMotionRetainLandingHistory() {
        assertTrue(MotionMath.controlledLanding(true, false, -0.03, p));
        assertFalse(MotionMath.controlledLanding(false, false, -0.03, p));
        assertFalse(MotionMath.controlledLanding(true, true, -0.03, p));
        assertFalse(MotionMath.controlledLanding(true, false, -1, p));
        assertFalse(MotionMath.controlledLanding(true, false, 0.42, p));
    }
    @Test void invalidPoliciesRejectedAndExtremeInputFinite() {
        assertThrows(IllegalArgumentException.class, () -> new MotionMath.Policy(0.08, Double.NaN, 0.02));
        assertThrows(IllegalArgumentException.class, () -> new MotionMath.Policy(2, 0.05, 0.02));
        assertEquals(0, MotionMath.entryStep(65, 65, Double.NEGATIVE_INFINITY, p));
    }
}
