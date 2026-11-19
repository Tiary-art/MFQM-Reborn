# MoreFunQuicksandMod/main/blocks/BlockMeatHole

ID `class:2557c817cac891a27519e048`；class SHA `a255efcbc744e17de8ad139ec97cfa0a954467d3d42c987122790a30da7eaa5d`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockMeatHole`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockMeatHole.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `temp_meat`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:910e015eda5c782b064028a1` `theEmptyIIcon:Lnet/minecraft/util/IIcon;` access 1
- `field:6d5e85db94d7bf0bf5a31fec` `maxOpacity:I` access 2
- `field:34fac11eabf7c825f4ec6e85` `lastOpacity:I` access 2
- `field:7a75b0f0ed59eb3ac4a33796` `incOpacity:I` access 2

## 方法目录

- `method:8b46e5a7da536e5282e69607` `<init>(III)V` access 1，60 code bytes；语义 NOT_ANALYZED
- `method:48ce87decf4a99567b5f38de` `isSideSolid(Lnet/minecraft/world/IBlockAccess;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:8a1bd36416f11de108fcc615` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，1492 code bytes；语义 NOT_ANALYZED
- `method:3180b81903c8e6e2f499fb79` `func_149668_a(Lnet/minecraft/world/World;III)Lnet/minecraft/util/AxisAlignedBB;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:6c35d5e9044ffdca06446da8` `func_149662_c()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:5d636d8663d103db91cb3f6a` `func_149686_d()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:39c5c6720f52da2ef39a019c` `func_149645_b()I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:61c22baa1f80fbd284fde350` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:f82c063e6df02267be172a21` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，17 code bytes；语义 NOT_ANALYZED
- `method:c5bfba71cda1b97f29ab7e4d` `checkMeatNear(Lnet/minecraft/world/World;III)V` access 1，202 code bytes；语义 NOT_ANALYZED
- `method:9e18c78fc951155a5057ca5f` `func_149700_E()Z` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:94e548a0d49980213e396cee` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:2f8d8cdc2d5d231c46237ddf` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:885d3a79b8af5c4a012f9927` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:78447227f5cd49f9068051ec` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，17 code bytes；语义 NOT_ANALYZED
- `method:115e03ef136490a174b291a0` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，17 code bytes；语义 NOT_ANALYZED
- `method:9278e57aa4c18b5937ead20f` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:062920bf4b6531153e37f2e1` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:06bcaa6ad52885121f619485` `func_149745_a(Ljava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:bdb1875969be68267a601d49` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，69 code bytes；语义 NOT_ANALYZED
- `method:3891eb9f5a3432332aa86131` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，124 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
