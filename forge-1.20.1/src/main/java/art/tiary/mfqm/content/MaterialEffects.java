package art.tiary.mfqm.content;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.MaterialProfile;
import art.tiary.mfqm.state.SinkState;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.sounds.*;
import net.minecraft.world.entity.LivingEntity;
import net.minecraftforge.registries.*;

/** One centrally budgeted effect source per entity; legal vanilla event fallbacks. */
public final class MaterialEffects {
    public static final DeferredRegister<SoundEvent> SOUNDS=DeferredRegister.create(ForgeRegistries.SOUND_EVENTS,MfqmReborn.MOD_ID);
    public static final RegistryObject<SoundEvent> ENTER=event("material_enter"), MOVE=event("material_move"),
        STRUGGLE=event("material_struggle"), EXIT=event("material_exit"), BUBBLE=event("mud_bubble");
    private static RegistryObject<SoundEvent> event(String id) { return SOUNDS.register(id,()->SoundEvent.createVariableRangeEvent(new ResourceLocation(MfqmReborn.MOD_ID,id))); }
    private static void play(ServerLevel l,LivingEntity e,RegistryObject<SoundEvent> sound,float volume) {
        l.playSound(null,e.getX(),e.getY(),e.getZ(),sound.get(),SoundSource.PLAYERS,volume,.9f+e.getRandom().nextFloat()*.2f);
    }
    public static void tick(ServerLevel l,LivingEntity e,SinkState d,boolean before,long tick) {
        if(!before && d.active()) play(l,e,ENTER,.35f);
        else if(before && !d.active()) play(l,e,EXIT,.3f);
        if(!d.active() || tick%16!=Math.floorMod(e.getId(),16)) return;
        boolean moving=e.getDeltaMovement().horizontalDistanceSqr()>.00000225;
        if(d.jumpHeld) play(l,e,STRUGGLE,.3f);
        else if(moving) play(l,e,MOVE,.18f);
        if(d.material==MaterialProfile.MUD && (moving || d.jumpHeld) && e.getRandom().nextInt(3)==0) {
            var c=art.tiary.mfqm.physics.ContactSampler.sample(l,e);
            l.sendParticles(ParticleTypes.BUBBLE_POP,e.getX(),c.surface()+.025,e.getZ(),2,.25,.01,.25,0);
            play(l,e,BUBBLE,.12f);
        }
    }
}
