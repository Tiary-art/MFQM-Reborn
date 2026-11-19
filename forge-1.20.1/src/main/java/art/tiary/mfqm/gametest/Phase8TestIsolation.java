package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.SinkConfig;
import art.tiary.mfqm.integration.StuckAdapter;
import net.minecraft.gametest.framework.BeforeBatch;
import net.minecraft.gametest.framework.AfterBatch;
import net.minecraft.server.level.ServerLevel;
import net.minecraftforge.gametest.GameTestHolder;

/** Only the disposable GameTest harness: stop disk watcher racing rapid test-side ConfigValue.set calls.
 * Production servers keep their normal Forge config watcher.
 */
@GameTestHolder(MfqmReborn.MOD_ID)
public final class Phase8TestIsolation {
    @BeforeBatch(batch="defaultBatch")
    public static void isolateFixtureConfiguration(ServerLevel level) throws Exception {
        for (var config : net.minecraftforge.fml.config.ConfigTracker.INSTANCE.configSets().get(net.minecraftforge.fml.config.ModConfig.Type.SERVER)) {
            if (config.getSpec() != SinkConfig.SPEC) continue;
            com.electronwill.nightconfig.core.file.FileWatcher.defaultInstance().removeWatch(config.getFullPath());
            MfqmReborn.LOGGER.info("PHASE8_TEST_CONFIG_WATCH_DISABLED {} (GameTest fixtures only)",config.getFullPath());
        }
    }
    @AfterBatch(batch="phase8_rollback")
    public static void resetTestServerRollbackLatch(ServerLevel level) throws Exception {
        // Simulate a new test server boundary between independent cases, not a production re-enable API.
        var field=StuckAdapter.class.getDeclaredField("forcedDisabled");field.setAccessible(true);field.setBoolean(null,false);
        SinkConfig.EXPERIMENTAL_STUCK.set(false);SinkConfig.ORIGINAL_CONTACTS.set(false);SinkConfig.PHASE7_TEST_WORLD.set(false);
    }
}
