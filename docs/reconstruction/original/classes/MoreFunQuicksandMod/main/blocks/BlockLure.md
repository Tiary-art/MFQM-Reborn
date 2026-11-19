# MoreFunQuicksandMod/main/blocks/BlockLure

ID `class:8d9d1e91f2c431445aa8dd51`；class SHA `33f1c476f3ae21317c99d50b196366cd5f17ce41776fb2c63aa3721b9c58d128`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/BlockContainer`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockLure`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockLure.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `lure_block`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:36b10cbf298549ebafe5c311` `theCSIIcon:Lnet/minecraft/util/IIcon;` access 1

## 方法目录

- `method:74fdf3241411e3603e25bd2e` `<init>()V` access 1，38 code bytes；语义 NOT_ANALYZED
- `method:1188395da8eefb62d674038f` `func_149915_a(Lnet/minecraft/world/World;I)Lnet/minecraft/tileentity/TileEntity;` access 1，19 code bytes；语义 NOT_ANALYZED
- `method:c3582c253a265a647c25055f` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:a9a91ec7c5cd3a60f3ff975f` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，13 code bytes；语义 NOT_ANALYZED
- `method:67968129bbb5a21f0f469477` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，112 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
