# MoreFunQuicksandMod/main/liquids/BlockSlurry

ID `class:58854726bf339c71b35cab8b`；class SHA `b5c8cb9c372141fdd44656572f1b244bb0ff3bc228b25d6c7d8dec4ea9af08e1`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockSlurry`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockSlurry.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `slurry`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:18f21133fadbfb5cea0cf627` `theSlurryIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:db7e3f457ff74e21de17b355` `materialSlurry:Lnet/minecraft/block/material/Material;` access 25
- `field:d88a65247f179f7ecaa9ff27` `maxOpacity:I` access 2
- `field:27e3435666978f1494531dbe` `lastOpacity:I` access 2
- `field:18689ece0878e11e4d31cb1b` `incOpacity:I` access 2

## 方法目录

- `method:ff373a3aadf7a3b6c7b90da0` `<init>(III)V` access 1，94 code bytes；语义 NOT_ANALYZED
- `method:d5ae9d59207e41ccea624210` `func_149749_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，109 code bytes；语义 NOT_ANALYZED
- `method:33fff56e7f1ee2b788fa680b` `func_149678_a(IZ)Z` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:8016e3e283a1c4c6b7eaaad3` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:f0e210ae1cad85ca2b106771` `CheckPoisonProtect(Lnet/minecraft/entity/Entity;)Z` access 9，314 code bytes；语义 NOT_ANALYZED
- `method:5274389555075e2b4a8de3a3` `CheckBreathProtect(Lnet/minecraft/entity/Entity;)Z` access 1，139 code bytes；语义 NOT_ANALYZED
- `method:b367dd813ef0c53f580216dc` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2936 code bytes；语义 NOT_ANALYZED
- `method:c8cad9108d45267e35241581` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:5638aa1a64465af38180ba16` `checkFusion(Lnet/minecraft/world/World;IIILjava/util/Random;)I` access 1，408 code bytes；语义 NOT_ANALYZED
- `method:a4b56d423ba9021f979ed1f7` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，526 code bytes；语义 NOT_ANALYZED
- `method:d6301932d9c72c9b6203bedc` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:72049657adc43fae9a987578` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，84 code bytes；语义 NOT_ANALYZED
- `method:c197cde23f3f4c6cd866dd0b` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:a89e474562fe7b3df110da87` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:7789038b93d5972495f9474b` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:0df3da2fcd7b5dbf99f944ae` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:87bedd3a7d04e3e3e34fb185` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，70 code bytes；语义 NOT_ANALYZED
- `method:76969c68e1afd45cc5253016` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，122 code bytes；语义 NOT_ANALYZED
- `method:4a5c0062d669a78429606978` `<clinit>()V` access 8，17 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
