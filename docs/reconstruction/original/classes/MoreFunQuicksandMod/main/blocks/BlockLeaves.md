# MoreFunQuicksandMod/main/blocks/BlockLeaves

ID `class:c221ed30fe3b1238a568ba6c`；class SHA `39b6a836f2357fca2f6244a9aaf2c7f0081b05d294127d1a241b1bbf8f58567c`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/BlockBush`；interfaces `net/minecraftforge/common/IShearable`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockLeaves`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockLeaves.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `leaves_pile`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:360a561a2de6afd0768c7b47` `ic1:Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:1bfbf3b2ff67e04a705af122` `<init>()V` access 1，71 code bytes；语义 NOT_ANALYZED
- `method:79f49345a46def7286b63c67` `func_149645_b()I` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:a8bd39ba7499c0ab4ee074d4` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:d5c65db0c17a91b0341b09ca` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:737f768da4eaa90f84a2b29b` `func_149745_a(Ljava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:61b50c8d82487995e2a5480a` `quantityDropped(IILjava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:3565f08fba8bc69accc58002` `func_149679_a(ILjava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:2bb15ea8cd555081f0e182c3` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，13 code bytes；语义 NOT_ANALYZED
- `method:55fb17ec8ab2f867cc40afdf` `func_149718_j(Lnet/minecraft/world/World;III)Z` access 1，42 code bytes；语义 NOT_ANALYZED
- `method:b409ab84e346dd41ea01b22f` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:eb0559b8f0958aabdbb507e7` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:8de2fe0323a67fe1f7c057f5` `canThisPlantGrowOnThisBlock(Lnet/minecraft/block/Block;)Z` access 4，11 code bytes；语义 NOT_ANALYZED
- `method:c9e7475a792cd1ea00df0363` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:a2f43c8292035850b5993499` `isShearable(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/IBlockAccess;III)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:97e1d48c0444563fb04c9584` `onSheared(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/IBlockAccess;IIII)Ljava/util/ArrayList;` access 1，42 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 63–65
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 84–86 · 85 morefunquicksandmod:Leaves

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|LeavesPile|0|Dead Leaves Pile|`mfqm:leaves_pile`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
