package art.tiary.mfqm.physics;

import java.util.Random;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.EnumSource;
import static org.junit.jupiter.api.Assertions.*;

final class SinkMathTest {
    @ParameterizedTest @EnumSource(MaterialProfile.class)
    void finiteAndBoundedEvenForCorruptInputs(MaterialProfile profile) {
        for (double bad : new double[]{Double.NaN, Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, -1e300, 1e300}) {
            var result = SinkMath.solve(profile, new SinkMath.Motion(bad, bad, bad), bad, bad, bad, bad, true, true, false);
            assertTrue(Double.isFinite(result.motion().x()));
            assertTrue(Double.isFinite(result.motion().y()));
            assertTrue(Double.isFinite(result.motion().z()));
            assertTrue(Math.abs(result.motion().x()) <= 0.25);
            assertTrue(result.motion().y() >= -0.25 && result.motion().y() <= 0.08);
            assertTrue(result.speedFactor() >= 0.02 && result.speedFactor() <= 1);
        }
    }

    @ParameterizedTest @EnumSource(MaterialProfile.class)
    void deeperMotionHasLessSupportAndMoreStuck(MaterialProfile profile) {
        var shallow = SinkMath.solve(profile, new SinkMath.Motion(0, 0, 0), 0.1, 0.1, 0, 0, false, false, false);
        var deep = SinkMath.solve(profile, new SinkMath.Motion(0, 0, 0), 0.9, 1.7, 0, 0, false, false, false);
        assertTrue(deep.motion().y() < shallow.motion().y());
        assertTrue(deep.stuck() > shallow.stuck());
        assertTrue(deep.speedFactor() < shallow.speedFactor());
    }

    @ParameterizedTest @EnumSource(MaterialProfile.class)
    void movementAndStruggleHaveDistinctSuction(MaterialProfile profile) {
        var input = new SinkMath.Motion(0.04, 0, 0);
        var still = SinkMath.solve(profile, input, 0.4, 0.7, 0, 0, false, false, false);
        var moving = SinkMath.solve(profile, input, 0.4, 0.7, 0, 0, true, false, false);
        var struggling = SinkMath.solve(profile, input, 0.4, 0.7, 0, 0, true, true, false);
        assertTrue(moving.motion().y() < still.motion().y());
        assertTrue(struggling.motion().y() < moving.motion().y());
    }

    @Test void quicksandClearsHorizontalMomentumButSoftSandRetainsSurfaceMotion() {
        var input = new SinkMath.Motion(0.1, 0, -0.1);
        var quick = SinkMath.solve(MaterialProfile.QUICKSAND, input, 0.2, 0.3, 0, 0, false, false, false);
        var soft = SinkMath.solve(MaterialProfile.SOFT_QUICKSAND, input, 0.2, 0.3, 0, 0, false, false, false);
        assertEquals(0, quick.motion().x());
        assertEquals(0.071, soft.motion().x(), 1e-9);
    }

    @Test void deepSoftSandPullsTowardCellCenterOnlyWithinTheRecoveredAnnulus() {
        var input = new SinkMath.Motion(0.1, 0, 0.1);
        var pull = SinkMath.solve(MaterialProfile.SOFT_QUICKSAND, input, 0.8, 1.4, 0.3, -0.2, false, false, false);
        assertTrue(pull.motion().x() > 0 && pull.motion().z() < 0);
        var center = SinkMath.solve(MaterialProfile.SOFT_QUICKSAND, input, 0.8, 1.4, 0.01, 0.01, false, false, false);
        var outside = SinkMath.solve(MaterialProfile.SOFT_QUICKSAND, input, 0.8, 1.4, 0.6, 0, false, false, false);
        assertEquals(0, center.motion().x());
        assertEquals(0, outside.motion().x());
    }

    @Test void mudDampsFastFallsMoreStronglyAndGroundedHorizontalMotionSeparately() {
        var input = new SinkMath.Motion(0.1, -0.4, 0);
        var mud = SinkMath.solve(MaterialProfile.MUD, input, 0.2, 0.3, 0, 0, false, false, true);
        var quick = SinkMath.solve(MaterialProfile.QUICKSAND, input, 0.2, 0.3, 0, 0, false, false, false);
        assertEquals(0.0071, mud.motion().x(), 1e-9);
        assertTrue(mud.motion().y() > quick.motion().y());
    }

    @Test void deterministicPropertySweepCannotProduceNonFiniteMotion() {
        Random random = new Random(3003);
        for (var profile : MaterialProfile.values()) for (int i = 0; i < 2000; i++) {
            var result = SinkMath.solve(profile, new SinkMath.Motion(random.nextGaussian(), random.nextGaussian(), random.nextGaussian()),
                    random.nextDouble() * 2, random.nextDouble() * 5, random.nextGaussian(), random.nextGaussian(),
                    random.nextBoolean(), random.nextBoolean(), random.nextBoolean());
            assertTrue(Double.isFinite(result.motion().x() + result.motion().y() + result.motion().z()));
            assertTrue(result.stuck() >= 5 && result.stuck() <= profile.maxStuck);
        }
    }

    @Test void clientPositionBatchesCannotBypassServerMotionBudget() {
        var limited = SinkMath.limitPlayerStep(new SinkMath.Motion(2, -1.4, 2), -0.005, 0.1, false);
        assertTrue(Math.hypot(limited.x(), limited.z()) <= 0.13 + 1e-9);
        assertEquals(-0.015, limited.y(), 1e-9);
        assertEquals(0.05, SinkMath.limitPlayerStep(new SinkMath.Motion(0, 0.42, 0), 0, 0.1, false).y(), 1e-9);
        assertEquals(0.42, SinkMath.limitPlayerStep(new SinkMath.Motion(0, 0.42, 0), 0, 0.1, true).y(), 1e-9);
        var corrupt = SinkMath.limitPlayerStep(new SinkMath.Motion(Double.NaN, Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY),
                Double.NaN, Double.NaN, false);
        assertTrue(Double.isFinite(corrupt.x() + corrupt.y() + corrupt.z()));
    }
}
