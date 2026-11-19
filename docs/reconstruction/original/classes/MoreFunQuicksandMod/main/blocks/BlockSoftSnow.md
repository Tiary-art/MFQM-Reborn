# MoreFunQuicksandMod/main/blocks/BlockSoftSnow

ID `class:e652e076d861cf6d6ee5b7e5`；class SHA `c3ba8d15372507becdd02fcbbb0854ea8eee7651efe81ec0adea6cc02b8402a3`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/BlockSnowBlock`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockSoftSnow`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockSoftSnow.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `soft_snow`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:6c664028680105870209dd0e` `theSnowIIcon:Lnet/minecraft/util/IIcon;` access 1

## 方法目录

- `method:ea31cea778c46f1df0304c65` `<init>()V` access 1，64 code bytes；语义 NOT_ANALYZED
- `method:01f1aa8a2e8eb4ca46e6551b` `func_149643_k(Lnet/minecraft/world/World;III)I` access 1，9 code bytes；语义 NOT_ANALYZED
- `method:52ee66a235993aca0ab7368e` `func_149666_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:1f153d37398f00a38d6b9101` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:0123a01b15792328b1692476` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2020 code bytes；语义 NOT_ANALYZED
- `method:59461cd2ea158a94e5e4d8be` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:0319aec85530ab71be4eb748` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:a6367fd3751bb9b3ed796f32` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，100 code bytes；语义 NOT_ANALYZED
- `method:cefa1ba60530032812407952` `func_149700_E()Z` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:728eb7b01ac925028dea84a8` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:f569c43af6712717c4a7d7ba` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，51 code bytes；语义 NOT_ANALYZED
- `method:51915f2c628785df5fb2117e` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:9bc6ffc592b0bcc0902c24c7` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:e41c9dc99bf2fb6b471e9cb4` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:678a18843699f6b3a732a33b` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，49 code bytes；语义 NOT_ANALYZED
- `method:6df10ab49ea9d00a925518d0` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:e65b940cb25d0a4b1287c334` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，15 code bytes；语义 NOT_ANALYZED
- `method:bc7a7fc53a69b9029e607408` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:54957979b8557ddfa6fa1aac` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:8ae9d518f40ce7ecca0da0c4` `isSolid()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:0612fe21490e7868bd8ac539` `func_149635_D()I` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:69ce54c313c9ff12baffb1fc` `func_149741_i(I)I` access 1，50 code bytes；语义 NOT_ANALYZED
- `method:e933439dcb6ed32af6d8ba1e` `func_149720_d(Lnet/minecraft/world/IBlockAccess;III)I` access 1，63 code bytes；语义 NOT_ANALYZED
- `method:1b3088761f91eb97bf32d84a` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，107 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149666_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` · CFR 78–81 · 79 damage=0 | 80 damage=1
- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 287–292
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 353–355 · 354 morefunquicksandmod:SoftSnow

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|SoftSnow|0|Soft Snow|`mfqm:soft_snow`|
|SoftSnow|1|Soft Ash|`mfqm:soft_ash`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
