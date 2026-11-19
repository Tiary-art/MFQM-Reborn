# MoreFunQuicksandMod/main/client/RenderSlimeHole

ID `class:702c43c700ae9392e3c3f4ca`；class SHA `4916ed2e6b39a2e15ee97d7913d7820f79b635ba0eeec9c7edd0028574f699f0`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/client/renderer/entity/Render`；interfaces ``；access `33`；annotations/attributes `SourceFile;RuntimeVisibleAnnotations`。内部类宿主 `MoreFunQuicksandMod/main/client/RenderSlimeHole`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__RenderSlimeHole.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:d29c6c02c05bcb387aa02a60` `slimeHole0:Lnet/minecraft/util/ResourceLocation;` access 26
- `field:8e8bbd5e0bd5c6482d55e69f` `slimeHole1:Lnet/minecraft/util/ResourceLocation;` access 26
- `field:87740d86dab207cf8bc613ac` `slimeHole2:Lnet/minecraft/util/ResourceLocation;` access 26
- `field:d327d5723b19991f4efbbe5a` `slimeHole3:Lnet/minecraft/util/ResourceLocation;` access 26

## 方法目录

- `method:dd26f0828db7db4efb168c6d` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:08aaa2a64a6ab8874f34fc21` `doRenderSlimeHole(LMoreFunQuicksandMod/main/entity/EntitySlimeHole;DDDFF)V` access 1，1397 code bytes；语义 NOT_ANALYZED
- `method:73f8f9f4f99eba5a991ee2e9` `drawQuad(Lnet/minecraft/client/renderer/Tessellator;DDDDDDDDD)V` access 1，69 code bytes；语义 NOT_ANALYZED
- `method:d1fc8f5c5e7b2ba713475c69` `func_110775_a(Lnet/minecraft/entity/Entity;)Lnet/minecraft/util/ResourceLocation;` access 4，9 code bytes；语义 NOT_ANALYZED
- `method:1dda4622a5bd48022e5a975a` `getHoleType(LMoreFunQuicksandMod/main/entity/EntitySlimeHole;)Lnet/minecraft/util/ResourceLocation;` access 4，40 code bytes；语义 NOT_ANALYZED
- `method:036c2eb2721fff06f79203a3` `func_76986_a(Lnet/minecraft/entity/Entity;DDDFF)V` access 1，18 code bytes；语义 NOT_ANALYZED
- `method:2f38dd3dc79717d87e1ff545` `<clinit>()V` access 8，57 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
