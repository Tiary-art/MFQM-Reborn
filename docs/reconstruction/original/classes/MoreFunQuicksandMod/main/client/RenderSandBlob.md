# MoreFunQuicksandMod/main/client/RenderSandBlob

ID `class:1a07cc86f8ab61aa6ff6f8f6`；class SHA `001d3e43e5687ae83ce4d032fe62af6a0fc0b1a37eaa38069f0c50ac4dc43b2b`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/client/renderer/entity/RenderLiving`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/client/RenderSandBlob`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__RenderSandBlob.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:b13e7693eeb6347f2247e40d` `slimeTextures:Lnet/minecraft/util/ResourceLocation;` access 26
- `field:0b8251fcb7d4378787d9e092` `scaleAmount:Lnet/minecraft/client/model/ModelBase;` access 2

## 方法目录

- `method:91137d1ca64b059e4bb6654f` `<init>(Lnet/minecraft/client/model/ModelBase;Lnet/minecraft/client/model/ModelBase;F)V` access 1，12 code bytes；语义 NOT_ANALYZED
- `method:7f2399942b9fbfa2a962a123` `shouldRenderPass(LMoreFunQuicksandMod/main/entity/EntitySandBlob;IF)I` access 4，155 code bytes；语义 NOT_ANALYZED
- `method:2052a2a3895fb0db0362fc26` `preRenderCallback(LMoreFunQuicksandMod/main/entity/EntitySandBlob;F)V` access 4，71 code bytes；语义 NOT_ANALYZED
- `method:28009390269230b08c252499` `getEntityTexture(LMoreFunQuicksandMod/main/entity/EntitySandBlob;)Lnet/minecraft/util/ResourceLocation;` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:4bd687b5ae069a06b7a92b5e` `func_77041_b(Lnet/minecraft/entity/EntityLivingBase;F)V` access 4，10 code bytes；语义 NOT_ANALYZED
- `method:a074d1785ad90e8e8c01b69d` `func_77032_a(Lnet/minecraft/entity/EntityLivingBase;IF)I` access 4，11 code bytes；语义 NOT_ANALYZED
- `method:f3d8ab467260a1b9ac9d800b` `func_110775_a(Lnet/minecraft/entity/Entity;)Lnet/minecraft/util/ResourceLocation;` access 4，9 code bytes；语义 NOT_ANALYZED
- `method:46c1f5051fb698e36344d1bc` `<clinit>()V` access 8，15 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
