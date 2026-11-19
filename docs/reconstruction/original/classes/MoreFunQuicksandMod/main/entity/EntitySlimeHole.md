# MoreFunQuicksandMod/main/entity/EntitySlimeHole

ID `class:13726022863144f6b85054c4`；class SHA `cb8b5af4d8ae0af18fa344239e790ccde6a5c8ef5718f60761b06767e5b732cd`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/Entity`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntitySlimeHole`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntitySlimeHole.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:86029896844beb0951f682e5` `ticksInWorld:I` access 1
- `field:66f666b2d755e0002ee28009` `tickWorld:I` access 1
- `field:d0b6f0b56ac56375623e2141` `size:I` access 1
- `field:fe6dee9e5bee8b0d63718a29` `rotate:F` access 1

## 方法目录

- `method:550cce6a31bfa640e0020677` `<init>(Lnet/minecraft/world/World;)V` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:862cd47c05707fc9633bf0cc` `<init>(Lnet/minecraft/world/World;DDDLnet/minecraft/entity/Entity;)V` access 1，20 code bytes；语义 NOT_ANALYZED
- `method:1ca56ea73bbedce8f415d484` `<init>(Lnet/minecraft/world/World;DDDIILnet/minecraft/entity/Entity;)V` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:27433664093fe86ceac26c1f` `<init>(Lnet/minecraft/world/World;Lnet/minecraft/entity/EntityLivingBase;)V` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:5e19877d381e77f073f54119` `func_70088_a()V` access 4，1 code bytes；语义 NOT_ANALYZED
- `method:fd573473adc00035c3f9cc70` `func_70112_a(D)Z` access 1，32 code bytes；语义 NOT_ANALYZED
- `method:605ef40ca44b3e0ce66a4b51` `func_70071_h_()V` access 1，83 code bytes；语义 NOT_ANALYZED
- `method:0b34fba92c5f1461e3c47a3f` `func_70014_b(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:242a3cfdc5d3c6adcf1b1c44` `func_70037_a(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:699ea4b8b64ba79ed8df5795` `func_70053_R()F` access 1，2 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
