# MoreFunQuicksandMod/main/client/MudModelRenderer

ID `class:95f986c519b1653347e9f044`；class SHA `ef7421fd6c7930ad3ce4a103dacb225e3cd5b0ce103be6337d8ea2cf949a03bc`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/client/model/ModelRenderer`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/client/MudModelRenderer`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__MudModelRenderer.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:c6749cbc5144a85a30a980b6` `currentPlayer:Lnet/minecraft/entity/player/EntityPlayer;` access 1
- `field:a7e768c569552f02036deab5` `currentPlayerUUID:Ljava/util/UUID;` access 1
- `field:b131829afd5411d1a6890371` `currentPlayerNick:Ljava/lang/String;` access 1
- `field:1f0b6fdef723794e799255a6` `world:Lnet/minecraft/world/World;` access 1
- `field:60bcf5cd21a10dc86cebe0fa` `eventShow:Z` access 1

## 方法目录

- `method:b32536ad870df2927f9212da` `<init>(Lnet/minecraft/client/model/ModelBase;Ljava/lang/String;)V` access 1，12 code bytes；语义 NOT_ANALYZED
- `method:22ef00ec45fdd908d79efb24` `<init>(Lnet/minecraft/client/model/ModelBase;)V` access 1，11 code bytes；语义 NOT_ANALYZED
- `method:eae247d5fcda1ac8741b70d8` `<init>(Lnet/minecraft/client/model/ModelBase;Lnet/minecraft/entity/player/EntityPlayer;)V` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:6781724609d129303bace11e` `<init>(Lnet/minecraft/client/model/ModelBase;IILnet/minecraft/entity/player/EntityPlayer;)V` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:dd41f705c2ebd86406a69e51` `<init>(Lnet/minecraft/client/model/ModelBase;II)V` access 1，13 code bytes；语义 NOT_ANALYZED
- `method:a0df13f421dcbfaa27c8c9b5` `func_78785_a(F)V` access 1，395 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
