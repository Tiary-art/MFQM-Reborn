# MoreFunQuicksandMod/main/liquids/BlockJungleQuicksand

ID `class:d321748f2f9b36970e57679b`；class SHA `dc5a0368082945a519ef8a265a33c10206ffa087cdcffac7522eae67e1920d63`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockJungleQuicksand`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockJungleQuicksand.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `jungle_quicksand`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:dca30ba96de1185d821a304d` `theJQIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:b89af3bb68139f0d9de1ecde` `materialQuicksand:Lnet/minecraft/block/material/Material;` access 25
- `field:1a85af92d96e0c7331046b5a` `maxOpacity:I` access 2
- `field:b266ea5ba30ad7de7534a3e9` `lastOpacity:I` access 2
- `field:ca3b5adadab94ec6119b1645` `incOpacity:I` access 2

## 方法目录

- `method:b536594dc9751180b6880b88` `<init>(III)V` access 1，94 code bytes；语义 NOT_ANALYZED
- `method:2c747ef213e241ceca355979` `func_149749_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，109 code bytes；语义 NOT_ANALYZED
- `method:18f497fb88abd52ffa0fe9df` `func_149678_a(IZ)Z` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:72d81c287a2e70b603aa3ef9` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:d7dda6632400d8c9d931cf4a` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2506 code bytes；语义 NOT_ANALYZED
- `method:585d0c9c13bf9b815c67de6d` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:be4a2ba116050382b27f01a4` `checkFusion(Lnet/minecraft/world/World;IIILjava/util/Random;)I` access 1，346 code bytes；语义 NOT_ANALYZED
- `method:22a6eb8091dd882637deb8c4` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，323 code bytes；语义 NOT_ANALYZED
- `method:7a946b7897449464588b0e0f` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:fdc3e5b1e5614f2cafe77ef8` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，87 code bytes；语义 NOT_ANALYZED
- `method:45a4eea1590af388c7c90682` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:20645296f282ea5ba954d2fe` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:5b59408c78270255836882e6` `isSideSolid(Lnet/minecraft/world/World;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:55013306d1fe738c4e97019b` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:923d55074f95b6f371941df6` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:aaf570a42dbc193d54692899` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，70 code bytes；语义 NOT_ANALYZED
- `method:072d5abee4baa8ef63eca667` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，122 code bytes；语义 NOT_ANALYZED
- `method:24bf14e6564cbdbbff8a0bda` `<clinit>()V` access 8，17 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
