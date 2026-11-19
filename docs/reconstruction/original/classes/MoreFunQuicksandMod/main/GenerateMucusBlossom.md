# MoreFunQuicksandMod/main/GenerateMucusBlossom

ID `class:ae32873dac2dc0fd2015518d`；class SHA `efb106b36558342b15cac1989ea5d1eb6135eb7b5a8ba445a60d49094f6424df`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/world/gen/feature/WorldGenerator`；interfaces `cpw/mods/fml/common/IWorldGenerator`；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/GenerateMucusBlossom`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__GenerateMucusBlossom.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

无声明字段。

## 方法目录

- `method:9e27d4b752df7e0018fe8d95` `validMaterial(IIILnet/minecraft/world/World;Z)Z` access 10，198 code bytes；语义 NOT_ANALYZED
- `method:46a5873643207d670881efb0` `genCheckVolume(IIIILnet/minecraft/world/World;ZZ)Z` access 10，152 code bytes；语义 NOT_ANALYZED
- `method:f6c23b2acda2ff7a19186210` `checkCanGrow(Lnet/minecraft/world/World;IIIZ)Z` access 9，52 code bytes；语义 NOT_ANALYZED
- `method:e421d67ad143b3f3fa9d73fb` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:e4981ec61feebd59edc330be` `generate(Ljava/util/Random;IILnet/minecraft/world/World;Lnet/minecraft/world/chunk/IChunkProvider;Lnet/minecraft/world/chunk/IChunkProvider;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:351a08188482d1a5662c9fdb` `setBlock(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，15 code bytes；语义 NOT_ANALYZED
- `method:405e85270d75f7dc9712a8f0` `collumnBlocks(Lnet/minecraft/world/World;IIIILnet/minecraft/block/Block;I)V` access 1，34 code bytes；语义 NOT_ANALYZED
- `method:d933f08a84c57b9278a098fb` `func_76484_a(Lnet/minecraft/world/World;Ljava/util/Random;III)Z` access 1，3429 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
