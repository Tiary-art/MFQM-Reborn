package art.tiary.mfqm.registry;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.MaterialProfile;
import art.tiary.mfqm.physics.SinkingBlock;
import art.tiary.mfqm.physics.MudBlock;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public final class ModBlocks {
    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, MfqmReborn.MOD_ID);
    // Ordinary solid block: deliberately no custom sinking, suffocation or rescue behavior.
    public static final RegistryObject<Block> DEV_TEST_BLOCK = BLOCKS.register("dev_test_block",
            () -> new Block(BlockBehaviour.Properties.copy(Blocks.SAND).strength(0.5F)));

    public static final RegistryObject<Block> QUICKSAND = BLOCKS.register("quicksand",
            () -> new art.tiary.mfqm.physics.CoreSinkingBlock(MaterialProfile.QUICKSAND, BlockBehaviour.Properties.copy(Blocks.SAND).strength(2.5F)));
    public static final RegistryObject<Block> MUD = BLOCKS.register("mud",
            () -> new MudBlock(BlockBehaviour.Properties.copy(Blocks.MUD).strength(0.6F)));
    public static final RegistryObject<Block> SOFT_QUICKSAND = BLOCKS.register("soft_quicksand",
            () -> new art.tiary.mfqm.physics.CoreSinkingBlock(MaterialProfile.SOFT_QUICKSAND, BlockBehaviour.Properties.copy(Blocks.RED_SAND).strength(2.0F)));

    public static final java.util.Map<String, RegistryObject<Block>> LEGACY = new java.util.LinkedHashMap<>();
    static {
        LEGACY.put("quicksand",QUICKSAND); LEGACY.put("mud",MUD); LEGACY.put("soft_quicksand",SOFT_QUICKSAND);
        for (var spec : art.tiary.mfqm.content.LegacyCatalog.ALL) if (!LEGACY.containsKey(spec.id()))
            LEGACY.put(spec.id(), BLOCKS.register(spec.id(), () -> art.tiary.mfqm.content.LegacyBlocks.create(spec)));
    }

    private ModBlocks() { }
}
