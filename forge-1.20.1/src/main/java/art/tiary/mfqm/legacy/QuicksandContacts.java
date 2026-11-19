package art.tiary.mfqm.legacy;

import java.util.function.IntConsumer;

/** Contact-only dataflow projection of original BlockQuicksand.func_149670_a.
 * No motion/particle/sound/RNG port. Current admitted runtime domain: non-player living entities.
 */
public final class QuicksandContacts {
    private QuicksandContacts() { }
    public static void emit(double legacyEntityY, int blockY, boolean aboveSame, boolean twoAboveSame,
                            boolean trulySink, IntConsumer contact) {
        double kof = -((double) blockY - legacyEntityY - 0.5);
        double km = Math.max(kof, 0.0);
        float mtdkof = 10.0f;
        int level = (int) Math.min(5.0 + Math.floor(Math.max(0.0, (double) (mtdkof * 10.0f) * (1.5 - km))), 145.0);
        if (!aboveSame || twoAboveSame) {
            if (aboveSame && twoAboveSame) kof = 0.001;
            if (kof >= 1.2) return;
            if (kof >= 0.9) {
                contact.accept(level);
            } else {
                if (trulySink) contact.accept(level);
                if (kof < 0.45 && trulySink) contact.accept(145);
            }
        } else if (kof < 0.5 && trulySink) {
            contact.accept(145);
        }
    }
}
