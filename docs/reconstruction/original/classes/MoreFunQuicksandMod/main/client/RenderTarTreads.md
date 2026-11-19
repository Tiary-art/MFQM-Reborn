# MoreFunQuicksandMod/main/client/RenderTarTreads

ID `class:2db570319e477f32c1e8bbbd`；class SHA `5148f8069d50f45fa29b6c9201a6ce2b3fd8fa0d11a22f2cb8e55c04a0b8998d`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/client/renderer/entity/Render`；interfaces ``；access `33`；annotations/attributes `SourceFile;RuntimeVisibleAnnotations`。内部类宿主 `MoreFunQuicksandMod/main/client/RenderTarTreads`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__RenderTarTreads.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:bcee086689a241289c659066` `TarTreads0:Lnet/minecraft/util/ResourceLocation;` access 26

## 方法目录

- `method:447d4f2e382f924f37e645f2` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:68f69d9c384e7c405a40e096` `doRenderTentacles(LMoreFunQuicksandMod/main/entity/EntityTarTreads;DDDFF)V` access 1，498 code bytes；语义 NOT_ANALYZED
- `method:413369d26279916df7bad7d6` `drawCrossedSquares(Lnet/minecraft/client/renderer/Tessellator;DDDDD)V` access 1，332 code bytes；语义 NOT_ANALYZED
- `method:bbac5a6a9161ab764543f3fc` `func_110775_a(Lnet/minecraft/entity/Entity;)Lnet/minecraft/util/ResourceLocation;` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:d38f2810316227927aad502e` `func_76986_a(Lnet/minecraft/entity/Entity;DDDFF)V` access 1，18 code bytes；语义 NOT_ANALYZED
- `method:fc213623d0343703831d91cb` `<clinit>()V` access 8，17 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
