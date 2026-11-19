# MoreFunQuicksandMod/main/items/ItemLifeJacket

ID `class:68549afeefe725bcb69e2161`；class SHA `452553e00bf7019abf5a8339293db31af769f81e086236c044a37f470bb4a944`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/item/ItemArmor`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/items/ItemLifeJacket`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__items__ItemLifeJacket.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:a68e9ea3756b5cb12bab71b5` `quicksandHardCoof:[F` access 9

## 方法目录

- `method:a4bfe1d7e5b4045fd179ef5c` `<init>(Lnet/minecraft/item/ItemArmor$ArmorMaterial;II)V` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:5573c66dfcb06264de686960` `onArmorTick(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/item/ItemStack;)V` access 1，287 code bytes；语义 NOT_ANALYZED
- `method:846c7096f45b2a64eebdda4e` `getQSDifficult(Lnet/minecraft/block/Block;)F` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:d8ddc83cbfae86fe98f56aed` `getArmorTexture(Lnet/minecraft/item/ItemStack;Lnet/minecraft/entity/Entity;ILjava/lang/String;)Ljava/lang/String;` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:742f8e6d4fda816d3b22b159` `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，13 code bytes；语义 NOT_ANALYZED
- `method:4cb52b50fe722b350468a088` `crouchKey(Lnet/minecraft/entity/player/EntityPlayer;)Z` access 1，38 code bytes；语义 NOT_ANALYZED
- `method:dea85682d73f2d09ab06936b` `func_77624_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/entity/player/EntityPlayer;Ljava/util/List;Z)V` access 1，148 code bytes；语义 NOT_ANALYZED
- `method:8b94425f64a0a7021b12709b` `<clinit>()V` access 8，207 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
