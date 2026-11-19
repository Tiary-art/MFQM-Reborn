# MoreFunQuicksandMod/main/blocks/BlockTent

ID `class:66c9e8fd35095d431ee86b81`；class SHA `1e4a2aeedfa9379a4d88ba1d16222e5b564ff798827c55b9520780228ab2e1b5`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/BlockBush`；interfaces `net/minecraftforge/common/IShearable`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockTent`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockTent.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `tendrils`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:d06cb8c84915b007df346059` `IIconArray:[Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:8788e07fe49a7ff8a838d4d3` `<init>()V` access 1，71 code bytes；语义 NOT_ANALYZED
- `method:10c7c44e0ddb557932c01397` `getSubBlocks(ILnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` access 1，69 code bytes；语义 NOT_ANALYZED
- `method:b6d5624a59752558d8ae051a` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，11 code bytes；语义 NOT_ANALYZED
- `method:0c100d31f3c0f4e508551b31` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，6 code bytes；语义 NOT_ANALYZED
- `method:e822eb5b8432b16dc0c9d02f` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:1aff9f37baf45917b41ecaba` `func_149745_a(Ljava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:4392ca6e6226fa7925ddf6db` `quantityDropped(IILjava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:bb6398b87547ee6217424923` `func_149679_a(ILjava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:d0a6384151011d94dffa343e` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，65 code bytes；语义 NOT_ANALYZED
- `method:cde8a71e4ea93d8f5314c0cd` `func_149718_j(Lnet/minecraft/world/World;III)Z` access 1，75 code bytes；语义 NOT_ANALYZED
- `method:ba84d1afaa5196445fcfdfd0` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:c83b2f16adb8598f1962ee5f` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:a9c92e964b2d42d341ec6c84` `canThisPlantGrowOnThisBlock(Lnet/minecraft/block/Block;)Z` access 4，11 code bytes；语义 NOT_ANALYZED
- `method:90fc30f86c081a11e42e31d4` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:536a3315fe11bb6098ab96dc` `isShearable(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/IBlockAccess;III)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:c56a34095c23060ad094df5b` `onSheared(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/IBlockAccess;IIII)Ljava/util/ArrayList;` access 1，42 code bytes；语义 NOT_ANALYZED
- `method:99f7260ac064c3c6ebb120cc` `func_149749_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，81 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `getSubBlocks(ILnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` · CFR 63–68 · 64 damage=0 | 65 damage=1 | 66 damage=2 | 67 damage=3
- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 71–73
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 96–102 · 98 morefunquicksandmod:Tent0 | 99 morefunquicksandmod:Tent1 | 100 morefunquicksandmod:Tent2 | 101 morefunquicksandmod:Tent3

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Tendrils|0|Tendrils|`mfqm:tendrils`|
|Tendrils|1|Tendrils|`未映射`|
|Tendrils|2|Tendrils|`未映射`|
|Tendrils|3|Tendrils|`未映射`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
