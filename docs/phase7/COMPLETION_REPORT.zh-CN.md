# Phase7 完成报告

**总体 PARTIAL。** 基于已合并 Phase6 的 main9eda883，完成默认关闭的服务端属性适配、受控 Dry 世界端口与测试命令；未声称原版完整物理/自然世界生成恢复。自动材料→Level生产者仍BLOCKED；跳跃空气控制与真实玩家客户端验证尚未完成。任务在本轮范围停止，不继续全面接入。

## 逐项状态

| 项目 | 状态 | 交付与限制 |
|---|---|---|
| 集成前审计 | PASS / 有显式阻塞 | INTEGRATION_AUDIT 调用时序、旧XY与旧UUID互斥、49材料来源矩阵；跨材料原始碰撞顺序和生产者不猜测 |
| 保持Phase6纯组件 | PASS | legacy目录算法不变，全部45 JUnit含112数学向量继续通过 |
| Stuck服务端属性适配 | PARTIAL | integration/StuckAdapter，固定UUID、MULTIPLY_TOTAL、transient、服务端写入、默认关闭、生命周期清理；测试输入可运行；无自动材料生产者 |
| 生命周期验证 | PARTIAL | 真实服务端属性与END更新、Player handler fixtures通过的运行记录；实际联网重生/重登/维度/任意传送未完成；短延时释放失败保留 |
| 旧水平减速互斥 | PASS（受控域） | SinkEngine仅managed时保留输入XY/移除旧UUID；MotionRuntime客户端仅收到新UUID后旁路旧XY；网络过渡未测 |
| Dry真实世界端口 | PARTIAL / 限定切片通过 | integration/DryWorldAdapter，seed0 extent5，401事件、12现代同状态false差异、56最终写入格一致；guard/AIR测试；跨区块与完整现代副作用未测 |
| 自然生成 | 未实现、禁止默认开启 | 无Feature/PlacedFeature/BiomeModifier；完整Surface0/25 |
| B1/B2回归 | PARTIAL | 基线29既有GameTests通过；候选含既有测试，45JUnit；40tick配对猪Y数据一致、无双UUID帧；连接客户端高速/纠正/音效未测 |
| 专服 | PASS（启动/停止冒烟） | localhost25579，正常控制台stop与全维度存盘；未测真实客户端连接 |
| 原JAR/素材 | PASS | JAR hash不变；无资源改动/旧素材公开上传/AI贴图 |

## 源码范围

新增 `forge-1.20.1/src/main/java/art/tiary/mfqm/integration/{StuckAdapter,DryWorldAdapter,Phase7Commands}.java` 和 `gametest/Phase7GameTests.java`。修改 SinkConfig（3个默认false开关）、SinkEngine（只对managed租约互斥旧XY/UUID）、MotionRuntime（客户端已同步UUID时互斥旧XY）、SinkCapability.invalidate（清理新租约）、build.gradle（GameTest向量路径/独立工作目录）。没有改 MotionMath/SinkMath、网络、客户端FOV/预测类或资源。

测试/日志见 TEST_MATRIX、logs、evidence、RESULTS.json；最终是否通过必须查实际GameTest pass marker，不能只看Gradle退出成功。首轮31断言通过后保存卡住，另一次锁文件启动失败以及新增测试释放时序失败均保留，未删除失败样本。旧Task003资源审计在本基线也失败（SoftQuicksand filled模型假设过时）；不调整旧期望来掩盖。

## 下一阶段物理证据优先级（研究衔接，不实施）

先关闭 Quicksand 原callback的kof1/kof1m坐标约定、isTrulySink门、分支/RNG和setStuck调用顺序，再单独准入生产者；Dry需跟踪mtdkof20f的1.5幂/cap128；Mud需metadata/早退，Mire需特殊255，Honey需深区50，不能统一单调曲线。参考Phase5 material-level-callbacks.csv与Phase3原完整callback签名/偏移。Stuck只是行动限制，不能代替浮力、净Y、随机吸力、挣扎和材料特例。

本轮不用近似深度→Level绕过证据闸门，也不把旧jumpMovementFactor映射为motionY。原版1.7.10实机仍NOT_RUN。实验开关默认false；按用户指南在备份的一次性世界验收后，下一轮接入需另行授权。

最终运行：35项GameTest及45项JUnit通过，正常停服。需注意：曾失败的2-fixture-tick释放检查改为3-tick有界观察后通过，**严格一世界tick释放时序的差异根因尚未定位**。这不是修复了原版全局时序，仍列PARTIAL；原失败日志未删除。下一步最小验证为追踪实体加入实体管理器、GameTest回调tick和Level END的相对时序。

补充最终证据：最新 `timing-diagnostic-run.log` 为36项GameTest全部通过并正常退出，45项JUnit通过。新增已注册实体测试与详细日志显示：2tick hold在697/698消费，699释放；另一个已注册实体在707获得租约、708释放、709确认无状态。之前还出现一次hold早期快照失败，保留在registered-timing-verification.log。最后一次通过不抹去间歇失败；这部分 fixture/全局时序仍不标完整PASS。`RESULTS.json`及日志解析脚本以最新36项实际marker为准。
