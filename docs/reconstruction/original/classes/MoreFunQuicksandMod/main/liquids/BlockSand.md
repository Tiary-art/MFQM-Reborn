# MoreFunQuicksandMod/main/liquids/BlockSand

ID `class:d27a3e3f71a3869dd1973bc1`；class SHA `9c6e0f7a8b8210f354f7e6dcf1bf5f9da9903fce04426d3fc9996d72e52ea1ca`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockSand`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockSand.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `dry_quicksand`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:487879ad3163552a681bcc21` `theSandIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:9f42fc8073aeef5157a83cc9` `materialSand:Lnet/minecraft/block/material/Material;` access 25

## 方法目录

- `method:5a018ec88f173858a4242d76` `<init>()V` access 1，71 code bytes；语义 NOT_ANALYZED
- `method:c04abd8d0d108cf47013ea6f` `func_149749_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，109 code bytes；语义 NOT_ANALYZED
- `method:d6ddf27f42f16dc38f5c2e8d` `func_149678_a(IZ)Z` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:222a81a0a009f2933198dff3` `getMaxRenderHeightMeta()I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:7910c4dc533f8234a7833e78` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:2f8f14271c9789546c18a359` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2349 code bytes；语义 NOT_ANALYZED
- `method:58643e3143e928a01e7781bc` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:200aa4710f46b5d58111db0f` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:9ebd19924d82eafa49a0ee75` `checkFusion(Lnet/minecraft/world/World;IIILjava/util/Random;)I` access 1，340 code bytes；语义 NOT_ANALYZED
- `method:305056eb4de3d4adbe1f3641` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，322 code bytes；语义 NOT_ANALYZED
- `method:171cd20ee8f11d07c8b0ff36` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:d374690a9c26bcc24bf28443` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:486d39cfd17a0c85410f7a12` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:2c91a38a2f848ae0b6dca106` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:fd7ac026be52d70fa0e7b0f2` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，107 code bytes；语义 NOT_ANALYZED
- `method:7ae46c320948f46bdbcdc48c` `func_149635_D()I` access 1，87 code bytes；语义 NOT_ANALYZED
- `method:8cbb81a903c9fac3bf50b62c` `func_149741_i(I)I` access 1，87 code bytes；语义 NOT_ANALYZED
- `method:05e47ede1c4d9e74631e0b81` `func_149720_d(Lnet/minecraft/world/IBlockAccess;III)I` access 1，87 code bytes；语义 NOT_ANALYZED
- `method:41327bada893970358047f99` `<clinit>()V` access 8，17 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
