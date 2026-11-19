# MoreFunQuicksandMod/main/liquids/BlockMucus

ID `class:6e9848e291b40c1cf4263cb3`；class SHA `555db62d5305e235f464a701e38a4c58fc0bf84f899133b7e17f6324cb0cfa54`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockMucus`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockMucus.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `mucus`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:577bc91d34b39314aa8fa1e2` `theMucusIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:7884fbef916ac5600aefed91` `materialMucus:Lnet/minecraft/block/material/Material;` access 25
- `field:5b9fb5ba1f81d849b6819726` `maxOpacity:I` access 2
- `field:ce1afa4bd0efebe3892449c9` `lastOpacity:I` access 2
- `field:a7635509b9341614e945f448` `incOpacity:I` access 2

## 方法目录

- `method:315e7f2924fb40bb80fda038` `<init>(III)V` access 1，88 code bytes；语义 NOT_ANALYZED
- `method:c90bc99ec11e499ecd6f4060` `func_149749_a(Lnet/minecraft/world/World;IIILnet/minecraft/block/Block;I)V` access 1，88 code bytes；语义 NOT_ANALYZED
- `method:4c1f90c88754c57f71017aaa` `func_149678_a(IZ)Z` access 1，10 code bytes；语义 NOT_ANALYZED
- `method:4da91bf235d97a3965f660dc` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，3 code bytes；语义 NOT_ANALYZED
- `method:8fd1773ab71618f13ae7ffbd` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，3091 code bytes；语义 NOT_ANALYZED
- `method:38dfa549f4975ef68a4aaca2` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:31af0caa178516565d0c34ee` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，670 code bytes；语义 NOT_ANALYZED
- `method:affc129c3840b2888eb1c4ea` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:0102d01edec2adc34e2c4714` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:f1f8f066cb7ea6d9eb3f3491` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:df133a36e85b6ea252310f32` `isSideSolid(Lnet/minecraft/world/World;IIILnet/minecraftforge/common/util/ForgeDirection;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:1382e657dbaeab7909027061` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:6c2e686396cbee52f5ceacfa` `func_149721_r()Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:569822a25a2a222fbc7eb455` `func_149635_D()I` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:dfac9352ff4a323e7750cbcd` `func_149741_i(I)I` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:8469697b71f2d6899a24b1ae` `func_149720_d(Lnet/minecraft/world/IBlockAccess;III)I` access 1，48 code bytes；语义 NOT_ANALYZED
- `method:ff9b3b2ffcf9491c02b257d9` `checkEntityUnder(Lnet/minecraft/entity/Entity;)V` access 1，70 code bytes；语义 NOT_ANALYZED
- `method:a31a7e4a80bb9af89913902c` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，124 code bytes；语义 NOT_ANALYZED
- `method:ca475912509ec1c38460fa94` `<clinit>()V` access 8，17 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 377–379
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 517–521 · 519 morefunquicksandmod:Mucus_Still | 519 morefunquicksandmod:Mucus_Flowing

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|Mucus|0|Mucus|`mfqm:mucus`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
