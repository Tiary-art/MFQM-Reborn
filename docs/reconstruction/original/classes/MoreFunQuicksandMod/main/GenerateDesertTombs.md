# MoreFunQuicksandMod/main/GenerateDesertTombs

ID `class:f19c9f3120e2110c15c9da8e`；class SHA `2d4034676b94ddf455746ca33b13252e8b3be2fe7cccd2227d40f60bdfd10125`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/world/gen/feature/WorldGenerator`；interfaces `cpw/mods/fml/common/IWorldGenerator`；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/GenerateDesertTombs`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__GenerateDesertTombs.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

无声明字段。

## 方法目录

- `method:394ec42ab0bc889c8b201fb1` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:d12d7da64e81ffc421895aa4` `generate(Ljava/util/Random;IILnet/minecraft/world/World;Lnet/minecraft/world/chunk/IChunkProvider;Lnet/minecraft/world/chunk/IChunkProvider;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:4abc6fb8fd71b8ff869f4159` `generateSpawner(Lnet/minecraft/world/World;III)V` access 1，144 code bytes；语义 NOT_ANALYZED
- `method:f6618b0ba9ca5cc2ef7933f1` `generateChest(Lnet/minecraft/world/World;IIII)V` access 1，490 code bytes；语义 NOT_ANALYZED
- `method:19362992d55e6233d9c34c3c` `generateChest2(Lnet/minecraft/world/World;IIII)V` access 1，490 code bytes；语义 NOT_ANALYZED
- `method:677d6402004bc62db787b7d6` `setBlock(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，15 code bytes；语义 NOT_ANALYZED
- `method:37a1e3326ff13923a21f13d3` `func_76484_a(Lnet/minecraft/world/World;Ljava/util/Random;III)Z` access 1，33638 code bytes；语义 NOT_ANALYZED
- `method:ad8eb7e4ae32c0f7d0d9bf00` `generate2(Lnet/minecraft/world/World;Ljava/util/Random;III)Z` access 1，33972 code bytes；语义 NOT_ANALYZED
- `method:505d45f022032899f619ffec` `generate3(Lnet/minecraft/world/World;Ljava/util/Random;III)Z` access 1，33934 code bytes；语义 NOT_ANALYZED
- `method:6c2ccdde9fe3a6b7c5305202` `generate4(Lnet/minecraft/world/World;Ljava/util/Random;III)Z` access 1，33965 code bytes；语义 NOT_ANALYZED
- `method:c856b5d52f717cb727792ff9` `generate5(Lnet/minecraft/world/World;Ljava/util/Random;III)Z` access 1，34030 code bytes；语义 NOT_ANALYZED
- `method:3225eec056051a75d5d8a126` `generate6(Lnet/minecraft/world/World;Ljava/util/Random;III)Z` access 1，22412 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
