package art.tiary.mfqm.client;

import art.tiary.mfqm.MfqmReborn;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;

/** Client-only registration boundary. No custom renderers exist in Task 002. */
@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID, bus = Mod.EventBusSubscriber.Bus.MOD, value = Dist.CLIENT)
public final class ClientLifecycle {
    private ClientLifecycle() { }

    @SubscribeEvent
    public static void onClientSetup(FMLClientSetupEvent event) {
        MfqmReborn.LOGGER.info("MFQM client boundary initialized; using vanilla block models/textures");
    }
}
