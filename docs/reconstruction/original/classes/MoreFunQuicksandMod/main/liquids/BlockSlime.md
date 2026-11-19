# MoreFunQuicksandMod/main/liquids/BlockSlime

ID `class:e01b6d18d59d51eef2e0863e`；class SHA `bd4b42cffc19dfea1bc11085068a75c2f9dce3ce06a5874d29c67f32e2e683a4`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockSlime`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockSlime.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `sinking_slime`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:70767f8283a8e75a2c5f3aab` `theSlimeIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:50f73c077412fcb2ae35ba2b` `materialSlime:Lnet/minecraft/block/material/Material;` access 25
- `field:44a8dfeaef3bfa41fac23b99` `maxOpacity:I` access 2
- `field:67ab420e9d3ef7d16fbc426f` `lastOpacity:I` access 2
- `field:8aafc2eb69cf5e2b0871d6a7` `incOpacity:I` access 2

## 方法目录

- `method:6d552db3439a8c063f6d8421` `<init>(III)V` access 1，101 code bytes；语义 NOT_ANALYZED
- `method:83ee51343664929f537cf3a3` `func_149749_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，88 code bytes；语义 NOT_ANALYZED
- `method:b64c9cd806910d6bb168b07d` `func_149678_a(IZ)Z` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:8b52efa77e220e3e80114d1a` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:ca969f5d33e4266398303b86` `getMaxRenderHeightMeta()I` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:86302d551b956c35b6933ae2` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，2931 code bytes；语义 NOT_ANALYZED
- `method:5f27d59f57dd0788dba403a1` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:8a915bbc1c56d401fcdd2666` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，676 code bytes；语义 NOT_ANALYZED
- `method:ff00eb8953d63ae0fb4da008` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:ad853b16d05e1925634632f1` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:538fb1a978e5b0ae56a5795d` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:18e6a9a8742b543b1dbcca7a` `isSideSolid(Lnet/minecraft/world/World;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:63ec70ecae22699b91bd0cbf` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:08990aafc593d2e09505a883` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:794077554e85b57e9db53723` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，60 code bytes；语义 NOT_ANALYZED
- `method:faf6a7bb9d6b2d554ad8ea33` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，124 code bytes；语义 NOT_ANALYZED
- `method:7bb8efc51c661ada040a9689` `<clinit>()V` access 8，17 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 356–358
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 497–501 · 499 morefunquicksandmod:Slime_Still | 499 morefunquicksandmod:Slime_Flowing

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|SinkingSlime|0|Sinking Slime|`mfqm:sinking_slime`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
