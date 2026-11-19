# Phase8 完成报告

**总体 PARTIAL；已达到普通流沙“非玩家 Contact 子链”的真实碰撞自动接入门槛。** 未宣称玩家、全部材料、完整碰撞物理或自然生成恢复。基线为已合并Phase7的main b1461ba。

## 结果分项

| 项目 | 状态 | 实际交付/边界 |
|---|---|---|
| QS原版Contact输出证据 | CONFIRMED限定域 | 原callback/setter偏移、72边界向量、原isTrulySink九指令复制指纹/4组合执行；不是完整native callback实测 |
| QS真实自动碰撞 | PASS限定域 | SinkingBlock.entityInside→OriginalContactBridge→有序Contact→StuckAdapter；自然猪回调85→88，无手动注入；非玩家、有限体积、纯QS接触域 |
| 玩家自动化 | BLOCKED | 原client-side isTrulySink及posY/yOffset/pose映射未闭环，不拿现代脚底或三profile猜测 |
| Dry/Mud/其他生产者 | PARTIAL/BLOCKED | 49行矩阵；Dry metadata整除/ABC系数、Mud metadata0早退等单列；保持旧行为 |
| 后写覆盖/互斥 | PASS限定域 | 不排序/去重/max；保留mr→145两次请求；未知混合材料拒绝自动租约；沿用Phase7旧UUID/XY互斥，未改Y/网络 |
| A2释放缺陷 | PASS复现路径；历史归因有界 | 基线可见性缺口确定失败，候选按跟踪状态结算；恢复2fixture-tick观测并检查实际N+1 END释放记录；另定位测试文件watcher干扰，不把3tick当1tick |
| shape关服安全 | PASS限定路径 | FILLED状态/传入邻居替代光照线程的世界读取；禁止所有World读取的worker测试通过，候选正常退出/世界锁另检 |
| 一键关闭 | PASS自动测试 | 真实Brigadier disable命令、只清自己UUID、外部UUID保留；stop latch阻止旧配置重载重新打开；重启才可重新启用 |
| 实际客户端 | PARTIAL | 两实际客户端同时在线；属性/FOV、模式、死亡重生、活动租约退出重登、服务端传送清理有记录；不是假玩家替代，也不是玩家自动化 |
| Dry世界回归 | PASS样本/整体PARTIAL |401原样本/12同状态false差异保留；443事件跨4区块；flags3实际产生1下落沙实体，和纯事件分开；非完整副作用证明 |
| 原B1/B2 | PASS自动回归、人工PARTIAL | JUnit及既有GameTests保留；实际客户端trial/计数有记录，未做Phase7二进制真人输入A/B；无原Y公式重写 |
| 完整Surface/遗迹/素材 | 未实施 |25分支仍0/25；无Feature/自然生成/旧存档迁移/原素材分发/AI贴图 |

## 测试与失败保留

基线：45JUnit与36既有GameTests运行；另加入最小可见性失败输入，基线在worldTick280仍停留updated278/Level0，失败日志保留。首轮候选39项通过，扩展42项通过；加入回退后43项曾出现2项失败。诊断确认回退fixture设置true后读取enabled=false（实体存活且非豁免），隔离测试用配置文件watcher后43项通过；后续干净构建再验证。最终结果以TEST_RESULTS、RESULTS.json和原始日志的实际计数/退出/世界锁为准，不仅看Gradle成功。

保留失败输入、原日志与baseline复现Java。两类问题分别处理：缺失可见实体更新是运行时遗漏；快速set配置与磁盘监听重载干扰是GameTest fixture问题，隔离只在测试服，正式服watcher未被全局关闭。额外stop latch保证正式回退不可被旧缓存重新开启。未通过更改期望数值、删样本或延长到3tick掩盖。

真实客户端共4份有限捕获，分别3600/2209/3600/2709 client ticks，其中session2有643个lease=true帧。客户端观测的药水+外部UUID速度0.154，带租约0.005695266381302885，释放后恢复；活动租约创造模式、死亡、退出及重登均有记录。FOV确实变化，没有全局关闭原版药水FOV。客户端人工走动/挣扎、视角舒适性和听觉判断未运行；部分后续维度操作超出采样预算，标为仅服务端观察。最终新增stop latch/测试隔离后没有再重跑联网客户端；最终树由构建与GameTest覆盖。

## 源码与复现

新增 legacy/QuicksandContacts、integration/OriginalContactBridge、Phase8GameTests/Phase8TestIsolation、只读开发启动客户端追踪器及72向量。修改SinkingBlock的受控回调、CoreSinkingBlock的状态形状查询、StuckAdapter跟踪结算/可观测记录/回退、开关与受控命令、GameTest时序断言及开发运行参数。Phase6的StuckLease、DryQuicksandCore等原纯核心不变；SinkEngine/MotionRuntime/MotionMath/SinkMath、既有网络代码未改。

从仓库根目录：`bash docs/phase8/tools/reproduce.sh`（JDK17、依赖缓存；首次可去掉--offline）；`python -B docs/phase8/tools/contact_vectors.py`确定性生成静态向量；`summarize_observations.py`重算真实记录统计；`verify_results.py`核对计数/退出/锁/不变文件。原helper重新执行需私有原JAR与run_helper_probe.py；JAR没有改动且不随工程分发。详细命令、种子、JUnit XML、原始日志和轨迹均在本目录。

产物由项目现有候选版本名生成，不能仅凭旧文件名判断阶段；请以ARTIFACTS.json的SHA256和本PR提交为准。打包JAR是构建产物，服务端/客户端验证主要使用Forge开发运行类路径，不声称已在任意整合包测试。完成后停止，不开始下一轮全材料/全面世界生成。
