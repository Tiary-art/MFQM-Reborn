# MoreFunQuicksandMod/main/liquids/BlockTar

ID `class:446b1e734d4a8dd46f8d7b01`；class SHA `8fb441fa8abc3769461ab01dbf1ccc084308775faa1caf750a8c8fd60a8eea93`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockTar`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockTar.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `tar`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:9b01570b4455b0b9bcaf5bd4` `theTarIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:999aa69a285f1fced248465d` `materialTar:Lnet/minecraft/block/material/Material;` access 25
- `field:9a4a163347ef2f44f928d47c` `maxOpacity:I` access 2
- `field:6368b88a7a9f9afb40044367` `lastOpacity:I` access 2
- `field:6de3c5db1d1162c23850db83` `incOpacity:I` access 2

## 方法目录

- `method:c4d5a26bae633d7e17712487` `<init>(III)V` access 1，88 code bytes；语义 NOT_ANALYZED
- `method:38c4640ee986de63246ac37c` `func_149749_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，88 code bytes；语义 NOT_ANALYZED
- `method:cabef0e49bbb53706a277fad` `func_149678_a(IZ)Z` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:adb1cc57eba28babbe07e391` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:7dd4ab22e2a3122cc0f27250` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，3520 code bytes；语义 NOT_ANALYZED
- `method:dc8e965b9918b273e7893d3f` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:e88ba64d86e72b431db0496c` `TBLSpawnTarBeast(Lnet/minecraft/world/World;III)V` access 1，270 code bytes；语义 NOT_ANALYZED
- `method:5fc74c8911915b971660cb62` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，835 code bytes；语义 NOT_ANALYZED
- `method:1ab8700d2e158bd1f3c6e980` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:39a9fd508fdcdaeb7ee4fec0` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，180 code bytes；语义 NOT_ANALYZED
- `method:249ef5445138f6cdac293b0d` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:8e5da876925c7ae1a4df8c28` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:afc71f3e037b7a4edb9fef90` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:709222c55468a5bf99a9b3a8` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:dce19054c7dfc014e0cb1368` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，70 code bytes；语义 NOT_ANALYZED
- `method:c8010526c05c9db8b66d8ed0` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，122 code bytes；语义 NOT_ANALYZED
- `method:91b5308b25e0fcf54eb5b45e` `<clinit>()V` access 8，17 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
