package art.tiary.mfqm.state;

import art.tiary.mfqm.MfqmReborn;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Locale;
import net.minecraft.world.entity.LivingEntity;

/** Optional operator-started real-tick measurement. Owned/closed by the entity capability. */
public final class TraceSession implements AutoCloseable {
    private final BufferedWriter writer;
    private int remaining;
    private boolean closed;
    public final Path path;

    public TraceSession(Path path, int ticks) throws IOException {
        Files.createDirectories(path.getParent());
        this.path = path;
        writer = Files.newBufferedWriter(path);
        remaining = ticks;
        writer.write("tick,entity,material,contacts,x,y,z,vx,vy,vz,immersion,stuck,eye_covered,air,health,damage_requests,settlements,on_ground,jump_held,mud_depth\n");
    }

    public void record(LivingEntity entity, SinkState state, long time) {
        if (closed) return;
        var v = entity.getDeltaMovement();
        try {
            writer.write(String.format(Locale.ROOT,
                    "%d,%s,%s,%d,%.8f,%.8f,%.8f,%.8f,%.8f,%.8f,%.6f,%d,%s,%d,%.2f,%d,%d,%s,%s,%d%n",
                    time, entity.getUUID(), state.active() ? state.material.id : "none", state.contacts,
                    entity.getX(), entity.getY(), entity.getZ(), v.x, v.y, v.z, state.immersion, state.stuck,
                    state.eyeCovered, state.air, entity.getHealth(), state.damageEvents, state.settlements,
                    entity.onGround(), state.jumpHeld, state.mudDepth));
            writer.flush();
            if (--remaining <= 0) close();
        } catch (IOException e) { MfqmReborn.LOGGER.warn("Cannot write MFQM measurement", e); close(); }
    }

    @Override public void close() {
        if (closed) return;
        closed = true;
        try { writer.close(); } catch (IOException e) { MfqmReborn.LOGGER.warn("Cannot close MFQM measurement", e); }
    }
}
