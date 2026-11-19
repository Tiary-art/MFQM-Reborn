# MoreFunQuicksandMod/main/entity/EntityBee

ID `class:8161980885a4d64691c41c14`；class SHA `ed697e01e1954669f8ed6e449da9595cf042bcced940080213eb0b2efbad1ba5`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/entity/monster/EntityMob`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/entity/EntityBee`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__entity__EntityBee.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:5e49d5bca9ca69ad5ee7e454` `courseChangeCooldown:I` access 1
- `field:ca9745ae173b5f064bc27e4b` `waypointX:D` access 1
- `field:6be0bea9a37d7b896a44c9d7` `waypointY:D` access 1
- `field:8cfef81375c97633a93b69f0` `waypointZ:D` access 1
- `field:baab799696d0dcc1449239d2` `targetedEntity:Lnet/minecraft/entity/Entity;` access 2
- `field:bfe110a30d7cc5a1cdeda118` `aggroCooldown:I` access 2

## 方法目录

- `method:28e160d9c452a8b164aae892` `<init>(Lnet/minecraft/world/World;)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:b5b08136d7a98eee99413972` `func_70069_a(F)V` access 4，1 code bytes；语义 NOT_ANALYZED
- `method:81eaa3eddbb5bd69802ca073` `func_70064_a(DZ)V` access 4，1 code bytes；语义 NOT_ANALYZED
- `method:124e8fe12121029954303612` `func_70612_e(FF)V` access 1，425 code bytes；语义 NOT_ANALYZED
- `method:459f3ab8eeadc0a8166a85ee` `func_70617_f_()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:7fe2df9ec38a7fdf55c82845` `func_110147_ax()V` access 4，35 code bytes；语义 NOT_ANALYZED
- `method:5152cb2e2d55fc8eb28788c3` `func_70626_be()V` access 4，756 code bytes；语义 NOT_ANALYZED
- `method:45f25e5f311dfd3a4702502c` `isCourseTraversable(DDDD)Z` access 2，103 code bytes；语义 NOT_ANALYZED
- `method:2c287bf41d5573cd97fec2fb` `func_70599_aP()F` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:16ee702483227d68d320753a` `func_70639_aQ()Ljava/lang/String;` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:7db911b3f896c3cf3db5cec1` `func_70621_aR()Ljava/lang/String;` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:b1d0e0067d81e67ea75d1044` `func_70673_aS()Ljava/lang/String;` access 4，4 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
