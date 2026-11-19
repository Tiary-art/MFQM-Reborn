# MoreFunQuicksandMod/main/blocks/BlockHardenedClay

ID `class:da9037ac23bee384c631a153`；class SHA `9e558db4941b26a49348c2749df0f103e96726e94a15674991a5c857bf9569a2`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockHardenedClay`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockHardenedClay.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `hardened_clay`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:1e1ec19f1938bb0d99734d38` `IIconNormalArray:[Lnet/minecraft/util/IIcon;` access 2
- `field:02be0d69f5b13ea1d1a6d0c9` `IIconBrokenArray:[Lnet/minecraft/util/IIcon;` access 2
- `field:840ae893a430a0a8c8abb2e7` `IIconSideNormal:Lnet/minecraft/util/IIcon;` access 2
- `field:c55ee3a71619d0837cc6ce4b` `IIconSideBroken:Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:3dcbadfc0b0de7bfa17345b7` `<init>()V` access 1，45 code bytes；语义 NOT_ANALYZED
- `method:986da0a71ebce9f8048346bc` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，38 code bytes；语义 NOT_ANALYZED
- `method:dbe612561465e53546bcac0f` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，153 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 43–50
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 53–66 · 56 morefunquicksandmod:clay0_0 | 57 morefunquicksandmod:clay0_1 | 58 morefunquicksandmod:clay0_2 | 59 morefunquicksandmod:clay0_3 | 60 morefunquicksandmod:clay0_4 | 61 morefunquicksandmod:clay1 | 62 morefunquicksandmod:clay2 | 63 morefunquicksandmod:clay3 | 64 morefunquicksandmod:clay4 | 65 morefunquicksandmod:clay5

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|HardenedClay|0|Hardened Clay|`mfqm:hardened_clay`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
