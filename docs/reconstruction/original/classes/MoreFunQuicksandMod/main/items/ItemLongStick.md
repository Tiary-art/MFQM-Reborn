# MoreFunQuicksandMod/main/items/ItemLongStick

ID `class:bebc5ba6537a309af325b846`；class SHA `e8b27d2dc05abc29c25b17a34beba28c37feb727a7dd2b4306f8257abd9c717a`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/item/Item`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/items/ItemLongStick`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__items__ItemLongStick.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:6b0453b9474a8aa7be198cf2` `itemIcon:Lnet/minecraft/util/IIcon;` access 2
- `field:c00b2cbc8707993a4242f64a` `itemL1Icon:Lnet/minecraft/util/IIcon;` access 1
- `field:540c3b5b6af35c18375ba946` `itemL2Icon:Lnet/minecraft/util/IIcon;` access 1
- `field:24a6d345fd1d8b14be5919bc` `quicksandHardCoof:[I` access 9

## 方法目录

- `method:679e0abb8605448c5653197d` `<init>()V` access 1，26 code bytes；语义 NOT_ANALYZED
- `method:f33597d1bbb9f6b5db7372b8` `func_77661_b(Lnet/minecraft/item/ItemStack;)Lnet/minecraft/item/EnumAction;` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:2a68f798c99000099b5e06ea` `func_77626_a(Lnet/minecraft/item/ItemStack;)I` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:1902af73576e8fb02bc4da0a` `func_77659_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)Lnet/minecraft/item/ItemStack;` access 1，26 code bytes；语义 NOT_ANALYZED
- `method:72bf8b048b113a8f9bf0a6f6` `func_77662_d()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:b1746c4dc6161bfe75516e0d` `func_77629_n_()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:7f3e9d1d8fbe101a37955263` `func_77648_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;IIIIFFF)Z` access 1，72 code bytes；语义 NOT_ANALYZED
- `method:b74acff6c2fb0b192d0e3cf1` `func_77663_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/Entity;IZ)V` access 1，620 code bytes；语义 NOT_ANALYZED
- `method:e31e646db367f338721975d5` `CheckQS(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)I` access 9，185 code bytes；语义 NOT_ANALYZED
- `method:b5b4c41be4d349b3c5172755` `FoodControl(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)V` access 1，54 code bytes；语义 NOT_ANALYZED
- `method:5c72ca556905dbd74b55774c` `rightKey(Lnet/minecraft/entity/player/EntityPlayer;)Z` access 1，42 code bytes；语义 NOT_ANALYZED
- `method:382ed777fa8f1c2592b31526` `getQSDifficult(Lnet/minecraft/block/Block;)I` access 9，46 code bytes；语义 NOT_ANALYZED
- `method:5a6dace5b502d2ce920e2db2` `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，40 code bytes；语义 NOT_ANALYZED
- `method:f6b98a80bc796132103d11f6` `func_77617_a(I)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:3acf922b3ca1cdfefe157774` `func_77624_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/entity/player/EntityPlayer;Ljava/util/List;Z)V` access 1，235 code bytes；语义 NOT_ANALYZED
- `method:90d1c6dfd3af1ea474f074a5` `func_111205_h()Lcom/google/common/collect/Multimap;` access 1，39 code bytes；语义 NOT_ANALYZED
- `method:7378ddbd51db20a36be24710` `<clinit>()V` access 8，178 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
