# MFQM Reborn 003.5-B2 候选交付报告

2026-11-18（北京时间）。从已合并B1的main `c399b3b`开发；独立分支 `task/0035-b2-consolidated`，不直接修改main、不自动合并，不开展Task004/005。

本次交付可构建候选，不是“49种旧玩法已全部复刻”。硬注册目标已覆盖：**49个可证实旧Block**（另1开发块），**13组真实Forge FluidType/source/flowing/bucket**。实现矩阵保守标记 **44 PARTIAL、5 REGISTERED_ONLY、0 COMPLETE**。特别是Gas及Larvae/Lure/Blossom/MeatWall依赖没有被写成完成。

已交付：

- 按旧注册证据逐项映射稳定ID，增加ItemBlock/创造分类/模型/中英名称/loot；植物、薄层、固体、黏稠材料、Slab、睡莲、砂岩陷阱等分类行为；13液体接入同一SinkingMedium接触框架。
- 将持续下沉上限.055降至.012，分离基础速度、深度、移动/挣扎和短入池阻尼；新motionV2配置避免旧世界保留快速B1默认。保留高速入口扫掠与有条件着陆处理。数值是现代提案，不假装原版曲线。
- SS叠层轮廓/模型、两沙条件随机下移（Mud不重力下落）、内部合法射线起点处理、仅抵消MFQM速度FOV分量。
- 单独船体浮力，普通船与箱船共用，保留原版划桨/转向/水平阻力，不把三核心伪装成水，不给骑手套旧陷落纠正。
- 原生airSupply/UI、服务端单结算防双耗、相机遮挡、动作SoundEvent合法fallback、动作泥泡、服务端持久/同步脏污、独立人物/标准盔甲/第一人称手臂可视层、水雨清洗。

验证：**23/23 JUnit、29/29 GameTest、最终build通过**。运行过真实专服及Dev/Observer两个真实客户端（同时SS/Mud）、位置/状态CSV、水肺和原生气泡UI、相机遮挡、人物/手臂/铁胸甲可视层、SS载人船输入。单人集成服务器加载/创造栏/桶显示/保存冒烟完成。所有未运行项目见[回归矩阵](MECHANICS_REGRESSION_MATRIX.md)，不将编译或模型存在当作玩法通过。真实GUI测试代码53ad311；末次免疫角色清洗修正由新增GameTest覆盖，未重跑完整GUI。

交付文件：仓库 `deliverables/task-0035-b2/mfqm-reborn-0.0.3.5-b2-candidate.jar` 与SHA256SUMS；本目录完整报告、矩阵、`evidence/logs`（包括失败轮）、`evidence/junit`、`evidence/traces`、`evidence/trace-summary.csv`。另提供完整Git工程源码ZIP和报告日志ZIP。候选JAR SHA-256：`beef245fd6f642fe2510548a9f1ec668eafa6bde28757dedaa853d44d8c22355`。

没有AI美术，没有修改原始JAR，没有新增旧PNG/OGG公开素材。原始JAR再次验算SHA-256与初始一致，见[资源授权报告](RESOURCE_AND_LICENSE_REPORT.md)。13流体和桶的原版水纹/桶图标属于明确占位，不代表旧美术完成。

复现：Java17进入forge-1.20.1，运行 `./gradlew --no-daemon test runGameTestServer build`，资源检查 `python3 tools/audit_b2_resources.py`。实际客户端 `./gradlew runClient`，第二客户端 `./gradlew runObserver`，专服 `./gradlew runServer`；专服EULA由使用者自行确认。本次测试用户此前已明确同意。服务器与客户端均需相同候选版本；网络协议升级3-b2，不与旧B1客户端混用。

后续评审先执行[25–30分钟清单](USER_TEST_CHECKLIST.zh-CN.md)，优先实测主/副手放置、各材料载人靠岸、水切换/Respiration、FOV组合、长时流体及清洗重登。旧TileEntity/实体链、Gas、生态/元数据动画/特殊掉落等缺口详见[KNOWN_GAPS](KNOWN_GAPS.md)。保留审查后再决定下一任务，不直接启动Task004。
