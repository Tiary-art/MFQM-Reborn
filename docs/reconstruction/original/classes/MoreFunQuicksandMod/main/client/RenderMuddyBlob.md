# MoreFunQuicksandMod/main/client/RenderMuddyBlob

ID `class:199fbfac6dccd3c20321d546`；class SHA `7aaf2a69700e538ba1029463392a0653894c6870738f1233d305f2fe4da1e855`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/client/renderer/entity/RenderLiving`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/client/RenderMuddyBlob`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__RenderMuddyBlob.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:cecc844fad31d82000d4cfd2` `slimeTextures:Lnet/minecraft/util/ResourceLocation;` access 26
- `field:d527f9d727ff76a9ac08cc11` `scaleAmount:Lnet/minecraft/client/model/ModelBase;` access 2
- `field:10fce528b03445fa4a5aff8e` `texType:I` access 2

## 方法目录

- `method:2460643a7e115b91d10f6564` `<init>(Lnet/minecraft/client/model/ModelBase;Lnet/minecraft/client/model/ModelBase;F)V` access 1，12 code bytes；语义 NOT_ANALYZED
- `method:6f0021b7e07da3a77431d2a8` `shouldRenderPass(LMoreFunQuicksandMod/main/entity/EntityMuddyBlob;IF)I` access 4，64 code bytes；语义 NOT_ANALYZED
- `method:2d7c0cc81f3840a49200bf91` `preRenderCallback(LMoreFunQuicksandMod/main/entity/EntityMuddyBlob;F)V` access 4，71 code bytes；语义 NOT_ANALYZED
- `method:9e11d9ef32d8b198fa097090` `getEntityTexture(LMoreFunQuicksandMod/main/entity/EntityMuddyBlob;)Lnet/minecraft/util/ResourceLocation;` access 4，4 code bytes；语义 NOT_ANALYZED
- `method:626d988bebf7fc3c59834539` `func_77041_b(Lnet/minecraft/entity/EntityLivingBase;F)V` access 4，10 code bytes；语义 NOT_ANALYZED
- `method:a0ccdf51972cae4a68ae087d` `func_77032_a(Lnet/minecraft/entity/EntityLivingBase;IF)I` access 4，11 code bytes；语义 NOT_ANALYZED
- `method:fab5c7671551b957a30a6e54` `func_110775_a(Lnet/minecraft/entity/Entity;)Lnet/minecraft/util/ResourceLocation;` access 4，9 code bytes；语义 NOT_ANALYZED
- `method:4a88a0dd837dcd0e4c9855b4` `<clinit>()V` access 8，15 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
