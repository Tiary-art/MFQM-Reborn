# Surface25分支逐项验收

原签名`CustomWorldGen#generateSurface(Lnet/minecraft/world/World;Ljava/util/Random;III)V`，25支路来自Phase3原序列。完整表`evidence/results/surface-25-audit.csv`逐行包含群系/配置/高度/半径等原表达式、原字段→注册名映射、callee descriptor/offset、实际trace、block/meta结果、独立验证与阻碍。

下面范围是**按外层配置锚点划分的审查区间**，不是证明每块只属于该分支；跳转/公共准备以原CFG为准。所有未闭环offset均保留在对应区间与Phase2 CFG中。

|分支|外层原条件|锚点offset区间|seed0写调用|另有正例|整支路准入|
|---|---|---|---:|---|---|
|1|`if (MFQM.GenDesertTombs && !blockGen) {`|114..313|0|UNRESOLVED|BLOCKED|
|2|`if (MFQM.GenWastePit && !blockGen) {`|314..652|0|UNRESOLVED|BLOCKED|
|3|`if (MFQM.GenWax && !blockGen) {`|653..807|0|UNRESOLVED|BLOCKED|
|4|`if (MFQM.GenHoney && !blockGen) {`|808..1080|0|UNRESOLVED|BLOCKED|
|5|`if (MFQM.GenSlime) {`|1081..1371|0|UNRESOLVED|BLOCKED|
|6|`if (MFQM.GenWeb && !blockGen) {`|1372..2051|0|UNRESOLVED|BLOCKED|
|7|`if (MFQM.GenLarv && !blockGen) {`|2052..2680|0|UNRESOLVED|BLOCKED|
|8|`if (MFQM.GenSSnow && !blockGen) {`|2681..3055|0|UNRESOLVED|BLOCKED|
|9|`if (MFQM.GenSSand && !blockGen) {`|3056..3450|0|surface-softsand-positive|BLOCKED|
|10|`if (MFQM.GenMucBl && !blockGen) {`|3451..3762|0|UNRESOLVED|BLOCKED|
|11|`if (MFQM.GenQS && !blockGen) {`|3763..4263|0|surface-qs-positive|BLOCKED|
|12|`if (MFQM.GenJQS && !blockGen) {`|4264..4683|0|UNRESOLVED|BLOCKED|
|13|`if (MFQM.GenGP && !blockGen) {`|4684..5062|0|UNRESOLVED|BLOCKED|
|14|`if (MFQM.GenMorass && !blockGen) {`|5063..6516|0|UNRESOLVED|BLOCKED|
|15|`if (MFQM.GenMoor && this.T_BoP && biomeId == MFQM.SwampBiomes[7]) {`|6517..6959|0|UNRESOLVED|BLOCKED|
|16|`if (MFQM.GenTar && !blockGen) {`|6960..7620|0|UNRESOLVED|BLOCKED|
|17|`if (MFQM.GenSQSF && !blockGen) {`|7621..7921|0|UNRESOLVED|BLOCKED|
|18|`if (MFQM.GenSQS && !blockGen) {`|7922..8705|0|UNRESOLVED|BLOCKED|
|19|`if (MFQM.GenMoss) {`|8706..9102|0|UNRESOLVED|BLOCKED|
|20|`if (MFQM.GenBog && !blockGen) {`|9103..9797|0|UNRESOLVED|BLOCKED|
|21|`if (MFQM.GenLiqMire && !blockGen) {`|9798..10387|0|UNRESOLVED|BLOCKED|
|22|`if ((MFQM.GenBClay ∣∣ MFQM.GenHClay) && !blockGen) {`|10388..10970|0|UNRESOLVED|BLOCKED|
|23|`if ((MFQM.GenMire ∣∣ MFQM.GenMud) && !blockGen) {`|10971..12706|0|UNRESOLVED|BLOCKED|
|24|`if (MFQM.GenHClay) {`|12707..13326|0|UNRESOLVED|BLOCKED|
|25|`if (MFQM.GenHPClay) {`|13327..14261|0|UNRESOLVED|BLOCKED|

## 运行内容与边界

25条都在原generateSurface字节码中实际运行，仅启用表中配置，种子0、dimension调用上下文/height62、mock desert biome与沙地；配置/群系/概率拒绝也是真实原分支结果。部分自然概率不会触发，不能将该负例当整条正例通过。涉及BoP/AoA配置默认未安装/关闭，未伪装成外部模组实机。

QS追加seed10 desert正例与empty无地面负例；GenSSand追加seed38 desert正例；它调用generateSoftSand，写原SandBlock（注册DryQuicksand），不能误认成SoftQuicksand。使用原generateMire/generateSoftSand等共用helper指令及真实Random，完整按序RNG/读写/分支/配置/blockGen日志保留。观测到的块/meta只证明该fixture里的结果；不是穷尽全部变体或自然群系分布。

## 逐条关闭条件

每条目前都缺少所有路径/变体/外部环境的独立读写oracle，因此**完整语义闭环0/25、整支路PORT_READY全BLOCKED**。表内给出每条精确锚区间、全部callee位置与源表达式，待关点不是一条空白UNKNOWN。配置门/已执行正负例属于MODEL_TESTED，不冒充SEMANTICALLY_CLOSED。

下一批优先QS与GenSSand（DryQuicksand）的独立helper oracle，然后共享Mire/Mud/Bog/Moor等依赖。保留各材料实际字段，不统一三种profile。Waxes/蜂巢/Web/幼虫/Clay等依然各有独立条件；模板化PlacedFeature不能改原有顺序或假设失败无副作用。
