# MoreFunQuicksandMod/main/client/RenderVoreSlime

ID `class:b4fd43b2d5a9de426c79f219`；class SHA `afa400928ee05a9e82a8132dc06207ff921fcf049d4f20a6e4e2d14b0ede7d96`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/client/renderer/entity/RenderLiving`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/client/RenderVoreSlime`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__RenderVoreSlime.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:9f39eb3ff0fee75b0bbc03ab` `slimeTextures:Lnet/minecraft/util/ResourceLocation;` access 26
- `field:970981ee12975ab70d45f556` `scaleAmount:Lnet/minecraft/client/model/ModelBase;` access 2

## 方法目录

- `method:cd5bbfd477f92a487003d554` `<init>(Lnet/minecraft/client/model/ModelBase;Lnet/minecraft/client/model/ModelBase;F)V` access 1，12 code bytes；语义 NOT_ANALYZED
- `method:d23a7d26be2e7990dcff913d` `shouldRenderPass(LMoreFunQuicksandMod/main/entity/EntityVoreSlime;IF)I` access 4，64 code bytes；语义 NOT_ANALYZED
- `method:a0f2aaa77d773f18986eb60a` `preRenderCallback(LMoreFunQuicksandMod/main/entity/EntityVoreSlime;F)V` access 4，71 code bytes；语义 NOT_ANALYZED
- `method:860aa1e065086f28bd27f721` `getEntityTexture(LMoreFunQuicksandMod/main/entity/EntityVoreSlime;)Lnet/minecraft/util/ResourceLocation;` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:20be12bc8c9fa97bb08849d1` `func_77041_b(Lnet/minecraft/entity/EntityLivingBase;F)V` access 4，10 code bytes；语义 NOT_ANALYZED
- `method:001ffcd839d99184bb42a3df` `func_77032_a(Lnet/minecraft/entity/EntityLivingBase;IF)I` access 4，11 code bytes；语义 NOT_ANALYZED
- `method:615c26dca2a9f49f39863a95` `func_110775_a(Lnet/minecraft/entity/Entity;)Lnet/minecraft/util/ResourceLocation;` access 4，9 code bytes；语义 NOT_ANALYZED
- `method:daa7c2b4fa95bf4d4f3b6679` `<clinit>()V` access 8，15 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
