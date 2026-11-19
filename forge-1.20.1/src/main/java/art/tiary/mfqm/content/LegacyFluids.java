package art.tiary.mfqm.content;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.physics.*;
import art.tiary.mfqm.registry.*;
import java.util.*;
import net.minecraft.core.BlockPos;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.*;
import net.minecraft.world.item.*;
import net.minecraft.world.level.*;
import net.minecraft.world.level.block.*;
import net.minecraft.world.level.block.state.*;
import net.minecraft.world.level.material.*;
import net.minecraftforge.client.extensions.common.IClientFluidTypeExtensions;
import net.minecraftforge.fluids.*;
import net.minecraftforge.registries.*;

/** Thirteen original fluid families. Transport is modern Forge behavior, not recovered legacy viscosity parity. */
public final class LegacyFluids {
    public static final DeferredRegister<FluidType> TYPES=DeferredRegister.create(ForgeRegistries.Keys.FLUID_TYPES,MfqmReborn.MOD_ID);
    public static final DeferredRegister<Fluid> FLUIDS=DeferredRegister.create(ForgeRegistries.FLUIDS,MfqmReborn.MOD_ID);
    public record Family(LegacyCatalog.Spec spec,RegistryObject<FluidType> type,RegistryObject<FlowingFluid> source,
                         RegistryObject<FlowingFluid> flowing,RegistryObject<Item> bucket) {}
    public static final Map<String,Family> ALL=new LinkedHashMap<>();
    static {
        for(var s:LegacyCatalog.ALL) if(!s.fluid().isEmpty()) {
            RegistryObject<FluidType> type=TYPES.register(s.id(),()->new MaterialType(s));
            RegistryObject<FlowingFluid> source=FLUIDS.register(s.id(),()->new ForgeFlowingFluid.Source(properties(s.id())));
            RegistryObject<FlowingFluid> flowing=FLUIDS.register("flowing_"+s.id(),()->new ForgeFlowingFluid.Flowing(properties(s.id())));
            RegistryObject<Item> bucket=ModItems.ITEMS.register(s.id()+"_bucket",()->new BucketItem(source,new Item.Properties().craftRemainder(Items.BUCKET).stacksTo(1)));
            ALL.put(s.id(),new Family(s,type,source,flowing,bucket));
        }
    }
    private static ForgeFlowingFluid.Properties properties(String id) {
        var f=ALL.get(id);
        return new ForgeFlowingFluid.Properties(f.type(),f.source(),f.flowing()).bucket(f.bucket())
            .block(()->(LiquidBlock)ModBlocks.LEGACY.get(id).get()).tickRate(20).slopeFindDistance(2).levelDecreasePerBlock(2).explosionResistance(100);
    }
    public static final class MaterialType extends FluidType {
        private final LegacyCatalog.Spec spec;
        MaterialType(LegacyCatalog.Spec s) {
            super(Properties.create().descriptionId("block.mfqm."+s.id()).canSwim(false).canDrown(false)
                .canPushEntity(false).canConvertToSource(false).canExtinguish(false).canHydrate(false)
                .supportsBoating(false).density(1500).viscosity(6000).motionScale(0).lightLevel(s.emission())); spec=s;
        }
        @Override public void initializeClient(java.util.function.Consumer<IClientFluidTypeExtensions> consumer) {
            consumer.accept(new IClientFluidTypeExtensions() {
                @Override public ResourceLocation getStillTexture() { return art.tiary.mfqm.client.OriginalTextureBindings.fluid(spec.id(), false); }
                @Override public ResourceLocation getFlowingTexture() { return art.tiary.mfqm.client.OriginalTextureBindings.fluid(spec.id(), true); }
                @Override public int getTintColor() {
                    if (art.tiary.mfqm.client.OriginalTextureBindings.hasFluid(spec.id())) return 0xffffffff;
                    return switch(spec.id()) { case "acid"->0xffa0bd37;case "honey"->0xffc18c27;case "liquid_chocolate"->0xff613923;
                        case "tar"->0xff272627;case "sinking_slime","mucus"->0xff71964b;case "dry_quicksand"->0xffd4c58f;
                        default->0xff6e6443; };
                }
            });
        }
    }
    public static final class MaterialLiquid extends LiquidBlock implements SinkingMedium {
        private final LegacyCatalog.Spec spec;
        public MaterialLiquid(LegacyCatalog.Spec s,BlockBehaviour.Properties p) {
            super(ALL.get(s.id()).source(),p.noCollission().noOcclusion().replaceable().liquid()
                .isSuffocating((a,b,c)->false).isViewBlocking((a,b,c)->false)); spec=s;
        }
        @Override public MaterialProfile profile() { return spec.profile(); }
        @Override public double motionScale() { return spec.motionScale(); }
        @Override public double surfaceHeight(BlockState s,BlockGetter l,BlockPos p) { return s.getFluidState().getHeight(l,p); }
        @Override public void entityInside(BlockState s,Level l,BlockPos p,Entity e) {
            if(!l.isClientSide && spec.damage()>0 && e instanceof LivingEntity living && living.tickCount%20==0)
                living.hurt(l.damageSources().magic(),spec.damage());
        }
    }
}
