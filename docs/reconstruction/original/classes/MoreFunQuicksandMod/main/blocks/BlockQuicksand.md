# MoreFunQuicksandMod/main/blocks/BlockQuicksand

ID `class:cdcd2203767d941d78ed7e7e`；class SHA `051d8d3d7d1122efa025ba039c2d6f0495a5a2128d9f64586f03c02624cad7e4`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / FIRST_BATCH_PARTIAL**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockQuicksand`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockQuicksand.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `quicksand`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:c829170767f3e4308e427f11` `theQIIcon:Lnet/minecraft/util/IIcon;` access 1
- `field:d7d8aca93585de38a1911e9d` `maxOpacity:I` access 2
- `field:e34cebcddc728131acc765b3` `lastOpacity:I` access 2
- `field:9a2217f6d73504d232880fed` `incOpacity:I` access 2

## 方法目录

- `method:ab05afb4440a32fbbc246228` `<init>(III)V` access 1，89 code bytes；语义 NOT_ANALYZED
- `method:3a09f87a1b6755def323a627` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:481214887ec40d85d9ff0c5b` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2515 code bytes；语义 NOT_ANALYZED
- `method:57c16ce8a9c2667e4fb6e78e` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:ed21a425d0b4672bb5c9f50f` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:ae7ff64fee72185a3474ad5b` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，444 code bytes；语义 NOT_ANALYZED
- `method:5411278c3fd35531c0e63dfa` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:4edf58a9f1f1b0ce52313460` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:b64b379f0dedb93e9e1bc7b0` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:ed18dd436719a3e13e2bdf0c` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，83 code bytes；语义 NOT_ANALYZED
- `method:1183d4bd0f7bf116908f98f5` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:19476ccc467ba614322f92e9` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:3aa1a208b8cab176e1b08312` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:ead517f13c72e798357e8050` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:cfc19208578a52a8321ee302` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，64 code bytes；语义 NOT_ANALYZED
- `method:1aa7e0b0ffe60d32f768509c` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:e0250e975a5c19ca32e564f0` `isSolid()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:85ef335a8506e5194a8799ea` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:231fe9759768226b62d483f9` `func_149635_D()I` access 1，66 code bytes；语义 NOT_ANALYZED
- `method:3c792b1d259dc45ff009c5c2` `func_149741_i(I)I` access 1，66 code bytes；语义 NOT_ANALYZED
- `method:fabe6e93f28f6acede17c284` `func_149720_d(Lnet/minecraft/world/IBlockAccess;III)I` access 1，66 code bytes；语义 NOT_ANALYZED
- `method:3269e49cfa74b4416bf62212` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，69 code bytes；语义 NOT_ANALYZED
- `method:3544bf58ab8e46cfe823db2f` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，122 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## 首批深度档案入口

接触坐标/强制Stuck：BlockQuicksand.analysis.txt:88–140、288–332；重点报告§2。

[深度证据、规范与对照](../../../../../../../reconstruction/reports/DEEP_FIRST_BATCH.md)

1. 身份/字节哈希/工具：本页顶部，原始来源非原作者源码。
2. 原文证据与解释：按上述位置与重点报告分栏读取。
3. 职责和触发：重点报告对应模块列出输入、调用次序、提前返回。
4. 功能与资源：对应 ORIGINAL_REGISTRY、RESOURCE_USAGE 和本类调用边，不将名字映射当语义。
5. 行为规范：重点报告的分支和边界；未列分支 UNKNOWN。
6. 现代差异：重点报告逐模块对照现代真实路径及存档风险。
7. 测试设计：原版对照本轮 NOT_RUN，现有现代回归见 R0_TEST_RESULTS.json。
8. 结论：PARTIAL，仅已列静态链；下一步按 NEXT_WORK_PACKAGES.md 闭合。
