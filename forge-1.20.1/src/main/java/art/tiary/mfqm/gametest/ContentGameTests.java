package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.content.LegacyCatalog;
import art.tiary.mfqm.registry.ModBlocks;
import art.tiary.mfqm.registry.ModItems;
import net.minecraft.core.BlockPos;
import net.minecraft.core.registries.Registries;
import net.minecraft.gametest.framework.GameTest;
import net.minecraft.gametest.framework.GameTestHelper;
import net.minecraft.nbt.NbtUtils;
import net.minecraft.world.level.block.Blocks;
import net.minecraftforge.gametest.GameTestHolder;
import net.minecraftforge.gametest.PrefixGameTestTemplate;
import net.minecraftforge.registries.ForgeRegistries;

@GameTestHolder(MfqmReborn.MOD_ID)
@PrefixGameTestTemplate(false)
public final class ContentGameTests {
    @GameTest(template="pool_test")
    public static void allVerifiedLegacyBlocksRegisterPlaceAndRoundtripNbt(GameTestHelper h) {
        h.assertTrue(LegacyCatalog.ALL.size()==49,"49 verified source registrations, excluding dev block");
        int index=0;
        for (var s : LegacyCatalog.ALL) {
            var block=ModBlocks.LEGACY.get(s.id()).get();
            var item=ModItems.LEGACY.get(s.id()).get();
            h.assertTrue(ForgeRegistries.BLOCKS.getKey(block).getPath().equals(s.id()),"stable block ID "+s.id());
            h.assertTrue(ForgeRegistries.ITEMS.getKey(item).getPath().equals(s.id()),"verified ItemBlock "+s.id());
            var pos=new BlockPos(2+index%10,2,2+index/10);index++;
            h.setBlock(pos.below(),s.kind()==LegacyCatalog.Kind.LILY?Blocks.WATER:Blocks.DIRT);
            h.setBlock(pos,block);
            h.assertBlockPresent(block,pos);
            var state=block.defaultBlockState();
            var tag=NbtUtils.writeBlockState(state);
            var loaded=NbtUtils.readBlockState(h.getLevel().holderLookup(Registries.BLOCK),tag);
            h.assertTrue(loaded.equals(state),"blockstate NBT registry roundtrip "+s.id());
        }
        h.succeed();
    }
    @GameTest(template="pool_test")
    public static void poweredSandstoneTrapConvertsHorizontalCluster(GameTestHelper h) {
        var p=new BlockPos(8,3,8);
        h.setBlock(p.below(),Blocks.STONE);h.setBlock(p.north().below(),Blocks.STONE);
        var trap=ModBlocks.LEGACY.get("sandstone_trap").get();
        h.setBlock(p,trap);h.setBlock(p.north(),trap);h.setBlock(p.east(),Blocks.REDSTONE_BLOCK);
        h.runAfterDelay(2,()->{
            h.assertBlockPresent(ModBlocks.QUICKSAND.get(),p);
            h.assertBlockPresent(ModBlocks.QUICKSAND.get(),p.north());h.succeed();
        });
    }
}
