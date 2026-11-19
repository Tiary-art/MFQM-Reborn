# MoreFunQuicksandMod/main/CustomWorldGenLakes

ID `class:68016b5edc393157abe3fb2a`；class SHA `3c531bcc35960ff7ae965f159eab2f289fe0f2221c5e941c15fb153c6c6a7c2c`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/world/gen/feature/WorldGenerator`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/CustomWorldGenLakes`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__CustomWorldGenLakes.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:0b1993456337259d5a3fe8fa` `blockIndex:Lnet/minecraft/block/Block;` access 2

## 方法目录

- `method:50c0618074bea817fde24dc1` `<init>(Lnet/minecraft/block/Block;)V` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:f0e10acc56f3a8c79e8ddd9b` `func_76484_a(Lnet/minecraft/world/World;Ljava/util/Random;III)Z` access 1，13 code bytes；语义 NOT_ANALYZED
- `method:f42fef86b08c2bceb80abc6f` `generate(Lnet/minecraft/world/World;Ljava/util/Random;IIII)Z` access 1，1519 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
