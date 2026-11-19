# MoreFunQuicksandMod/main/liquids/BlockAcid

ID `class:db2dc12b6d4cb2f2487c0883`；class SHA `d77ad2052d709971dd88907233f24906093d9902e9727140a33a455f90f49e17`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockAcid`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockAcid.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `acid`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:d4f74b9a20471feb7cc3b56d` `theAcidIIcon:[Lnet/minecraft/util/IIcon;` access 1

## 方法目录

- `method:78d5e09d8b2b33a9eca41c27` `<init>()V` access 1，60 code bytes；语义 NOT_ANALYZED
- `method:818aece8e7121cb5b187af8d` `func_149701_w()I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:b04b5cc8d7d26026cab9b2df` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，112 code bytes；语义 NOT_ANALYZED
- `method:a4f5afd0ee1ccb52e03eea04` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:c06ebfda66dc88f4fe95e935` `drain(Lnet/minecraft/world/World;IIIZ)Lnet/minecraftforge/fluids/FluidStack;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:21a5deaadb238a491b2ed76c` `canDrain(Lnet/minecraft/world/World;III)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:34a6fde38d0c5afef5d0fa88` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，1595 code bytes；语义 NOT_ANALYZED
- `method:7e1ec317cb731ed8cdfd50c1` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:a2d70980382a5e0cc503b950` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:b342a84f59528e51f97c8e20` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:61a1c6e79f3f1869a5dc0d7f` `func_149635_D()I` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:46d5a3b8468cb25b3ab40cc0` `func_149741_i(I)I` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:d1405b6d636ae5efdf7e63e8` `func_149720_d(Lnet/minecraft/world/IBlockAccess;III)I` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:412be847413f7199f76fdb70` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:d261e2f78afb50d92510e619` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，171 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
