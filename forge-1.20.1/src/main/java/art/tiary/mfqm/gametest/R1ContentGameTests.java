package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.registry.*;
import com.google.gson.*;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.gametest.framework.*;
import net.minecraft.world.item.*;
import net.minecraftforge.gametest.*;
import net.minecraftforge.registries.ForgeRegistries;
import java.nio.file.*;
import java.util.*;

@GameTestHolder(MfqmReborn.MOD_ID)
@PrefixGameTestTemplate(false)
public final class R1ContentGameTests {
    @GameTest(template="pool_test")
    public static void enumerateRegistryAndCreativeStacks(GameTestHelper helper) throws Exception {
        var level = helper.getLevel();
        var tab = ModTabs.CONTENT.get();
        tab.buildContents(new CreativeModeTab.ItemDisplayParameters(level.enabledFeatures(), true, level.registryAccess()));
        var output = new JsonObject();
        var registries = new TreeMap<String,List<String>>();
        registries.put("BLOCK", keys(ForgeRegistries.BLOCKS.getKeys()));
        registries.put("ITEM", keys(ForgeRegistries.ITEMS.getKeys()));
        registries.put("FLUID", keys(ForgeRegistries.FLUIDS.getKeys()));
        registries.put("CREATIVE_TAB", keys(BuiltInRegistries.CREATIVE_MODE_TAB.keySet()));
        registries.put("FLUID_TYPE", keys(ForgeRegistries.FLUID_TYPES.get().getKeys()));
        output.add("registries", new Gson().toJsonTree(registries));
        var stacks = new JsonArray();
        var unique = new HashSet<String>();
        var seen = new HashSet<Item>();
        for (var stack : tab.getDisplayItems()) {
            var row = new JsonObject();
            String id = ForgeRegistries.ITEMS.getKey(stack.getItem()).toString();
            String nbt = stack.hasTag() ? stack.getTag().toString() : "";
            helper.assertTrue(unique.add(id + nbt), "duplicate creative stack " + id + nbt);
            helper.assertTrue(ItemStack.matches(stack,ItemStack.of(stack.save(new net.minecraft.nbt.CompoundTag()))), "stack NBT round trip " + id);
            seen.add(stack.getItem());
            row.addProperty("id",id);
            row.addProperty("nbt",nbt);
            row.addProperty("name",stack.getHoverName().getString());
            row.addProperty("type",stack.getItem().getClass().getSimpleName());
            stacks.add(row);
        }
        for (var entry : ModItems.RESTORED) {
            helper.assertTrue(seen.contains(entry.get()) && !(entry.get() instanceof BlockItem), "new independent stack " + entry.getId());
        }
        helper.assertTrue(!seen.contains(ModItems.DEV_TEST_BLOCK.get()),"dev content in player tab");
        output.add("creative",stacks);
        Files.writeString(Path.of("r1-runtime.json"),new GsonBuilder().setPrettyPrinting().create().toJson(output));
        helper.succeed();
    }

    private static List<String> keys(Collection<net.minecraft.resources.ResourceLocation> keys) {
        return keys.stream().filter(id -> id.getNamespace().equals("mfqm")).map(Object::toString).sorted().toList();
    }
}
