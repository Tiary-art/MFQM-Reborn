# MoreFunQuicksandMod/main/entity/EntityRope

ID `class:1a6c2f81328d36b414badc22`；class SHA `6569b640ddd14db7e729d830c6d2cd8371ad36822990b61168dc63f23c30f81d`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/Entity`；interfaces `net/minecraft/entity/IProjectile;cpw/mods/fml/common/registry/IEntityAdditionalSpawnData`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntityRope`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntityRope.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:e2234945dd59c1887cbb0e17` `curPlayer:Lnet/minecraft/entity/player/EntityPlayer;` access 1
- `field:72999aa38711981baa7c78c3` `curGrabbed:Lnet/minecraft/entity/EntityLivingBase;` access 1
- `field:e3ca4f29e0a1435799c4ca56` `grabTick:I` access 1
- `field:3716af483b4f3c8730d8bb5b` `BlockPosX:D` access 1
- `field:202cc71f6374d4c21a8ed073` `BlockPosY:D` access 1
- `field:8b632b5ee59366bc1888d2ec` `BlockPosZ:D` access 1
- `field:3cab229b78391e95dbe6fabf` `isRegistered:Z` access 1
- `field:c4fb777dc9ceb506eaad7e77` `hitted:Z` access 1
- `field:0f484df3091f7c54f8d1dddf` `GrabType:I` access 1
- `field:e93240bb4d73695640fc8839` `xTile:I` access 2
- `field:6107eccb5335ccfc2c5bac65` `yTile:I` access 2
- `field:d63fa1800147aebc961e94e0` `zTile:I` access 2
- `field:f5e647c73abc062cfb6a6304` `inGround:Z` access 1
- `field:8e068df75abc7cad0b89df7b` `throwableShake:I` access 1
- `field:fa41dcecf6d5b28ca6cbc60b` `curLen:D` access 1
- `field:8281bf2992da3db8489533e0` `beginCurLen:D` access 1
- `field:d2e4d9bf03498055f2774d64` `maxLen:D` access 2
- `field:f1901cd5c8db3c751b9bd72e` `brkLen:D` access 2
- `field:2b2ba346bd72ce1574220f18` `mathLen:D` access 2
- `field:2617461a96893d84f3f6bfd7` `quicksandIDS:[Lnet/minecraft/block/Block;` access 9
- `field:f249875dda535218e933df2e` `quicksandHardCoof:[I` access 9
- `field:2a358af21dee9bae53c1fb1b` `thrower:Lnet/minecraft/entity/EntityLivingBase;` access 2
- `field:e1c747639c9e6be5eb234e79` `throwerName:Ljava/lang/String;` access 2
- `field:ba704f68131b9f0efde34010` `ticksInGround:I` access 2
- `field:47bd7da8cb8ae5dc86245a6b` `ticksInAir:I` access 2

## 方法目录

- `method:6c1c3ce8c5282ca6defbc9eb` `<init>(Lnet/minecraft/world/World;)V` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:a3780fd7939a07964d1760b7` `<init>(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)V` access 1，289 code bytes；语义 NOT_ANALYZED
- `method:f8a83cedf640af29ef80dca0` `<init>(Lnet/minecraft/world/World;DDD)V` access 1，64 code bytes；语义 NOT_ANALYZED
- `method:ba87e7d822579f6bfdf18e01` `<init>(Lnet/minecraft/world/World;DDDLnet/minecraft/entity/player/EntityPlayer;)V` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:683e91fe0d675557be308214` `func_70088_a()V` access 4，5 code bytes；语义 NOT_ANALYZED
- `method:879fad44141ee504a3b96d80` `initWatcherGrabbed()V` access 4，92 code bytes；语义 NOT_ANALYZED
- `method:f23838f904f3a09559a882d2` `setWatcherGrabbed()V` access 1，123 code bytes；语义 NOT_ANALYZED
- `method:19f2898575f0a2d61ebd8771` `getWatcherLenMP()V` access 1，15 code bytes；语义 NOT_ANALYZED
- `method:a837ad60606ad91d47be47d1` `setWatcherLenMP()V` access 1，18 code bytes；语义 NOT_ANALYZED
- `method:c3a7ac01434c03625b586c35` `sendPacketCurLenToServer(D)V` access 1，39 code bytes；语义 NOT_ANALYZED
- `method:521350e83e1645d63be9695a` `getWatcherGrabbed()V` access 1，355 code bytes；语义 NOT_ANALYZED
- `method:0f2c5f7cad38a970d052b549` `func_70112_a(D)Z` access 1，32 code bytes；语义 NOT_ANALYZED
- `method:730bbae006f16e6edf00e8c4` `func_70182_d()F` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:eca82f96b8de8096cbd1a410` `func_70183_g()F` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:b5f5428e025bd8f47882f145` `func_70186_c(DDDFF)V` access 1，199 code bytes；语义 NOT_ANALYZED
- `method:8c3f1a8d41846b79ef7bf59a` `func_70016_h(DDD)V` access 1，98 code bytes；语义 NOT_ANALYZED
- `method:026d5329bc40d0540b178bcb` `writeSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，24 code bytes；语义 NOT_ANALYZED
- `method:d44bd3182dbef86b03955fc4` `readSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，19 code bytes；语义 NOT_ANALYZED
- `method:dd392c4dd03ae71b31d69819` `func_70014_b(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:eb9af141de4de5a59765ccb2` `func_70037_a(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:1094069681dd8dc12dccabe4` `func_70071_h_()V` access 1，641 code bytes；语义 NOT_ANALYZED
- `method:7299b375a5adf77945f535bd` `getGravityVelocity()F` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:7deb64b3a8f17d4292b2c26d` `onImpact(Lnet/minecraft/util/MovingObjectPosition;)V` access 4，715 code bytes；语义 NOT_ANALYZED
- `method:1fc8db9133cfcb9b9118c030` `throwPhysics()V` access 4，1034 code bytes；语义 NOT_ANALYZED
- `method:f85ba81160dce06ec209e2c8` `updatePhysics()V` access 4，365 code bytes；语义 NOT_ANALYZED
- `method:c7539cc7d81bd8552b91530c` `checkValidToGrab(Lnet/minecraft/util/MovingObjectPosition;)Z` access 4，334 code bytes；语义 NOT_ANALYZED
- `method:8ea53a7c773f086f1bf5827f` `func_70053_R()F` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:171d0bad43d3d1a94fc7ef50` `getThrower()Lnet/minecraft/entity/EntityLivingBase;` access 1，44 code bytes；语义 NOT_ANALYZED
- `method:9f268b131cd1e9984107fc86` `playerControl()V` access 1，1352 code bytes；语义 NOT_ANALYZED
- `method:b23597281c35f37adf9bddf5` `hookPhysic()V` access 1，193 code bytes；语义 NOT_ANALYZED
- `method:705606916d07fe907350a992` `getPlayerMC()Lnet/minecraft/entity/player/EntityPlayer;` access 1，7 code bytes；语义 NOT_ANALYZED
- `method:b90bbc91c6f9da9f683957a1` `livingGrab()V` access 1，2143 code bytes；语义 NOT_ANALYZED
- `method:d106bc83ca10bb1a351108a3` `func_70070_b(F)I` access 1，82 code bytes；语义 NOT_ANALYZED
- `method:d83b71fb9b8586cf002e3054` `func_70013_c(F)F` access 1，81 code bytes；语义 NOT_ANALYZED
- `method:ddcbd447c0111f62af221301` `checkingInHotBar()I` access 1，79 code bytes；语义 NOT_ANALYZED
- `method:22bec711aedf6c990b08f090` `isInsideOfQuicksand(Lnet/minecraft/entity/EntityLivingBase;)I` access 1，133 code bytes；语义 NOT_ANALYZED
- `method:55678c19efcd3224603f680e` `getMovFactor(Lnet/minecraft/entity/EntityLivingBase;I)D` access 1，169 code bytes；语义 NOT_ANALYZED
- `method:07b1254cc189024f053d0a43` `getWeight(Lnet/minecraft/entity/EntityLivingBase;)D` access 1，37 code bytes；语义 NOT_ANALYZED
- `method:a79afb352ad4d82679b05d7d` `getMoCreatureValid(Lnet/minecraft/entity/EntityLivingBase;)Z` access 1，89 code bytes；语义 NOT_ANALYZED
- `method:85a76516ab01c9f3bb03873c` `unGrabServer()V` access 1，55 code bytes；语义 NOT_ANALYZED
- `method:d2ce4fea48e767a09bb259aa` `breakSound()V` access 1，95 code bytes；语义 NOT_ANALYZED
- `method:1333892cd1edcbd8c3117eb7` `GrabSound()V` access 1，44 code bytes；语义 NOT_ANALYZED
- `method:b6cb10d7c42e389a000ca7ef` `unGrabSound()V` access 1，95 code bytes；语义 NOT_ANALYZED
- `method:87f26ff10e91b4b4f48f5b17` `stretchSound()V` access 1，95 code bytes；语义 NOT_ANALYZED
- `method:3bcb5f476238e2704938efe9` `midKey()Z` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:d084d7b2a733bb362997d0c6` `leftKey()Z` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:a6f7eb738613073b0c240c99` `jumpKey()Z` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:0ef9bb43dbba536e190ce513` `crouchKey()Z` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:69f2e185c2ec9ada3aacea76` `getMaxYSpeed(DI)D` access 1，101 code bytes；语义 NOT_ANALYZED
- `method:67ffd91733f5a0dadd4de26b` `saveMeInPacketHandler()V` access 1，97 code bytes；语义 NOT_ANALYZED
- `method:446dfc2499887087271d3464` `<clinit>()V` access 8，423 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
