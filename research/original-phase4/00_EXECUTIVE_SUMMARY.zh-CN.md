# Phase 4：原指令执行、局部闭环与准入

**总体PARTIAL；没有完成全量移植或本轮全部验收。** 本轮从Phase3的跳过helper模型推进到读取原始class并在Java17执行实际方法体；内存插入日志，原JAR文件只读。所有环境是声明的mock，绝非Minecraft1.7.10实机。

基线main `37d18a17a1d6cdc679c4b8182c8621df97024c57` 已合并Phase1–3。原JAR SHA-256前后保持 `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。没有修改旧报告、Forge1.20.1代码、原素材，没有候选游戏JAR，没有启动004/005。

## 本轮真正推进

- Gardencia实际指令模型覆盖**99/100基本块**；Phase3未覆盖10块逐块解释。剩余B694有局部循环界证明：最多10次增量，无法通过countBlock>10；不伪造执行该块。
- **GenMud片段B0..190的14个块在明确API合同下局部闭环**：14组独立手工控制流实现与JVM执行的完整有序事件（含分支/helper/config/RNG/读写）及最终方块状态一致。包括开关关闭、无水、混合支撑、拒绝写入、不同seed及负坐标。这个结论有范围限制，不是Gardencia全方法闭环。
- MireO、MireOD、LiquidMire、Morass、Water及相关检测helper执行的是原方法体；Java JVM承担int/long、类型/返回/异常语义，不再跳过这些helper。仍有2条Morass模型在PlantingThis类型边界失败，完整错误/写入前缀保留。
- 共65组模型：62组正常结束，1组预期非法bound异常，2组未解环境异常。**不把65组称作全部通过**。
- Surface25分支逐条有验收行、原条件/参数/offset、依赖与实际seed0轨迹；QS和GenSSand（SandBlock / DryQuicksand，不是SoftQuicksand）另有放置正例，QS无地面负例。**完整分支闭环0/25**，全部整支路准入仍BLOCKED。
- 剩余10个碰撞入口追到Vanilla父链的Block方法offset0 return；明确Forge补丁/外部事件未闭环，不宣称这些对象没有玩法。
- 112组受困数学核数值向量、247个原始资源路径/hash的现代目标提案和私有导入工具。Phase3回归、官方840项Java RNG对照保持通过。

## 现在可以移植什么

该片段仅属于原`world.dimension==MFQM.AOADimGardencia`路由内的Y60..66水底泥层变换，**不能当成主世界通用泥浆生成规则**；现代AoA/Gardencia维度映射未明确前不能挂载自然生成。可作为首批实现依据的是**GenMud局部算法控制流与纯水/固体检测接口**，前提是现代适配保持已声明API/材料语义、调用顺序和RNG边界；不是整套自然分布已验收。受困数值公式可按证据编写接口，但完整事件/材料物理族尚未准入。资源仅提供路径映射与私有导入方案，不能据此公开分发旧图。

## 仍不可以声称什么

Gardencia完整方法、Surface25完整支路、所有物理族、Tombs完整结构和WLD结构都没有整体PORT_READY。Tombs15 helper本轮未执行，WLD端到端结构本轮未完成；其旧证据未丢失，精确缺口见03/07。原版客户端/专服/净速度/视觉/生成分布**全部NOT_RUN**。研究交付后停止，等待验收。
