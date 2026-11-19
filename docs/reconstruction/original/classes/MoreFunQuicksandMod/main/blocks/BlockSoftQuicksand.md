# MoreFunQuicksandMod/main/blocks/BlockSoftQuicksand

ID `class:4e7217539ffc5dbce834d58c`；class SHA `bd9d78fcad252b32c84c273260f89a9592cda99c73b7fce14d6dc1d724832606`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / FIRST_BATCH_PARTIAL**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockSoftQuicksand`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockSoftQuicksand.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `soft_quicksand`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:71eae07c2d13e9ef0444ef12` `theQIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:f5967b922777dbb31803f64b` `maxOpacity:I` access 2
- `field:49c969b6877df01d574ece7a` `lastOpacity:I` access 2
- `field:bbea36c6253ab960bdc7b954` `incOpacity:I` access 2

## 方法目录

- `method:e580336c59ca80621e46e5dd` `<init>(III)V` access 1，71 code bytes；语义 NOT_ANALYZED
- `method:00e09c44ddd47a535a305c5e` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:44a97981a7f567572a0e0731` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:67a07b1c73d20e2cbdb5f646` `isSolid()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:053b736e98643cf4ac7fcbef` `func_149686_d()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:8847e63c19c12a46850368bd` `func_149719_a(Lnet/minecraft/world/IBlockAccess;III)V` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:ce71b7dc4fb1f456e606a7d6` `func_149683_g()V` access 1，12 code bytes；语义 NOT_ANALYZED
- `method:406845b2411a03970ecad5b4` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2883 code bytes；语义 NOT_ANALYZED
- `method:e2b10c76cb3961e769446b8d` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:0047560606b2aef730ae7d93` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，15 code bytes；语义 NOT_ANALYZED
- `method:2514f6012ecc1b11f07a6745` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，447 code bytes；语义 NOT_ANALYZED
- `method:c7cc1681b1baf581f98f27cb` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:05ab8844c0c84805c591a0be` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:e28500797b5b812442b271c0` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:3e20f6f7a215a2dddf83a184` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，54 code bytes；语义 NOT_ANALYZED
- `method:a71b31cb333f6ef0fcb36fcc` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:c63735c45593ade90cd46f64` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:aa78dde11c7bf7f1785eae14` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:ff9714c33d4388f6316c57bc` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，64 code bytes；语义 NOT_ANALYZED
- `method:af8d85a06fa1a40f8d5c402d` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:0ada69f5308e600f564b87fc` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，60 code bytes；语义 NOT_ANALYZED
- `method:64cbe963d760e76b4e38b94f` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，122 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## 首批深度档案入口

独立幂指数/175/metadata图标：BlockSoftQuicksand.analysis.txt:104、265、350；重点报告§2/§4。

[深度证据、规范与对照](../../../../../../../reconstruction/reports/DEEP_FIRST_BATCH.md)

1. 身份/字节哈希/工具：本页顶部，原始来源非原作者源码。
2. 原文证据与解释：按上述位置与重点报告分栏读取。
3. 职责和触发：重点报告对应模块列出输入、调用次序、提前返回。
4. 功能与资源：对应 ORIGINAL_REGISTRY、RESOURCE_USAGE 和本类调用边，不将名字映射当语义。
5. 行为规范：重点报告的分支和边界；未列分支 UNKNOWN。
6. 现代差异：重点报告逐模块对照现代真实路径及存档风险。
7. 测试设计：原版对照本轮 NOT_RUN，现有现代回归见 R0_TEST_RESULTS.json。
8. 结论：PARTIAL，仅已列静态链；下一步按 NEXT_WORK_PACKAGES.md 闭合。
