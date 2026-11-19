package art.tiary.mfqm.legacy;

import java.util.UUID;

/** Pure lease reducer. Port must not reenter/update this UUID during one update. */
public final class StuckLease {
    public static final UUID UUID_KEY = UUID.fromString("73a49882-85a3-4896-ad2d-8c591e24aa62");
    public interface AttributePort {
        boolean contains(UUID uuid);
        void remove(UUID uuid);
        void addTransient(UUID uuid, double amount, int operation, boolean saved);
    }
    public interface LevelPort {
        boolean present();
        int level();
        void level(int value);
    }
    private StuckLease() { }
    public static void contact(LevelPort state, int level) { state.level(level); }
    public static void update(LevelPort state, boolean horizontalCollision, AttributePort attributes) {
        if (attributes.contains(UUID_KEY)) attributes.remove(UUID_KEY);
        if (!state.present()) return;
        int level = state.level();
        if (level > 0) {
            int p = level - 5;
            double c = horizontalCollision ? 0 : 1;
            double speed = p >= 250 ? 0.02 : Math.max(1 / Math.pow(1 + p * (1 + c / 2) / 50, 2), 0.02);
            if (!attributes.contains(UUID_KEY)) attributes.addTransient(UUID_KEY, speed - 1, 2, false);
            state.level(0);
        } else if (level == 0) state.level(-1);
    }
}
