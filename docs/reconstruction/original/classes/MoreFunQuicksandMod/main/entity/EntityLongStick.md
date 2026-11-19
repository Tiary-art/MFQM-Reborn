# MoreFunQuicksandMod/main/entity/EntityLongStick

ID `class:840fcd148a485041a61d0919`；class SHA `7fc33b580abd304344ccde97dcaafb727f427581c631001b5efa18f501b24e90`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/Entity`；interfaces `cpw/mods/fml/common/registry/IEntityAdditionalSpawnData`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntityLongStick`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntityLongStick.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:902eb7e420d3a45e2624a99c` `xx:I` access 1
- `field:0dfe284b1592ef1071b511dd` `yy:I` access 1
- `field:458fe0cacc743bdb355a5993` `zz:I` access 1
- `field:cae704924a60d17561f53506` `curPlayer:Lnet/minecraft/entity/Entity;` access 1

## 方法目录

- `method:7bcc7c4d6cce2fb0de3c1341` `<init>(Lnet/minecraft/world/World;)V` access 1，34 code bytes；语义 NOT_ANALYZED
- `method:8f87079e8a640ae2a4488043` `<init>(Lnet/minecraft/world/World;DDDLnet/minecraft/entity/Entity;)V` access 1，26 code bytes；语义 NOT_ANALYZED
- `method:eda2e02e6a39770e8cf66e4c` `<init>(Lnet/minecraft/world/World;DDDLnet/minecraft/entity/Entity;III)V` access 1，31 code bytes；语义 NOT_ANALYZED
- `method:de3ef39edc59b7c7373dd43f` `<init>(Lnet/minecraft/world/World;Lnet/minecraft/entity/EntityLivingBase;)V` access 1，50 code bytes；语义 NOT_ANALYZED
- `method:cdbee5346c1b2c3f87900238` `func_70088_a()V` access 4，1 code bytes；语义 NOT_ANALYZED
- `method:a554c9c36e2d82fb488e120e` `writeSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，51 code bytes；语义 NOT_ANALYZED
- `method:33c814450728ba7fba192446` `readSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，40 code bytes；语义 NOT_ANALYZED
- `method:3a189a18f709a2d6219a6c0f` `func_70112_a(D)Z` access 1，32 code bytes；语义 NOT_ANALYZED
- `method:c821ce356e6f5f01a7bd769f` `func_70071_h_()V` access 1，3374 code bytes；语义 NOT_ANALYZED
- `method:d9eea875a93c85e0f674286d` `spawnParticle(Lnet/minecraft/block/Block;IIDDD)V` access 1，138 code bytes；语义 NOT_ANALYZED
- `method:c1bc9124dc9e65b72e25d40f` `playSound(Ljava/lang/String;FFF)V` access 1，38 code bytes；语义 NOT_ANALYZED
- `method:317e597b5da95d6c14177b5d` `playBottom(Lnet/minecraft/block/Block;)V` access 1，49 code bytes；语义 NOT_ANALYZED
- `method:ea14da6b6124bc0465fff220` `playSuction(F)V` access 1，193 code bytes；语义 NOT_ANALYZED
- `method:164562aa29e31c10f3b9ce4e` `func_70014_b(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:b99f276e92f95fd12a07a453` `func_70037_a(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:a7e9dd9ff9f1ef2ab9c528dc` `func_70053_R()F` access 1，2 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
