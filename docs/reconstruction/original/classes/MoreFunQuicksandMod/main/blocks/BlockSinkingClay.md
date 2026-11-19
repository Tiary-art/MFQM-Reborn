# MoreFunQuicksandMod/main/blocks/BlockSinkingClay

ID `class:80bc7b64bd3c89ceec520e1c`；class SHA `73cd96b05e86bb4bc4f45f2fc492d6ed3a44bf5afbc58c49a541bc428ae04aae`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockSinkingClay`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockSinkingClay.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `sinking_clay`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:f4ad4ed57efdad7b2ee2151f` `IIconNormalArray:[Lnet/minecraft/util/IIcon;` access 2
- `field:60122cf86a194b2248fc83f3` `IIconBrokenArray:[Lnet/minecraft/util/IIcon;` access 2
- `field:0f420cf7efd5f43e6c7d1644` `IIconSideNormal:Lnet/minecraft/util/IIcon;` access 2
- `field:543c64a711a6320f6a274b01` `IIconSideBroken:Lnet/minecraft/util/IIcon;` access 2
- `field:390dc8c322008d93fc65460f` `maxOpacity:I` access 2
- `field:1916e3022a4d5de24541ee89` `lastOpacity:I` access 2
- `field:2b81a5d643d79b717f26a500` `incOpacity:I` access 2

## 方法目录

- `method:fe1607852041e5c0f3894842` `<init>(III)V` access 1，89 code bytes；语义 NOT_ANALYZED
- `method:67a9c0f83b6dcb9b7c455fd7` `isAboveFreeSpace(IIILnet/minecraft/world/World;)Z` access 2，46 code bytes；语义 NOT_ANALYZED
- `method:d2ab58e8c03fe0031e675f73` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:ee9cdf4a53ca13ca71681c05` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，861 code bytes；语义 NOT_ANALYZED
- `method:cf256f0b3dae9164fb40a559` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，3774 code bytes；语义 NOT_ANALYZED
- `method:a2f1769fb48cf8545c401132` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:0f5cd5714ae3d95b10d70d6a` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:42bec49fd2c5e2d6d0f35226` `func_149745_a(Ljava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:1b6017727deb0e6f04b4ad67` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:30544c11ade9114dd785deab` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，105 code bytes；语义 NOT_ANALYZED
- `method:3445ba12a859e88a39c7e129` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:499aaee883915e3054e41c65` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:40b3c6c92583fc11183d6fdf` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，142 code bytes；语义 NOT_ANALYZED
- `method:eef6604991322515b1a5d7b3` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，120 code bytes；语义 NOT_ANALYZED
- `method:e5894da5f19b2753d7352151` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，163 code bytes；语义 NOT_ANALYZED
- `method:2cb4bab92c343f498f2920cd` `func_149700_E()Z` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:1baa57ab63e388c91158fa44` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:8cbeb9454c9e733884ac159a` `isSolid()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:99a54864f745229d9592ffb6` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:06d34594a45bdedb36503307` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，71 code bytes；语义 NOT_ANALYZED
- `method:9a5eb241ad2b0b5dde1f128d` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，122 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
