package art.tiary.mfqm.state;

import art.tiary.mfqm.MfqmReborn;
import net.minecraft.core.Direction;
import net.minecraft.nbt.CompoundTag;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.LivingEntity;
import net.minecraftforge.common.capabilities.AutoRegisterCapability;
import net.minecraftforge.common.capabilities.Capability;
import net.minecraftforge.common.capabilities.CapabilityManager;
import net.minecraftforge.common.capabilities.CapabilityToken;
import net.minecraftforge.common.capabilities.ICapabilitySerializable;
import net.minecraftforge.common.util.LazyOptional;
import net.minecraftforge.event.AttachCapabilitiesEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

@Mod.EventBusSubscriber(modid = MfqmReborn.MOD_ID)
public final class SinkCapability {
    @AutoRegisterCapability
    public interface Storage { SinkState state(); }
    public static final Capability<Storage> CAP = CapabilityManager.get(new CapabilityToken<>() { });
    public static final ResourceLocation ID = new ResourceLocation(MfqmReborn.MOD_ID, "sink_state");
    private SinkCapability() { }

    public static SinkState get(LivingEntity entity) {
        return entity.getCapability(CAP).map(Storage::state).orElse(null);
    }

    @SubscribeEvent
    public static void attach(AttachCapabilitiesEvent<Entity> event) {
        if (!(event.getObject() instanceof LivingEntity living)) return;
        Provider provider = new Provider(living);
        event.addCapability(ID, provider);
        event.addListener(provider::invalidate);
    }

    private static final class Provider implements ICapabilitySerializable<CompoundTag> {
        private final LivingEntity owner;
        private final SinkState state = new SinkState();
        private LazyOptional<Storage> optional = LazyOptional.of(() -> () -> state);
        Provider(LivingEntity owner) { this.owner = owner; }
        @Override public <T> @NotNull LazyOptional<T> getCapability(@NotNull Capability<T> cap, @Nullable Direction side) {
            if (cap != CAP) return LazyOptional.empty();
            // Forge revives the same ServerPlayer dispatcher during dimension transfer.
            // The outer CapabilityProvider blocks queries while invalid; once revived,
            // issue a new handle without reviving any previously invalidated handle.
            if (!optional.isPresent()) optional = LazyOptional.of(() -> () -> state);
            return optional.cast();
        }
        @Override public CompoundTag serializeNBT() { return state.save(); }
        @Override public void deserializeNBT(CompoundTag nbt) { state.load(nbt); }
        void invalidate() {
            art.tiary.mfqm.integration.StuckAdapter.clear(owner);
            art.tiary.mfqm.physics.SinkEngine.removeModifier(owner);
            state.resetTransient();
            optional.invalidate();
        }
    }
}
