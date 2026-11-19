package art.tiary.mfqm.physics;

import art.tiary.mfqm.MfqmReborn;
import net.minecraftforge.event.entity.living.LivingBreatheEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** MFQM settles native air once at level END; prevent vanilla refill/consumption in the same core contact. */
@Mod.EventBusSubscriber(modid=MfqmReborn.MOD_ID)
public final class NativeAir {
    @SubscribeEvent public static void breathe(LivingBreatheEvent e) {
        if(SinkEngine.exempt(e.getEntity()) || !ContactSampler.sample(e.getEntity().level(),e.getEntity()).eyes()) return;
        e.setCanBreathe(true);
        e.setCanRefillAir(false);
    }
}
