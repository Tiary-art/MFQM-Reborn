package art.tiary.mfqm.state;

import art.tiary.mfqm.physics.MaterialProfile;
import art.tiary.mfqm.physics.SinkMath;
import net.minecraft.nbt.CompoundTag;

/** Entity-owned data; only residue survives NBT. No packed integers or global entity slots. */
public final class SinkState {
    public MaterialProfile material;
    public double immersion;
    public int stuck;
    public int air = 300;
    public boolean eyeCovered;
    public int contacts;
    public int mudDepth;
    public long lastTick = Long.MIN_VALUE;
    public String lastDimension = "";
    public long settlements;
    public long damageEvents;
    public long lastDamageTick = Long.MIN_VALUE;
    public long lastStruggleTick = Long.MIN_VALUE;
    public boolean jumpHeld;
    public long inputTick = Long.MIN_VALUE;
    public double previousX, previousY, previousZ;
    public double lastVertical;
    public boolean hasPrevious;
    public long lastSnapshotTick = Long.MIN_VALUE;
    public int lastSyncedAir = 300;
    public boolean wasActive;
    public String residueType = "";
    public int residueTicks;
    public int lastSyncedResidue;
    public TraceSession trace;
    public long motionCorrections;
    public String correctionReason = "none";

    public art.tiary.mfqm.physics.MotionMath.Phase motionPhase = art.tiary.mfqm.physics.MotionMath.Phase.OUTSIDE;
    public int motionAge;
    public long motionNano;
    public boolean controlledMotion;

    public boolean active() { return material != null; }

    public void leaveContact() {
        motionPhase = motionPhase == art.tiary.mfqm.physics.MotionMath.Phase.OUTSIDE
                ? motionPhase : art.tiary.mfqm.physics.MotionMath.Phase.EXITING;
        motionAge = 0;
        controlledMotion = false;
        material = null;
        immersion = 0;
        stuck = 0;
        eyeCovered = false;
        contacts = 0;
        mudDepth = 0;
        jumpHeld = false;
    }

    public void resetTransient() {
        leaveContact();
        air = 300;
        lastTick = Long.MIN_VALUE;
        lastDimension = "";
        inputTick = Long.MIN_VALUE;
        lastStruggleTick = Long.MIN_VALUE;
        lastDamageTick = Long.MIN_VALUE;
        lastSnapshotTick = Long.MIN_VALUE;
        hasPrevious = false;
        motionPhase = art.tiary.mfqm.physics.MotionMath.Phase.OUTSIDE;
        motionNano = 0;
        wasActive = false;
        closeTrace();
    }

    public void clearAll() {
        resetTransient();
        residueType = "";
        residueTicks = 0;
    }

    public CompoundTag save() {
        CompoundTag tag = new CompoundTag();
        tag.putInt("schema", 1);
        tag.putString("residueType", residueType);
        tag.putInt("residueTicks", (int) SinkMath.clamp(residueTicks, 0, 10000));
        return tag;
    }

    public void load(CompoundTag tag) {
        clearAll();
        if (tag.getInt("schema") != 1) return;
        String type = tag.getString("residueType");
        residueType = MaterialProfile.byId(type) == null ? "" : type;
        residueTicks = residueType.isEmpty() ? 0 : (int) SinkMath.clamp(tag.getInt("residueTicks"), 0, 10000);
    }

    public void closeTrace() {
        if (trace != null) { trace.close(); trace = null; }
    }
}
