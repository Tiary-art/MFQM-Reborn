# 全量 Block 实装矩阵

基线 main c399b3b，静态 registerBlock 调用逐项复核 **49**，另有开发方块1个；13个 Fluid 名称单列，不计作额外旧 Block。无旧实例 registry dump，数量代表可证实调用，不承诺旧环境加载结果。完整属性、缺口和置信度见 [CSV](block-implementation-matrix.csv) 与 [证据数据](catalog-evidence.json)。

最终状态按实际行为保守标注；49 个注册项不等于49个完整复刻。PARTIAL 不代表完整复刻。所有 registerBlock 使用默认或显式 ItemBlock 类，未见 null ItemBlock；技术方块保留物品形式但隐藏创造栏。无新增自然生成。

|旧ID / 类|现代ID|类别；形状/碰撞|状态|缺口|
|---|---|---|---|---|
|Mud / BlockMud|`mfqm:mud`|SINKING; h=1; none|PARTIAL|核心运动可实测；旧曲线未测定；下移调度、混合边界、跨模组视觉兼容仍有缺口|
|Bog / BlockBog|`mfqm:bog`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|SoftSnow / BlockSoftSnow|`mfqm:soft_snow`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|DryQuicksand / BlockSand|`mfqm:dry_quicksand`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|SoftQuicksand / BlockSoftQuicksand|`mfqm:soft_quicksand`|SINKING; h=0.85; none|PARTIAL|核心运动可实测；旧曲线未测定；下移调度、混合边界、跨模组视觉兼容仍有缺口|
|Morass / BlockMorass|`mfqm:morass`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|WetPeat / BlockWetPeat|`mfqm:wet_peat`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|HPeat / BlockPeat|`mfqm:h_peat`|SOLID; h=1; solid|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|BrownClay / BlockBrownClay|`mfqm:brown_clay`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|Wax / BlockWax|`mfqm:wax`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|Quicksand / BlockQuicksand|`mfqm:quicksand`|SINKING; h=1; none|PARTIAL|核心运动可实测；旧曲线未测定；下移调度、混合边界、跨模组视觉兼容仍有缺口|
|SandstoneTrapBlock / BlockSandstoneTrap|`mfqm:sandstone_trap`|TRAP; h=1; solid|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|JungleQuicksand / BlockJungleQuicksand|`mfqm:jungle_quicksand`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|LiquidMire0 / BlockLiquidMire|`mfqm:liquid_mire`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|LiquidMire1 / BlockStableLiquidMire|`mfqm:stable_liquid_mire`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|SinkyLiquid / BlockSinkyLiquid|`mfqm:sinky_liquid`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|SinkingSlime / BlockSlime|`mfqm:sinking_slime`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|Mucus / BlockMucus|`mfqm:mucus`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|Mire / BlockMire|`mfqm:mire`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|Moor / BlockMoor|`mfqm:moor`|SOLID; h=1; solid|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|HardenedClay / BlockHardenedClay|`mfqm:hardened_clay`|SOLID; h=1; solid|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|SinkingClay / BlockSinkingClay|`mfqm:sinking_clay`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|TangleRootMoss / BlockMoss|`mfqm:tangle_root_moss`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|DenseWebbing / BlockDenseWeb|`mfqm:dense_webbing`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|Tar / BlockTar|`mfqm:tar`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|Larvae / BlockLarvae|`mfqm:larvae`|DEPENDENT; h=1; solid|REGISTERED_ONLY|原版 TileEntity/实体/传播或气体伤害系统未恢复；当前基础方块仅保证注册、物品与资源占位|
|CorruptedSand / BlockCorruptedSand|`mfqm:corrupted_sand`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|SwallowingFlesh / BlockSwallowingFlesh|`mfqm:swallowing_flesh`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|Acid / BlockAcid|`mfqm:acid`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|Slurry / BlockSlurry|`mfqm:slurry`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|Gas / BlockGas|`mfqm:gas`|GAS; h=1; none|REGISTERED_ONLY|原版 TileEntity/实体/传播或气体伤害系统未恢复；当前基础方块仅保证注册、物品与资源占位|
|SoftGravel / BlockSoftGravel|`mfqm:soft_gravel`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|Honey / BlockHoney|`mfqm:honey`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|SolidHoney / BlockSolidHoney|`mfqm:solid_honey`|SOLID; h=1; inset .025|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|Honeycomb / BlockHoneycomb|`mfqm:honeycomb`|SOLID; h=1; solid|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|LiquidChocolate / BlockLiquidChocolate|`mfqm:liquid_chocolate`|VISCOUS; h=1; none|PARTIAL|真实 Forge 流体/源/流动/桶已实现；现代默认流动参数，旧版黏度曲线、混合反应与特效未完整复刻|
|ChocolateBlock / BlockChocolate|`mfqm:chocolate`|SOLID; h=1; solid|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|SinkingRug / BlockSinkingWool|`mfqm:sinking_rug`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|LureBlock / BlockLure|`mfqm:lure_block`|DEPENDENT; h=1; solid|REGISTERED_ONLY|原版 TileEntity/实体/传播或气体伤害系统未恢复；当前基础方块仅保证注册、物品与资源占位|
|BlossomBlock / BlockBlossom|`mfqm:blossom`|DEPENDENT; h=1; solid|REGISTERED_ONLY|原版 TileEntity/实体/传播或气体伤害系统未恢复；当前基础方块仅保证注册、物品与资源占位|
|BlossomBlockSlab / BlockBlossomSlab|`mfqm:blossom_slab`|SLAB; h=0.5; slab|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|TempVore / BlockVoreHole|`mfqm:temp_vore`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|MeatWall / BlockMeat|`mfqm:meat_wall`|DEPENDENT; h=1; solid|REGISTERED_ONLY|原版 TileEntity/实体/传播或气体伤害系统未恢复；当前基础方块仅保证注册、物品与资源占位|
|TempMeat / BlockMeatHole|`mfqm:temp_meat`|SINKING; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|WaxWood / BlockWaxWood|`mfqm:wax_wood`|SOLID; h=1; solid|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|CustomLilyPad / BlockCustomLilyPad|`mfqm:custom_lily_pad`|LILY; h=0.0625; vanilla lily|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|MoorGrass / BlockMoorGrass|`mfqm:moor_grass`|PLANT; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|Tendrils / BlockTent|`mfqm:tendrils`|PLANT; h=1; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|
|LeavesPile / BlockLeaves|`mfqm:leaves_pile`|LEAVES; h=0.015625; none|PARTIAL|Legacy curve/meta, special drops and interactions need per-class parity validation; vanilla texture placeholder.|

## 13个旧 Fluid：独立核对

|旧 Fluid 名称|旧 Block / 现代关系|当前状态|
|---|---|---|
|Bog|BlockBog / `mfqm:bog`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|SandFluid|BlockSand / `mfqm:dry_quicksand`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|JungleQuicksand|BlockJungleQuicksand / `mfqm:jungle_quicksand`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|LiquidMire|BlockLiquidMire / `mfqm:liquid_mire`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|LiquidMireS|BlockStableLiquidMire / `mfqm:stable_liquid_mire`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|SinkyFluid|BlockSinkyLiquid / `mfqm:sinky_liquid`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|SlimeFluid|BlockSlime / `mfqm:sinking_slime`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|MucusFluid|BlockMucus / `mfqm:mucus`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|Tar|BlockTar / `mfqm:tar`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|AcidFluid|BlockAcid / `mfqm:acid`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|Slurry|BlockSlurry / `mfqm:slurry`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|Honey|BlockHoney / `mfqm:honey`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
|LiquidChocolate|BlockLiquidChocolate / `mfqm:liquid_chocolate`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|
