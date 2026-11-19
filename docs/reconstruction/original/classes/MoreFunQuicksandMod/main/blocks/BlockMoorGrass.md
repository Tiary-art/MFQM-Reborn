# MoreFunQuicksandMod/main/blocks/BlockMoorGrass

ID `class:b9ba66dc0987df327f303ab8`；class SHA `cd6460621e5272fba99996b34669e023f37c0a44c8f4cf9f18715c645a769314`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/BlockBush`；interfaces `net/minecraftforge/common/IShearable`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockMoorGrass`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockMoorGrass.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `moor_grass`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:c63a1c363502117d5d2ed28f` `IIconArray:[Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:2abd56ed3a29b9e19baca63c` `<init>()V` access 1，63 code bytes；语义 NOT_ANALYZED
- `method:7ccdb72d69502b2e44777dbe` `func_149719_a(Lnet/minecraft/world/IBlockAccess;III)V` access 1，80 code bytes；语义 NOT_ANALYZED
- `method:6c3c876acf1c1776e65e2daa` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，87 code bytes；语义 NOT_ANALYZED
- `method:1d873606fd97d3f97a1536d1` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，56 code bytes；语义 NOT_ANALYZED
- `method:ccbb57a4dd4eab2f918b51eb` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:9050da009e005597350a9772` `func_149727_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/player/EntityPlayer;IFFF)Z` access 1，61 code bytes；语义 NOT_ANALYZED
- `method:d26544ae7de2a4042915d402` `func_149745_a(Ljava/util/Random;)I` access 1，8 code bytes；语义 NOT_ANALYZED
- `method:a4d960be4952e8ff2696ccda` `quantityDropped(IILjava/util/Random;)I` access 1，23 code bytes；语义 NOT_ANALYZED
- `method:2cd3be38ee07dcf46aedcd84` `func_149679_a(ILjava/util/Random;)I` access 1，12 code bytes；语义 NOT_ANALYZED
- `method:872d9e8b2a36190e148ad21b` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:18ac51a52acc7e19648a4466` `func_149635_D()I` access 1，12 code bytes；语义 NOT_ANALYZED
- `method:a4205ce1de55cf004ca0b8e1` `func_149741_i(I)I` access 1，59 code bytes；语义 NOT_ANALYZED
- `method:554e1b59375cdbedd741a944` `func_149720_d(Lnet/minecraft/world/IBlockAccess;III)I` access 1，84 code bytes；语义 NOT_ANALYZED
- `method:fbc63d1822e6b09494fef743` `func_149643_k(Lnet/minecraft/world/World;III)I` access 1，9 code bytes；语义 NOT_ANALYZED
- `method:6f586cf879eeb8f5577c5378` `getSubBlocks(ILnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` access 1，103 code bytes；语义 NOT_ANALYZED
- `method:38633c17f23681d00d1427d2` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，51 code bytes；语义 NOT_ANALYZED
- `method:4d4b44ef077681a81c06181e` `func_149718_j(Lnet/minecraft/world/World;III)Z` access 1，76 code bytes；语义 NOT_ANALYZED
- `method:246900284c15e386934c8c12` `canThisPlantGrowOnThisBlock(Lnet/minecraft/block/Block;)Z` access 4，27 code bytes；语义 NOT_ANALYZED
- `method:8dcb1af22828b80741984804` `func_149659_a(Lnet/minecraft/world/Explosion;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:c1b1cec0a4d9051094217829` `isShearable(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/IBlockAccess;III)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:289dcaa6e7c63c6b40366d05` `onSheared(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/IBlockAccess;IIII)Ljava/util/ArrayList;` access 1，51 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
