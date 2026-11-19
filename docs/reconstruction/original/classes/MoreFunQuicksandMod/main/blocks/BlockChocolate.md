# MoreFunQuicksandMod/main/blocks/BlockChocolate

ID `class:8f049be02fa42069f96efb50`；class SHA `38370d63f64f3b2527213805ba85afb631f10a3dfaab7d944b1c0bebfe593a17`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockChocolate`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockChocolate.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `chocolate`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:e0cf52f17c39de2119a356ac` `theQIIcon:Lnet/minecraft/util/IIcon;` access 0

## 方法目录

- `method:a47e1b2b944f6f7433eaa80f` `<init>()V` access 1，44 code bytes；语义 NOT_ANALYZED
- `method:46bf61f6a7b3db36c7c252e1` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，341 code bytes；语义 NOT_ANALYZED
- `method:701e79faacd7036f5fbfc056` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:3e9d1fa8754fbe0cc1b87b31` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，22 code bytes；语义 NOT_ANALYZED
- `method:b7bb9aee48925b3399e88e1e` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:074076d8400edfd72c4ad4cb` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，13 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 121–123
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 126–128 · 127 morefunquicksandmod:Chocolate

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|ChocolateBlock|0|Solid Chocolate|`mfqm:chocolate`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
