# Surface全部材料相关生成链

范围来自49对象/字段反查，不预先只选三种。原入口：`MoreFunQuicksandMod.main.CustomWorldGen#generateSurface(Lnet/minecraft/world/World;Ljava/util/Random;III)V`，CFG B0起，完整1054块见Phase2同名CFG。

`surface-all-chains.csv`有26个外层区域，首区是BoP兼容/探测准备，后25区按原代码顺序。每段保留单独第二反编译器源码片段、原配置字段读取offset和所有局部数值/门/循环/退出表达式。配置offset可能在嵌套或其他段重复，不将它冒充该整段唯一的精确边界；指令定位以方法+CFG为准。

|顺序|原始外层条件|配置（含嵌套）|直接产品字段|全部表达式与写序|配置读取offset|
|---|---|---|---|---|---|
|1|`if (MFQM.PBoP`|setup|UNKNOWN/helper-produced|[evidence/source/surface-01.vineflower.txt](evidence/source/surface-01.vineflower.txt)|NONE|
|2|`if (MFQM.GenDesertTombs && !blockGen) {`|GenDesertTombs|UNKNOWN/helper-produced|[evidence/source/surface-02.vineflower.txt](evidence/source/surface-02.vineflower.txt)|114|
|3|`if (MFQM.GenWastePit && !blockGen) {`|GenWastePit|SlurryBlock;TarBlock|[evidence/source/surface-03.vineflower.txt](evidence/source/surface-03.vineflower.txt)|314|
|4|`if (MFQM.GenWax && !blockGen) {`|GenWax|UNKNOWN/helper-produced|[evidence/source/surface-04.vineflower.txt](evidence/source/surface-04.vineflower.txt)|653|
|5|`if (MFQM.GenHoney && !blockGen) {`|GenHoney|UNKNOWN/helper-produced|[evidence/source/surface-05.vineflower.txt](evidence/source/surface-05.vineflower.txt)|808|
|6|`if (MFQM.GenSlime) {`|GenSlime|UNKNOWN/helper-produced|[evidence/source/surface-06.vineflower.txt](evidence/source/surface-06.vineflower.txt)|1081|
|7|`if (MFQM.GenWeb && !blockGen) {`|GenWeb|DenseWebBlock|[evidence/source/surface-07.vineflower.txt](evidence/source/surface-07.vineflower.txt)|1372|
|8|`if (MFQM.GenLarv && !blockGen) {`|GenLarv|LarvaeBlock|[evidence/source/surface-08.vineflower.txt](evidence/source/surface-08.vineflower.txt)|2052|
|9|`if (MFQM.GenSSnow && !blockGen) {`|GenSSnow|UNKNOWN/helper-produced|[evidence/source/surface-09.vineflower.txt](evidence/source/surface-09.vineflower.txt)|2681|
|10|`if (MFQM.GenSSand && !blockGen) {`|GenSSand|UNKNOWN/helper-produced|[evidence/source/surface-10.vineflower.txt](evidence/source/surface-10.vineflower.txt)|3056|
|11|`if (MFQM.GenMucBl && !blockGen) {`|GenMucBl|UNKNOWN/helper-produced|[evidence/source/surface-11.vineflower.txt](evidence/source/surface-11.vineflower.txt)|3451|
|12|`if (MFQM.GenQS && !blockGen) {`|GenQS|QuicksandBlock|[evidence/source/surface-12.vineflower.txt](evidence/source/surface-12.vineflower.txt)|3763|
|13|`if (MFQM.GenJQS && !blockGen) {`|GenJQS|JungleQuicksandBlock|[evidence/source/surface-13.vineflower.txt](evidence/source/surface-13.vineflower.txt)|4264|
|14|`if (MFQM.GenGP && !blockGen) {`|GenGP|SoftGravelBlock|[evidence/source/surface-14.vineflower.txt](evidence/source/surface-14.vineflower.txt)|4684|
|15|`if (MFQM.GenMorass && !blockGen) {`|GenMorass|MorassBlock|[evidence/source/surface-15.vineflower.txt](evidence/source/surface-15.vineflower.txt)|5063|
|16|`if (MFQM.GenMoor && this.T_BoP && biomeId == MFQM.SwampBiomes[7]) {`|GenMoor|MorassBlock;MudBlock|[evidence/source/surface-16.vineflower.txt](evidence/source/surface-16.vineflower.txt)|6517|
|17|`if (MFQM.GenTar && !blockGen) {`|GenTar|TarBlock|[evidence/source/surface-17.vineflower.txt](evidence/source/surface-17.vineflower.txt)|6960|
|18|`if (MFQM.GenSQSF && !blockGen) {`|GenSQSF|SoftQuicksandBlock|[evidence/source/surface-18.vineflower.txt](evidence/source/surface-18.vineflower.txt)|7621|
|19|`if (MFQM.GenSQS && !blockGen) {`|GenSQS|SoftQuicksandBlock|[evidence/source/surface-19.vineflower.txt](evidence/source/surface-19.vineflower.txt)|7922|
|20|`if (MFQM.GenMoss) {`|GenMoss|UNKNOWN/helper-produced|[evidence/source/surface-20.vineflower.txt](evidence/source/surface-20.vineflower.txt)|8706|
|21|`if (MFQM.GenBog && !blockGen) {`|GenBog|BogBlock|[evidence/source/surface-21.vineflower.txt](evidence/source/surface-21.vineflower.txt)|9103|
|22|`if (MFQM.GenLiqMire && !blockGen) {`|GenLiqMire|UNKNOWN/helper-produced|[evidence/source/surface-22.vineflower.txt](evidence/source/surface-22.vineflower.txt)|9798|
|23|`if ((MFQM.GenBClay ∣∣ MFQM.GenHClay) && !blockGen) {`|GenBClay;GenHClay;GenMClay|BrownClayBlock|[evidence/source/surface-23.vineflower.txt](evidence/source/surface-23.vineflower.txt)|10388;10394;10455;10506;10556;12707|
|24|`if ((MFQM.GenMire ∣∣ MFQM.GenMud) && !blockGen) {`|GenMire;GenMud|MireBlock|[evidence/source/surface-24.vineflower.txt](evidence/source/surface-24.vineflower.txt)|10971;10977;11304;11310;11472;11521;11873;11918;12084;12090;12329;12335;12357;12426;12462;12474;12496;12544|
|25|`if (MFQM.GenHClay) {`|GenHClay|UNKNOWN/helper-produced|[evidence/source/surface-25.vineflower.txt](evidence/source/surface-25.vineflower.txt)|10394;10556;12707|
|26|`if (MFQM.GenHPClay) {`|GenHPClay;GenSClay|UNKNOWN/helper-produced|[evidence/source/surface-26.vineflower.txt](evidence/source/surface-26.vineflower.txt)|13327;13780|

## 精度与不可省略部分

dHeight=height-62，wordSizer=height/62f。height配置默认62不是高度偏移。Surface顺序包含墓室、废坑、蜡树、蜂巢、黏液、网、幼虫、软雪/软沙、植物、QS/JQS、砾石、Morass/Moor、Tar、SQS族、Moss、Bog、LiquidMire、Clay组、Mire/Mud与末尾硬黏土分支。这里名称只是导航；真正生成物ID/metadata及辅助算法按主矩阵字段与子调用追踪。未在片段直接出现产品字段的链仍标UNKNOWN/helper-produced，不能据名填块ID。

前序失败仍可留下写入；blockGen不等于成功放置数。Slime/Moss等不统一受!blockGen约束；某些门前已经采样count/radius。完整条件、Y、概率、数量、半径、短路都在每段表达式中原样保留，**尚未全部转成已证明等价的语义规格**。没有为未解参数补现代默认值。

可证实的局部事实继承Phase2：Tombs浮点门nextFloat()*750>749；一次扫描70+d下到>60+d后构建Y-8-nextInt9，返回值不阻止blockGen=true。Wax/Honey成功终止、Slime独立门/高度拒绝、Clay/Mud嵌套都有各自条件。完整偏移/RNG调用查Phase2 rng-call-sites/write-and-subgenerator-sites；本批MODEL_TRACE只执行Gardencia和墓室直线指令，不执行Surface，所有Surface运行均NOT_RUN。

尚未闭环1054/1054块，逐块列five-method-block-status.csv。下一步应先按产品字段把外层链拆为实际材料子链，用读/写/RNG差分记录失败副作用；不能把“25段全部列到”宣称“25段算法已完成”。
