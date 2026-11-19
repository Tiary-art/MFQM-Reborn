# MoreFunQuicksandMod/main/items/ItemRescue

ID `class:8860e9f4f5d43d2bab2e9f46`；class SHA `eb059e2a1a1d32bbd5668cdc9d63f59b03e8473f886586cdd50b6c26babf7282`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/item/Item`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/items/ItemRescue`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__items__ItemRescue.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:83b8e2e1354577c8d5d80239` `itemIIcon1:Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:18a23cbda1b7486820755f2b` `<init>()V` access 1，18 code bytes；语义 NOT_ANALYZED
- `method:a91dba8dab9b1f489eceaca6` `func_77661_b(Lnet/minecraft/item/ItemStack;)Lnet/minecraft/item/EnumAction;` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:c828b7e9ba08de6d0db52c15` `func_77626_a(Lnet/minecraft/item/ItemStack;)I` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:6d337be39d99ba88bf694647` `func_77662_d()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:21285d284f47124932b12087` `func_77629_n_()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:29cd5f3796ca1491065fc574` `func_77663_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/Entity;IZ)V` access 1，107 code bytes；语义 NOT_ANALYZED
- `method:3339afc18399424b01f13d30` `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，13 code bytes；语义 NOT_ANALYZED
- `method:c756a42b119d34b2c1bd8e4a` `func_77617_a(I)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:71eb451f59a8c07d8026e449` `onEntityItemUpdate(Lnet/minecraft/entity/item/EntityItem;)Z` access 1，6 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `<init>()V` · CFR 36–39
- `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 81–83 · 82 morefunquicksandmod:Rescue
- `func_77617_a(I)Lnet/minecraft/util/IIcon;` · CFR 86–88

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Rescuing|0|Rescuing|`mfqm:rescuing`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
