# MoreFunQuicksandMod/main/items/ItemClayBucket

ID `class:3ac2675edfb0da35b90273f2`；class SHA `974665bdc1d07443bb4b2756a5f5a40d4c0e9486b3f5995cfbf53d0b2d6fe68f`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/item/ItemBucket`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/items/ItemClayBucket`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__items__ItemClayBucket.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:2e912bbcc6118268dac7d9b6` `itemIIcon1:Lnet/minecraft/util/IIcon;` access 2
- `field:394ee2d4206dee896e8d84d6` `itemIIcon2:Lnet/minecraft/util/IIcon;` access 2
- `field:54bbf9d6c36bd03593b8d4e5` `items:[Ljava/lang/String;` access 10
- `field:72e7ae8ce0e3ffd60e8aeb4c` `block:Lnet/minecraft/block/Block;` access 1

## 方法目录

- `method:c9c625ac5c6f3135c4fbf11f` `<init>(Lnet/minecraft/block/Block;)V` access 1，32 code bytes；语义 NOT_ANALYZED
- `method:e68e6cc087ce41eeb8f1430e` `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:f6a2401eb0a6fdbbf322e1cc` `func_77617_a(I)Lnet/minecraft/util/IIcon;` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:57f18bd33a2f3278a95bf979` `func_150895_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:8f274555ed29775d5da239d8` `func_77667_c(Lnet/minecraft/item/ItemStack;)Ljava/lang/String;` access 1，50 code bytes；语义 NOT_ANALYZED
- `method:5ce2290f1465d93a7a90ba0b` `func_77659_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)Lnet/minecraft/item/ItemStack;` access 1，198 code bytes；语义 NOT_ANALYZED
- `method:10672344dc7275bcf169614d` `tryPlaceContainedLiquid2(Lnet/minecraft/world/World;IIILnet/minecraft/item/ItemStack;)Z` access 1，126 code bytes；语义 NOT_ANALYZED
- `method:0f326b761ea126b88499036d` `<clinit>()V` access 8，23 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `<init>(Lnet/minecraft/block/Block;)V` · CFR 49–55
- `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 58–61 · 59 morefunquicksandmod:BucketOfBrownClay | 60 morefunquicksandmod:BucketOfMineralClay
- `func_77617_a(I)Lnet/minecraft/util/IIcon;` · CFR 64–69
- `func_150895_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` · CFR 72–75 · 73 damage=0 | 74 damage=1
- `func_77667_c(Lnet/minecraft/item/ItemStack;)Ljava/lang/String;` · CFR 77–83

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Bucket of Clay|0|Bucket of Brown Clay|`mfqm:brown_clay_bucket`|
|Bucket of Clay|1|Bucket of Mineral Clay|`mfqm:mineral_clay_bucket`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
