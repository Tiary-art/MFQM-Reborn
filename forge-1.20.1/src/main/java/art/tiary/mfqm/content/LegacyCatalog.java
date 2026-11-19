package art.tiary.mfqm.content;

import art.tiary.mfqm.physics.MaterialProfile;
import com.google.gson.JsonParser;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;

/** Fixed registration evidence, loaded from this mod's JAR rather than a mutable datapack. */
public final class LegacyCatalog {
    public enum Kind { SOLID, SINKING, VISCOUS, TRAP, SLAB, PLANT, LILY, LEAVES, GAS, DEPENDENT }
    public record Spec(String id, String legacyId, String legacyClass, Kind kind, float hardness,
                       double height, MaterialProfile profile, double motionScale, boolean visible,
                       String fluid, String tileDependency, float damage, int emission, String drop) { }
    public static final List<Spec> ALL = load();
    private static List<Spec> load() {
        var input = LegacyCatalog.class.getResourceAsStream("/data/mfqm/legacy_block_catalog.json");
        if (input == null) throw new IllegalStateException("Missing immutable block catalog");
        try (var reader = new InputStreamReader(input, StandardCharsets.UTF_8)) {
            var specs = new ArrayList<Spec>(); var ids = new HashSet<String>();
            for (var entry : JsonParser.parseReader(reader).getAsJsonArray()) {
                var o = entry.getAsJsonObject(); String id = o.get("id").getAsString();
                if (!id.matches("[a-z0-9_]+") || !ids.add(id)) throw new IllegalStateException("Duplicate/invalid legacy ID " + id);
                specs.add(new Spec(id, o.get("legacy_id").getAsString(), o.get("legacy_class").getAsString(),
                        Kind.valueOf(o.get("kind").getAsString()), o.get("hardness").getAsFloat(), o.get("height").getAsDouble(),
                        MaterialProfile.valueOf(o.get("profile").getAsString()), o.get("motion_scale").getAsDouble(),
                        o.get("visible").getAsBoolean(), o.get("fluid").getAsString(), o.get("tile_dependency").getAsString(),
                        o.get("damage").getAsFloat(), o.get("emission").getAsInt(), o.get("drop").getAsString()));
            }
            return List.copyOf(specs);
        } catch (Exception ex) { throw new IllegalStateException("Invalid legacy catalog", ex); }
    }
    public static Spec byId(String id) { return ALL.stream().filter(s -> s.id.equals(id)).findFirst().orElse(null); }
    private LegacyCatalog() { }
}
