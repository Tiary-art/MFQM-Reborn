# MoreFunQuicksandMod/main/blocks/BlockDenseWeb

ID `class:c117693add7b71ebc6a56a2c`；class SHA `2f1a2aa03ff2f9c1b5791ac54c0dfaa1aec0718e111321e83ef176e01b4ec5e2`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces `net/minecraftforge/common/IShearable`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockDenseWeb`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockDenseWeb.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `dense_webbing`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:2766476185b76febb127ed6f` `theQIIcon:Lnet/minecraft/util/IIcon;` access 1
- `field:553b96b7cc2549e3155f1513` `maxOpacity:I` access 2
- `field:2178142517c96e44b0782ab7` `lastOpacity:I` access 2
- `field:7511d30e577db95ac638de30` `incOpacity:I` access 2

## 方法目录

- `method:8c9c55c3c54076d30a3faa02` `<init>(III)V` access 1，66 code bytes；语义 NOT_ANALYZED
- `method:8a8441ebf9ba406ef47d4ff7` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:fe75f11687cf5d26a98a91cd` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:e6361bbf53a2d523e92276c3` `isSolid()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:32463c622fb453c1df6105d7` `func_149686_d()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:0bd05563096141d2448bd304` `func_149719_a(Lnet/minecraft/world/IBlockAccess;III)V` access 1，54 code bytes；语义 NOT_ANALYZED
- `method:9e1b23e30deeb813750cd0b0` `func_149683_g()V` access 1，12 code bytes；语义 NOT_ANALYZED
- `method:f28d6fe63eb35abed2ce8ad1` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2634 code bytes；语义 NOT_ANALYZED
- `method:73070911789c79c5e616f71e` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:acffc656ab1a726be9411bcb` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:45957d7474638b7d2607c599` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，59 code bytes；语义 NOT_ANALYZED
- `method:f113e2019a95f4c3c327e6bc` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:73015b6ea953e06d25499b57` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:136eda8834769af17c0f879a` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:2f4244e8d5d9a5c20f73196f` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:1f4412cb902ec704849ab197` `func_149745_a(Ljava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:89045f79f3891c40348f0b6d` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，69 code bytes；语义 NOT_ANALYZED
- `method:9accc0317077afde1bc84b7c` `isShearable(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/IBlockAccess;III)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:32ece809d37e0a080cdf88ca` `onSheared(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/IBlockAccess;IIII)Ljava/util/ArrayList;` access 1，26 code bytes；语义 NOT_ANALYZED
- `method:6f3c46e00d52c77da76dcfc2` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:ade259aacfc4ec366acaa92d` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，60 code bytes；语义 NOT_ANALYZED
- `method:ccb3c8bd502b86f8d759c525` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，122 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
