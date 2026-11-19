# MoreFunQuicksandMod/main/blocks/BlockWaxWood

ID `class:7cdb8602ccbbf58ec73c4676`；class SHA `dddf933eca391076ca72a7b40c4ebcde5107df9782297b2b8cb157e8af7bd692`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockWaxWood`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockWaxWood.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `wax_wood`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:3332c9e72d911805c8fd0a33` `IIconSideNormal:Lnet/minecraft/util/IIcon;` access 2
- `field:6e5fe206a34752485f097f4b` `IIconSideWax0:Lnet/minecraft/util/IIcon;` access 2
- `field:4b6fa0107d8215173c4a30a0` `IIconSideWax1:Lnet/minecraft/util/IIcon;` access 2
- `field:906cc1ca99d14f4f78ca46dc` `IIconLog:Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:19dd051a6c613a22c40baf6a` `<init>()V` access 1，37 code bytes；语义 NOT_ANALYZED
- `method:215a489a6caca7b8bca7c099` `func_149745_a(Ljava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:24a2c8f1b8d5e87ed9526d7d` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，7 code bytes；语义 NOT_ANALYZED
- `method:6d3345ba408c0e3239b4e241` `func_149692_a(I)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:3ea64f88ad3e0e7377ecfe2a` `func_149666_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:c261a9b00110847511ad2a5a` `func_149689_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/EntityLivingBase;Lnet/minecraft/item/ItemStack;)V` access 1，85 code bytes；语义 NOT_ANALYZED
- `method:b78e3cdef5d896a65299b621` `func_149643_k(Lnet/minecraft/world/World;III)I` access 1，18 code bytes；语义 NOT_ANALYZED
- `method:6ba392678fac3850c8e94903` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，201 code bytes；语义 NOT_ANALYZED
- `method:186b1dd4a78b1efbaa437b17` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，145 code bytes；语义 NOT_ANALYZED
- `method:d2d85a00a046cc7d701fbe5f` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，49 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
