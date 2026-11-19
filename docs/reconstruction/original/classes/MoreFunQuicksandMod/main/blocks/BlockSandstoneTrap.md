# MoreFunQuicksandMod/main/blocks/BlockSandstoneTrap

ID `class:2c4bbd3ba55c02b90fc67925`；class SHA `333def52907019629a0f6ab4daea6d6edf9575d16d53a775606901ff65560387`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/BlockSandStone`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockSandstoneTrap`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockSandstoneTrap.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `sandstone_trap`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

无声明字段。

## 方法目录

- `method:cf0cccc9191c1f74823702eb` `<init>()V` access 1，27 code bytes；语义 NOT_ANALYZED
- `method:ef7d913447eef30f92e1440b` `func_149726_b(Lnet/minecraft/world/World;III)V` access 1，30 code bytes；语义 NOT_ANALYZED
- `method:f222673578519ec9e9acc944` `func_149695_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;)V` access 1，21 code bytes；语义 NOT_ANALYZED
- `method:d04dab8a2d02ea2000248b77` `chainReaction(Lnet/minecraft/world/World;III)V` access 1，111 code bytes；语义 NOT_ANALYZED
- `method:d123941a461cedd771c2472d` `func_149692_a(I)I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:aec6cfa90a59b0f5ee9bd120` `func_149666_a(Lnet/minecraft/item/Item;Lnet/minecraft/creativetab/CreativeTabs;Ljava/util/List;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:8735867457ab96a8a3ce493d` `func_149700_E()Z` access 4，2 code bytes；语义 NOT_ANALYZED
- `method:8dda0f64e4d4723620676229` `canHarvestBlock(Lnet/minecraft/entity/player/EntityPlayer;I)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:773c2fd44ee6274a675e5625` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，7 code bytes；语义 NOT_ANALYZED
- `method:99f5f4c030945cf572b22112` `func_149745_a(Ljava/util/Random;)I` access 1，2 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
