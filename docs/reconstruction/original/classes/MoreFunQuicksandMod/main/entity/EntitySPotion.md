# MoreFunQuicksandMod/main/entity/EntitySPotion

ID `class:b9cf124f5814518ab6acf654`；class SHA `7885e090da76c0c603fb05c4994d09195e80015d0dac1d3049fd59032129faa6`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/projectile/EntityThrowable`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntitySPotion`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntitySPotion.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

无声明字段。

## 方法目录

- `method:1db7966b0080f8f28de261ca` `<init>(Lnet/minecraft/world/World;)V` access 1，6 code bytes；语义 NOT_ANALYZED
- `method:f548f20cc702917843f2745a` `<init>(Lnet/minecraft/world/World;Lnet/minecraft/entity/EntityLivingBase;I)V` access 1，19 code bytes；语义 NOT_ANALYZED
- `method:57393fe5cb6302925ef9834e` `<init>(Lnet/minecraft/world/World;Lnet/minecraft/entity/EntityLivingBase;Lnet/minecraft/item/ItemStack;)V` access 1，7 code bytes；语义 NOT_ANALYZED
- `method:57c1eaa9d0a0bf76d906fe6d` `<init>(Lnet/minecraft/world/World;DDDI)V` access 1，24 code bytes；语义 NOT_ANALYZED
- `method:4c0c9011f0cfd57cce968c2b` `<init>(Lnet/minecraft/world/World;DDDLnet/minecraft/item/ItemStack;)V` access 1，11 code bytes；语义 NOT_ANALYZED
- `method:0e6a3189e526cd86f60e13c5` `func_70185_h()F` access 4，3 code bytes；语义 NOT_ANALYZED
- `method:6a2cf57ea92a64efe59db4bf` `func_70182_d()F` access 4，3 code bytes；语义 NOT_ANALYZED
- `method:42200a21e01f7fa58cc63695` `func_70183_g()F` access 4，3 code bytes；语义 NOT_ANALYZED
- `method:718bc7dfb3b85c23b6db8d32` `validForSpread(Lnet/minecraft/world/World;III)Z` access 4，72 code bytes；语义 NOT_ANALYZED
- `method:4d7b8d3b917629712d3887fc` `func_70184_a(Lnet/minecraft/util/MovingObjectPosition;)V` access 4，741 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
