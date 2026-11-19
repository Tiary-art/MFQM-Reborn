# MoreFunQuicksandMod/main/MuddyEvent

ID `class:d3c451224638c5c6181a9680`；class SHA `e1fedfef5a87cbf3952664102a8ea97507ba851ce2dc12d886fa09d46a6f986f`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / FIRST_BATCH_PARTIAL**（除重点模块报告给出的分支外）。super `java/lang/Object`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/MuddyEvent`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__MuddyEvent.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

无声明字段。

## 方法目录

- `method:02a69f5efcdc0c6a3d670140` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:bc15db42d0da3d7f5c31cba0` `onEntityConstructing(Lnet/minecraftforge/event/entity/EntityEvent$EntityConstructing;)V` access 1，34 code bytes；语义 NOT_ANALYZED
- `method:6a4f6f339837c8d6cb2eb6dc` `onLivingDeathEvent(Lnet/minecraftforge/event/entity/living/LivingDeathEvent;)V` access 1，50 code bytes；语义 NOT_ANALYZED
- `method:25c19f5495601c922f47e2ba` `onLivingUpdateEvent(Lnet/minecraftforge/event/entity/living/LivingEvent$LivingUpdateEvent;)V` access 1，240 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## 首批深度档案入口

湿润/干燥分支与残留阈值：original-phase3/08_COATING_CAMERA_TEXTURE_SPEC.md；重点报告§5。

[深度证据、规范与对照](../../../../../../reconstruction/reports/DEEP_FIRST_BATCH.md)

1. 身份/字节哈希/工具：本页顶部，原始来源非原作者源码。
2. 原文证据与解释：按上述位置与重点报告分栏读取。
3. 职责和触发：重点报告对应模块列出输入、调用次序、提前返回。
4. 功能与资源：对应 ORIGINAL_REGISTRY、RESOURCE_USAGE 和本类调用边，不将名字映射当语义。
5. 行为规范：重点报告的分支和边界；未列分支 UNKNOWN。
6. 现代差异：重点报告逐模块对照现代真实路径及存档风险。
7. 测试设计：原版对照本轮 NOT_RUN，现有现代回归见 R0_TEST_RESULTS.json。
8. 结论：PARTIAL，仅已列静态链；下一步按 NEXT_WORK_PACKAGES.md 闭合。
