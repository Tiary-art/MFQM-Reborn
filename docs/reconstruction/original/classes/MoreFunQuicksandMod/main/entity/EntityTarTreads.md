# MoreFunQuicksandMod/main/entity/EntityTarTreads

ID `class:f51c006c4c78b87a93466fdd`；class SHA `0dd5c19658a21a8a76caa338f4c3041aa4b9b11322ce0fa75e8d02e81aa49c52`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/Entity`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntityTarTreads`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntityTarTreads.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:c09f3e643e898e16d93a8251` `tickWorld:I` access 1
- `field:b994971de2943b4ee4baefa2` `hgrab:D` access 1
- `field:3d9008dc950f7788261831aa` `rsize:D` access 1
- `field:791fe2e250e6d77f9e91ed93` `limbs:I` access 1
- `field:89c686ec56c193efc87f1498` `target:Lnet/minecraft/entity/EntityLivingBase;` access 1
- `field:7ce21a1a746bb2fb08bd19be` `xs:D` access 1
- `field:6c527c915521c6fdb908b7cd` `zs:D` access 1
- `field:d4cdd70657b80018dfeadb29` `live:I` access 1

## 方法目录

- `method:c675a923e5690c6d1caaaeaf` `<init>(Lnet/minecraft/world/World;)V` access 1，107 code bytes；语义 NOT_ANALYZED
- `method:f89ae5335e0b2961a083be37` `<init>(Lnet/minecraft/world/World;DDDDILnet/minecraft/entity/EntityLivingBase;)V` access 1，62 code bytes；语义 NOT_ANALYZED
- `method:f8d3067ce3bd9dff5712854e` `func_70088_a()V` access 4，1 code bytes；语义 NOT_ANALYZED
- `method:a0eec16d855bf922c69654d5` `func_70112_a(D)Z` access 1，32 code bytes；语义 NOT_ANALYZED
- `method:01e28654bfcc624ffbfd8687` `func_70071_h_()V` access 1，429 code bytes；语义 NOT_ANALYZED
- `method:7757ed4b04473cbe1f5697d4` `func_70014_b(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:afd2207ba84d431adde291be` `func_70037_a(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:370560ef10522256b4ef482f` `func_70053_R()F` access 1，2 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
