package art.tiary.mfqm.registry;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.content.LegacyCatalog;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.world.item.CreativeModeTab;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;

public final class ModTabs {
    public static final DeferredRegister<CreativeModeTab> TABS=DeferredRegister.create(Registries.CREATIVE_MODE_TAB,MfqmReborn.MOD_ID);
    public static final RegistryObject<CreativeModeTab> CONTENT=TABS.register("materials",()->CreativeModeTab.builder()
            .title(Component.translatable("itemGroup.mfqm")).icon(()->new ItemStack(ModItems.QUICKSAND.get()))
            .displayItems((params,out)->{
                for (var kind : LegacyCatalog.Kind.values()) for (var s : LegacyCatalog.ALL)
                    if (s.visible() && !s.id().equals("sandstone_trap") && s.kind()==kind) out.accept(ModItems.LEGACY.get(s.id()).get());
                for(var f:art.tiary.mfqm.content.LegacyFluids.ALL.values()) out.accept(f.bucket().get());
                for (int depth = 1; depth <= 3; depth++) {
                    var stack = new ItemStack(ModItems.MUD.get());
                    stack.getOrCreateTagElement("BlockStateTag").putString("depth", Integer.toString(depth));
                    out.accept(stack);
                }
                for (var item : ModItems.RESTORED) out.accept(item.get());
            }).build());
    private ModTabs() { }
}
