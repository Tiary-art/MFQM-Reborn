package art.tiary.mfqm;

import art.tiary.mfqm.registry.ModBlocks;
import art.tiary.mfqm.registry.ModItems;
import art.tiary.mfqm.network.SinkNetwork;
import art.tiary.mfqm.physics.SinkConfig;
import net.minecraftforge.fml.ModLoadingContext;
import net.minecraftforge.fml.config.ModConfig;
import com.mojang.logging.LogUtils;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraftforge.event.BuildCreativeModeTabContentsEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import org.slf4j.Logger;

@Mod(MfqmReborn.MOD_ID)
public final class MfqmReborn {
    public static final String MOD_ID = "mfqm";
    public static final Logger LOGGER = LogUtils.getLogger();

    public MfqmReborn() {
        IEventBus bus = FMLJavaModLoadingContext.get().getModEventBus();
        ModBlocks.BLOCKS.register(bus);
        art.tiary.mfqm.content.MaterialEffects.SOUNDS.register(bus);
        art.tiary.mfqm.content.LegacyFluids.TYPES.register(bus);
        art.tiary.mfqm.content.LegacyFluids.FLUIDS.register(bus);
        ModItems.ITEMS.register(bus);
        art.tiary.mfqm.registry.ModTabs.TABS.register(bus);
        ModLoadingContext.get().registerConfig(ModConfig.Type.SERVER, SinkConfig.SPEC);
        SinkNetwork.register();
        bus.addListener(this::commonSetup);
        bus.addListener(this::creativeContents);
    }

    private void commonSetup(FMLCommonSetupEvent event) {
        LOGGER.info("MFQM Task 003 initialized; three server-authoritative core materials, static-evidence approximation");
    }

    private void creativeContents(BuildCreativeModeTabContentsEvent event) {
        if (event.getTabKey() == CreativeModeTabs.BUILDING_BLOCKS) {
            event.accept(ModItems.DEV_TEST_BLOCK);
            event.accept(ModItems.QUICKSAND);
            event.accept(ModItems.MUD);
            event.accept(ModItems.SOFT_QUICKSAND);
        }
    }
}
