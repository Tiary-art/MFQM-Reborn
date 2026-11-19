package art.tiary.mfqm.physics;

import net.minecraftforge.common.ForgeConfigSpec;

public final class SinkConfig {
    public static final ForgeConfigSpec SPEC;
    public static final ForgeConfigSpec.BooleanValue PLAYER_OXYGEN;
    public static final ForgeConfigSpec.BooleanValue MOB_OXYGEN;
    public static final ForgeConfigSpec.DoubleValue DAMAGE_MULTIPLIER;
    public static final ForgeConfigSpec.DoubleValue ENTRY_DEPTH, TERMINAL, DEPTH_GAIN, QS_BASE, MUD_BASE, SOFT_BASE, MOVING_EXTRA, STRUGGLE_EXTRA, ENTRY_DAMPING;
    public static MotionMath.Policy motionPolicy() {
        return new MotionMath.Policy(ENTRY_DEPTH.get(), TERMINAL.get(), DEPTH_GAIN.get(), QS_BASE.get(), MUD_BASE.get(), SOFT_BASE.get(), MOVING_EXTRA.get(), STRUGGLE_EXTRA.get(), ENTRY_DAMPING.get());
    }
    public static final ForgeConfigSpec.BooleanValue EXPERIMENTAL_STUCK, PHASE7_TEST_WORLD, PHASE7_DIAGNOSTICS, ORIGINAL_CONTACTS;
    static {
        var builder = new ForgeConfigSpec.Builder();
        PLAYER_OXYGEN = builder.comment("Use the separate 300-tick oxygen reservoir for players.")
                .define("playerOxygen", true);
        MOB_OXYGEN = builder.define("mobOxygen", true);
        DAMAGE_MULTIPLIER = builder.defineInRange("drowningDamageMultiplier", 1.0, 0.0, 100.0);
        // Preserve B1 keys on existing worlds, but do not silently reuse their fast defaults.
        builder.push("motionCandidate");
        builder.comment("Deprecated B1 settings, retained for configuration migration only.").defineInRange("entryDepth", .08, .01, .2);
        builder.defineInRange("terminalDescent", .055, .02, .1);
        builder.defineInRange("depthGain", .020, 0, .05);
        builder.pop();
        builder.push("motionV2");
        ENTRY_DEPTH = builder.comment("Blocks of first-step penetration; separate from continuous sinking.")
                .defineInRange("entryDepth", 0.08, 0.01, 0.2);
        TERMINAL = builder.comment("Maximum continuous descent in blocks/game tick; not legacy parity.")
                .defineInRange("terminalDescent", 0.012, 0.001, 0.1);
        DEPTH_GAIN = builder.defineInRange("depthGain", 0.004, 0.0, 0.05);
        QS_BASE = builder.defineInRange("quicksandBase", .0055, .001, .05);
        MUD_BASE = builder.defineInRange("mudBase", .0048, .001, .05);
        SOFT_BASE = builder.defineInRange("softQuicksandBase", .0065, .001, .05);
        MOVING_EXTRA = builder.defineInRange("movingExtra", .001, 0, .05);
        STRUGGLE_EXTRA = builder.defineInRange("struggleExtra", .002, 0, .05);
        ENTRY_DAMPING = builder.comment("Fraction of residual downward momentum, for the first three contact ticks only.").defineInRange("entryDamping", .08, 0, 1);
        builder.pop();
        builder.push("phase7");
        EXPERIMENTAL_STUCK = builder.comment("Experimental injected Stuck contacts only; no material Level approximation.").define("stuckLease", false);
        PHASE7_TEST_WORLD = builder.comment("Allow destructive test commands only in a backed-up MFQM_PHASE7_ named world.").define("testWorld", false);
        PHASE7_DIAGNOSTICS = builder.define("diagnostics", false);
        ORIGINAL_CONTACTS = builder.comment("Phase8: original Quicksand contact projection, non-player living entities only; players and other materials BLOCKED.").define("originalQuicksandContacts", false);
        builder.pop();
        SPEC = builder.build();
    }
    private SinkConfig() { }
}
