# MoreFunQuicksandMod/main/blocks/BlockSolidHoney

ID `class:48515def77c292991a77ed53`；class SHA `905e9f3fb32d78a774e99b8bb4b90b469abb3ac2257ac21b354820e825677056`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockSolidHoney`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockSolidHoney.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `solid_honey`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:77abe5d3110d8b97a9c1d5b2` `theQIIcon:Lnet/minecraft/util/IIcon;` access 0

## 方法目录

- `method:dc44e9a331f23bcadb2d6950` `<init>()V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:ed2bb6afff661449926827e8` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，52 code bytes；语义 NOT_ANALYZED
- `method:755f34b49940c0fc5f1753e7` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:67cb805c306f828caacaf06f` `validForSpread(Lnet/minecraft/world/World;III)Z` access 4，30 code bytes；语义 NOT_ANALYZED
- `method:441af6d9eb85f51d4ddc0275` `hyperHoney(Lnet/minecraft/world/World;IIII)V` access 1，483 code bytes；语义 NOT_ANALYZED
- `method:494212668e9297f9b42b2f85` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，292 code bytes；语义 NOT_ANALYZED
- `method:9493e14624f06de79da87501` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，333 code bytes；语义 NOT_ANALYZED
- `method:97712f322ffef545433c5f53` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，42 code bytes；语义 NOT_ANALYZED
- `method:3be9e076caa49fa41f0307cb` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，15 code bytes；语义 NOT_ANALYZED
- `method:a2181dd667c6c069573c7bfd` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:058ed5fb40c66e2b8d6339bc` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:f1e5ebd90a1749f25f271627` `func_149643_k(Lnet/minecraft/world/World;III)I` access 1，9 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 236–238
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 241–243 · 242 morefunquicksandmod:Honey

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|SolidHoney|0|Solid Honey|`mfqm:solid_honey`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
