# MoreFunQuicksandMod/main/items/ItemGrapplingHook

ID `class:bbf0aebebb8de9f8dd563c0e`；class SHA `85a0ca65deca6cfd74846abf9913fd740adf0f059dc495d111710f55d5091e69`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/item/Item`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/items/ItemGrapplingHook`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__items__ItemGrapplingHook.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:d42585d88fe3857f4aeb7beb` `itemIIcon1:Lnet/minecraft/util/IIcon;` access 2
- `field:b4bd0b0bdabf5653fcf28ed4` `itemIIcon2:Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:d00996e6726cd9f09042631c` `<init>()V` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:cce876d9c17ef728e42d2cdf` `func_77661_b(Lnet/minecraft/item/ItemStack;)Lnet/minecraft/item/EnumAction;` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:8939ec51a2e64c04f3561877` `func_77626_a(Lnet/minecraft/item/ItemStack;)I` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:de57624397a9df7f49dd6f7f` `func_77662_d()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:fa616220991198c4b6f8f408` `func_77629_n_()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:3b902ceda680f3a555b6f765` `func_77663_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/Entity;IZ)V` access 1，94 code bytes；语义 NOT_ANALYZED
- `method:85bd1fc8d82362d410b7489a` `func_77659_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)Lnet/minecraft/item/ItemStack;` access 1，330 code bytes；语义 NOT_ANALYZED
- `method:6be92cd19be430b9ad2c9ea9` `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:2ce14c76a7acf64dff2c7596` `func_77617_a(I)Lnet/minecraft/util/IIcon;` access 1，16 code bytes；语义 NOT_ANALYZED
- `method:da4f41d653f9279c4c369547` `onEntityItemUpdate(Lnet/minecraft/entity/item/EntityItem;)Z` access 1，40 code bytes；语义 NOT_ANALYZED
- `method:e1908a2a37a11f959667e090` `func_77624_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/entity/player/EntityPlayer;Ljava/util/List;Z)V` access 1，311 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
