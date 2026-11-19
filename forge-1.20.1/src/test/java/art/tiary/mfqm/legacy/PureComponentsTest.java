package art.tiary.mfqm.legacy;

import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestFactory;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.UUID;

import static org.junit.jupiter.api.Assertions.*;

class PureComponentsTest {
    static final Path DATA = Path.of("src/test/resources/phase6");
    record Pos(int x, int y, int z) { }

    static void assertEvents(List<String> expected, List<String> actual, String id) {
        assertEquals(expected.size(), actual.size(), id + " event count");
        for (int i = 0; i < expected.size(); i++) {
            String[] e = expected.get(i).split("\t"), a = actual.get(i).split("\t");
            // JSON/Python and Java spell exponents differently; compare the exact parsed double.
            if (e[0].equals("R") && e[1].equals("nextDouble")) e[3] = Double.toString(Double.parseDouble(e[3]));
            if (e[0].equals("N")) e[2] = Double.toString(Double.parseDouble(e[2]));
            assertArrayEquals(e, a, id + " event " + i);
        }
    }

    static class Grid implements VoxelPort {
        final String fixture;
        final List<String> events;
        final Map<Pos, LegacyBlock> cells = new HashMap<>();
        Grid(String fixture, List<String> events) { this.fixture = fixture; this.events = events; }
        LegacyBlock initial(int y) {
            if (fixture.equals("empty")) return LegacyBlock.AIR;
            if (fixture.equals("deny")) return y == 66 ? LegacyBlock.OTHER : LegacyBlock.AIR;
            if (y > 70) return LegacyBlock.AIR;
            return fixture.equals("protected") ? LegacyBlock.SOFT_QUICKSAND : LegacyBlock.SAND;
        }
        public LegacyBlock blockAt(int x, int y, int z) {
            LegacyBlock b = cells.getOrDefault(new Pos(x, y, z), initial(y));
            events.add("Q\t" + x + "\t" + y + "\t" + z + "\t" + b);
            return b;
        }
        public boolean write(int x, int y, int z, LegacyBlock b, int metadata, int flags) {
            boolean applied = !fixture.equals("desert-refuse") && (!fixture.equals("deny") || y != 63);
            if (applied) cells.put(new Pos(x, y, z), b);
            events.add("W\t" + x + "\t" + y + "\t" + z + "\t" + b + "\t" + metadata + "\t" + flags + "\t" + applied);
            return applied;
        }
    }

    static class RandomPort implements LegacyRandom {
        final Random rng;
        final List<String> events;
        RandomPort(long seed, List<String> events) { rng = new Random(seed); this.events = events; }
        public int nextInt(int bound) {
            int value = rng.nextInt(bound);
            events.add("R\tnextInt\t" + bound + "\t" + value);
            return value;
        }
        public double nextDouble() {
            double value = rng.nextDouble();
            events.add("R\tnextDouble\t-\t" + value);
            return value;
        }
    }

    @TestFactory Collection<DynamicTest> originalDryTraces() throws Exception {
        List<DynamicTest> tests = new ArrayList<>();
        List<String> cases = Files.readAllLines(DATA.resolve("dry-cases.tsv"));
        assertEquals(19, cases.size());
        for (String line : cases) {
            String[] c = line.split("\t");
            tests.add(DynamicTest.dynamicTest(c[0], () -> {
                List<String> actual = new ArrayList<>();
                RandomPort rng = new RandomPort(Long.parseLong(c[1]), actual);
                if (c[0].equals("parent38")) {
                    List<String> prefix = Files.readAllLines(DATA.resolve("parent38-prefix.tsv"));
                    for (String warm : prefix) {
                        String[] w = warm.split("\t");
                        if (w[1].equals("nextInt")) rng.nextInt(Integer.parseInt(w[2]));
                        else if (w[1].equals("nextDouble")) rng.nextDouble();
                        else fail("unsupported warmup RNG " + w[1]);
                    }
                    assertEvents(prefix, actual, "parent RNG warmup");
                    actual.clear();
                }
                DryQuicksandCore.generateDry(-16, 70, 0, Integer.parseInt(c[2]), new Grid(c[3], actual), rng);
                assertEvents(Files.readAllLines(DATA.resolve(c[0] + ".tsv")), actual, c[0]);
            }));
        }
        return tests;
    }

    static class Ports implements StuckLease.LevelPort, StuckLease.AttributePort {
        int level = -1;
        boolean attached = true;
        final Map<UUID, Double> mods = new HashMap<>();
        final List<String> events = new ArrayList<>();
        public boolean present() { events.add("P\t" + attached); return attached; }
        public int level() { return level; }
        public void level(int value) { level = value; events.add("L\t" + value); }
        public boolean contains(UUID uuid) {
            assertEquals(StuckLease.UUID_KEY, uuid);
            boolean present = mods.containsKey(uuid);
            events.add("A\t" + present);
            return present;
        }
        public void remove(UUID uuid) { events.add("D\t" + uuid); mods.remove(uuid); }
        public void addTransient(UUID uuid, double amount, int operation, boolean saved) {
            assertEquals(2, operation);
            assertFalse(saved);
            mods.put(uuid, amount);
            events.add("N\t" + uuid + "\t" + amount + "\t" + operation + "\t" + saved);
        }
    }

    @Test void originalEightCallbacks() throws Exception {
        Ports p = new Ports();
        int[][] contacts = {{145}, {}, {}, {145, 128}, {50}, {255}, {0}, {}};
        for (int tick = 0; tick < 8; tick++) {
            p.events.add("T\t" + tick);
            p.attached = tick != 7;
            for (int value : contacts[tick]) StuckLease.contact(p, value);
            StuckLease.update(p, tick % 2 == 0, p);
        }
        assertEvents(Files.readAllLines(DATA.resolve("stuck.tsv")), p.events, "lifecycle");
    }

    @Test void all112MathVectors() throws Exception {
        List<String> rows = Files.readAllLines(DATA.resolve("physics-vectors.csv"));
        assertEquals(113, rows.size());
        for (String row : rows.subList(1, rows.size())) {
            String[] c = row.split(",");
            Ports p = new Ports();
            p.level = Integer.parseInt(c[0]);
            StuckLease.update(p, Boolean.parseBoolean(c[1]), p);
            assertEquals(Double.parseDouble(c[6]), p.mods.get(StuckLease.UUID_KEY), 1e-12, row);
            assertEquals(0, p.level);
        }
    }

    @Test void cleanupIsolationAndNegativeLevels() {
        Ports p = new Ports();
        UUID other = new UUID(0, 1);
        p.mods.put(other, .25);
        p.mods.put(StuckLease.UUID_KEY, -.5);
        p.attached = false;
        StuckLease.update(p, false, p);
        assertEquals(List.of("A\ttrue", "D\t" + StuckLease.UUID_KEY, "P\tfalse"), p.events);
        assertEquals(Map.of(other, .25), p.mods);
        p.attached = true;
        p.level = -7;
        StuckLease.update(p, false, p);
        assertEquals(-7, p.level);
        StuckLease.contact(p, 145);
        StuckLease.update(p, false, p);
        assertEquals(0, p.level);
        assertTrue(p.mods.containsKey(StuckLease.UUID_KEY));
        StuckLease.update(p, false, p);
        assertEquals(-1, p.level);
        assertFalse(p.mods.containsKey(StuckLease.UUID_KEY));
        assertEquals(.25, p.mods.get(other));
    }
}
