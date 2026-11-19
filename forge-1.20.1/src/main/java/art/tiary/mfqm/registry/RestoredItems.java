package art.tiary.mfqm.registry;

import com.google.gson.JsonParser;
import net.minecraft.network.chat.Component;
import net.minecraft.world.food.FoodProperties;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.TooltipFlag;
import net.minecraft.world.level.Level;
import net.minecraftforge.registries.RegistryObject;
import javax.annotation.Nullable;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public final class RestoredItems {
    private RestoredItems() {}

    static List<RegistryObject<Item>> register() {
        var result = new ArrayList<RegistryObject<Item>>();
        var stream = RestoredItems.class.getResourceAsStream("/data/mfqm/r1_content.json");
        try (var reader = new InputStreamReader(Objects.requireNonNull(stream), StandardCharsets.UTF_8)) {
            for (var entry : JsonParser.parseReader(reader).getAsJsonArray()) {
                var row = entry.getAsJsonObject();
                var kind = row.get("mode").getAsString();
                if (kind.equals("bucket") || kind.equals("block")) continue;
                var id = row.get("id").getAsString();
                result.add(ModItems.ITEMS.register(id, () -> {
                    var properties = new Item.Properties().stacksTo(row.get("stack").getAsInt());
                    if (kind.equals("food")) {
                        var food = row.getAsJsonArray("food");
                        var builder = new FoodProperties.Builder().nutrition(food.get(0).getAsInt())
                                .saturationMod(food.get(1).getAsFloat());
                        if (food.get(2).getAsBoolean()) builder.meat();
                        properties.food(builder.build());
                    }
                    return kind.equals("sample") ? new DisplaySample(properties) : new Item(properties);
                }));
            }
        } catch (java.io.IOException ex) {
            throw new IllegalStateException("Unable to load R1 item catalog", ex);
        }
        return List.copyOf(result);
    }

    /** Inventory representation for items whose effects or placement still need porting. */
    private static final class DisplaySample extends Item {
        DisplaySample(Properties properties) { super(properties); }
        @Override public void appendHoverText(ItemStack stack, @Nullable Level level, List<Component> lines, TooltipFlag flag) {
            lines.add(Component.translatable("tooltip.mfqm.display_sample"));
        }
    }
}
