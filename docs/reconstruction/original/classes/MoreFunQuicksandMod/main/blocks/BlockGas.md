# MoreFunQuicksandMod/main/blocks/BlockGas

ID `class:f17a0866fdaeaa1c6ac7a3cd`；class SHA `8b4d56ecba655a753efa0b9d78bf50eb0d5a51f1667a45aeb4821915f266d080`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockGas`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockGas.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `gas`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:20b26222e0da5709bfb94036` `IIconNormalArray:[Lnet/minecraft/util/IIcon;` access 2
- `field:94f3dcc004faf9e3ade4380f` `arrayDirection:[I` access 2
- `field:96b6290ec83981539881ac11` `soundTypeGas:Lnet/minecraft/block/Block$SoundType;` access 25
- `field:8751574688530fa0e0e69d80` `materialGas:Lnet/minecraft/block/material/Material;` access 25

## 方法目录

- `method:27c7b6ad240960ac1cda46b6` `<init>()V` access 1，57 code bytes；语义 NOT_ANALYZED
- `method:95e0d8dddc0273cbd19c80dd` `func_149749_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，71 code bytes；语义 NOT_ANALYZED
- `method:110a28bd8c54472602c6fa25` `RandomSpread(Lnet/minecraft/world/World;IIII)I` access 1，424 code bytes；语义 NOT_ANALYZED
- `method:83ce428b394a8340f5964211` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，241 code bytes；语义 NOT_ANALYZED
- `method:aa6ccc9a7dcd853b22916239` `CheckBreathProtect(Lnet/minecraft/entity/Entity;)Z` access 1，139 code bytes；语义 NOT_ANALYZED
- `method:aca5a11a29807bcbc4822d50` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，1350 code bytes；语义 NOT_ANALYZED
- `method:c9296b65b4004e4141546c2d` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，19 code bytes；语义 NOT_ANALYZED
- `method:dae9bea61e7e62c731cebd89` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，39 code bytes；语义 NOT_ANALYZED
- `method:9f8ac895aa4ac7f4954361c6` `func_149643_k(Lnet/minecraft/world/World;III)I` access 1，9 code bytes；语义 NOT_ANALYZED
- `method:7a8a2450d53e11b07273873a` `func_149678_a(IZ)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:d47a8745bdf39908e73d260b` `func_149701_w()I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:7ce3d666530e1f5c4238acdd` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，7 code bytes；语义 NOT_ANALYZED
- `method:f018089d501557bfffb3a3be` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:5f90f89dba20a3dde391141a` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:70439e2ff6b2dc6681cb44be` `isSolid()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:9eb3a4bc80524c6a7bfd6ba6` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:3447ad6531d8a745c60f4b25` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:3b277cdba72d25baa5b8bc6c` `func_149646_a(Lnet/minecraft/world/IBlockAccess;IIII)Z` access 1，196 code bytes；语义 NOT_ANALYZED
- `method:8b05742e7726cbd4262599f8` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，59 code bytes；语义 NOT_ANALYZED
- `method:58da5afdda94e08c5f39639f` `func_149635_D()I` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:09f4f11b9ee7431fb738835d` `func_149741_i(I)I` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:470221f247c2178fe7137fb4` `func_149720_d(Lnet/minecraft/world/IBlockAccess;III)I` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:94e5d7fd01ffa61da7f882bc` `<clinit>()V` access 8，29 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 378–380
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 433–438 · 436 morefunquicksandmod:Gas

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Gas|0|Gas|`mfqm:gas`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
