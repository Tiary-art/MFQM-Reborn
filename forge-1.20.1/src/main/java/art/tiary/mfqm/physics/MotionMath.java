package art.tiary.mfqm.physics;

/** Candidate policy, not a measured reproduction of 1.7.10. Units: blocks/game tick. */
public final class MotionMath {
    public enum Phase { OUTSIDE, ENTERING, SUBMERGED, EXITING }
    public record Policy(double entryDepth, double terminal, double depthGain, double quicksandBase, double mudBase, double softBase, double movingExtra, double struggleExtra, double entryDamping) {
        public Policy(double entryDepth, double terminal, double depthGain) {
            this(entryDepth, terminal, depthGain, .0055, .0048, .0065, .001, .002, .08);
        }
        public Policy {
            if (!Double.isFinite(entryDepth) || !Double.isFinite(terminal) || !Double.isFinite(depthGain)
                    || entryDepth < 0.01 || entryDepth > 0.2 || terminal < 0.001 || terminal > 0.1
                    || depthGain < 0 || depthGain > 0.05) throw new IllegalArgumentException("motion policy bounds");
            for (double value : new double[]{quicksandBase, mudBase, softBase, movingExtra, struggleExtra, entryDamping})
                if (!Double.isFinite(value) || value < 0 || value > 1) throw new IllegalArgumentException("motion tuning bounds");
        }
    }
    private MotionMath() { }
    public static double velocity(MaterialProfile material, double depth, boolean moving, boolean struggle, Policy p) {
        double base = switch (material) { case QUICKSAND -> p.quicksandBase(); case MUD -> p.mudBase(); case SOFT_QUICKSAND -> p.softBase(); };
        double safeDepth = Double.isFinite(depth) ? SinkMath.clamp(depth, 0, 16) : 0;
        return -Math.min(p.terminal(), base + p.depthGain() * Math.min(1, safeDepth / 2)
                + (moving ? p.movingExtra() : 0) + (struggle ? p.struggleExtra() : 0));
    }
    /** Short bounded momentum transition; never a permanent surface lock. */
    public static double dampEntry(double target, double incoming, int age, Policy p) {
        if (age > 3 || incoming >= target || !Double.isFinite(incoming)) return target;
        return Math.max(-p.terminal(), target + (incoming - target) * Math.pow(p.entryDamping(), Math.max(1, age)));
    }
    public static double entryStep(double feet, double surface, double proposed, Policy p) {
        if (!Double.isFinite(feet) || !Double.isFinite(surface) || !Double.isFinite(proposed)) return 0;
        return Math.max(proposed, Math.min(0, surface - p.entryDepth() - feet));
    }
    public static double downwardBudget(double elapsedTicks, Policy p) {
        return p.terminal() * SinkMath.clamp(elapsedTicks, 1, 4) + 0.08;
    }
    public static boolean controlledLanding(boolean contact, boolean passenger, double vertical, Policy p) {
        return contact && !passenger && Double.isFinite(vertical) && vertical <= 0.001 && vertical >= -p.terminal() - 0.001;
    }
}
