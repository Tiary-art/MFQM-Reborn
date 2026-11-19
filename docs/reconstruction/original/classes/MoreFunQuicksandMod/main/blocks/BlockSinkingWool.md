# MoreFunQuicksandMod/main/blocks/BlockSinkingWool

ID `class:aba5f12aea7e97627e9c7977`；class SHA `bd9ce752ea28cf725dc632d5980017ab7f527d971873cbbc4f9c450fddcb7fef`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/BlockColored`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockSinkingWool`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockSinkingWool.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `sinking_rug`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

无声明字段。

## 方法目录

- `method:bd99a9cf94be21c9df3cbb14` `<init>()V` access 1，81 code bytes；语义 NOT_ANALYZED
- `method:39fdd900d6aec02c4b9f14ae` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:e839871f723847e7b6da757e` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2681 code bytes；语义 NOT_ANALYZED
- `method:d347d765ef2ccad3ef6427b5` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:a24fe5e38be071953d45227a` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，107 code bytes；语义 NOT_ANALYZED
- `method:b25fba4a97c08547c54be32c` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，63 code bytes；语义 NOT_ANALYZED
- `method:9cbbb56d18938a6f79efc02b` `func_149664_b(Lnet/minecraft/world/World;IIII)V` access 1，42 code bytes；语义 NOT_ANALYZED
- `method:165cadd7e40f39006d3a5900` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:1c7ef732c6d0bb4d2321d2a3` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:f607c6227c0f244219bc7c7b` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:0df31f709796622e4b73a937` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:877dd9a53d44d405cab6f73b` `isSolid()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:69200fc17fbeb943f80d4464` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，59 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
