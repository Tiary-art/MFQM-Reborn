package art.tiary.mfqm.legacy;
/** Inject the same java.util.Random-compatible stream; never reseed in the core. */
public interface LegacyRandom {
    int nextInt(int bound);
    double nextDouble();
}
