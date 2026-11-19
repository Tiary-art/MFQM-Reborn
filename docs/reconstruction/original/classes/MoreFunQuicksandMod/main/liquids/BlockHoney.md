# MoreFunQuicksandMod/main/liquids/BlockHoney

ID `class:4d8f027a15d12e0d3e7c0ea7`；class SHA `d22a7e8ec23d7595c04eb818d2e562f77cd550c6d0d9e9beeb3f88cbcee71213`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockHoney`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockHoney.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `honey`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:4d3d12ad5e862a67dc5f933b` `theHoneyIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:2505583d4c1f2ab296b86490` `materialHoney:Lnet/minecraft/block/material/Material;` access 25
- `field:6255bf0ef72fb432d0251b0d` `maxOpacity:I` access 2
- `field:3215751576d3543e9a2b9d27` `lastOpacity:I` access 2
- `field:ef3cc6d1b403cd7807fae7bd` `incOpacity:I` access 2

## 方法目录

- `method:6d3d9d3ac201c9e80e564949` `<init>(III)V` access 1，94 code bytes；语义 NOT_ANALYZED
- `method:bacfd962fce6f2c04cf17d5e` `func_149749_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，109 code bytes；语义 NOT_ANALYZED
- `method:395fd44b16db2f3d6e1de34b` `func_149678_a(IZ)Z` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:5e0a03ca3a9004fa17d8db26` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:a1952afbeaa64945c4cdc6cb` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2644 code bytes；语义 NOT_ANALYZED
- `method:539f82e134c8c9883128c5ec` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:6bfff9752b7f2f4463dec5ff` `checkFusion(Lnet/minecraft/world/World;IIILjava/util/Random;)I` access 1，293 code bytes；语义 NOT_ANALYZED
- `method:e08761ce8090afabf31c89ff` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，323 code bytes；语义 NOT_ANALYZED
- `method:bdb73dec4b2d26a447f87a2c` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:8d167641d853e61935685b68` `func_149727_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/player/EntityPlayer;IFFF)Z` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:939e1646507fa9b81060c9af` `eatMe(Lnet/minecraft/world/World;IIILnet/minecraft/entity/player/EntityPlayer;)V` access 2，86 code bytes；语义 NOT_ANALYZED
- `method:5570509331971e5dfe6b274c` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，84 code bytes；语义 NOT_ANALYZED
- `method:fd5589d9e4b0c257609fca95` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:e27afca00469a449c8d0058f` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:da7c444e59abe066b5342982` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:7d3818e96c635770e330de47` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:17e158ce26c307022c58fc9d` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，70 code bytes；语义 NOT_ANALYZED
- `method:374d8a8c04c6f92615909925` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，122 code bytes；语义 NOT_ANALYZED
- `method:f175cdd6798366a62523c32b` `<clinit>()V` access 8，17 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 352–354
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 518–520 · 519 morefunquicksandmod:Honey_Still | 519 morefunquicksandmod:Honey_Flowing

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Honey|0|Honey|`mfqm:honey`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
