# MoreFunQuicksandMod/main/blocks/BlockVoreHole

ID `class:2ebde7fe617af994122f0872`；class SHA `3a1b8e39d3546a12e71d2d97842f2c2a56c7cdde876dda10fb07881fb4022a12`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockVoreHole`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockVoreHole.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `temp_vore`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:39d836da054516ce50f3104c` `theEmptyIIcon:Lnet/minecraft/util/IIcon;` access 1
- `field:bb36fa5b46754b7ed3309d6e` `maxOpacity:I` access 2
- `field:02a7f5a68077487205960706` `lastOpacity:I` access 2
- `field:466c4a2fb00739fe551ba1f4` `incOpacity:I` access 2

## 方法目录

- `method:110e03a13d945f35e0f8e9c5` `<init>(III)V` access 1，66 code bytes；语义 NOT_ANALYZED
- `method:0017611d64d038e02a44f06c` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:c5bf28cb75f48ab4c5cd6e97` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，1388 code bytes；语义 NOT_ANALYZED
- `method:c7c8fc19f402c603b41003cc` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:d2264fd13c4ad82dd3c29a59` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:cc1f047591edda2232f4aad8` `func_149686_d()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:c4f5823a4768b5370f8f92d2` `func_149645_b()I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:cebf0d8f00ea39ba8610f8d5` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:0a6c8e3fe1d38d092e93f0f3` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，17 code bytes；语义 NOT_ANALYZED
- `method:b990c605835ca3bac397915a` `checkBlossomNear(Lnet/minecraft/world/World;III)V` access 1，190 code bytes；语义 NOT_ANALYZED
- `method:019ca6d0ed3c39d03eba4b20` `func_149700_E()Z` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:7ba8ece80ad43d73c7dd4c99` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:9782e06e50ed6ecfcf238c2a` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:a8c0c4095fe2a21eb79683ac` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:121b6ff937f2b726432d8bcc` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，17 code bytes；语义 NOT_ANALYZED
- `method:2d38ffdf2852006d70128c82` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，17 code bytes；语义 NOT_ANALYZED
- `method:9b3c0c86c7d87390f25efd7d` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:daed719cc7a3ca0f8c1e1a80` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:6b4780140932060fe0db0efd` `func_149745_a(Ljava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:7b8c1c965ed2e0de5fe47d20` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，124 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 216–218
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 301–303 · 302 morefunquicksandmod:Acid_Still

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|TempVore|0|Temp Vore Hole|`mfqm:temp_vore`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
