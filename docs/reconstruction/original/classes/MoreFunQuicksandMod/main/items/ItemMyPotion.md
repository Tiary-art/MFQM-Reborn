# MoreFunQuicksandMod/main/items/ItemMyPotion

ID `class:690746da0eae5fd8d04ca350`；class SHA `c1e889f6f8077bcfc011e39c35f720fa91ba5e1db6fb7cd4c81a6fa6d597b206`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/item/Item`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/items/ItemMyPotion`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__items__ItemMyPotion.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:49f7ea52863f953dbddebafc` `itemIcons:[Lnet/minecraft/util/IIcon;` access 2
- `field:667be45dc7be0783a5c5e4c0` `items:[Ljava/lang/String;` access 10

## 方法目录

- `method:2afe914499e628a7276b4fc4` `<init>()V` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:89f8e740587a2cfcc9304e14` `func_77654_b(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)Lnet/minecraft/item/ItemStack;` access 1，228 code bytes；语义 NOT_ANALYZED
- `method:e52da101108e39baea98469d` `func_77626_a(Lnet/minecraft/item/ItemStack;)I` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:74c4e0c5229ee2b9e2aa40d1` `func_77661_b(Lnet/minecraft/item/ItemStack;)Lnet/minecraft/item/EnumAction;` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:e390355387a583804813d383` `func_77659_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)Lnet/minecraft/item/ItemStack;` access 1，12 code bytes；语义 NOT_ANALYZED
- `method:5392fa28ad6689aaaf97ba0d` `func_77648_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;IIIIFFF)Z` access 1，67 code bytes；语义 NOT_ANALYZED
- `method:bb4ffdabfa7108aa9f15de6a` `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:bde20b1724e8e4095f0576cd` `func_77667_c(Lnet/minecraft/item/ItemStack;)Ljava/lang/String;` access 1，50 code bytes；语义 NOT_ANALYZED
- `method:0712d5f3e3590d4952d45ece` `func_150895_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` access 1，52 code bytes；语义 NOT_ANALYZED
- `method:85b5001f2c8557ed7c7645cf` `func_77617_a(I)Lnet/minecraft/util/IIcon;` access 1，11 code bytes；语义 NOT_ANALYZED
- `method:6a9cdc35a1dcd8e5092eba49` `func_77624_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/entity/player/EntityPlayer;Ljava/util/List;Z)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:b052cc2293dc7d732d1f4e6f` `checkCanSpawnMucusBlossom(Lnet/minecraft/world/World;III)Z` access 1，103 code bytes；语义 NOT_ANALYZED
- `method:54664cc9b73ba97cd102b848` `spawnMucusBlossom(Lnet/minecraft/world/World;III)V` access 1，280 code bytes；语义 NOT_ANALYZED
- `method:f08cb7ba47ea305e587c619d` `validMaterial(IIILnet/minecraft/world/World;)Z` access 2，171 code bytes；语义 NOT_ANALYZED
- `method:78b7a2c8407910fed6551018` `<clinit>()V` access 8，32 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
