# MoreFunQuicksandMod/main/items/ItemMucusBucket

ID `class:d6607116a687f54f692469ef`；class SHA `b0a9c420f6729a92a722e9c95f30b82c0e7dcefb2a920bf587bfff61a672ba26`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/item/ItemBucket`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/items/ItemMucusBucket`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__items__ItemMucusBucket.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

无声明字段。

## 方法目录

- `method:857698156bf9484d266448a8` `<init>(Lnet/minecraft/block/Block;)V` access 1，21 code bytes；语义 NOT_ANALYZED
- `method:0a977066e7fad5b43553894d` `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，13 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `<init>(Lnet/minecraft/block/Block;)V` · CFR 22–26
- `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 29–31 · 30 morefunquicksandmod:BucketOfMucus

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|BucketOfMucus|0|Bucket of Mucus|`mfqm:mucus_bucket`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
