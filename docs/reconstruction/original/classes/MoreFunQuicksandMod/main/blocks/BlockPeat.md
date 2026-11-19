# MoreFunQuicksandMod/main/blocks/BlockPeat

ID `class:df098a2594b489a28d1bce68`；class SHA `fed5debdb392652b533156163a33a5bc268e73d821bd8d37553a241e9ecae2e2`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraft/block/Block`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/blocks/BlockPeat`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockPeat.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `h_peat`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:090678ff6b4d9975a81c7571` `theQIIcon:Lnet/minecraft/util/IIcon;` access 0

## 方法目录

- `method:5d6c58491dad24375019a82a` `<init>()V` access 1，44 code bytes；语义 NOT_ANALYZED
- `method:50bdab9fb991e5b14e884b4f` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:9d700a6574a23ad7c4dd01ae` `func_149650_a(ILjava/util/Random;I)Lnet/minecraft/item/Item;` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:a8fb652f85ed420753e69841` `func_149745_a(Ljava/util/Random;)I` access 1，9 code bytes；语义 NOT_ANALYZED
- `method:70a3512b6b800ebf18563026` `func_149636_a(Lnet/minecraft/world/World;Lnet/minecraft/entity/player/EntityPlayer;IIII)V` access 1，48 code bytes；语义 NOT_ANALYZED
- `method:dc2cf20c07b11fad7f402d8d` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，13 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
