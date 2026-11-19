# MoreFunQuicksandMod/main/liquids/BlockBog

ID `class:ff9385b9a6cc1bd678b0e294`；class SHA `99f99a06517ec0407bd17e4c7420222d3d01cf7d83842aba6eb5bea1253512a3`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockBog`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockBog.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `bog`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:9e169c7bfef0323706175c39` `theBogIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:d5a4aa150085deac58d73552` `materialBog:Lnet/minecraft/block/material/Material;` access 25
- `field:c07924b73ed443461f7df6ff` `maxOpacity:I` access 2
- `field:3ac60f7729775996a4179189` `lastOpacity:I` access 2
- `field:34fbe96f0732be5aa9a83f0a` `incOpacity:I` access 2

## 方法目录

- `method:0a670790f602624c61c262f4` `<init>(III)V` access 1，94 code bytes；语义 NOT_ANALYZED
- `method:6eb13230dff8ab31a8c498ea` `func_149749_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，109 code bytes；语义 NOT_ANALYZED
- `method:cb5915643378a990ba134612` `func_149678_a(IZ)Z` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:3c7faea0044b693c07afe537` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:9506cdad360b34dd23e2af35` `getMaxRenderHeightMeta()I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:e2b9befd701498a26f509044` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2729 code bytes；语义 NOT_ANALYZED
- `method:f0c2226872ef1a2ea98370d2` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:90e78e0326b12ab8b4f0d096` `checkFusion(Lnet/minecraft/world/World;IIILjava/util/Random;)I` access 1，346 code bytes；语义 NOT_ANALYZED
- `method:ba2f03a0936a540ef51c8a18` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，322 code bytes；语义 NOT_ANALYZED
- `method:90751e2a21ea56a3b6d4d16f` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:6b9ab97d2f1ca4a8a21fe6f2` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，83 code bytes；语义 NOT_ANALYZED
- `method:68604388c76e79a4e70541dc` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:63c201804bc4e91cae423a30` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:3748ee2902d227d47cdb3e34` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:037a6e5d6130d061dd462366` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:dc23aa3a71e4179193fa4e57` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，70 code bytes；语义 NOT_ANALYZED
- `method:92ccfbda955cdfc7ec25d17f` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，122 code bytes；语义 NOT_ANALYZED
- `method:a5ab946f64415293128366ec` `<clinit>()V` access 8，17 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 335–337
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 488–490 · 489 morefunquicksandmod:Bog_Still | 489 morefunquicksandmod:Bog_Flowing

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Bog|0|Bog|`mfqm:bog`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
