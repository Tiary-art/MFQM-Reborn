# MoreFunQuicksandMod/main/entity/EntityRescue

ID `class:038db33bba9a9aede0b0ff43`；class SHA `8807981db9b2d9fc40d7dae0eac433d661ecf467721bf823badb6d9e2aa1b637`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/Entity`；interfaces `net/minecraft/entity/IProjectile;cpw/mods/fml/common/registry/IEntityAdditionalSpawnData`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntityRescue`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntityRescue.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:44be19da856ab9cf09507f96` `curPlayer:Lnet/minecraft/entity/player/EntityPlayer;` access 1
- `field:b5718579c5076c01c399b3c3` `curGrabbed:Lnet/minecraft/entity/EntityLivingBase;` access 1
- `field:e4a340dcc35a76670b1def7a` `grabTick:I` access 1
- `field:ce95068e0d4f6bf47630bc9f` `BlockPosX:D` access 1
- `field:2ae8bd5d4e96b0f913582d53` `BlockPosY:D` access 1
- `field:6bf1430127f850884cf8b3d9` `BlockPosZ:D` access 1
- `field:372349049f62ea92d4baca23` `isRegistered:Z` access 1
- `field:9af8fa54e55348c43320dba3` `hitted:Z` access 1
- `field:5de1d3afbb460b87a6448927` `GrabType:I` access 1
- `field:9f70cddf8138f0e8f18edf8c` `xTile:I` access 2
- `field:614077c8a09579f460842195` `yTile:I` access 2
- `field:028c9f67c8499c92bb33bcb3` `zTile:I` access 2
- `field:7b0ac8c6aee732575dc51f46` `inGround:Z` access 1
- `field:de9ccf1bffac15f1204e6e33` `throwableShake:I` access 1
- `field:ba30b756934cf16e4d4aa054` `curLen:D` access 1
- `field:338e26fbb888fd3a94e395d5` `beginCurLen:D` access 1
- `field:944f2ea0c6bf753a70c5bbca` `maxLen:D` access 2
- `field:eb5b83111b16a77264cb7073` `brkLen:D` access 2
- `field:9791331e458f41f33f2a0c77` `mathLen:D` access 2
- `field:c8f47da668d546feabf4023b` `thrower:Lnet/minecraft/entity/EntityLivingBase;` access 2
- `field:70ab6300a6b1079d8eef2c7b` `throwerName:Ljava/lang/String;` access 2
- `field:f6ff6e17f0c14d3742941ece` `ticksInGround:I` access 2
- `field:e0623303b2c0cbf091258c05` `ticksInAir:I` access 2

## 方法目录

- `method:0b33bb2921b2fb71ba558a10` `<init>(Lnet/minecraft/world/World;)V` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:08fffbc6b6c75911258cb2a3` `<init>(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)V` access 1，289 code bytes；语义 NOT_ANALYZED
- `method:9c008cea27182d1485c0a950` `<init>(Lnet/minecraft/world/World;DDD)V` access 1，64 code bytes；语义 NOT_ANALYZED
- `method:403fab0ae9e9b5c06bc02e8d` `<init>(Lnet/minecraft/world/World;DDDLnet/minecraft/entity/player/EntityPlayer;)V` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:4675f7bb610152c9ec50cd88` `func_70088_a()V` access 4，5 code bytes；语义 NOT_ANALYZED
- `method:1c9039c44e612468ca567695` `initWatcherGrabbed()V` access 4，92 code bytes；语义 NOT_ANALYZED
- `method:d90c71d3ae2fbfa7abba1652` `setWatcherGrabbed()V` access 1，123 code bytes；语义 NOT_ANALYZED
- `method:bcd3b72a0f568965740c366d` `getWatcherLenMP()V` access 1，15 code bytes；语义 NOT_ANALYZED
- `method:7442052e4a48cdb2074b7c74` `setWatcherLenMP()V` access 1，18 code bytes；语义 NOT_ANALYZED
- `method:862a5a476d04aae3e0e769dc` `sendPacketCurLenToServer(D)V` access 1，39 code bytes；语义 NOT_ANALYZED
- `method:6e3bb44ecd49b4bb78e0932e` `getWatcherGrabbed()V` access 1，355 code bytes；语义 NOT_ANALYZED
- `method:a2c822976ca70ef154b282a4` `func_70112_a(D)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:62a444b7dd29c0dd4c20b1e3` `func_70182_d()F` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:b4603873c4d2507db53e1273` `func_70183_g()F` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:51ea326b1926910a6709aa93` `func_82150_aj()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:58b38e6f15a65c82a32e85cd` `func_70186_c(DDDFF)V` access 1，199 code bytes；语义 NOT_ANALYZED
- `method:2deefb26538d16e062d9df41` `func_70016_h(DDD)V` access 1，98 code bytes；语义 NOT_ANALYZED
- `method:9419c6d0de7ec97fcaa280ee` `writeSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，24 code bytes；语义 NOT_ANALYZED
- `method:7aea9767cbe7f00c69ada8e0` `readSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，19 code bytes；语义 NOT_ANALYZED
- `method:de5c0f994405fabd675565a5` `func_70014_b(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:ac160f3d5f574564e5da07e1` `func_70037_a(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:e5cb3ee17a8ee98bf5b63772` `func_70071_h_()V` access 1，345 code bytes；语义 NOT_ANALYZED
- `method:39b3733a3cee43f6ea9e1a46` `getGravityVelocity()F` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:6ae08b248210a4f5970cb991` `onImpact(Lnet/minecraft/util/MovingObjectPosition;)V` access 4，542 code bytes；语义 NOT_ANALYZED
- `method:546caace346055415f7ee258` `throwPhysics()V` access 4，1034 code bytes；语义 NOT_ANALYZED
- `method:9f303f6315ef54ef8697cfd7` `updatePhysics()V` access 4，365 code bytes；语义 NOT_ANALYZED
- `method:2789899549f67c8d4f201523` `func_70053_R()F` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:7eb0b7f2ad8e0a7dfa5be64a` `getThrower()Lnet/minecraft/entity/EntityLivingBase;` access 1，44 code bytes；语义 NOT_ANALYZED
- `method:699478f5144b19d83d62f3ed` `playerControl()V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:da38463d6570b8633555f3f4` `hookPhysic()V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:d3ce50390094cc8a65b68f3f` `getPlayerMC()Lnet/minecraft/entity/player/EntityPlayer;` access 1，7 code bytes；语义 NOT_ANALYZED
- `method:94dc8a8f2a906fca83030798` `livingGrab()V` access 1，1806 code bytes；语义 NOT_ANALYZED
- `method:14ea7f806d76927be30a7206` `checkingInHotBar()I` access 1，51 code bytes；语义 NOT_ANALYZED
- `method:d820fdfac5d89d9dbf2b000c` `isInsideOfQuicksand(Lnet/minecraft/entity/EntityLivingBase;)I` access 9，130 code bytes；语义 NOT_ANALYZED
- `method:0b63ae5199d5705c9b174d15` `getMovFactor(Lnet/minecraft/entity/EntityLivingBase;I)D` access 1，169 code bytes；语义 NOT_ANALYZED
- `method:47cccb3b60df235c3bf3bde9` `getWeight(Lnet/minecraft/entity/EntityLivingBase;)D` access 1，37 code bytes；语义 NOT_ANALYZED
- `method:d50f5541a5709355c433b54c` `getMoCreatureValid(Lnet/minecraft/entity/EntityLivingBase;)Z` access 1，98 code bytes；语义 NOT_ANALYZED
- `method:aef1b1f3fcd97b2e65475195` `unGrabServer()V` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:0927b0c5d330ff109bad873b` `breakSound()V` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:344aeb2d143cc39ce1796a5a` `GrabSound()V` access 1，42 code bytes；语义 NOT_ANALYZED
- `method:006dd57c577ab5f0af14a183` `unGrabSound()V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:8da35648409b3c739c961341` `stretchSound()V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:920f85c7a6028cf18037115e` `midKey()Z` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:88f9a4059e4748cc955e2826` `leftKey()Z` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:3587883cd439ec9e64f9f968` `jumpKey()Z` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:821d15c8551c36656a0feca7` `crouchKey()Z` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:ec5afd27120f03000159da5f` `getMaxYSpeed(DI)D` access 1，101 code bytes；语义 NOT_ANALYZED
- `method:ecfdbbabcc89c3706eff516a` `saveMeInPacketHandler()V` access 1，97 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
