package art.tiary.mfqm.physics;

/** Pure solver: no game tick side effects, no client state, and no legacy Y-coordinate assumptions. */
public final class SinkMath {
    public record Motion(double x, double y, double z) { }
    public record Result(Motion motion, int stuck, double speedFactor) { }

    private SinkMath() { }

    public static double finite(double value, double fallback) {
        return Double.isFinite(value) ? value : fallback;
    }

    public static double clamp(double value, double min, double max) {
        return Math.max(min, Math.min(max, finite(value, min)));
    }

    /** Bound client-reported displacement against the last server decision, not client velocity.
     * Vanilla clients integrate gravity between motion packets; position batches can arrive late. */
    public static Motion limitPlayerStep(Motion step, double lastVertical, double movementSpeed, boolean shallowMud) {
        double x = finite(step.x(), 0), z = finite(step.z(), 0);
        double distance = Math.hypot(x, z);
        double horizontal = Math.max(0.02, clamp(movementSpeed, 0, 2) * 1.3);
        if (distance > horizontal) { x *= horizontal / distance; z *= horizontal / distance; }
        double fall = Math.max(0.015, Math.min(0.35, Math.abs(finite(lastVertical, 0)) * 1.5 + 0.003));
        return new Motion(x, clamp(step.y(), -fall, shallowMud ? 0.5 : 0.05), z);
    }

    public static Result solve(MaterialProfile profile, Motion input, double immersion, double depthBlocks,
                               double centerX, double centerZ, boolean moving, boolean struggle, boolean grounded) {
        double d = clamp(immersion, 0, 1);
        double blocks = clamp(depthBlocks, 0, 4);
        double x = clamp(input.x(), -2, 2);
        double y = clamp(input.y(), -4, 4);
        double z = clamp(input.z(), -2, 2);
        double movementPenalty = moving ? 1 + Math.hypot(x, z) * (profile == MaterialProfile.MUD ? 5 : 2) : 1;
        // Legacy positive buoyancy was combined with vanilla gravity/web. Here we explicitly return
        // a net sinking velocity. These coefficients are NOT a recovered 1.7.10 trajectory.
        double support = profile.buoyancy / (1 + blocks * blocks * 0.08) / movementPenalty;
        double fall = y < -0.1 ? y / (profile == MaterialProfile.MUD ? 10 : 2) : 0;
        double nextY = fall + (support - 0.08) * 0.98;
        if (struggle) nextY -= 0.05 * (1 + Math.min(0.75, blocks));
        x *= profile.horizontalRetention;
        z *= profile.horizontalRetention;
        if (profile == MaterialProfile.MUD && grounded) { x *= 0.1; z *= 0.1; }
        if (profile == MaterialProfile.SOFT_QUICKSAND && d >= 0.5) {
            x = 0;
            z = 0;
            double cx = clamp(centerX, -1, 1), cz = clamp(centerZ, -1, 1);
            double radius = Math.hypot(cx, cz);
            if (radius >= 0.075 && radius < 0.5) {
                x = cx / Math.max(10, blocks * 50);
                z = cz / Math.max(10, blocks * 50);
            }
        }
        int stuck = (int) Math.round(5 + (profile.maxStuck - 5) * d);
        // A single transient vanilla attribute modifier, composed with other mods' modifiers.
        double factor = Math.max(0.02, 1 / Math.pow(1 + Math.max(0, stuck - 5) / 50.0, 2));
        return new Result(new Motion(clamp(x, -0.25, 0.25), clamp(nextY, -0.25, 0.08),
                clamp(z, -0.25, 0.25)), stuck, factor);
    }
}
