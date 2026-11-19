# MoreFunQuicksandMod/main/CustomPotionEvent

ID `class:6dd3ade458327121b3f9a6cf`；class SHA `4098f0c86337e4b1a4ab543cb29a6382322afcf307d11cd3e9c3b83e679b3a35`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / FIRST_BATCH_PARTIAL**（除重点模块报告给出的分支外）。super `java/lang/Object`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/CustomPotionEvent`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__CustomPotionEvent.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:9e329d0f94bdfffffc75bd66` `stuckModifierUUID:Ljava/util/UUID;` access 25

## 方法目录

- `method:66e3d2b06ad31203da408a16` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:d2f0f3a579906c7efd7f4e10` `onEntityConstructing(Lnet/minecraftforge/event/entity/EntityEvent$EntityConstructing;)V` access 1，50 code bytes；语义 NOT_ANALYZED
- `method:9236c5689fdf42d58c49bd64` `onCheckSpawn(Lnet/minecraftforge/event/entity/living/LivingSpawnEvent$CheckSpawn;)V` access 1，513 code bytes；语义 NOT_ANALYZED
- `method:4051daa32a6bf756c319a2bb` `onLivingUpdateEvent(Lnet/minecraftforge/event/entity/living/LivingEvent$LivingUpdateEvent;)V` access 1，273 code bytes；语义 NOT_ANALYZED
- `method:3a769d725fd76d218fbd473e` `onFOVUpdateEvent(Lnet/minecraftforge/client/event/FOVUpdateEvent;)V` access 1，138 code bytes；语义 NOT_ANALYZED
- `method:0270213c6785ea1621a6a4fb` `<clinit>()V` access 8，10 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## 首批深度档案入口

UUID更新/level续租/jumpMovementFactor：历史reports/03_stuck_and_tick_order.md；重点报告§3。

[深度证据、规范与对照](../../../../../../reconstruction/reports/DEEP_FIRST_BATCH.md)

1. 身份/字节哈希/工具：本页顶部，原始来源非原作者源码。
2. 原文证据与解释：按上述位置与重点报告分栏读取。
3. 职责和触发：重点报告对应模块列出输入、调用次序、提前返回。
4. 功能与资源：对应 ORIGINAL_REGISTRY、RESOURCE_USAGE 和本类调用边，不将名字映射当语义。
5. 行为规范：重点报告的分支和边界；未列分支 UNKNOWN。
6. 现代差异：重点报告逐模块对照现代真实路径及存档风险。
7. 测试设计：原版对照本轮 NOT_RUN，现有现代回归见 R0_TEST_RESULTS.json。
8. 结论：PARTIAL，仅已列静态链；下一步按 NEXT_WORK_PACKAGES.md 闭合。
