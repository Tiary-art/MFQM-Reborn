# 机制族：按代码入口与行为轴分组

证据：01主矩阵、material-instruction-sites.csv、metadata-read-sites.csv及逐类javap。所有定位均带完整方法descriptor和十进制offset。下面是**候选复用组**，不是已证实的物理族全集；不能凭名称或三核心样本确定族数。

39个contact入口产生37个指令指纹；10个没有找到模组contact覆盖的对象列未知组。指纹去除常量池编号但保留操作数/调用目标；指纹不同不能证明算法完全不同，指纹相同也不能证明构造参数、metadata、外部事件等价。两个共享入口对象可能是继承，需独立核对注册构造参数和状态。

机制分类采用多轴：直接Y补偿/位置回退、水平阻碍/web、窒息/伤害、黏污、流体更新、生态/结构触发。这些轴可重叠。已有setStuck/air/hurt/motion字段写入的位置只证明入口存在，不能自动证明玩家在任何深度必定触发。流体类与普通Block不能仅因都减速就共用旧物理profile。

## 复用准入

共享原版算法必须同时关闭：同输入域/坐标框架、实体例外、metadata、装备、RNG消费、事件顺序及副作用。仅数值不同的参数化分支还要从构造/注册实参定位。无证据时保持独立，现代B1安全层可共用，算法层不强行合并。

注册却没有陷落能力的**确定名单尚未形成**；未知组不能冒称非陷落。可选模组和配置分支从各类常量引用/调用图进一步追踪，未闭环不作默认行为。原始材料名（包括流体、装饰、植物、结构）全部保留如下，不按英语名称猜测。

### 候选组 1: Mud

碰撞指令规范化指纹 `eea4bc6d9627ca66359927902c7b16ad97e0d72bfcef9c0e6dac40cf356e504b`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockMud`；入口 `MoreFunQuicksandMod.main.blocks.BlockMud#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..3522`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMud.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMud.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 2: Bog

碰撞指令规范化指纹 `34a17fef7c9a12553e602ff43e4dbe249634da11469455c653d6dd6a39525b03`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockBog`；入口 `MoreFunQuicksandMod.main.liquids.BlockBog#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2728`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockBog.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockBog.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 3: SoftSnow

碰撞指令规范化指纹 `fcc2e2d731adfe2600d9473723209e0b4cd3a1e9579aac729946c88be1ca55bc`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockSoftSnow`；入口 `MoreFunQuicksandMod.main.blocks.BlockSoftSnow#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2019`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSoftSnow.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSoftSnow.txt)；父类 `net.minecraft.block.BlockSnowBlock`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 4: DryQuicksand

碰撞指令规范化指纹 `6c9d67629abc036c5711f9507648218a4136ea62a2d6a540b1de7399f9c016ab`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockSand`；入口 `MoreFunQuicksandMod.main.liquids.BlockSand#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2348`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockSand.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockSand.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 5: SoftQuicksand

碰撞指令规范化指纹 `01c8cfe0f3d7c74ebc715044e8a2133c03bd27c2dfda08babcd19fde70a121a6`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockSoftQuicksand`；入口 `MoreFunQuicksandMod.main.blocks.BlockSoftQuicksand#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2882`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSoftQuicksand.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSoftQuicksand.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 6: Morass

碰撞指令规范化指纹 `ac4f1238f137e57d40fab413f82251afe31e4f452039070c6d135834fb664d99`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockMorass`；入口 `MoreFunQuicksandMod.main.blocks.BlockMorass#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..3052`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMorass.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMorass.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 7: WetPeat

碰撞指令规范化指纹 `3be552d07d5d27de9d3ce5119818006de5f980ad565976768eb79d6930a99727`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockWetPeat`；入口 `MoreFunQuicksandMod.main.blocks.BlockWetPeat#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2325`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockWetPeat.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockWetPeat.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 8: HPeat, SandstoneTrapBlock, HardenedClay, Honeycomb, ChocolateBlock, LureBlock, WaxWood, CustomLilyPad, MoorGrass, LeavesPile

UNKNOWN：未在模组继承链找到contact覆盖，不能证明无陷落。

- `MoreFunQuicksandMod.main.blocks.BlockPeat`；入口 `NONE_DECLARED; external inherited semantics UNKNOWN`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockPeat.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockPeat.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

- `MoreFunQuicksandMod.main.blocks.BlockSandstoneTrap`；入口 `NONE_DECLARED; external inherited semantics UNKNOWN`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSandstoneTrap.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSandstoneTrap.txt)；父类 `net.minecraft.block.BlockSandStone`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

- `MoreFunQuicksandMod.main.blocks.BlockHardenedClay`；入口 `NONE_DECLARED; external inherited semantics UNKNOWN`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockHardenedClay.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockHardenedClay.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

- `MoreFunQuicksandMod.main.blocks.BlockHoneycomb`；入口 `NONE_DECLARED; external inherited semantics UNKNOWN`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockHoneycomb.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockHoneycomb.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

- `MoreFunQuicksandMod.main.blocks.BlockChocolate`；入口 `NONE_DECLARED; external inherited semantics UNKNOWN`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockChocolate.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockChocolate.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

- `MoreFunQuicksandMod.main.blocks.BlockLure`；入口 `NONE_DECLARED; external inherited semantics UNKNOWN`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockLure.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockLure.txt)；父类 `net.minecraft.block.BlockContainer`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

- `MoreFunQuicksandMod.main.blocks.BlockWaxWood`；入口 `NONE_DECLARED; external inherited semantics UNKNOWN`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockWaxWood.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockWaxWood.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

- `MoreFunQuicksandMod.main.blocks.BlockCustomLilyPad`；入口 `NONE_DECLARED; external inherited semantics UNKNOWN`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockCustomLilyPad.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockCustomLilyPad.txt)；父类 `net.minecraft.block.BlockLilyPad`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

- `MoreFunQuicksandMod.main.blocks.BlockMoorGrass`；入口 `NONE_DECLARED; external inherited semantics UNKNOWN`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMoorGrass.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMoorGrass.txt)；父类 `net.minecraft.block.BlockBush`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

- `MoreFunQuicksandMod.main.blocks.BlockLeaves`；入口 `NONE_DECLARED; external inherited semantics UNKNOWN`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockLeaves.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockLeaves.txt)；父类 `net.minecraft.block.BlockBush`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 9: BrownClay

碰撞指令规范化指纹 `67b5ff4dd7e304825e06e03b16056756258c09738bcdd2fa4b1056b84f1a287e`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockBrownClay`；入口 `MoreFunQuicksandMod.main.blocks.BlockBrownClay#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2244`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockBrownClay.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockBrownClay.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 10: Wax

碰撞指令规范化指纹 `8fe1e3efb032c9377561fe958d57b6f13ce41e1ba1f6a09ce0f0da2328f0ef82`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockWax`；入口 `MoreFunQuicksandMod.main.blocks.BlockWax#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..3378`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockWax.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockWax.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 11: Quicksand

碰撞指令规范化指纹 `803d8ce8118661c42edd2e26f0529ab37d420ddb05d66b17749e8ddcb97e032c`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockQuicksand`；入口 `MoreFunQuicksandMod.main.blocks.BlockQuicksand#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2514`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockQuicksand.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockQuicksand.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 12: JungleQuicksand

碰撞指令规范化指纹 `75143e9bf36f816787162e5c0949f8294e1d3bdf0c40da62f5b97c67f5b1004e`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockJungleQuicksand`；入口 `MoreFunQuicksandMod.main.liquids.BlockJungleQuicksand#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2505`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockJungleQuicksand.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockJungleQuicksand.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 13: LiquidMire0, LiquidMire1

碰撞指令规范化指纹 `4cc85c0d14a09961cc00375f5dc0c1670ee8755cd139cb233f9148171739e4e8`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockLiquidMire`；入口 `MoreFunQuicksandMod.main.liquids.BlockLiquidMire#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..1422`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockLiquidMire.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockLiquidMire.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

- `MoreFunQuicksandMod.main.liquids.BlockStableLiquidMire`；入口 `MoreFunQuicksandMod.main.liquids.BlockStableLiquidMire#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..1422`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockStableLiquidMire.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockStableLiquidMire.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 14: SinkyLiquid

碰撞指令规范化指纹 `72effa38beb3c7e529c521b0cbeb48cd953192f822aeada47e0a9caf5c6dc56c`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockSinkyLiquid`；入口 `MoreFunQuicksandMod.main.liquids.BlockSinkyLiquid#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..1429`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockSinkyLiquid.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockSinkyLiquid.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 15: SinkingSlime

碰撞指令规范化指纹 `8c11d2c317b5b75f6a15225017869ce2b32bde96e36cfc315f79639ab163616f`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockSlime`；入口 `MoreFunQuicksandMod.main.liquids.BlockSlime#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2930`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockSlime.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockSlime.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 16: Mucus

碰撞指令规范化指纹 `d8fbbcf32ea2b5681c956603e67ae5d3686582d28c62bf810415102aa0f9009b`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockMucus`；入口 `MoreFunQuicksandMod.main.liquids.BlockMucus#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..3090`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockMucus.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockMucus.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 17: Mire

碰撞指令规范化指纹 `a482e2571c4516ed657c381416e039c302e1fa2f9e9a54c4a3e9099bd5c7f134`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockMire`；入口 `MoreFunQuicksandMod.main.blocks.BlockMire#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..3758`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMire.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMire.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 18: Moor, Tendrils

碰撞指令规范化指纹 `53a0dd00a1d25bb1a6146f4be4c4cafb8a338da7c1c0e21acba758b0a0d4b1d3`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockMoor`；入口 `MoreFunQuicksandMod.main.blocks.BlockMoor#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..5`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMoor.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMoor.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

- `MoreFunQuicksandMod.main.blocks.BlockTent`；入口 `MoreFunQuicksandMod.main.blocks.BlockTent#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..5`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockTent.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockTent.txt)；父类 `net.minecraft.block.BlockBush`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 19: SinkingClay

碰撞指令规范化指纹 `cecf44db80ea0a2297528bffc28fdd2b2c181cedc7a136ab2fb07fd4e7fce716`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockSinkingClay`；入口 `MoreFunQuicksandMod.main.blocks.BlockSinkingClay#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..3773`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSinkingClay.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSinkingClay.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 20: TangleRootMoss

碰撞指令规范化指纹 `a82cfef39d007c0cd61dafeb2b7ad89cf966315078571c3de269282405771af5`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockMoss`；入口 `MoreFunQuicksandMod.main.blocks.BlockMoss#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2907`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMoss.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMoss.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 21: DenseWebbing

碰撞指令规范化指纹 `115a87f8fa79a85640588fdcbe6002c03aefb5895ed1493258b6c12116c7a995`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockDenseWeb`；入口 `MoreFunQuicksandMod.main.blocks.BlockDenseWeb#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2633`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockDenseWeb.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockDenseWeb.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 22: Tar

碰撞指令规范化指纹 `2cc6c1676b8e48abe22bc16c5cae5ae0204bbb2d1114650fcc1e9c9e5cf2fbcc`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockTar`；入口 `MoreFunQuicksandMod.main.liquids.BlockTar#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..3519`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockTar.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockTar.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 23: Larvae

碰撞指令规范化指纹 `355bc748a564002221b0ce338e6a31f88882f7b7f64389c1a2d18729b6b47f21`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockLarvae`；入口 `MoreFunQuicksandMod.main.blocks.BlockLarvae#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2455`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockLarvae.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockLarvae.txt)；父类 `net.minecraft.block.BlockContainer`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 24: CorruptedSand

碰撞指令规范化指纹 `c40e0d9d24030765cd79a1c0df32b9089c085192165c708955d9cb8f719e48c8`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockCorruptedSand`；入口 `MoreFunQuicksandMod.main.blocks.BlockCorruptedSand#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2387`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockCorruptedSand.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockCorruptedSand.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 25: SwallowingFlesh

碰撞指令规范化指纹 `517fdefc0be3d033c631f8ba4bd3a76834ccc51c1fc2622abf83337751bd5bf9`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockSwallowingFlesh`；入口 `MoreFunQuicksandMod.main.blocks.BlockSwallowingFlesh#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2502`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSwallowingFlesh.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSwallowingFlesh.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 26: Acid

碰撞指令规范化指纹 `3c49c755acbfca264a04d6fd88855038020512c0feafccb490af627728477d90`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockAcid`；入口 `MoreFunQuicksandMod.main.liquids.BlockAcid#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..1594`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockAcid.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockAcid.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 27: Slurry

碰撞指令规范化指纹 `27c3c822fd2e112c4018df92e41a54082a08c9f295de088db2c69f4d49f73019`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockSlurry`；入口 `MoreFunQuicksandMod.main.liquids.BlockSlurry#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2935`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockSlurry.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockSlurry.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 28: Gas

碰撞指令规范化指纹 `333c58890b58bba3fe3a447ffcdb70b1f8cadc34b2290938c16fd32d49685315`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockGas`；入口 `MoreFunQuicksandMod.main.blocks.BlockGas#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..1349`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockGas.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockGas.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 29: SoftGravel

碰撞指令规范化指纹 `6e57ff13fc5258aefb4826663ec0f77388ce1046ba56fefa0b45fba86aacd7b6`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockSoftGravel`；入口 `MoreFunQuicksandMod.main.blocks.BlockSoftGravel#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2930`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSoftGravel.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSoftGravel.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 30: Honey

碰撞指令规范化指纹 `d1baca5f1860633db58cc702e0ef142bf1c333cf191a0e64ed2ab4230d6571c1`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockHoney`；入口 `MoreFunQuicksandMod.main.liquids.BlockHoney#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2643`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockHoney.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockHoney.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 31: SolidHoney

碰撞指令规范化指纹 `4e175b4adef21c9f67f29f9c7f0afd645fa9f3e7f3ce670e58fc2d34c6da36ef`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockSolidHoney`；入口 `MoreFunQuicksandMod.main.blocks.BlockSolidHoney#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..291`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSolidHoney.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSolidHoney.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 32: LiquidChocolate

碰撞指令规范化指纹 `2d322aa4c4747767f08ea204e86e08a15e6377ca8a7f4c4b2faa729c4073c85d`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.liquids.BlockLiquidChocolate`；入口 `MoreFunQuicksandMod.main.liquids.BlockLiquidChocolate#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2253`；[evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockLiquidChocolate.txt](evidence/bytecode/MoreFunQuicksandMod__main__liquids__BlockLiquidChocolate.txt)；父类 `net.minecraftforge.fluids.BlockFluidClassic`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 33: SinkingRug

碰撞指令规范化指纹 `e281965b873dcdee23afaa71f01b1477ab83528b06155c3071ed101c3d2ffd07`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockSinkingWool`；入口 `MoreFunQuicksandMod.main.blocks.BlockSinkingWool#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..2680`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSinkingWool.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockSinkingWool.txt)；父类 `net.minecraft.block.BlockColored`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 34: BlossomBlock

碰撞指令规范化指纹 `253373ae17d1b981995fc7f164d0dd92c389dc82f9f7f5f83817bcf9ab97c221`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockBlossom`；入口 `MoreFunQuicksandMod.main.blocks.BlockBlossom#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..36`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockBlossom.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockBlossom.txt)；父类 `net.minecraft.block.BlockContainer`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 35: BlossomBlockSlab

碰撞指令规范化指纹 `cbc41aa01cfe19a01abf9dfef063a31e0314a78569a0a94b0e4a6e6a5af0e801`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockBlossomSlab`；入口 `MoreFunQuicksandMod.main.blocks.BlockBlossomSlab#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..136`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockBlossomSlab.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockBlossomSlab.txt)；父类 `net.minecraft.block.Block`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 36: TempVore

碰撞指令规范化指纹 `0419de731c85527c16332e87aa0a92ec8c15a094bfc03e267c6592234e01d0bb`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockVoreHole`；入口 `MoreFunQuicksandMod.main.blocks.BlockVoreHole#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..1387`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockVoreHole.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockVoreHole.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。

### 候选组 37: MeatWall

碰撞指令规范化指纹 `9a25ba9250d19c005aa2318b12ce7b060285a316ef8c3b213b1581fec02209f2`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockMeat`；入口 `MoreFunQuicksandMod.main.blocks.BlockMeat#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..260`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMeat.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMeat.txt)；父类 `net.minecraft.block.BlockContainer`；污渍 `UNKNOWN_INHERITED_OR_EXTERNAL`。

### 候选组 38: TempMeat

碰撞指令规范化指纹 `f51c95dd48dca0505dfdfba0eadd55e3237dd0912150334fe0785a50795c85b2`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。

- `MoreFunQuicksandMod.main.blocks.BlockMeatHole`；入口 `MoreFunQuicksandMod.main.blocks.BlockMeatHole#func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V@0..1491`；[evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMeatHole.txt](evidence/bytecode/MoreFunQuicksandMod__main__blocks__BlockMeatHole.txt)；父类 `net.minecraft.block.Block`；污渍 `CONDITIONAL_DIRECT_CALL`。
