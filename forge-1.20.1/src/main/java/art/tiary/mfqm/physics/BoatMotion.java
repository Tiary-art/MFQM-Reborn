package art.tiary.mfqm.physics;

import art.tiary.mfqm.MfqmReborn;
import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.util.Mth;
import net.minecraft.world.entity.vehicle.Boat;
import net.minecraftforge.event.TickEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;

/** MODERN_COMPAT approved by B2: hull-only support, including ChestBoat. No fake water FluidState. */
@Mod.EventBusSubscriber(modid=MfqmReborn.MOD_ID)
public final class BoatMotion {
    private BoatMotion() {}
    @SubscribeEvent public static void tick(TickEvent.LevelTickEvent e) {
        if(e.phase!=TickEvent.Phase.START || !(e.level instanceof ServerLevel l)) return;
        for(var entity:l.getAllEntities()) if(entity instanceof Boat b && b.isControlledByLocalInstance()) prepare(b);
    }
    public static double surface(Boat boat) {
        var l=boat.level(); var box=boat.getBoundingBox(); double highest=Double.NEGATIVE_INFINITY;
        double bottom=Math.min(boat.getY()-.5,boat.getY()+Math.max(-4,boat.getDeltaMovement().y));
        for(int x=Mth.floor(box.minX+.01); x<=Mth.floor(box.maxX-.01); x++)
            for(int z=Mth.floor(box.minZ+.01); z<=Mth.floor(box.maxZ-.01); z++)
                for(int y=Mth.floor(boat.getY()+.8); y>=Mth.floor(bottom); y--) {
                    BlockPos p=new BlockPos(x,y,z);
                    if(!l.hasChunkAt(p)) continue;
                    var s=l.getBlockState(p);
                    if(!(s.getBlock() instanceof SinkingBlock b) || l.getBlockState(p.above()).is(b)) continue;
                    // Only the three core pools are approved by the compatibility requirement.
                    var id=net.minecraftforge.registries.ForgeRegistries.BLOCKS.getKey(b);
                    if(id==null || !(id.getPath().equals("quicksand") || id.getPath().equals("soft_quicksand") || id.getPath().equals("mud"))) continue;
                    double surface=y+b.surfaceHeight(s,l,p);
                    if(boat.getY()>=surface-.65 && boat.getY()+Math.min(0,boat.getDeltaMovement().y)<=surface+.5)
                        highest=Math.max(highest,surface);
                }
        return highest;
    }
    public static void prepare(Boat b) {
        if(b.isRemoved() || b.isNoGravity()) return;
        double surface=surface(b); if(!Double.isFinite(surface)) return;
        var v=b.getDeltaMovement();
        // Boat.floatBoat(IN_AIR) applies -0.04 gravity, horizontal drag .9 and vanilla steering.
        // Pre-move compensation retains that steering/drag; the spring damps entry and settles the hull.
        double target=surface-b.getBbHeight()*.65;
        double desired=Mth.clamp(v.y*.65+(target-b.getY())*.18,-.08,.08);
        b.setDeltaMovement(v.x, desired+(double).04f, v.z);
        b.fallDistance=0;
    }
}
