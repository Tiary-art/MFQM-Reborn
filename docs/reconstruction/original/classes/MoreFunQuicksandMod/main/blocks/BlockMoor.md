# MoreFunQuicksandMod/main/blocks/BlockMoor

ID `class:bcfbde87be8c8affa96d1057`；class SHA `eaaa54eb8045a2af7563e95571133e0afc82fc3ae3665827f1be89e93b0db03c`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockMoor`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockMoor.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `moor`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:cb53a3d861cdcd546322aa85` `IIconSide0:Lnet/minecraft/util/IIcon;` access 2
- `field:92de87e282d7e451c1a4cf31` `maxOpacity:I` access 2
- `field:5fe43d4bd243e3c3df1b39fa` `lastOpacity:I` access 2
- `field:0ecdbb466ebed5095db99150` `incOpacity:I` access 2

## 方法目录

- `method:7c9a4fd71e2e8c29b893f76d` `<init>(III)V` access 1，89 code bytes；语义 NOT_ANALYZED
- `method:bbebc0e603204a1603c92222` `SetBlockThere(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;II)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:4b46d9f256ac66682a1fb42b` `SetBlockThere(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，39 code bytes；语义 NOT_ANALYZED
- `method:c44123cdd65a61680de9b84f` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，1118 code bytes；语义 NOT_ANALYZED
- `method:906322cc0b235770e70532a0` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，6 code bytes；语义 NOT_ANALYZED
- `method:85984f507ddb1d4ee20818cb` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，15 code bytes；语义 NOT_ANALYZED
- `method:46550b0dd802dba5ba9bf91a` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，53 code bytes；语义 NOT_ANALYZED
- `method:d8550e4e8cbbbf0e943d61d0` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:9ce922c882eaec696dc226d2` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:6692e35cb871b413d6e28cbd` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:430f6b331ff03adf90834b61` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:bd2aace54f321b7b52afe519` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:3c07a788b530d37b3c6e3bc0` `func_149700_E()Z` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:289563c0ee8a89ccc71469c9` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:55e408aa85c23ce8ba5f4cdd` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:54ef8ba4478e637730bdeeec` `isSolid()Z` access 1，2 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 240–242
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 245–247 · 246 morefunquicksandmod:Moor0

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Moor|0|Moor|`mfqm:moor`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
