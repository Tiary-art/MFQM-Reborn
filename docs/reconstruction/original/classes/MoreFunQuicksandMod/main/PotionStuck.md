# MoreFunQuicksandMod/main/PotionStuck

ID `class:2096fc9d195cf8c3397c3f63`；class SHA `20c1f40570db1d48127d59c10c51f0c808a0bfda03793fe2f2dbc35b72b8846f`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / FIRST_BATCH_PARTIAL**（除重点模块报告给出的分支外）。super `java/lang/Object`；interfaces `net/minecraftforge/common/IExtendedEntityProperties`；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/PotionStuck`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__PotionStuck.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:fe5b8fb12524078fd7a597ff` `EXT_PROP_NAME:Ljava/lang/String;` access 25
- `field:4e1d226d70e1f88cfbdee3ef` `MUDDYLEVEL_WATCHER:I` access 25
- `field:9e41790a7b02dd2a1605641f` `entLiv:Lnet/minecraft/entity/EntityLivingBase;` access 18
- `field:9c87dc01580ee3389143f4fb` `Level:I` access 2
- `field:ff2854e758d9f8f0c5a91f02` `TarTreads:I` access 2

## 方法目录

- `method:49d6665cb7a78064f429b7e7` `<init>(Lnet/minecraft/entity/EntityLivingBase;)V` access 1，20 code bytes；语义 NOT_ANALYZED
- `method:4695572ee6a7687946de9b22` `register(Lnet/minecraft/entity/EntityLivingBase;)V` access 25，16 code bytes；语义 NOT_ANALYZED
- `method:a135b9f5657d651a89e10039` `get(Lnet/minecraft/entity/EntityLivingBase;)LMoreFunQuicksandMod/main/PotionStuck;` access 25，10 code bytes；语义 NOT_ANALYZED
- `method:cb1f6326ca7a9c125860baa7` `saveNBTData(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:80d6eaf6fdbb180013c3a598` `loadNBTData(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:d088ff926c028781637bf421` `init(Lnet/minecraft/entity/Entity;Lnet/minecraft/world/World;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:e4e6dcc48c32ad2e683b9ed0` `DoInit()V` access 1，11 code bytes；语义 NOT_ANALYZED
- `method:087f6508e9ea4ee2277ed42b` `getLevel()I` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:bc8d2ddf4af340626c336787` `getTarTreads()I` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:dca0ffa26bf24a5fd560e05a` `setTarTreads(I)V` access 1，6 code bytes；语义 NOT_ANALYZED
- `method:d5c103c2ccc612be545d0037` `setStuckLevel(I)V` access 1，6 code bytes；语义 NOT_ANALYZED
- `method:42c5bfd412fccccf81504bd6` `<clinit>()V` access 8，7 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## 首批深度档案入口

状态setter与非持久属性；MFQM.analysis.txt:2641委派；重点报告§3。

[深度证据、规范与对照](../../../../../../reconstruction/reports/DEEP_FIRST_BATCH.md)

1. 身份/字节哈希/工具：本页顶部，原始来源非原作者源码。
2. 原文证据与解释：按上述位置与重点报告分栏读取。
3. 职责和触发：重点报告对应模块列出输入、调用次序、提前返回。
4. 功能与资源：对应 ORIGINAL_REGISTRY、RESOURCE_USAGE 和本类调用边，不将名字映射当语义。
5. 行为规范：重点报告的分支和边界；未列分支 UNKNOWN。
6. 现代差异：重点报告逐模块对照现代真实路径及存档风险。
7. 测试设计：原版对照本轮 NOT_RUN，现有现代回归见 R0_TEST_RESULTS.json。
8. 结论：PARTIAL，仅已列静态链；下一步按 NEXT_WORK_PACKAGES.md 闭合。
