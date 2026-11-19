# MoreFunQuicksandMod/main/blocks/BlockHoneycomb

ID `class:299ca62419e37d400ee8ec59`；class SHA `29c4a513fc520e2802eea61b15c9bc38695236fc9652e8b2ceb5d6f0e259b33d`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockHoneycomb`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockHoneycomb.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `honeycomb`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:6fc22ddfbea054d1f4f308b6` `IIconMArray:[Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:ade06fe8da03dfe52103611d` `<init>()V` access 1，50 code bytes；语义 NOT_ANALYZED
- `method:e34f2d1260fd815010053ad3` `func_149666_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` access 1，52 code bytes；语义 NOT_ANALYZED
- `method:d57f567baf8e65744a359b2e` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，11 code bytes；语义 NOT_ANALYZED
- `method:b7e4bd6c07404b93f2d733f1` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:872502def43b47d1aa86461b` `quantityDropped(IILjava/util/Random;)I` access 1，26 code bytes；语义 NOT_ANALYZED
- `method:ce098eba2d66c0299f858341` `func_149692_a(I)I` access 1，38 code bytes；语义 NOT_ANALYZED
- `method:09725189459a05dc32b1593b` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:9878ded46fa00f1bcc3fb218` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:3885d7c753681e398d846038` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，173 code bytes；语义 NOT_ANALYZED
- `method:764328bf218337fc69dceea4` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，27 code bytes；语义 NOT_ANALYZED
- `method:420d14edd8aaf534f26e94a7` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，51 code bytes；语义 NOT_ANALYZED
- `method:64529a9e7f30669f9c4b1bd4` `func_149643_k(Lnet/minecraft/world/World;III)I` access 1，9 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149666_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` · CFR 57–61 · 58 damage=0 | 59 damage=1 | 60 damage=2
- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 64–66
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 141–146 · 143 morefunquicksandmod:honeycomb0 | 144 morefunquicksandmod:honeycomb1 | 145 morefunquicksandmod:honeycomb2

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Honeycomb|0|Honeycomb|`mfqm:honeycomb`|
|Honeycomb|1|Honeycomb Empty|`mfqm:honeycomb_empty`|
|Honeycomb|2|Honeycomb Filled|`mfqm:honeycomb_filled`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
