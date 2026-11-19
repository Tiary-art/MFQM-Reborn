# MoreFunQuicksandMod/main/client/RenderTentacles

ID `class:a8b9aa1fab4edf6214edadad`；class SHA `366d462cff420021c9b82bff2bd0a4e463a9ac629af44e62eda0195cfed750f3`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/client/renderer/entity/Render`；interfaces ``；access `33`；annotations/attributes `SourceFile;RuntimeVisibleAnnotations`。内部类宿主 `MoreFunQuicksandMod/main/client/RenderTentacles`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__RenderTentacles.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:39addb6c4f0121522be812df` `Tentacles0:Lnet/minecraft/util/ResourceLocation;` access 2
- `field:d84e8772e603a84258f59a41` `Tentacles1:Lnet/minecraft/util/ResourceLocation;` access 2
- `field:3f4abc729140b0a134eea755` `Tentacles2:Lnet/minecraft/util/ResourceLocation;` access 2
- `field:cc8b6084d5efaf7444546a56` `Tentacles3:Lnet/minecraft/util/ResourceLocation;` access 2
- `field:2d5912a7d140ade26a963b79` `TentType:I` access 2

## 方法目录

- `method:1aca8d574fa1052cddf9fa00` `<init>(I)V` access 1，141 code bytes；语义 NOT_ANALYZED
- `method:16462db13083828d0b68ba7e` `doRenderTentacles(LMoreFunQuicksandMod/main/entity/EntityTentacles;DDDFF)V` access 1，902 code bytes；语义 NOT_ANALYZED
- `method:50692b3c32efd5420d9aa841` `drawCrossedSquares(Lnet/minecraft/client/renderer/Tessellator;DDDDF)V` access 1，340 code bytes；语义 NOT_ANALYZED
- `method:dc450976d969e98a73ff2246` `renderFleshCube(Lnet/minecraft/client/renderer/Tessellator;DDDDD)V` access 1，535 code bytes；语义 NOT_ANALYZED
- `method:b034f23727feaf6e589d9d4e` `func_110775_a(Lnet/minecraft/entity/Entity;)Lnet/minecraft/util/ResourceLocation;` access 4，58 code bytes；语义 NOT_ANALYZED
- `method:cd00a781764831deb3f75627` `func_76986_a(Lnet/minecraft/entity/Entity;DDDFF)V` access 1，18 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
