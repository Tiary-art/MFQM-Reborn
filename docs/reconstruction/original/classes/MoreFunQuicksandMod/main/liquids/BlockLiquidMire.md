# MoreFunQuicksandMod/main/liquids/BlockLiquidMire

ID `class:1b7de0bf05a5af0b937c4cb6`；class SHA `0deb3669c1d2ef7f4f1a1722887cfba03c79f2d1d1133bbb6d7ed5c2ee50f41e`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockLiquidMire`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockLiquidMire.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `liquid_mire`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:d0dae024a682b5ff6cfd7dab` `theMireIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:ba7860f5c849eab41e70dc33` `maxOpacity:I` access 2
- `field:c49dc3167e6cc0dc0590ca14` `lastOpacity:I` access 2
- `field:22434c9254fde7876f3bf14f` `incOpacity:I` access 2

## 方法目录

- `method:01a46b7ef93e910b61d22426` `<init>(III)V` access 1，74 code bytes；语义 NOT_ANALYZED
- `method:069c5a3ce859ee2a8682d81c` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，969 code bytes；语义 NOT_ANALYZED
- `method:e240a99ab398393d106c62b8` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:77230aa47fb7eceb7d4c7de9` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，1423 code bytes；语义 NOT_ANALYZED
- `method:95ed6d99f0a908941cd70c4e` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，143 code bytes；语义 NOT_ANALYZED
- `method:feef4c1418314dfacabdc56f` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:4ab24f0106873f4adec1603b` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:bf977e5166b2ca46f4d82b05` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:cc7bc2d559bd377d01fae810` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:ce3d3d408c6f08522fa9a51b` `func_149727_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/player/EntityPlayer;IFFF)Z` access 1，167 code bytes；语义 NOT_ANALYZED
- `method:48630645da54e272632d8608` `func_149678_a(IZ)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:3bda7b15b2a45cead8b2dba3` `findItem(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/item/Item;I)I` access 1，74 code bytes；语义 NOT_ANALYZED
- `method:cf49e5f640ee2fd61e75ef53` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:d27cec1a5d66dd512993b977` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，124 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
