# MoreFunQuicksandMod/main/items/ItemLiqGun

ID `class:7176cf6be32588294245f71d`；class SHA `1cc361a000cd404ee7210970f76368b1ff33b262867413471d5fce9253ad6e38`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/item/Item`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/items/ItemLiqGun`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__items__ItemLiqGun.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:7a9035c295813d10b08a7379` `itemIcon:Lnet/minecraft/util/IIcon;` access 2

## 方法目录

- `method:05a383a72abf26d9ca9674e0` `<init>()V` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:6f15460e6cdfc877c0e26487` `func_77661_b(Lnet/minecraft/item/ItemStack;)Lnet/minecraft/item/EnumAction;` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:04967653dd02e964cdc3ecf7` `func_77645_m()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:d1e8cc2962b609f5735f2061` `func_77626_a(Lnet/minecraft/item/ItemStack;)I` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:f0777eab4ece924be471c3c2` `func_77662_d()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:3ae3e1a555811bb9a201a9a6` `func_77629_n_()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:f6f599f80d5de3abb392d92a` `func_77615_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;I)V` access 1，186 code bytes；语义 NOT_ANALYZED
- `method:70dd32c2923b59b4f3f2960d` `func_77622_d(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)V` access 1，55 code bytes；语义 NOT_ANALYZED
- `method:37bbb373d85fcd4fce0052d9` `func_77659_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;)Lnet/minecraft/item/ItemStack;` access 1，236 code bytes；语义 NOT_ANALYZED
- `method:8a39217a326a530e433aa342` `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:00202ff34f701915c8306d02` `func_77617_a(I)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:33a0174aa7293030104961fd` `func_77624_a(Lnet/minecraft/item/ItemStack;Lnet/minecraft/entity/player/EntityPlayer;Ljava/util/List;Z)V` access 1，142 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `<init>()V` · CFR 50–55
- `func_94581_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 150–152 · 151 morefunquicksandmod:LiqGun
- `func_77617_a(I)Lnet/minecraft/util/IIcon;` · CFR 155–157

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|LiqGunItem|0|Liquid Gun|`mfqm:liq_gun_item`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
