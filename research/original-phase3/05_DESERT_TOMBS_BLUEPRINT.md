# 墓室连续拼装蓝图（直接写入已差分）

原类`MoreFunQuicksandMod.main.GenerateDesertTombs`；六方法共同签名`(Lnet/minecraft/world/World;Ljava/util/Random;III)Z`。func_76484_a→generate2→generate3→generate4→generate5→generate6顺序执行，非六选一。

`evidence/indexes/tombs-direct-write-blueprint.csv`逐条记录类/方法、调用offset、相对XYZ、原字段/metadata、flags和坐标0锚点下区块号。原方法指令在trace-methods.json及Phase2同名CFG。直线方法中每次literal坐标加法/取字段/setBlock调用由受限解释器执行，未手写8489条坐标。

|段|直接写数|XYZ相对范围|metadata字面值|
|---|---:|---|---|
|`func_76484_a`|1490|[[0, 15], [4, 14], [7, 22]]|[0, 1, 2, 9]|
|`generate2`|1500|[[15, 22], [1, 16], [1, 27]]|[0, 1, 2]|
|`generate3`|1499|[[22, 28], [0, 19], [1, 27]]|[0, 1, 2]|
|`generate4`|1500|[[28, 34], [0, 19], [1, 27]]|[0, 1, 2]|
|`generate5`|1498|[[34, 44], [4, 14], [3, 25]]|[0, 1, 2]|
|`generate6`|1002|[[16, 47], [1, 18], [2, 26]]|[0, 1, 2]|

共8489次直接写入，8489个不同坐标；**必须按序保留覆盖**，不能仅当无序体素集合。所有坐标相对输入锚点。跨chunk区间由floor division计算，负坐标不能使用向0截断。origin(-16,40,0)示例trace与origin0蓝图分开，不能混合两者坐标。

独立CFR文本字面解析器逐项对比全部8489次坐标、块、metadata及顺序，完全相同（MODEL_TESTED）。它是独立提取路线的差分，不是两个反编译器输出相似就宣称证明整个Minecraft行为。

这六段没有输入旋转参数/旋转变换：以固定literal偏移和metadata摆放。metadata不自动等于现代facing，不能根据整数2/3/9统一旋转；各原方块映射尚待对应Vanilla/Forge状态语义核对。

## 不包含的内容

有15次宝箱/刷怪笼helper调用只记录位置、原方法及参数，内部没有执行；trace中的RNG计数0只指这六个直线调用体，不代表完整墓室生成无随机数。TileEntity写入、loot、额外block写入和世界更新尚未合并，故这不是最终完整结构存档。

Phase2源/字节码保留generateSpawner、generateChest/2。刷怪笼可见SpawnRange32、Count1、MinDelay400/Max1600/MaxNearby3及Skeleton/Zombie随机；宝箱混合ChestGenHooks和权重物品。继续逐helper核对World RNG顺序和下游写入，不能凭直接蓝图宣称完整结构已可移植。
