# MoreFunQuicksandMod/main/blocks/BlockMire

ID `class:35a31b34ba35645d6d4be7d9`；class SHA `b1d7944d0f1584fc56e5a466ee913104074f71f7d5eb4f5693f6c16ce28cbfd2`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockMire`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockMire.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `mire`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:cf608d33afdb9d543c00db3e` `IIconArray:[Lnet/minecraft/util/IIcon;` access 2
- `field:4a924c68f8892ae71e5237e5` `IIconSide0:Lnet/minecraft/util/IIcon;` access 2
- `field:45eacbb3618835657574e81a` `IIconSide1:Lnet/minecraft/util/IIcon;` access 2
- `field:b467b6da838f20d36dda3b3c` `maxOpacity:I` access 2
- `field:b019162a7c6ff990ef771a46` `lastOpacity:I` access 2
- `field:fbf705b6b864c435625d66a9` `incOpacity:I` access 2

## 方法目录

- `method:eda69711fb5929cb54d398dc` `<init>(III)V` access 1，89 code bytes；语义 NOT_ANALYZED
- `method:bf383a140123f512f5bc4c5a` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:1b1130e08df610c3283c0e28` `Breaking(Lnet/minecraft/world/World;IIII)I` access 1，110 code bytes；语义 NOT_ANALYZED
- `method:c87a9b298604bee7afcd8d86` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，714 code bytes；语义 NOT_ANALYZED
- `method:4ebc1569a0d0c81bcf4f9e51` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，3759 code bytes；语义 NOT_ANALYZED
- `method:f4099c5f2706246135aa5c10` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:b8b973735f6c6822621fd795` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:6e5b8a6e00e87ff4e47e96c0` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，69 code bytes；语义 NOT_ANALYZED
- `method:46467ae0f4efc43bd2ef31f6` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:ded98ed9536c42796c0bc078` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:79408ecf25b4184639ecdd2e` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:2bc0040d0865b7228d69f746` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，156 code bytes；语义 NOT_ANALYZED
- `method:0195c458ed7b7f1681897c6d` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，316 code bytes；语义 NOT_ANALYZED
- `method:0a67fcc834ec3d4887db8baa` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，84 code bytes；语义 NOT_ANALYZED
- `method:4e0c825af562546e51d8c663` `func_149700_E()Z` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:43650fb30c096e1261b98fe8` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:db59261d2a9532f1a0365c87` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:8c87d7a2837cb197252d9b08` `isSolid()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:45e09fcdd4de6dccfb7d5546` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，70 code bytes；语义 NOT_ANALYZED
- `method:481678ddbcc612dbec809a79` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，122 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 637–761
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 764–771 · 767 morefunquicksandmod:Mire | 769 morefunquicksandmod:Mire_side0 | 770 morefunquicksandmod:Mire_side1

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Mire|0|Mire|`mfqm:mire`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
