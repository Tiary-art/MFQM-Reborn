# MoreFunQuicksandMod/main/liquids/BlockSinkyLiquid

ID `class:fea1e6e928ef480ee4a288d6`；class SHA `62157d0ada95f109c622efa5982a2143526a3d5309772c4cdd9191972b4cdf62`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockSinkyLiquid`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockSinkyLiquid.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `sinky_liquid`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:3e208705d30c4d991b1a64b8` `theMireIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:9d749d52c7d02926f61da217` `materialSinky:Lnet/minecraft/block/material/Material;` access 25
- `field:9eac04e66586edba02a5fe10` `maxOpacity:I` access 2
- `field:a8889533c8033e865a37b42f` `lastOpacity:I` access 2
- `field:b13f90ebd64abaad3c1571c5` `incOpacity:I` access 2

## 方法目录

- `method:219e0a6bbbd4179b08136cd1` `<init>(III)V` access 1，74 code bytes；语义 NOT_ANALYZED
- `method:a873f3c2cabe55dc58e5593b` `IsReplaceable(Lnet/minecraft/world/World;III)Z` access 4，72 code bytes；语义 NOT_ANALYZED
- `method:f205f0cf11fa15304a1f9e36` `IsSolidM(Lnet/minecraft/world/World;III)Z` access 1，222 code bytes；语义 NOT_ANALYZED
- `method:57454a8419c63d5da0a1b812` `IsNear(Lnet/minecraft/world/World;III)Z` access 1，62 code bytes；语义 NOT_ANALYZED
- `method:a63deea637e580db495fd03b` `SetBlockThere(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;II)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:7922fabb40909d81442024a1` `Fusion(Lnet/minecraft/world/World;IIIZZ)Z` access 1，3859 code bytes；语义 NOT_ANALYZED
- `method:62258de88549466b446cf663` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，849 code bytes；语义 NOT_ANALYZED
- `method:94975b8c4234de4201bd8c07` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:5df5cb3ff00d7b1d8e3782b4` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，1430 code bytes；语义 NOT_ANALYZED
- `method:8b22c902c2f90451e586bf22` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，145 code bytes；语义 NOT_ANALYZED
- `method:e7bc13c05aa9bf67dcc82a66` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:d67045c408527271c22d107a` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:a448b2ec733801d8c2a388fb` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:116d883461ac889e5ad45b4c` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:864e4ca02cfff5d15b792abd` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:38bf3c852871ebed8632e62f` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，70 code bytes；语义 NOT_ANALYZED
- `method:6fa26357353600f153d81ffb` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，124 code bytes；语义 NOT_ANALYZED
- `method:75f4cbbe47072afd90ad202c` `<clinit>()V` access 8，17 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
