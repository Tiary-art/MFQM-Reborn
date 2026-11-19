# MoreFunQuicksandMod/main/blocks/BlockBlossom

ID `class:27e60629960569a34fa631ed`；class SHA `64acf1bffbea9a01d9597076ea00cad4162dde286843b3ec3650dec41a2dd5ab`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/BlockContainer`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockBlossom`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockBlossom.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `blossom`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:f7ce1498823fecf5a471f25d` `IIconMArray:[Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:cacf88aa61cde75ca16f6ad2` `<init>()V` access 1，44 code bytes；语义 NOT_ANALYZED
- `method:ea49e18e5c95ea129ab02e16` `func_149915_a(Lnet/minecraft/world/World;I)Lnet/minecraft/tileentity/TileEntity;` access 1，51 code bytes；语义 NOT_ANALYZED
- `method:9f3618b8d66316c7c2f74ce1` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:79a31410f5cb3d525fe8c830` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:d6b772536fa6c037cbbe9b94` `func_149666_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` access 1，211 code bytes；语义 NOT_ANALYZED
- `method:55a6467f180cb9fa328fd98f` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，37 code bytes；语义 NOT_ANALYZED
- `method:0472c9c7f8f3c9d2d8807203` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，32 code bytes；语义 NOT_ANALYZED
- `method:9cf4e8ff5eef9fde307f6900` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，419 code bytes；语义 NOT_ANALYZED
- `method:aff64a3c99f3a9393b89834c` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，188 code bytes；语义 NOT_ANALYZED
- `method:cee27fa60acf7a69bf9539fc` `func_149700_E()Z` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:085183e9d88030494b81d76f` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，63 code bytes；语义 NOT_ANALYZED
- `method:255f71cd7dbcbc2d6cfe865d` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，63 code bytes；语义 NOT_ANALYZED
- `method:98f904b0ce05798334dbf712` `checkVoreHole(Lnet/minecraft/world/World;IIII)V` access 1，176 code bytes；语义 NOT_ANALYZED
- `method:15b1ed6489f82bc834d66a8a` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，58 code bytes；语义 NOT_ANALYZED
- `method:251e4299eb284170bf04c73e` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:cbe7c82b2da5e1b2ebbf1683` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:ac8930b314b89bc58bd84f5b` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:f2fdd52a4212f2b71adaa1fc` `func_149745_a(Ljava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:35393f20893d48db36ae59ba` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，84 code bytes；语义 NOT_ANALYZED
- `method:980678eb60465d59252fb030` `func_149643_k(Lnet/minecraft/world/World;III)I` access 1，9 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
