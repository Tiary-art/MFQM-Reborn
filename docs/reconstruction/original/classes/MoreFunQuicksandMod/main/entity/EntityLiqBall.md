# MoreFunQuicksandMod/main/entity/EntityLiqBall

ID `class:b86be58a42ebeb7abbc9901c`；class SHA `acc0193c7375f5ad92a238bbc071adc07d99fd5dcc4731fda19963c615bb7ba1`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/projectile/EntityThrowable`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntityLiqBall`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntityLiqBall.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:92f9e838f1c1b285d7d8bbd2` `block:Lnet/minecraft/block/Block;` access 1
- `field:a495f42242bf5bf56def3b01` `LiqStable:Z` access 2

## 方法目录

- `method:0a97d656ffbf6c091eb75c6c` `<init>(Lnet/minecraft/world/World;)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:afff0c6b9a84200d0b7fc060` `<init>(Lnet/minecraft/world/World;Lnet/minecraft/entity/EntityLivingBase;)V` access 1，23 code bytes；语义 NOT_ANALYZED
- `method:f11de2eddb8aadbe864c46bb` `<init>(Lnet/minecraft/world/World;DDD)V` access 1，27 code bytes；语义 NOT_ANALYZED
- `method:62b5c46a465a56f56d4f7ff0` `<init>(Lnet/minecraft/world/World;Lnet/minecraft/entity/EntityLivingBase;Lnet/minecraft/block/Block;)V` access 1，21 code bytes；语义 NOT_ANALYZED
- `method:7f96fe9eab388bda157ed6f3` `func_70053_R()F` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:c03b2b8b5832f2dc6fb0b5f9` `func_70088_a()V` access 4，5 code bytes；语义 NOT_ANALYZED
- `method:8ed1ace8070b39bb8bf9ec68` `initWatcherLiq()V` access 4，15 code bytes；语义 NOT_ANALYZED
- `method:fed876256a1a18de26e1f632` `setWatcherLiq()V` access 1，30 code bytes；语义 NOT_ANALYZED
- `method:bfcc49b5a5a3d4e21e4f478f` `getWatcherLiq()V` access 1，59 code bytes；语义 NOT_ANALYZED
- `method:e305c3df49444d691cf5b17d` `writeSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:58213b10ae8a9f00184bb819` `readSpawnData(Lio/netty/buffer/ByteBuf;)V` access 1，39 code bytes；语义 NOT_ANALYZED
- `method:bb52a71d1cdb47b5e48c1bd2` `func_70014_b(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:cf708e9352ab228ca46d6711` `func_70037_a(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:3867a19d55151f8cf1b8a3b8` `func_70185_h()F` access 4，3 code bytes；语义 NOT_ANALYZED
- `method:40627b4636ff74ded52d853f` `func_82150_aj()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:8bb7d999dc18abd53dfcaa0b` `func_70112_a(D)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:9281218f060f9f0bc29bb93c` `validForSpread(Lnet/minecraft/world/World;III)Z` access 4，72 code bytes；语义 NOT_ANALYZED
- `method:7b19bc65fa1fcb13196d6c4f` `func_70184_a(Lnet/minecraft/util/MovingObjectPosition;)V` access 4，765 code bytes；语义 NOT_ANALYZED
- `method:d519d467d31b3d92349773cf` `func_70071_h_()V` access 1，221 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
