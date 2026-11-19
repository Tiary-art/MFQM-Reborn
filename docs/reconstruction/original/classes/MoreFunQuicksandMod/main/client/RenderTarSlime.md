# MoreFunQuicksandMod/main/client/RenderTarSlime

ID `class:941f54154faae5f61e930009`；class SHA `c3f92ceeeb4601b0e252bea2aa87cc35c61287239632193e2bcbfc2bc78e9790`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/client/renderer/entity/RenderLiving`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/client/RenderTarSlime`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__RenderTarSlime.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:488159e71952b0a4806c59a3` `slimeTextures:Lnet/minecraft/util/ResourceLocation;` access 26
- `field:ddcd57eaff6e26c3ba49a05a` `scaleAmount:Lnet/minecraft/client/model/ModelBase;` access 2
- `field:71572c7cb8932cc8a2c387db` `texType:I` access 2

## 方法目录

- `method:3bc8da37e48875a849bca10f` `<init>(Lnet/minecraft/client/model/ModelBase;Lnet/minecraft/client/model/ModelBase;F)V` access 1，12 code bytes；语义 NOT_ANALYZED
- `method:f2c2c319a8896594554bd975` `shouldRenderPass(LMoreFunQuicksandMod/main/entity/EntityTarSlime;IF)I` access 4，64 code bytes；语义 NOT_ANALYZED
- `method:1a9d52c0652585eff426ad6d` `preRenderCallback(LMoreFunQuicksandMod/main/entity/EntityTarSlime;F)V` access 4，71 code bytes；语义 NOT_ANALYZED
- `method:992a7bdbbe07f8f3393a6d2b` `getEntityTexture(LMoreFunQuicksandMod/main/entity/EntityTarSlime;)Lnet/minecraft/util/ResourceLocation;` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:ea612c2bd287e3675dc8ffa3` `func_77041_b(Lnet/minecraft/entity/EntityLivingBase;F)V` access 4，10 code bytes；语义 NOT_ANALYZED
- `method:7e519a857612b961fccbd431` `func_77032_a(Lnet/minecraft/entity/EntityLivingBase;IF)I` access 4，11 code bytes；语义 NOT_ANALYZED
- `method:1bf5cc3cd155162719d952ba` `func_110775_a(Lnet/minecraft/entity/Entity;)Lnet/minecraft/util/ResourceLocation;` access 4，9 code bytes；语义 NOT_ANALYZED
- `method:d466b23cd82a54888a37688f` `<clinit>()V` access 8，15 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
