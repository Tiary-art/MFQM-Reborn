# MoreFunQuicksandMod/main/entity/EntityBubble

ID `class:f483f66a36d6f080adae46d1`；class SHA `4ad94b92adb21fe033c5edb274d4499bf59f9770a6e5b4036fc932ab2cc4762f`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/Entity`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntityBubble`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntityBubble.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:df5fcaf502d084f78f3e14c5` `ticksWorld:J` access 1
- `field:72160780665c3ed97ba6156a` `liveTime:I` access 1
- `field:1e85609dd5c63c85896b3a2c` `size:F` access 1
- `field:cd7388748458bd8c67846df2` `block:Lnet/minecraft/block/Block;` access 1
- `field:edae490b0b85cc29f427d253` `meta:I` access 1
- `field:a2428f7ea3238e8b732716f8` `rotate:F` access 1

## 方法目录

- `method:4648df57124a388321b5ad76` `<init>(Lnet/minecraft/world/World;)V` access 1，30 code bytes；语义 NOT_ANALYZED
- `method:5b8e1a3828b904d6a886927a` `<init>(Lnet/minecraft/world/World;DDDLnet/minecraft/block/Block;IFI)V` access 1，258 code bytes；语义 NOT_ANALYZED
- `method:a875159367a135c7766ebd5a` `<init>(Lnet/minecraft/world/World;DDDLnet/minecraft/block/Block;IFII)V` access 1，31 code bytes；语义 NOT_ANALYZED
- `method:0d335aeb9158360389a7d003` `func_70088_a()V` access 4，1 code bytes；语义 NOT_ANALYZED
- `method:b8f4609b3a23569b808b2dfc` `func_70112_a(D)Z` access 1，32 code bytes；语义 NOT_ANALYZED
- `method:c278b141ab0ee9b1bc256bcc` `func_70071_h_()V` access 1，358 code bytes；语义 NOT_ANALYZED
- `method:d0de88611d7ee80ecdc8edc4` `func_70014_b(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:4cce46afa20b9038aa3c51a8` `func_70037_a(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:0637d451120277a29615e192` `func_70053_R()F` access 1，2 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
