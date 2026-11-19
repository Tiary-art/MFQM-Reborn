# 原版研究 Phase5：已闭环的限定域与首批实施规格

**总体PARTIAL，但本轮有实质性新增闭环与两个可实施的算法组件规格。** 基线main `c8fa7214525dfecb6b66835a903edd25a19dfe9c`，即用户仓库快照，不要求重新上传ZIP/JAR。原JAR只读hash保持 `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。没有改Forge1.20.1生产逻辑、原JAR或素材，没有候选游戏JAR、没有注册新世界生成。

本轮 62 组原方法体与独立Python栈机的**完整有序事件及最终状态**对照；其中 44 组另有不执行字节码的几何/事务或随机游走 oracle。原始/native和oracle日志完整gzip保存，没有采样裁剪。独立VM不是唯一的算法证明。

## 可以开始实施的两个小组件

1. **Stuck属性租约与Level状态reducer**：原事件体执行8次、123个有序事件与独立状态机一致；现代 UUID remove/addTransientModifier、MULTIPLY_TOTAL 映射和接口明确。只准入这个纯组件；jumpMovementFactor的现代空气控制映射、整体Forge时序、材料碰撞和净Y尚未准入。
2. **DryQuicksand体素事务核心**：原generateSoftSand（SandBlock / DryQuicksand，绝不是SoftQuicksand）有独立VM及几何/有序侵蚀oracle、边界和失败写入用例；旧块身份→现代资源/状态映射、LegacyRandom和顺序写入接口明确。只准入算法核心；不注册Feature，不宣称自然分布或DryQuicksand完整物理完成。

## 与Phase4的实际差异

- 修好Morass类型/对象关系：模拟类型装入**未改指令的原PlantingThis与原func_149721_r**，材料标识恢复原151583_m。复制前后指令/操作数/跳转指纹相同，原JAR不变；不是跳过回调或强制成功。两条旧失败seed10/2132现在均正常结束，父方法仍仅MODEL_TESTED。
- QS与DryQuicksand有正例、概率拒绝、无地面、拒绝写入、边界、组合配置对照。指定Desert/BoP关闭等测试域闭环；**整个25支路全群系闭环仍0/25**，不把有限域验证扩成全部完成。
- 真正执行原stuck事件生命周期；原碰撞材料回调本轮没有执行，Quicksand/Dry/Mud/Mire/Honey的Level关系仍按静态证据分列。
- Tombs完成spawner/chest正常、空Tile和不同World seed垂直切片；独立NBT/库存/随机对照。未再抄8489直接写入，15次父调用链/Chest2/现代NBT仍未闭环。
- WLD执行真正金字塔搜索与lava→Tar/基础支撑路径：正例38格、无邻区拒绝及重叠群系回归；完整原事件流与独立VM一致，另有稀疏几何事务oracle。整个466块方法没有完成。

保留失败：protected环境缺支路、WLD尝试次数在群系门前消费RNG、开放顶砂格先触发World RNG但不抽puddle概率等差异都已记录，失败输入仍在回归。Phase2/3/4回归在隔离副本运行，旧证据不覆盖。**所有真实MC1.7.10客户端/专服/视觉/净下沉统计仍NOT_RUN**。
