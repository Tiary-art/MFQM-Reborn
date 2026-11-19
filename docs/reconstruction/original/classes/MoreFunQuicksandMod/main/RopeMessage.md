# MoreFunQuicksandMod/main/RopeMessage

ID `class:78e5c14502ab85f26cb077d5`；class SHA `bd39b59a42cc4ccde3a86e5bce5dd0eb6121607960a664804aa320a43129a7fd`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `java/lang/Object`；interfaces `cpw/mods/fml/common/network/simpleimpl/IMessage`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/RopeMessage`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__RopeMessage.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:a93006371ae3d1b2a69a8121` `Len:F` access 2

## 方法目录

- `method:c2dcb5376c4e2a49da9fe34e` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:0c57cd78b53abb9d13e1145c` `<init>(F)V` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:0a51383f46571fc54fbf8ced` `fromBytes(Lio/netty/buffer/ByteBuf;)V` access 1，9 code bytes；语义 NOT_ANALYZED
- `method:69f01a4acaaa9f4a73fe3d8d` `toBytes(Lio/netty/buffer/ByteBuf;)V` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:e3737d828ce3a06806498cc1` `handleCurLen(FLnet/minecraft/entity/player/EntityPlayerMP;)V` access 9，50 code bytes；语义 NOT_ANALYZED
- `method:74466c35cf3d4edeaafc468d` `access$000(LMoreFunQuicksandMod/main/RopeMessage;)F` access 4104，5 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
