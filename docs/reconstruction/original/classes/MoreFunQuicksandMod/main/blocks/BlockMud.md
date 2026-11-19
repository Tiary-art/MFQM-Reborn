# MoreFunQuicksandMod/main/blocks/BlockMud

ID `class:20ad9252be580cab31783272`；class SHA `5cd16ac7e916bc1a0d7c2623c3b983715ffb66113592f252f8f460289cfc1abc`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / FIRST_BATCH_PARTIAL**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockMud`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockMud.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `mud`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:6566561710512f1afc71589e` `mudTypes:[Ljava/lang/String;` access 26
- `field:042bfeb6d1f632bef324e731` `texture:Lnet/minecraft/util/IIcon;` access 0

## 方法目录

- `method:6285a68bcc1a35f3768f9610` `<init>()V` access 1，68 code bytes；语义 NOT_ANALYZED
- `method:547b96ab3beacf585739cbc4` `getMudDepth(Lnet/minecraft/world/World;III)I` access 1，375 code bytes；语义 NOT_ANALYZED
- `method:446c9a8a4ff9d1afb7938725` `getMudSafe(Lnet/minecraft/world/World;III)I` access 1，205 code bytes；语义 NOT_ANALYZED
- `method:2ad8f8c85548cb7a61c09ba6` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，153 code bytes；语义 NOT_ANALYZED
- `method:6c8f4ff7876d2a2db6f4361b` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，3523 code bytes；语义 NOT_ANALYZED
- `method:a186d97cdd300ff026ef4e75` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:2f247e7c75ff98245171c8ac` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:30a10c9505c44f4ccfaae15f` `isSolid()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:87e3fcfe0fed25d1cd974987` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:9fa877636ea18dd390724d3f` `func_149643_k(Lnet/minecraft/world/World;III)I` access 1，9 code bytes；语义 NOT_ANALYZED
- `method:df48f6e402b9ba1ce347960b` `func_149666_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` access 1，69 code bytes；语义 NOT_ANALYZED
- `method:f45c20aa80b4e8d1a6dc4f31` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，18 code bytes；语义 NOT_ANALYZED
- `method:29a572e0d06d72e6ae547527` `quantityDropped(IILjava/util/Random;)I` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:48698fb866db07b515a24f87` `getUnlocalizedName(Ljava/lang/String;Lnet/minecraft/item/ItemStack;)Ljava/lang/String;` access 1，32 code bytes；语义 NOT_ANALYZED
- `method:d5a065376cd0558248b2030a` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:594473483129d8fa26fb794d` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:678ab882db92944227d243e1` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，164 code bytes；语义 NOT_ANALYZED
- `method:b2abb28e01d705afcb00af7c` `func_149635_D()I` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:8e6f2323a556da346421a3f3` `func_149741_i(I)I` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:9c69c6bb44598f8dd8fe7d3a` `func_149720_d(Lnet/minecraft/world/IBlockAccess;III)I` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:b0eb8c9f1d8b31542f2fe4b0` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，70 code bytes；语义 NOT_ANALYZED
- `method:7d89d55090172d487598d179` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，112 code bytes；语义 NOT_ANALYZED
- `method:122186288315932eaef8f182` `<clinit>()V` access 8，26 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## 首批深度档案入口

metadata深度和safe覆盖：BlockMud.analysis.txt:199–247、483–545、618起；重点报告§2/§4。

[深度证据、规范与对照](../../../../../../../reconstruction/reports/DEEP_FIRST_BATCH.md)

1. 身份/字节哈希/工具：本页顶部，原始来源非原作者源码。
2. 原文证据与解释：按上述位置与重点报告分栏读取。
3. 职责和触发：重点报告对应模块列出输入、调用次序、提前返回。
4. 功能与资源：对应 ORIGINAL_REGISTRY、RESOURCE_USAGE 和本类调用边，不将名字映射当语义。
5. 行为规范：重点报告的分支和边界；未列分支 UNKNOWN。
6. 现代差异：重点报告逐模块对照现代真实路径及存档风险。
7. 测试设计：原版对照本轮 NOT_RUN，现有现代回归见 R0_TEST_RESULTS.json。
8. 结论：PARTIAL，仅已列静态链；下一步按 NEXT_WORK_PACKAGES.md 闭合。
