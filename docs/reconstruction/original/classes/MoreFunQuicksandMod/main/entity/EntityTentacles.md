# MoreFunQuicksandMod/main/entity/EntityTentacles

ID `class:892b59b5eafd800f3ecae016`；class SHA `4012228a31e732e20ff533df1bad967068a9d42fcf0f83f7d7891dfd161e2881`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/Entity`；interfaces `cpw/mods/fml/common/registry/IEntityAdditionalSpawnData`；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntityTentacles`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntityTentacles.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:43ff50feda77718cd55b17d9` `target:Lnet/minecraft/entity/Entity;` access 1
- `field:e54c639e3961cb6d54704b6e` `targetUpdate:Z` access 1
- `field:10510904fbfee2f527390929` `targetUUID:Ljava/util/UUID;` access 1
- `field:d40237c36981fba17d1ef22b` `AnimLifeTime:I` access 1
- `field:681f7e18d7eefce5bb691fc1` `maxHurtResistantTime:I` access 1
- `field:551b2155454643447373161f` `health:F` access 1
- `field:821c49029ddadb32b21d4a4c` `high:I` access 1

## 方法目录

- `method:e0c2fe65169853d0ab9bc6be` `<init>(Lnet/minecraft/world/World;)V` access 1，53 code bytes；语义 NOT_ANALYZED
- `method:50fb57e8a60914315105389b` `<init>(Lnet/minecraft/world/World;DDDLnet/minecraft/entity/Entity;II)V` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:b32babd430ca8b77dcf42bb1` `func_70088_a()V` access 4，41 code bytes；语义 NOT_ANALYZED
- `method:288bcde7b65abc4718752af2` `checkTarget()V` access 4，214 code bytes；语义 NOT_ANALYZED
- `method:df83e59d89a3a9ab128ac08c` `CheckInQSBlock()V` access 1，88 code bytes；语义 NOT_ANALYZED
- `method:124162c7badca45e3cf9ab16` `ManipulateWithTerrain()V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:8ace290930a00b4935b93fe6` `func_70067_L()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:bc2cffbb389299adf213e2a0` `writeSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，51 code bytes；语义 NOT_ANALYZED
- `method:9dc9a1760d4dd890e00c5823` `readSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，40 code bytes；语义 NOT_ANALYZED
- `method:331a28a652c62424f80a8974` `func_70112_a(D)Z` access 1，32 code bytes；语义 NOT_ANALYZED
- `method:35ab56a40f7283e3d0b803f9` `CheckDead()V` access 1，51 code bytes；语义 NOT_ANALYZED
- `method:09fc2c307760b0d986ca0736` `DeadEffect()V` access 1，145 code bytes；语义 NOT_ANALYZED
- `method:56db9c51928db0e8315ac7ac` `func_70071_h_()V` access 1，1593 code bytes；语义 NOT_ANALYZED
- `method:55793e7631bdbfaab09f5647` `func_70047_e()F` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:0783a52cd2ec109c9596b7ef` `func_70097_a(Lnet/minecraft/util/DamageSource;F)Z` access 1，205 code bytes；语义 NOT_ANALYZED
- `method:17299db1927d2dd6a0dd7429` `func_70091_d(DDD)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:613247402888630dc12c1f7d` `func_70014_b(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，94 code bytes；语义 NOT_ANALYZED
- `method:e638e995c1cef0ea880dd83e` `func_70037_a(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，59 code bytes；语义 NOT_ANALYZED
- `method:6aecd27386c7b895e344200a` `func_70053_R()F` access 1，2 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
