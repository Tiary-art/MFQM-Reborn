# 1.20.1 Forge 适配规格（提案，未实施/未编译验证）

现代源码基线88b9ad1；worldgen目前只有包占位，不能把49方块注册视作生成完成。原版参数只取02/03与指令证据；本文件新增设计一律是 **PROPOSED_MODERN_ADAPTATION**。

|原版链|候选机制|语义差异与需决定事项|验收|
|---|---|---|---|
|Surface/Custom/Nether内有序地形斑块|一个编排Feature封装各旧算法，ConfiguredFeature参数化，PlacedFeature控制入口，Forge biome modifier挂载|独立PlacedFeature会打乱blockGen/共享RNG与失败副作用；先保持编排顺序，再决定是否拆分|相同mock地形+相同随机序列的写入/调用轨迹差分；实际世界只比较统计|
|Mire/MireD/MireOD等形状|Feature内确定性体素算法，使用RandomSource适配|nextInt1保留；Java Random与新版RNG不可默认序列一致；先允许显式legacy RNG策略|半径/深度/支撑/空洞边界fixture；失败前后写入差分|
|CustomWorldGenLakes|自定义Feature，不直接套现代LakeFeature|双写Y-1、壳验证、mode1衬层/结冰、原版材料分类和meta语义不同|16×16×8mask及实际写入范围、液体泄漏拒绝、边界位移|
|Tombs连续大结构|Structure+StructurePiece或模板化pieces，宝箱LootTable/刷怪笼BE|旧入口概率浮点门、跨区块一次直写、初始化顺序与piece按区块写不同；还未整理完整蓝图不能开始实现|结构锚点/每piece边界/metadata映射/宝箱刷怪笼数据；多区块重复生成与保存重载|
|MucusBlossom首次生成|Feature；生态再生另用block randomTick|checkCanGrow的force/dirt和调用偏移要保留；不可只做初次Feature|初生、破坏、邻接、强制放置、随机刻再生分别验收|
|Populate Post替换TNT/BoP/TBL|兼容模组专用Feature或安全区块后处理队列，待调度验证|没有可直接宣称等价的同名现代事件；禁止在异步生成中随意加载3×3/5×5邻区、直改section漏光照/高度图/脏标记|原邻区可用性重放；区块不额外加载；状态/光照/保存一致|
|TF/WLD/ABC/AOA维度与整数群系数组|ResourceKey/Tag可配置路由，软依赖检测|旧mod不存在时不能仅照抄整数ID；需要明确用户选择的现代对应模组；缺失依赖不生成、不崩溃|依赖存在/不存在/群系tag为空/维度冲突|
|MFQM.LiqFixer全局标记|显式局部GenerationContext，作用域finally清理|不能保留跨线程共享boolean；哪些流体更新抑制必须先追踪消费者|并发区块生成、异常回滚后无标记泄漏|

旧meta须逐块映射为BlockState属性，Mud3/Mire12等不能被统一默认状态吞掉。物品掉落、碰撞、液体source判定必须在材料规格闭环后决定。全局高度不应机械把旧62改成新版海平面：先提供legacy高度策略，再以现代地形高度作为用户可选适配。两种均不能伪装旧事实。

## 保真与统计验收门

第一层是纯算法：mock-world记录每次RNG调用类型/界限/顺序、读取坐标、写入块/状态/flags、提前退出；不要求运行Minecraft即可检查局部语义，但本批尚未实现该harness。

第二层是1.7.10参考实测：08中固定种子和坐标，分维度/群系/配置统计尝试、门通过、地面拒绝、成功斑块及部分写入。第三层是现代同类地形分层样本；不要求跨版本逐方块地形一致。报告每组样本量、按群系/高度分层的密度、连通面积/深度/失败率、置信区间和原始分布。

验收容差尚未指定：须先获得原版基线和误差/多次运行方差，再写入后续任务书。不能现在编造“相差5%即可”冒充历史要求。任务书授权的船兼容性增强与旧世界生成保真分开验收。
