# MoreFunQuicksandMod/main/client/RenderFish3

ID `class:db3455726539123fe79dfc4d`；class SHA `cf16472a7ac4d3827cce74722ec6849688874b1de71db47d0e9b7aa68c272cbc`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/client/renderer/entity/Render`；interfaces ``；access `33`；annotations/attributes `SourceFile;RuntimeVisibleAnnotations`。内部类宿主 `MoreFunQuicksandMod/main/client/RenderFish3`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__RenderFish3.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:b1e8a70961e81e1be0999980` `BeamTextures:Lnet/minecraft/util/ResourceLocation;` access 26
- `field:6b38afb7aed0a8b66f7436f9` `BaseTextures:Lnet/minecraft/util/ResourceLocation;` access 26

## 方法目录

- `method:caa197ff7fb3de22b8811929` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:6a65e7475b6043cce49f6fab` `doRenderFishHook(LMoreFunQuicksandMod/main/entity/EntityHook;DDDFF)V` access 1，2092 code bytes；语义 NOT_ANALYZED
- `method:b3a5b120e5ac868b0c62db10` `func_110791_a(LMoreFunQuicksandMod/main/entity/EntityHook;)Lnet/minecraft/util/ResourceLocation;` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:b650b650e79a73ede785b25c` `func_110775_a(Lnet/minecraft/entity/Entity;)Lnet/minecraft/util/ResourceLocation;` access 4，9 code bytes；语义 NOT_ANALYZED
- `method:9e552cce84dcb92506b4d5eb` `func_76986_a(Lnet/minecraft/entity/Entity;DDDFF)V` access 1，18 code bytes；语义 NOT_ANALYZED
- `method:879452ccadd72ed97aee96d5` `renderRope(Lnet/minecraft/client/renderer/Tessellator;Lnet/minecraft/util/Vec3;Lnet/minecraft/entity/Entity;DDDDDD)V` access 1，492 code bytes；语义 NOT_ANALYZED
- `method:541e88bdc0d98cd40392fc4a` `renderHook(Lnet/minecraft/client/renderer/Tessellator;Lnet/minecraft/entity/Entity;DDDLnet/minecraft/util/Vec3;)V` access 1，493 code bytes；语义 NOT_ANALYZED
- `method:94a1838e1305d2a79b03b57c` `renderCube(Lnet/minecraft/client/renderer/Tessellator;DDDDDD)V` access 1，535 code bytes；语义 NOT_ANALYZED
- `method:43f4b5ebc4e0df213b87a418` `<clinit>()V` access 8，33 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
