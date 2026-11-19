package art.tiary.mfqm.physics;

/** Modern, bounded approximations; see docs/task-003/EVIDENCE_TRACEABILITY.md. */
public enum MaterialProfile {
    QUICKSAND("quicksand", 1.0, 0.0, 0.075, 145, 2),
    MUD("mud", 1.0, 0.71, 0.075, 145, 1),
    SOFT_QUICKSAND("soft_quicksand", 0.85, 0.71, 0.0735, 175, 3);

    public final String id;
    public final double surfaceHeight;
    public final double horizontalRetention;
    public final double buoyancy;
    public final int maxStuck;
    public final int priority;

    MaterialProfile(String id, double height, double retention, double buoyancy, int stuck, int priority) {
        this.id = id;
        this.surfaceHeight = height;
        this.horizontalRetention = retention;
        this.buoyancy = buoyancy;
        this.maxStuck = stuck;
        this.priority = priority;
    }

    public static MaterialProfile byId(String id) {
        for (var value : values()) if (value.id.equals(id)) return value;
        return null;
    }
}
