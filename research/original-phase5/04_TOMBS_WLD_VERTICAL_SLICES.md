# 结构最小垂直切片

## Tombs

真实原`GenerateDesertTombs#generateSpawner(World,III)V`与`generateChest(World,IIII)V`已执行。spawner/chest各seed0/4096/-1和空Tile共8例；World随机种子等于case seed。原方法、分支、读取、NBT/库存/metadata与最终状态全部和独立Python栈机比较。

spawner正常：原@10置spawner0 flags2，@19查Tile，@45导出NBT，再写SpawnRange32/SpawnCount1、World nextInt2选Skeleton/Zombie、Min400/Max1600/MaxNearby3并导入。空Tile保留原stderr并正常返回，不伪造实体。合同初始NBT为空；真实Tile额外字段、现代SpawnData结构未纳入。

chest：固定ChestGenHooks返回一条fixture_token权重2，其后17条原字面loot仍由原方法构造；27槽，抽取量均可装为一堆。native逐项减权重实现与独立CDF查找对照，连nextInt1也消费；slot覆盖不合并。LOOT_TABLE/World RNG/INVENTORY_SET和最终slots均有日志。不是声称真实模组默认loot table或真实Vanilla WeightedRandom API已完整运行。

这是两个helper种类的有限域切片，不把6 spawner+9 chest的全部父调用次序减成“只剩13次”；15处父调用的交错RNG/最终完整结构仍未验证。Chest2表不同，本轮未闭环；8489直接写入保留不重抄。现代NBT版本转换仍BLOCKED。

## WLD实际结构路径

真实`CustomWorldGen#generateWLD(World,Random,II)V`执行。不是Surface替代。稀疏Chunk/World合同：仅首邻区存在；角点(-64,63,-48)为lava，底部探测候选(-69,63,-47)为sand，下两格stone，其它未写位置AIR；seed0，Desert-only WLDBiomes映射。没有隐式加载其它区块。

原搜索找到lava/底部后执行原截面改写：Tar2格及四向各9砂岩支撑，共38次/38格，跨3个区块。全有序事件和独立VM一致，另由稀疏几何事务规则独立预测RNG与38次写入及最终状态。无邻区拒绝和重叠ID回归也保留。

本轮查明两个易漏语义：Ashes后备支路在判断群系前已抽尝试次数；单一Desert即使不走Ashes也会消费该nextInt5。开放顶砂点先调用isAboveFreeSpace（World RNG），其否定条件不成立就**不抽**puddle概率。早期CFR未结构化片段不可当完整算法，修正有原CF/第二反编译器证据，失败oracle输入未删。

这个合同是globally sparse voxel存储+邻区存在接口，不等价真实Chunk加载、光照、邻更。只关闭该稀疏路径/输入域；整个466块WLD和完整金字塔仍BLOCKED。
