# MoreFunQuicksandMod/main/client/RenderFish2

ID `class:17b1669d582f0f389a950d1b`；class SHA `b7127e9fe097bd2b2d2aea5183aaf5def156697ec4d31cde4bd7a281b6448a7d`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/client/renderer/entity/Render`；interfaces ``；access `33`；annotations/attributes `SourceFile;RuntimeVisibleAnnotations`。内部类宿主 `MoreFunQuicksandMod/main/client/RenderFish2`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__RenderFish2.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:c14492ec8c9ddb8a4c5803c2` `field_110792_a:Lnet/minecraft/util/ResourceLocation;` access 26
- `field:cdf43504ffc5d726b6179eea` `BeamTextures:Lnet/minecraft/util/ResourceLocation;` access 26

## 方法目录

- `method:8103b03d202cd09e60ba4f15` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:30bf350443c276d164ea707e` `doRenderFishHook(LMoreFunQuicksandMod/main/entity/EntityRope;DDDFF)V` access 1，1307 code bytes；语义 NOT_ANALYZED
- `method:5107ee233e15b26a3ddd7960` `func_110791_a(LMoreFunQuicksandMod/main/entity/EntityRope;)Lnet/minecraft/util/ResourceLocation;` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:abeddabcb6207256acce427f` `func_110775_a(Lnet/minecraft/entity/Entity;)Lnet/minecraft/util/ResourceLocation;` access 4，9 code bytes；语义 NOT_ANALYZED
- `method:6855ebeb746f530f16eb9011` `func_76986_a(Lnet/minecraft/entity/Entity;DDDFF)V` access 1，18 code bytes；语义 NOT_ANALYZED
- `method:0d5c4a842dbeded89ba29788` `renderRope(Lnet/minecraft/client/renderer/Tessellator;Lnet/minecraft/util/Vec3;Lnet/minecraft/entity/Entity;DDDDDD)V` access 1，492 code bytes；语义 NOT_ANALYZED
- `method:4fc34ca4daad5ff425f5cfba` `renderLoop(Lnet/minecraft/client/renderer/Tessellator;Lnet/minecraft/entity/Entity;DDDLnet/minecraft/util/Vec3;Lnet/minecraft/util/Vec3;)V` access 1，1578 code bytes；语义 NOT_ANALYZED
- `method:cdc1fc885752f1cbf0acc7a3` `<clinit>()V` access 8，30 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
