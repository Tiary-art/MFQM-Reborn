package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.integration.StuckAdapter;
import art.tiary.mfqm.legacy.StuckLease;
import art.tiary.mfqm.physics.*;

import net.minecraft.core.BlockPos;
import net.minecraft.gametest.framework.*;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.gametest.*;

@GameTestHolder(MfqmReborn.MOD_ID)
@PrefixGameTestTemplate(false)
public final class Phase8VisibilityBaseline {
    @GameTest(template="pool_test", timeoutTicks=100, batch="phase8_visibility")
    public static void trackedLeaseNotLostBeforeEntityVisibility(GameTestHelper h) {
        SinkConfig.EXPERIMENTAL_STUCK.set(true);
        var pig=EntityType.PIG.create(h.getLevel()); // deliberately NOT addFreshEntity
        h.assertTrue(h.getLevel().getEntity(pig.getUUID())==null,"registration gap is real");
        StuckAdapter.contact(pig,145); StuckAdapter.update(pig);
        h.assertTrue(pig.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(StuckLease.UUID_KEY)!=null,"initial lease");
        long start=h.getLevel().getGameTime();
        h.runAfterDelay(2,()-> {
            // GameTest runs after a full server-world settlement. One next END is the contract.
            h.assertTrue(h.getLevel().getGameTime()==start+2,"exact one world tick, not three fixture ticks");
            h.assertTrue(pig.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(StuckLease.UUID_KEY)==null,
                    "unregistered tracked entity releases at next world END: "+StuckAdapter.diagnosticState(pig));
            MfqmReborn.LOGGER.info("PHASE8_RELEASE start={} end={} visible=false modifier=false",start,h.getLevel().getGameTime());
            StuckAdapter.clear(pig); SinkConfig.EXPERIMENTAL_STUCK.set(false); pig.discard(); h.succeed();
        });
    }

}
