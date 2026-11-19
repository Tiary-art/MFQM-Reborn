# MoreFunQuicksandMod/main/items/ItemRope

ID `class:7465e6f60528d2768cd9881e`；class SHA `51bf5aa7781a2f150404fbf40630f83c4346c59da9817f010d985634c0996890`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/item/Item`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/items/ItemRope`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__items__ItemRope.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:70aaaeaf242b5768c45e9106` `itemIIcon1:Lnet/minecraft/util/IIcon;` access 2
- `field:fa5b17fe5fd316578ff51fa1` `itemIIcon2:Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:bbc6fffd2530afab8dfe0be8` `<init>()V` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:cf42f00702d8405af5148bad` `func_77662_d()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:95fe2d2412cd279406cea493` `func_77629_n_()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:cdfff6a4823de9d67e44eb25` `func_77659_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)Lnet/minecraft/item/ItemStack;` access 1，290 code bytes；语义 NOT_ANALYZED
- `method:6a15faecfeb2369dce8101df` `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:5d9e28a2a27b4b8f72c4fc0c` `func_77617_a(I)Lnet/minecraft/util/IIcon;` access 1，16 code bytes；语义 NOT_ANALYZED
- `method:8f8b5e2cab2bf03d91146f37` `onEntityItemUpdate(Lnet/minecraft/entity/item/EntityItem;)Z` access 1，40 code bytes；语义 NOT_ANALYZED
- `method:58253897dbf87cb2d744bace` `func_77624_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/entity/player/EntityPlayer;Ljava/util/List;Z)V` access 1，299 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `<init>()V` · CFR 43–48
- `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 100–103 · 101 morefunquicksandmod:Rope1 | 102 morefunquicksandmod:Rope2
- `func_77617_a(I)Lnet/minecraft/util/IIcon;` · CFR 106–111

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Rope|0|Rope|`mfqm:rope`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
