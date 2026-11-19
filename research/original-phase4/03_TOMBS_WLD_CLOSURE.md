# Tombs与WLD：本轮未完成部分

**P1未完成，UNRESOLVED。** 本轮将资源优先投入Gardencia真实helper与独立对照；没有再抄8489条已比对直接写入。

`tombs-15-helper-audit.csv`逐一列原调用方法签名/offset/目标helper。全部15次（6刷怪笼、9宝箱）内部本轮NOT_RUN；仍缺NBT、TileEntity、ChestGenHooks与WeightedRandom的忠实mock及独立抽奖/写序oracle。原GenerateDesertTombs#generateSpawner、generateChest/2完整字节码/源片段沿用Phase2。

原六段连续func_76484_a→generate2→3→4→5→6、相对坐标/固定metadata以及跨区块布局沿用Phase3已核验8489直接写入。没有输入旋转参数不等于每种方块metadata可直接转成现代facing；宝箱/刷怪笼附加写入/保护/失败仍可能影响最终世界。不能称最终完整结构一致。

WLD `CustomWorldGen#generateWLD(Lnet/minecraft/world/World;Ljava/util/Random;II)V` 的466块保留Phase2 CFG和Phase3缺口，本轮没有完成所要求的结构路径端到端模型。原±3区块金字塔搜索、底部探测、截面重写/刷怪笼随机替换都是未解依赖，不用本轮QS普通地形模型冒充WLD结构通过。

下一最小P1任务：先一个Tombs spawner helper的NBT/World RNG/TileEntity空值与正常值对照，再ChestGenHooks固定表；WLD先定义邻区存在/Chunk storage合同后关闭一个真实结构分支。当前两项均BLOCKED。
