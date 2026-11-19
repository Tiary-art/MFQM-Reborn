package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.registry.ModBlocks;
import art.tiary.mfqm.registry.ModItems;
import net.minecraft.core.BlockPos;
import net.minecraft.gametest.framework.GameTest;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.storage.loot.LootParams;
import net.minecraft.world.level.storage.loot.parameters.LootContextParamSets;
import net.minecraft.world.level.storage.loot.parameters.LootContextParams;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.gametest.GameTestHolder;
import net.minecraftforge.gametest.PrefixGameTestTemplate;

@GameTestHolder(MfqmReborn.MOD_ID)
@PrefixGameTestTemplate(false)
public final class FoundationGameTests {
    private FoundationGameTests() { }

    @GameTest(template = "empty3x3")
    public static void registeredBlockPlacesAndDrops(GameTestHelper helper) {
        var block = ModBlocks.DEV_TEST_BLOCK.get();
        helper.assertTrue(Item.byBlock(block) == ModItems.DEV_TEST_BLOCK.get(), "BlockItem must point to registered block");
        BlockPos relative = new BlockPos(1, 1, 1);
        helper.setBlock(relative, block);
        helper.assertBlockPresent(block, relative);
        var params = new LootParams.Builder(helper.getLevel())
                .withParameter(LootContextParams.BLOCK_STATE, block.defaultBlockState())
                .withParameter(LootContextParams.ORIGIN, Vec3.atCenterOf(helper.absolutePos(relative)))
                .withParameter(LootContextParams.TOOL, ItemStack.EMPTY)
                .create(LootContextParamSets.BLOCK);
        var drops = helper.getLevel().getServer().getLootData().getLootTable(block.getLootTable()).getRandomItems(params);
        helper.assertTrue(drops.size() == 1 && drops.get(0).is(ModItems.DEV_TEST_BLOCK.get()) && drops.get(0).getCount() == 1,
                "Survival loot must drop exactly one development block");
        helper.succeed();
    }
}
