# MoreFunQuicksandMod/main/liquids/BlockStableLiquidMire

ID `class:e76147666c8d269b4605bf0d`；class SHA `f9ba42487b21ee9ad7ee2fffc45ffc4a0eec7d7a6a0471917d110d9be70cee66`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `net/minecraftforge/fluids/BlockFluidClassic`；interfaces ``；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/liquids/BlockStableLiquidMire`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__liquids__BlockStableLiquidMire.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `stable_liquid_mire`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:3fb400e39e6b95a4a52d8e6c` `theMireIIcon:[Lnet/minecraft/util/IIcon;` access 1
- `field:84c7e4e06eb2975e7586adf0` `maxOpacity:I` access 2
- `field:035b78adc514f6260bafd209` `lastOpacity:I` access 2
- `field:98069b207838b77c18b07ee5` `incOpacity:I` access 2

## 方法目录

- `method:e4908a5b2faa8cd034508912` `<init>(III)V` access 1，82 code bytes；语义 NOT_ANALYZED
- `method:c4967512cdcb835d028540b8` `func_149674_a(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，455 code bytes；语义 NOT_ANALYZED
- `method:3bb8de4bb8c7af41def1f24b` `func_149640_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;Lnet/minecraft/util/Vec3;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:bc37eb03ba5b26817bcdcac3` `drain(Lnet/minecraft/world/World;IIIZ)Lnet/minecraftforge/fluids/FluidStack;` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:20462a2a1320498244f30b42` `canDrain(Lnet/minecraft/world/World;III)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:000c480b5928184629e3fc16` `func_149670_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V` access 1，1423 code bytes；语义 NOT_ANALYZED
- `method:c0110b26bd073c140eea6daa` `func_149734_b(Lnet/minecraft/world/World;IIILjava/util/Random;)V` access 1，91 code bytes；语义 NOT_ANALYZED
- `method:cbd182d341b6a822825adabf` `func_149691_a(II)Lnet/minecraft/util/IIcon;` access 1，25 code bytes；语义 NOT_ANALYZED
- `method:53055f69b24411859412ae74` `canDisplace(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:32c590ae890f8b5934cbb1c2` `displaceIfPossible(Lnet/minecraft/world/World;III)Z` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:285156371ea31374ce8c2096` `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` access 1，43 code bytes；语义 NOT_ANALYZED
- `method:b0f79e1fae5a35e2ce080f10` `func_149727_a(Lnet/minecraft/world/World;IIILnet/minecraft/entity/player/EntityPlayer;IFFF)Z` access 1，167 code bytes；语义 NOT_ANALYZED
- `method:257e5ccbe9f3a5889d5dbe39` `func_149678_a(IZ)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:7ed8efad557b724042dfac02` `findItem(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/item/Item;I)I` access 1，74 code bytes；语义 NOT_ANALYZED
- `method:1fd20a082f15a3aa9eb82745` `func_149737_a(Lnet/minecraft/entity/player/EntityPlayer;Lnet/minecraft/world/World;III)F` access 1，4 code bytes；语义 NOT_ANALYZED
- `method:3ddc605e16cec7ade2c85b94` `checkPlayerMuddy(Lnet/minecraft/entity/player/EntityPlayer;IIILnet/minecraft/world/World;)V` access 1，124 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## R1 注册与显示证据

- `func_149691_a(II)Lnet/minecraft/util/IIcon;` · CFR 343–345
- `func_149651_a(Lnet/minecraft/client/renderer/texture/IIconRegister;)V` · CFR 362–366 · 364 morefunquicksandmod:Mire_Still | 364 morefunquicksandmod:Mire_Flowing

|旧对象|damage|旧名称候选|现代物品|
|---|---:|---|---|
|LiquidMire1|0|Liquid Mire|`mfqm:stable_liquid_mire`|

上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。
