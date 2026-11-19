# MoreFunQuicksandMod/main/entity/EntityHook

ID `class:1d5f9adfec6e01424b83c16a`；class SHA `8d422a215675de8ae7df4f386d5a95e33c071478a24a61a8e76516aa48f8510f`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/Entity`；interfaces `net/minecraft/entity/IProjectile;cpw/mods/fml/common/registry/IEntityAdditionalSpawnData`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntityHook`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntityHook.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:8704d4610787b4b3ea42526e` `curPlayer:Lnet/minecraft/entity/player/EntityPlayer;` access 1
- `field:e82b5ed84b9d2a891c746971` `curGrabbed:Lnet/minecraft/entity/EntityLivingBase;` access 1
- `field:4741cf3c2b1dcb319c942c44` `grabTick:I` access 1
- `field:90997ce4bfd15d3011676f2e` `inSand:I` access 1
- `field:7325107f650664862d70c9c2` `BlockPosX:D` access 1
- `field:dca5346b9fe0c77f5954c4fa` `BlockPosY:D` access 1
- `field:185a4584380fef4ced6e88fa` `BlockPosZ:D` access 1
- `field:e06eb8fd590d99e8a272fb8c` `isRegistered:Z` access 1
- `field:c1a2f67f3cfa840157c8ca4b` `hitted:Z` access 1
- `field:751c5e09e832458af5a8168d` `GrabType:I` access 1
- `field:1cae165bb1513308bc5ac2d5` `xTile:I` access 2
- `field:41b4c0722eee96daae4f1f50` `yTile:I` access 2
- `field:8115c4fc3bdb77e81a3bec81` `zTile:I` access 2
- `field:01385739e7afbb0633d9d503` `inGround:Z` access 1
- `field:2960291ad06ffe15828e3e79` `throwableShake:I` access 1
- `field:3513e2bd3dc089d30938da4b` `curLen:D` access 1
- `field:a4e7c9ea6ffd96c8e377eabb` `beginCurLen:D` access 1
- `field:e91b525a9e38bcee71be4ab7` `maxLen:D` access 2
- `field:d489442e4fd524b761e92dcc` `brkLen:D` access 2
- `field:a182416c1b811f7b4683f00b` `mathLen:D` access 2
- `field:58cdd548b4e5a66e50d5c755` `thrower:Lnet/minecraft/entity/EntityLivingBase;` access 2
- `field:408e653d25b70660ae36b574` `throwerName:Ljava/lang/String;` access 2
- `field:d2ec24342e318037c4d577af` `ticksInGround:I` access 2
- `field:c41b39c02dba4eb964cb714a` `ticksInAir:I` access 2

## 方法目录

- `method:f461ea96ccbc278bd43246bc` `<init>(Lnet/minecraft/world/World;)V` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:add255346073c4d97b5d440b` `<init>(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)V` access 1，289 code bytes；语义 NOT_ANALYZED
- `method:fd7f21d9f7e3ce41663f9a04` `<init>(Lnet/minecraft/world/World;DDD)V` access 1，64 code bytes；语义 NOT_ANALYZED
- `method:dba09558ce8405e760ba32bb` `<init>(Lnet/minecraft/world/World;DDDLnet/minecraft/entity/player/EntityPlayer;)V` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:24d56eb969221a085c40c0d8` `func_70088_a()V` access 4，5 code bytes；语义 NOT_ANALYZED
- `method:160b16a162453be9c423cb48` `initWatcherGrabbed()V` access 4，92 code bytes；语义 NOT_ANALYZED
- `method:377c48b43ff1c60e9f549496` `setWatcherGrabbed()V` access 1，123 code bytes；语义 NOT_ANALYZED
- `method:d50cb8c7eab3835d177531f9` `getWatcherLenMP()V` access 1，15 code bytes；语义 NOT_ANALYZED
- `method:8d9e4a3694a00b2cff17cef1` `setWatcherLenMP()V` access 1，18 code bytes；语义 NOT_ANALYZED
- `method:055dbf3c2dd846b1d7689a05` `sendPacketCurLenToServer(D)V` access 1，39 code bytes；语义 NOT_ANALYZED
- `method:9891d9cbf30d4b970f92f711` `getWatcherGrabbed()V` access 1，355 code bytes；语义 NOT_ANALYZED
- `method:2f273619740058f98503135b` `func_70112_a(D)Z` access 1，32 code bytes；语义 NOT_ANALYZED
- `method:f21f96c8668462c33f00ec88` `func_70182_d()F` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:39c858ea1324b6e4691faecf` `func_70183_g()F` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:38375a9498fce8c70d2271cb` `func_70186_c(DDDFF)V` access 1，199 code bytes；语义 NOT_ANALYZED
- `method:62338a4e566c2091a57584bb` `func_70016_h(DDD)V` access 1，98 code bytes；语义 NOT_ANALYZED
- `method:7826b6675e7a7e6dec67ee2a` `func_70071_h_()V` access 1，625 code bytes；语义 NOT_ANALYZED
- `method:fa85319b965df59b6aacf89e` `getGravityVelocity()F` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:02e749f2dad900af9d5276a3` `onImpact(Lnet/minecraft/util/MovingObjectPosition;)V` access 4，528 code bytes；语义 NOT_ANALYZED
- `method:795e0bec7b7ced74f257c6eb` `throwPhysics()V` access 4，1034 code bytes；语义 NOT_ANALYZED
- `method:b43a87c7aa160cb6819d67fe` `updatePhysics()V` access 4，365 code bytes；语义 NOT_ANALYZED
- `method:f2e070000a26b7a37df40be5` `setValidToGrab(Lnet/minecraft/util/MovingObjectPosition;)Z` access 1，483 code bytes；语义 NOT_ANALYZED
- `method:1e81c486afe0c8052f7f4357` `getValidStopMat(III)Z` access 1，107 code bytes；语义 NOT_ANALYZED
- `method:b5237d13dfcbcb143b78987a` `writeSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，24 code bytes；语义 NOT_ANALYZED
- `method:3c56fc64f090e62329722fe0` `readSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，19 code bytes；语义 NOT_ANALYZED
- `method:4c8c5778d93376cdfd23f5c8` `func_70014_b(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:62a39991d39f5e75e4e0caf5` `func_70037_a(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:1d9e6e6c393feab0937992e0` `func_70053_R()F` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:bfec0c83282b9ac3beeb648b` `getThrower()Lnet/minecraft/entity/EntityLivingBase;` access 1，44 code bytes；语义 NOT_ANALYZED
- `method:0fa299d33820e3e87c272fc6` `playerControl()V` access 1，1642 code bytes；语义 NOT_ANALYZED
- `method:5ae8b1711abf16e37a624a14` `hookPhysic()V` access 1，193 code bytes；语义 NOT_ANALYZED
- `method:d06ab55c07350a9761b121a1` `getPlayerMC()Lnet/minecraft/entity/player/EntityPlayer;` access 1，7 code bytes；语义 NOT_ANALYZED
- `method:2a16e29e9106a4a3ad71eee6` `livingGrab()V` access 1，2232 code bytes；语义 NOT_ANALYZED
- `method:d8d0aeb47a2022a60a01a5c3` `func_70070_b(F)I` access 1，82 code bytes；语义 NOT_ANALYZED
- `method:d9637300f996513108410dee` `func_70013_c(F)F` access 1，81 code bytes；语义 NOT_ANALYZED
- `method:d48f774cd55d9a6f01dea45f` `checkingInHotBar()I` access 1，79 code bytes；语义 NOT_ANALYZED
- `method:35e6891205a36a9ffd968a40` `isInsideOfQuicksand(Lnet/minecraft/entity/EntityLivingBase;)I` access 1，133 code bytes；语义 NOT_ANALYZED
- `method:5c66094a74edbc1fd57cd139` `getMovFactor(Lnet/minecraft/entity/EntityLivingBase;I)D` access 1，169 code bytes；语义 NOT_ANALYZED
- `method:3ffcd4e73929b0ba56c4fd41` `getWeight(Lnet/minecraft/entity/EntityLivingBase;)D` access 1，37 code bytes；语义 NOT_ANALYZED
- `method:e4d1eddf292215888353eb4a` `getBreakPos()Lnet/minecraft/util/Vec3;` access 1，197 code bytes；语义 NOT_ANALYZED
- `method:32131b139ce5b149844b0d58` `tryingBreakBlock()V` access 1，86 code bytes；语义 NOT_ANALYZED
- `method:05dcf21289035aa496f89535` `sandDigging()V` access 1，275 code bytes；语义 NOT_ANALYZED
- `method:e73e07c82980bd92b7094a36` `getMoCreatureValid(Lnet/minecraft/entity/EntityLivingBase;)Z` access 1，89 code bytes；语义 NOT_ANALYZED
- `method:6896781d170a71bd2aee9e31` `unGrabServer()V` access 1，55 code bytes；语义 NOT_ANALYZED
- `method:f34add1bce2bfaf8c18bd055` `breakSound()V` access 1，93 code bytes；语义 NOT_ANALYZED
- `method:0d3a3f9feab59afb4881696b` `GrabSound()V` access 1，51 code bytes；语义 NOT_ANALYZED
- `method:01662cf90eec89d47691eba2` `unGrabSound()V` access 1，137 code bytes；语义 NOT_ANALYZED
- `method:94625f145738fa73a393e2fc` `stretchSound()V` access 1，95 code bytes；语义 NOT_ANALYZED
- `method:2f0d3177369b930e0754f12e` `midKey()Z` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:7566c6479f6ca5121b77b51e` `leftKey()Z` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:03dc995e93fe278765215204` `jumpKey()Z` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:d2c03051accdc55d837a0d5f` `crouchKey()Z` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:1712d618c55962ac6ae958c2` `getMaxYSpeed(DI)D` access 1，101 code bytes；语义 NOT_ANALYZED
- `method:341a93a99b0f4bdab695b089` `saveMeInPacketHandler()V` access 1，97 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
