# 01 — JAR 只读盘点

本报告为 2026-11-17 静态分析。原始 JAR 未执行，未启动 Minecraft，未验证运行时表现。高置信度表示归档/指令直接支持；中置信度表示反编译控制流与旧版 SRG 名称解释，仍需旧版实机复核；设计建议不代表旧版事实。所有方法描述符与十进制字节码偏移见 `evidence/*bytecode.txt`；`*.analysis.txt` 是 CFR 0.152 反编译的带行号分析文本，不是原始源码，也不是新版实现。

## 输入与完整性

- 原文件：`[更多流沙] MoreFunQuicksandMod-1.1.1-1.7.10.jar`
- 字节数：1,644,655；ZIP 条目：484（文件 463、目录 21）；类 161；方法 1955。
- 分析前 SHA-256：`2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。分析后记录见 `evidence/audit.json` 与包内 README。
- ZIP CRC 校验将在打包前执行。未覆盖原文件，未提取原始纹理到交付包，未构建或发布移植版。
- Java class 文件、各资源的大小、CRC32、SHA-256 逐项列于 [archive_entries.csv](../evidence/archive_entries.csv)；类及父类见 [classes.csv](../evidence/classes.csv)，方法见 [methods.csv](../evidence/methods.csv)。

## 归档结构

| 类别 | 实测数量 |
| --- | --- |
| class | 161 |
| 方块 PNG | 162 |
| 物品 PNG | 54 |
| 实体 PNG（含 mudOverlays） | 25 |
| 盔甲 PNG | 5 |
| Logo PNG | 1 |
| PNG 合计 | 247 |
| 动画 mcmeta | 48 |
| 语言文件 | 2 |
| OGG | 2 |
| sounds.json | 1 |

## 元数据与依赖

`mcmod.info`：modid `MFQM`，version `1.1.1`，Minecraft `1.7.10`；assets namespace 为 `morefunquicksandmod`。三种名称不能混用。原始文本保存在 evidence。主类 `@Mod` 注解仅给出 modid/name/version，没有 `dependencies=` 硬依赖声明。

元数据列出 Biomes O' Plenty，但 `MFQM.preInit` 在配置 BoP 开启后检查 `Loader.isModLoaded("BiomesOPlenty")`，缺失时走兼容关闭/替代资源路径；`postInit` 在 `!BoP` 分支注册 Emptycomb/HoneycombItem。因此静态证据支持“可选兼容”，不支持仅凭 mcmod.info 宣称必装。仍需用无 BOP 的 1.7.10 独立服务端启动验证类加载与配置路径。

其他探测：TwilightForest、thebetweenlands、abyssalcraft、nolpfij_wildycraft、nevermine、ExtraUtilities；另有注册表扫描/名字匹配和肥料转换路径。完整配置键、默认值与上下文见 [config_and_compatibility.txt](../evidence/config_and_compatibility.txt)，外部类常量池引用见 [external_class_references.txt](../evidence/external_class_references.txt)。后者为空表示未发现过滤后的其他直接类引用，不表示不存在通过字符串或反射实现的兼容。

## 语言、音效与配方

- `assets/morefunquicksandmod/lang/en_US.lang`（8976 字节）
- `assets/morefunquicksandmod/lang/ru_RU.lang`（13149 字节）
- `assets/morefunquicksandmod/sounds/mob/bee/hurt.ogg`（14387 字节）
- `assets/morefunquicksandmod/sounds/mob/bee/say.ogg`（40650 字节）
- `assets/morefunquicksandmod/sounds.json`（190 字节）

`sounds.json` 原文：

```json
{
  "mob.bee.hurt": {
    "category": "hostile",
    "sounds": [
      "mob/bee/hurt"
    ]
  },
  "mob.bee.say": {
    "category": "hostile",
    "sounds": [
      "mob/bee/say"
    ]
  }
}
```

语言文件原样附在 evidence；`MFQM` 另通过 `LanguageRegistry.addName/addStringLocalization` 注册英文名，语言文件条目不等于内容注册表。音效还调用原版 `game.player.swim`、`mob.slime.attack`、`mob.magmacube.jump` 等键，不能用 OGG 数量推断所有播放行为。

旧版配方以代码注册，没有现代 `data/*/recipes/*.json`。全部配方调用、熔炼、燃料入口与附近条件见 [recipe_calls.txt](../evidence/recipe_calls.txt)；完整 MFQM 分析文本可复核循环。方块、物品、实体、流体的静态注册调用与资源名分开列在报告 03。

## 反编译边界

CFR 0.152，工具 SHA-256：`f686e8f3ded377d7bc87d216a90e9e9512df4156e75b06c655a16648ae8765b2`，来源 https://www.benf.org/other/cfr/cfr-0.152.jar 。仅静态读取 JAR。Jawa 用于直接解析 class 并输出指令、常量引用及偏移。缺少 Minecraft/Forge 类路径，反编译中的 `Could not load` 不表示原 Mod 在正确环境下无法运行。

CFR 对 `CustomWorldGen.generateAOADimGardencia/generateWLD/generateABC2/generateNether/generateSurface` 的控制流报告 “Unable to fully structure code”；这五处不当作可直接编译或完全可靠的源代码。原始指令已全部保存。

## 未解决问题与下一步

- 运行时注册成功、客户端资源加载失败、无 BOP 启动、多人表现均尚未实测。建议下一次仍先在隔离的 1.7.10 测试实例记录基线。
- 注册调用并不保证获取途径、创造栏可见或自然生成；不可用资源需结合运行时 atlas/日志确认。
- 许可证未提供；发布前按报告 06 核查。新版工程与重绘需单独授权。

## 附录：全部类

- `MoreFunQuicksandMod/main/AirEvent.class`
- `MoreFunQuicksandMod/main/blocks/BlockBlossom.class`
- `MoreFunQuicksandMod/main/blocks/BlockBlossomSlab.class`
- `MoreFunQuicksandMod/main/blocks/BlockBrownClay.class`
- `MoreFunQuicksandMod/main/blocks/BlockCorruptedSand.class`
- `MoreFunQuicksandMod/main/blocks/BlockCustomLilyPad.class`
- `MoreFunQuicksandMod/main/blocks/BlockDenseWeb.class`
- `MoreFunQuicksandMod/main/blocks/BlockHardenedClay.class`
- `MoreFunQuicksandMod/main/blocks/BlockLarvae.class`
- `MoreFunQuicksandMod/main/blocks/BlockLure.class`
- `MoreFunQuicksandMod/main/blocks/BlockMeat.class`
- `MoreFunQuicksandMod/main/blocks/BlockMeatHole.class`
- `MoreFunQuicksandMod/main/blocks/BlockMire.class`
- `MoreFunQuicksandMod/main/blocks/BlockMoor.class`
- `MoreFunQuicksandMod/main/blocks/BlockMoorGrass.class`
- `MoreFunQuicksandMod/main/blocks/BlockMorass.class`
- `MoreFunQuicksandMod/main/blocks/BlockMoss.class`
- `MoreFunQuicksandMod/main/blocks/BlockMud.class`
- `MoreFunQuicksandMod/main/blocks/BlockPeat.class`
- `MoreFunQuicksandMod/main/blocks/BlockQuicksand.class`
- `MoreFunQuicksandMod/main/blocks/BlockSinkingClay.class`
- `MoreFunQuicksandMod/main/blocks/BlockSinkingWool.class`
- `MoreFunQuicksandMod/main/blocks/BlockSoftQuicksand.class`
- `MoreFunQuicksandMod/main/blocks/BlockSoftSnow.class`
- `MoreFunQuicksandMod/main/blocks/BlockSwallowingFlesh.class`
- `MoreFunQuicksandMod/main/blocks/BlockVoreHole.class`
- `MoreFunQuicksandMod/main/blocks/BlockWax.class`
- `MoreFunQuicksandMod/main/blocks/BlockWaxWood.class`
- `MoreFunQuicksandMod/main/blocks/BlockWetPeat.class`
- `MoreFunQuicksandMod/main/blocks/ItemMeta.class`
- `MoreFunQuicksandMod/main/blocks/ItemMetaColor.class`
- `MoreFunQuicksandMod/main/client/ClientProxy.class`
- `MoreFunQuicksandMod/main/client/CustomRenderOverlayEvent.class`
- `MoreFunQuicksandMod/main/client/CustomRenderPlayerEvent.class`
- `MoreFunQuicksandMod/main/client/ModelVoreSlime.class`
- `MoreFunQuicksandMod/main/client/MudModelRenderer.class`
- `MoreFunQuicksandMod/main/client/RenderBubble.class`
- `MoreFunQuicksandMod/main/client/RenderFish2.class`
- `MoreFunQuicksandMod/main/client/RenderFish3.class`
- `MoreFunQuicksandMod/main/client/RenderLongStick.class`
- `MoreFunQuicksandMod/main/client/RenderMuddyBlob.class`
- `MoreFunQuicksandMod/main/client/RenderSlimeHole.class`
- `MoreFunQuicksandMod/main/client/RenderTarSlime.class`
- `MoreFunQuicksandMod/main/client/RenderVoreSlime.class`
- `MoreFunQuicksandMod/main/CommonProxy.class`
- `MoreFunQuicksandMod/main/CreativeTabsMFQM.class`
- `MoreFunQuicksandMod/main/CustomBucketEvent.class`
- `MoreFunQuicksandMod/main/CustomFuelHandler.class`
- `MoreFunQuicksandMod/main/CustomGenerationEvent.class`
- `MoreFunQuicksandMod/main/CustomMaterialLiquid.class`
- `MoreFunQuicksandMod/main/CustomPotionEvent.class`
- `MoreFunQuicksandMod/main/CustomRegister.class`
- `MoreFunQuicksandMod/main/CustomVarPlayer.class`
- `MoreFunQuicksandMod/main/CustomWorldGen.class`
- `MoreFunQuicksandMod/main/CustomWorldGenLakes.class`
- `MoreFunQuicksandMod/main/entity/EntityBubble.class`
- `MoreFunQuicksandMod/main/entity/EntityHook.class`
- `MoreFunQuicksandMod/main/entity/EntityLongStick.class`
- `MoreFunQuicksandMod/main/entity/EntityMuddyBlob.class`
- `MoreFunQuicksandMod/main/entity/EntityRope.class`
- `MoreFunQuicksandMod/main/entity/EntitySlimeHole.class`
- `MoreFunQuicksandMod/main/entity/EntityTarSlime.class`
- `MoreFunQuicksandMod/main/entity/EntityVoreSlime.class`
- `MoreFunQuicksandMod/main/Fields.class`
- `MoreFunQuicksandMod/main/GenerateDesertTombs.class`
- `MoreFunQuicksandMod/main/GenerateMucusBlossom.class`
- `MoreFunQuicksandMod/main/HookMessage$Handler.class`
- `MoreFunQuicksandMod/main/HookMessage.class`
- `MoreFunQuicksandMod/main/items/ItemAcidBucket.class`
- `MoreFunQuicksandMod/main/items/ItemBogBucket.class`
- `MoreFunQuicksandMod/main/items/ItemCable.class`
- `MoreFunQuicksandMod/main/items/ItemClayBucket.class`
- `MoreFunQuicksandMod/main/items/ItemCranberry.class`
- `MoreFunQuicksandMod/main/items/ItemGrapplingHook.class`
- `MoreFunQuicksandMod/main/items/ItemGrapplingHookBRK.class`
- `MoreFunQuicksandMod/main/items/ItemLifeJacket.class`
- `MoreFunQuicksandMod/main/items/ItemLongStick.class`
- `MoreFunQuicksandMod/main/items/ItemMireBucket.class`
- `MoreFunQuicksandMod/main/items/ItemMucusBucket.class`
- `MoreFunQuicksandMod/main/items/ItemMyPotion.class`
- `MoreFunQuicksandMod/main/items/ItemPreWadingBoots0.class`
- `MoreFunQuicksandMod/main/items/ItemPreWadingBoots1.class`
- `MoreFunQuicksandMod/main/items/ItemQuicksandBucket.class`
- `MoreFunQuicksandMod/main/items/ItemRope.class`
- `MoreFunQuicksandMod/main/items/ItemSandBucket.class`
- `MoreFunQuicksandMod/main/items/ItemSlimeBucket.class`
- `MoreFunQuicksandMod/main/items/ItemTarBucket.class`
- `MoreFunQuicksandMod/main/items/ItemWadingBoots.class`
- `MoreFunQuicksandMod/main/items/ItemWaxPiece.class`
- `MoreFunQuicksandMod/main/liquids/AcidFluid.class`
- `MoreFunQuicksandMod/main/liquids/BlockAcid.class`
- `MoreFunQuicksandMod/main/liquids/BlockBog.class`
- `MoreFunQuicksandMod/main/liquids/BlockJungleQuicksand.class`
- `MoreFunQuicksandMod/main/liquids/BlockLiquidMire.class`
- `MoreFunQuicksandMod/main/liquids/BlockMucus.class`
- `MoreFunQuicksandMod/main/liquids/BlockSand.class`
- `MoreFunQuicksandMod/main/liquids/BlockSlime.class`
- `MoreFunQuicksandMod/main/liquids/BlockStableLiquidMire.class`
- `MoreFunQuicksandMod/main/liquids/BlockTar.class`
- `MoreFunQuicksandMod/main/liquids/BogFluid.class`
- `MoreFunQuicksandMod/main/liquids/MireFluid.class`
- `MoreFunQuicksandMod/main/liquids/MucusFluid.class`
- `MoreFunQuicksandMod/main/liquids/QuicksandFluid.class`
- `MoreFunQuicksandMod/main/liquids/SandFluid.class`
- `MoreFunQuicksandMod/main/liquids/SlimeFluid.class`
- `MoreFunQuicksandMod/main/liquids/TarFluid.class`
- `MoreFunQuicksandMod/main/MFQM.class`
- `MoreFunQuicksandMod/main/MuddyEvent.class`
- `MoreFunQuicksandMod/main/PotionStuck.class`
- `MoreFunQuicksandMod/main/RopeMessage$Handler.class`
- `MoreFunQuicksandMod/main/RopeMessage.class`
- `MoreFunQuicksandMod/main/Tileentity/TileEntityBlossom.class`
- `MoreFunQuicksandMod/main/Tileentity/TileEntityBlossomRenderer.class`
- `MoreFunQuicksandMod/main/Tileentity/TileEntityLarvae.class`
- `MoreFunQuicksandMod/main/Tileentity/TileEntityLarvaeRenderer.class`
- `MoreFunQuicksandMod/main/Tileentity/TileEntityLure.class`
- `MoreFunQuicksandMod/main/Tileentity/TileEntityMeat.class`
- `MoreFunQuicksandMod/main/Tileentity/TileEntityMeatRenderer.class`
- `MoreFunQuicksandMod/main/blocks/BlockLeaves.class`
- `MoreFunQuicksandMod/main/items/ItemChocolateBucket.class`
- `MoreFunQuicksandMod/main/items/ItemChocolatePowderBucket.class`
- `MoreFunQuicksandMod/main/liquids/BlockLiquidChocolate.class`
- `MoreFunQuicksandMod/main/liquids/ChocolateFluid.class`
- `MoreFunQuicksandMod/main/blocks/BlockChocolate.class`
- `MoreFunQuicksandMod/main/liquids/BlockSlurry.class`
- `MoreFunQuicksandMod/main/liquids/SlurryFluid.class`
- `MoreFunQuicksandMod/main/items/ItemSlurryBucket.class`
- `MoreFunQuicksandMod/main/items/ItemFertilizer.class`
- `MoreFunQuicksandMod/main/blocks/BlockGas.class`
- `MoreFunQuicksandMod/main/HandEvent.class`
- `MoreFunQuicksandMod/main/entity/EntityRescue.class`
- `MoreFunQuicksandMod/main/items/ItemRescue.class`
- `MoreFunQuicksandMod/main/RescueMessage$Handler.class`
- `MoreFunQuicksandMod/main/RescueMessage.class`
- `MoreFunQuicksandMod/main/CustomMaterialGas.class`
- `MoreFunQuicksandMod/main/blocks/ItemMud.class`
- `MoreFunQuicksandMod/main/client/RenderTentacles.class`
- `MoreFunQuicksandMod/main/entity/EntityTentacles.class`
- `MoreFunQuicksandMod/main/blocks/BlockTent.class`
- `MoreFunQuicksandMod/main/client/RenderTarTreads.class`
- `MoreFunQuicksandMod/main/entity/EntityTarTreads.class`
- `MoreFunQuicksandMod/main/blocks/BlockSoftGravel.class`
- `MoreFunQuicksandMod/main/items/ItemHoneyBucket.class`
- `MoreFunQuicksandMod/main/liquids/BlockHoney.class`
- `MoreFunQuicksandMod/main/liquids/HoneyFluid.class`
- `MoreFunQuicksandMod/main/blocks/BlockSolidHoney.class`
- `MoreFunQuicksandMod/main/client/ModelBee.class`
- `MoreFunQuicksandMod/main/client/RenderBee.class`
- `MoreFunQuicksandMod/main/entity/EntityBee.class`
- `MoreFunQuicksandMod/main/blocks/BlockHoneycomb.class`
- `MoreFunQuicksandMod/main/items/ItemGasMask.class`
- `MoreFunQuicksandMod/main/items/ItemLiqGun.class`
- `MoreFunQuicksandMod/main/entity/EntityLiqBall.class`
- `MoreFunQuicksandMod/main/client/RenderSandBlob.class`
- `MoreFunQuicksandMod/main/entity/EntitySandBlob.class`
- `MoreFunQuicksandMod/main/entity/EntityMudTentacles.class`
- `MoreFunQuicksandMod/main/entity/EntitySPotion.class`
- `MoreFunQuicksandMod/main/items/ItemSPotion.class`
- `MoreFunQuicksandMod/main/liquids/BlockSinkyLiquid.class`
- `MoreFunQuicksandMod/main/liquids/SinkyFluid.class`
- `MoreFunQuicksandMod/main/blocks/BlockSandstoneTrap.class`

## 附录：全部非 class 文件

- `mcmod.info`
- `assets/morefunquicksandmod/Logo.png`
- `assets/morefunquicksandmod/textures/blocks/Acid_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/Acid_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Acid_Still.png`
- `assets/morefunquicksandmod/textures/blocks/Acid_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Bog_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/Bog_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/bog_grass.png`
- `assets/morefunquicksandmod/textures/blocks/bog_grass_cberry.png`
- `assets/morefunquicksandmod/textures/blocks/Bog_Still.png`
- `assets/morefunquicksandmod/textures/blocks/Bog_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/clay0_0.png`
- `assets/morefunquicksandmod/textures/blocks/clay0_1.png`
- `assets/morefunquicksandmod/textures/blocks/clay0_2.png`
- `assets/morefunquicksandmod/textures/blocks/clay0_3.png`
- `assets/morefunquicksandmod/textures/blocks/clay0_4.png`
- `assets/morefunquicksandmod/textures/blocks/clay1.png`
- `assets/morefunquicksandmod/textures/blocks/clay2.png`
- `assets/morefunquicksandmod/textures/blocks/clay3.png`
- `assets/morefunquicksandmod/textures/blocks/clay4.png`
- `assets/morefunquicksandmod/textures/blocks/clay5.png`
- `assets/morefunquicksandmod/textures/blocks/CorruptedSand.png`
- `assets/morefunquicksandmod/textures/blocks/CorruptedSand.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/DenseWeb.png`
- `assets/morefunquicksandmod/textures/blocks/JungleQuicksand_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/JungleQuicksand_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/JungleQuicksand_Still.png`
- `assets/morefunquicksandmod/textures/blocks/JungleQuicksand_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Larvae.png`
- `assets/morefunquicksandmod/textures/blocks/Larvae.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Meat0.png`
- `assets/morefunquicksandmod/textures/blocks/Meat1.png`
- `assets/morefunquicksandmod/textures/blocks/Meat10.png`
- `assets/morefunquicksandmod/textures/blocks/Meat2.png`
- `assets/morefunquicksandmod/textures/blocks/Meat3.png`
- `assets/morefunquicksandmod/textures/blocks/Meat4.png`
- `assets/morefunquicksandmod/textures/blocks/Meat5.png`
- `assets/morefunquicksandmod/textures/blocks/Meat6.png`
- `assets/morefunquicksandmod/textures/blocks/Meat7.png`
- `assets/morefunquicksandmod/textures/blocks/Meat8.png`
- `assets/morefunquicksandmod/textures/blocks/Meat9.png`
- `assets/morefunquicksandmod/textures/blocks/Mire0.png`
- `assets/morefunquicksandmod/textures/blocks/Mire1.png`
- `assets/morefunquicksandmod/textures/blocks/Mire2.png`
- `assets/morefunquicksandmod/textures/blocks/Mire3.png`
- `assets/morefunquicksandmod/textures/blocks/Mire4.png`
- `assets/morefunquicksandmod/textures/blocks/Mire_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/Mire_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Mire_side0.png`
- `assets/morefunquicksandmod/textures/blocks/Mire_side1.png`
- `assets/morefunquicksandmod/textures/blocks/Mire_Still.png`
- `assets/morefunquicksandmod/textures/blocks/Mire_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Moor0.png`
- `assets/morefunquicksandmod/textures/blocks/Moor1.png`
- `assets/morefunquicksandmod/textures/blocks/Moor_side0.png`
- `assets/morefunquicksandmod/textures/blocks/Moor_side1.png`
- `assets/morefunquicksandmod/textures/blocks/Morass0.png`
- `assets/morefunquicksandmod/textures/blocks/Morass1.png`
- `assets/morefunquicksandmod/textures/blocks/Morass2.png`
- `assets/morefunquicksandmod/textures/blocks/Morass3.png`
- `assets/morefunquicksandmod/textures/blocks/Morass4.png`
- `assets/morefunquicksandmod/textures/blocks/Morass5.png`
- `assets/morefunquicksandmod/textures/blocks/Morass6.png`
- `assets/morefunquicksandmod/textures/blocks/Morass_side0.png`
- `assets/morefunquicksandmod/textures/blocks/mud.png`
- `assets/morefunquicksandmod/textures/blocks/quicksand.png`
- `assets/morefunquicksandmod/textures/blocks/Sand_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/Sand_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Sand_Still.png`
- `assets/morefunquicksandmod/textures/blocks/Sand_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/SlimeHole0.png`
- `assets/morefunquicksandmod/textures/blocks/SlimeHole1.png`
- `assets/morefunquicksandmod/textures/blocks/SlimeHole2.png`
- `assets/morefunquicksandmod/textures/blocks/SlimeHole3.png`
- `assets/morefunquicksandmod/textures/blocks/Slime_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/Slime_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Slime_Still.png`
- `assets/morefunquicksandmod/textures/blocks/Slime_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/SoftQuicksand0.png`
- `assets/morefunquicksandmod/textures/blocks/SoftQuicksand1.png`
- `assets/morefunquicksandmod/textures/blocks/SoftQuicksand2.png`
- `assets/morefunquicksandmod/textures/blocks/SoftSnow.png`
- `assets/morefunquicksandmod/textures/blocks/Tar_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/Tar_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Tar_Still.png`
- `assets/morefunquicksandmod/textures/blocks/Tar_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/items/BucketOfAcid.png`
- `assets/morefunquicksandmod/textures/items/BucketOfLiquidBog.png`
- `assets/morefunquicksandmod/textures/items/BucketOfMire.png`
- `assets/morefunquicksandmod/textures/items/BucketOfQuicksand.png`
- `assets/morefunquicksandmod/textures/items/BucketOfSand.png`
- `assets/morefunquicksandmod/textures/items/BucketOfSlime.png`
- `assets/morefunquicksandmod/textures/items/BucketOfTar.png`
- `assets/morefunquicksandmod/textures/items/Cable.png`
- `assets/morefunquicksandmod/textures/items/CableTex.png`
- `assets/morefunquicksandmod/textures/items/Coil.png`
- `assets/morefunquicksandmod/textures/items/cranberry.png`
- `assets/morefunquicksandmod/textures/items/GrapplingHook.png`
- `assets/morefunquicksandmod/textures/items/GrapplingHookActive.png`
- `assets/morefunquicksandmod/textures/items/GrapplingHookBroken.png`
- `assets/morefunquicksandmod/textures/items/GrapplingHookTex.png`
- `assets/morefunquicksandmod/textures/items/Hook.png`
- `assets/morefunquicksandmod/textures/items/LarvaCooked.png`
- `assets/morefunquicksandmod/textures/items/LarvaRaw.png`
- `assets/morefunquicksandmod/textures/items/potion_mud.png`
- `assets/morefunquicksandmod/textures/items/potion_sinking.png`
- `assets/morefunquicksandmod/textures/items/Rope.png`
- `assets/morefunquicksandmod/textures/items/Rope1.png`
- `assets/morefunquicksandmod/textures/items/Rope2.png`
- `assets/morefunquicksandmod/textures/items/RopeTex.png`
- `assets/morefunquicksandmod/textures/armor/wadingboots.png`
- `assets/morefunquicksandmod/textures/items/wadingboots.png`
- `assets/morefunquicksandmod/textures/items/prewadingboots0.png`
- `assets/morefunquicksandmod/textures/items/prewadingboots1.png`
- `assets/morefunquicksandmod/textures/armor/prewadingboots0.png`
- `assets/morefunquicksandmod/textures/armor/prewadingboots1.png`
- `assets/morefunquicksandmod/lang/en_US.lang`
- `assets/morefunquicksandmod/textures/entity/VoreSlime.png`
- `assets/morefunquicksandmod/textures/entity/MuddyBlob.png`
- `assets/morefunquicksandmod/textures/entity/TarSlime.png`
- `assets/morefunquicksandmod/textures/blocks/SwallowingFlesh.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/MudOverlay0.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/MudOverlay1.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/MudOverlay2.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/MudOverlay3.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/MudOverlay4.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/MudOverlay5.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/MudOverlay6.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/MudOverlay7.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/MudOverlay8.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/MudOverlay9.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/SlimeOverlay5.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/SlimeOverlay6.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/SlimeOverlay7.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/SlimeOverlay8.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/SlimeOverlay9.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/SlimeOverlay0.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/SlimeOverlay1.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/SlimeOverlay2.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/SlimeOverlay3.png`
- `assets/morefunquicksandmod/textures/entity/mudOverlays/SlimeOverlay4.png`
- `assets/morefunquicksandmod/textures/blocks/Mucus_Still.png`
- `assets/morefunquicksandmod/textures/blocks/Mucus_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/Mucus_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Mucus_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/items/BucketOfMucus.png`
- `assets/morefunquicksandmod/textures/blocks/Blossom5.png`
- `assets/morefunquicksandmod/textures/blocks/Blossom0.png`
- `assets/morefunquicksandmod/textures/blocks/Blossom1.png`
- `assets/morefunquicksandmod/textures/blocks/Blossom2.png`
- `assets/morefunquicksandmod/textures/blocks/Blossom3.png`
- `assets/morefunquicksandmod/textures/blocks/Blossom4.png`
- `assets/morefunquicksandmod/textures/blocks/Blossom6.png`
- `assets/morefunquicksandmod/textures/blocks/Blossom7.png`
- `assets/morefunquicksandmod/textures/blocks/Moss_up.png`
- `assets/morefunquicksandmod/textures/blocks/Moss_up.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Moss_front.png`
- `assets/morefunquicksandmod/textures/blocks/Moss_front.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Brown_Clay1.png`
- `assets/morefunquicksandmod/textures/blocks/Brown_Clay2.png`
- `assets/morefunquicksandmod/textures/blocks/Brown_Clay3.png`
- `assets/morefunquicksandmod/textures/blocks/Brown_Clay0.png`
- `assets/morefunquicksandmod/textures/blocks/Mineral_Clay3.png`
- `assets/morefunquicksandmod/textures/blocks/Mineral_Clay0.png`
- `assets/morefunquicksandmod/textures/blocks/Mineral_Clay1.png`
- `assets/morefunquicksandmod/textures/blocks/Mineral_Clay2.png`
- `assets/morefunquicksandmod/textures/items/BucketOfMineralClay.png`
- `assets/morefunquicksandmod/textures/items/BucketOfBrownClay.png`
- `assets/morefunquicksandmod/textures/blocks/Peat3.png`
- `assets/morefunquicksandmod/textures/blocks/Peat0.png`
- `assets/morefunquicksandmod/textures/blocks/Peat1.png`
- `assets/morefunquicksandmod/textures/blocks/Peat2.png`
- `assets/morefunquicksandmod/textures/items/Peat.png`
- `assets/morefunquicksandmod/textures/blocks/Peat.png`
- `assets/morefunquicksandmod/textures/armor/LifeJacket.png`
- `assets/morefunquicksandmod/textures/items/LifeJacket.png`
- `assets/morefunquicksandmod/textures/items/LongStick.png`
- `assets/morefunquicksandmod/textures/items/LongStick0.png`
- `assets/morefunquicksandmod/textures/items/LongStick1.png`
- `assets/morefunquicksandmod/textures/blocks/Wax4S.png`
- `assets/morefunquicksandmod/textures/blocks/Wax0.png`
- `assets/morefunquicksandmod/textures/blocks/Wax0S.png`
- `assets/morefunquicksandmod/textures/blocks/Wax1.png`
- `assets/morefunquicksandmod/textures/blocks/Wax1S.png`
- `assets/morefunquicksandmod/textures/blocks/Wax2.png`
- `assets/morefunquicksandmod/textures/blocks/Wax2S.png`
- `assets/morefunquicksandmod/textures/blocks/Wax3.png`
- `assets/morefunquicksandmod/textures/blocks/Wax3S.png`
- `assets/morefunquicksandmod/textures/blocks/Wax4.png`
- `assets/morefunquicksandmod/textures/items/Wax.png`
- `assets/morefunquicksandmod/textures/blocks/WaxTree1.png`
- `assets/morefunquicksandmod/textures/blocks/WaxTree0.png`
- `assets/morefunquicksandmod/lang/ru_RU.lang`
- `META-INF/MANIFEST.MF`
- `assets/morefunquicksandmod/textures/blocks/Leaves.png`
- `assets/morefunquicksandmod/textures/items/BucketOfChocolatePowder.png`
- `assets/morefunquicksandmod/textures/items/BucketOfChocolate.png`
- `assets/morefunquicksandmod/textures/blocks/Choco_Still.png`
- `assets/morefunquicksandmod/textures/blocks/Choco_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/Choco_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Choco_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Chocolate.png`
- `assets/morefunquicksandmod/textures/items/HotChocolate.png`
- `assets/morefunquicksandmod/textures/items/Donut3.png`
- `assets/morefunquicksandmod/textures/items/Donut0.png`
- `assets/morefunquicksandmod/textures/items/Donut1.png`
- `assets/morefunquicksandmod/textures/items/Donut2.png`
- `assets/morefunquicksandmod/textures/items/Donut4.png`
- `assets/morefunquicksandmod/textures/blocks/Moor8.png`
- `assets/morefunquicksandmod/textures/blocks/Moor2.png`
- `assets/morefunquicksandmod/textures/blocks/Moor3.png`
- `assets/morefunquicksandmod/textures/blocks/Moor4.png`
- `assets/morefunquicksandmod/textures/blocks/Moor5.png`
- `assets/morefunquicksandmod/textures/blocks/Moor6.png`
- `assets/morefunquicksandmod/textures/blocks/Moor7.png`
- `assets/morefunquicksandmod/textures/blocks/Slurry_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/Slurry_Still.png`
- `assets/morefunquicksandmod/textures/blocks/Slurry_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Slurry_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/items/BucketOfSlurry.png`
- `assets/morefunquicksandmod/textures/items/Fertilizer.png`
- `assets/morefunquicksandmod/textures/blocks/Gas15.png`
- `assets/morefunquicksandmod/textures/blocks/Gas0.png`
- `assets/morefunquicksandmod/textures/blocks/Gas1.png`
- `assets/morefunquicksandmod/textures/blocks/Gas2.png`
- `assets/morefunquicksandmod/textures/blocks/Gas3.png`
- `assets/morefunquicksandmod/textures/blocks/Gas4.png`
- `assets/morefunquicksandmod/textures/blocks/Gas5.png`
- `assets/morefunquicksandmod/textures/blocks/Gas6.png`
- `assets/morefunquicksandmod/textures/blocks/Gas7.png`
- `assets/morefunquicksandmod/textures/blocks/Gas8.png`
- `assets/morefunquicksandmod/textures/blocks/Gas9.png`
- `assets/morefunquicksandmod/textures/blocks/Gas10.png`
- `assets/morefunquicksandmod/textures/blocks/Gas11.png`
- `assets/morefunquicksandmod/textures/blocks/Gas12.png`
- `assets/morefunquicksandmod/textures/blocks/Gas13.png`
- `assets/morefunquicksandmod/textures/blocks/Gas14.png`
- `assets/morefunquicksandmod/textures/blocks/Gas10.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas11.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas12.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas13.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas14.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas15.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas0.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas1.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas2.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas3.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas4.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas5.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas6.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas7.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas8.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Gas9.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Meat11.png`
- `assets/morefunquicksandmod/textures/items/Rescue.png`
- `assets/morefunquicksandmod/textures/blocks/Tentacles0.png`
- `assets/morefunquicksandmod/textures/blocks/Tentacles1.png`
- `assets/morefunquicksandmod/textures/blocks/Tentacles2.png`
- `assets/morefunquicksandmod/textures/blocks/Tent3.png`
- `assets/morefunquicksandmod/textures/blocks/Tent0.png`
- `assets/morefunquicksandmod/textures/blocks/Tent1.png`
- `assets/morefunquicksandmod/textures/blocks/Tent2.png`
- `assets/morefunquicksandmod/textures/blocks/Tent0.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Tent1.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Tent2.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Tent3.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/TarTread.png`
- `assets/morefunquicksandmod/textures/blocks/SoftGravel2.png`
- `assets/morefunquicksandmod/textures/blocks/SoftGravel0.png`
- `assets/morefunquicksandmod/textures/blocks/SoftGravel1.png`
- `assets/morefunquicksandmod/textures/blocks/SoftGravel3.png`
- `assets/morefunquicksandmod/textures/blocks/Honey_Still.png`
- `assets/morefunquicksandmod/textures/blocks/Honey_Flowing.png`
- `assets/morefunquicksandmod/textures/blocks/Honey_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/Honey_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/items/BucketOfHoney.png`
- `assets/morefunquicksandmod/textures/blocks/Honey.png`
- `assets/morefunquicksandmod/textures/entity/Bee.png`
- `assets/morefunquicksandmod/sounds/mob/bee/hurt.ogg`
- `assets/morefunquicksandmod/sounds/mob/bee/say.ogg`
- `assets/morefunquicksandmod/sounds.json`
- `assets/morefunquicksandmod/textures/blocks/honeycomb0.png`
- `assets/morefunquicksandmod/textures/blocks/honeycomb1.png`
- `assets/morefunquicksandmod/textures/blocks/honeycomb2.png`
- `assets/morefunquicksandmod/textures/blocks/hive.png`
- `assets/morefunquicksandmod/textures/items/emptyhoneycomb.png`
- `assets/morefunquicksandmod/textures/items/filledhoneycomb.png`
- `assets/morefunquicksandmod/textures/armor/gasmask.png`
- `assets/morefunquicksandmod/textures/items/GasMask.png`
- `assets/morefunquicksandmod/textures/items/Filter.png`
- `assets/morefunquicksandmod/textures/items/LiqGun.png`
- `assets/morefunquicksandmod/textures/entity/SandyBlob.png`
- `assets/morefunquicksandmod/textures/blocks/Tentacles0_1.png`
- `assets/morefunquicksandmod/textures/blocks/Tentacles1_1.png`
- `assets/morefunquicksandmod/textures/blocks/Tentacles2_1.png`
- `assets/morefunquicksandmod/textures/blocks/TentaclesBase.png`
- `assets/morefunquicksandmod/textures/blocks/SinkyLiquid_Flowing.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/SinkyLiquid_Still.png.mcmeta`
- `assets/morefunquicksandmod/textures/blocks/SinkyLiquid_Still.png`
- `assets/morefunquicksandmod/textures/blocks/SinkyLiquid_Flowing.png`
- `assets/morefunquicksandmod/textures/items/SPotion.png`
