# MFQM Reborn

More Fun Quicksand Mod 的 Minecraft Java 1.20.1 Forge 移植研究项目。

[R1 可安装公开 JAR](deliverables/r1/mfqm-reborn-r1-public.jar) · [R1 完成报告](docs/reconstruction/R1_COMPLETION_REPORT.zh-CN.md) · [私有贴图构建与安装](deliverables/r1/README.zh-CN.md)

当前已有研究、Forge 工程和三核心材料的近似实现。原代码及素材的许可证与再发布授权仍待核查；公开工程不分发旧素材。

## 任务 001：只读逆向盘点与移植设计

[报告导航与审计说明](research/task-001/README.md) · [六份报告](research/task-001/reports) · [字节码及审计证据](research/task-001/evidence)

本次仅提交研究文档与分析证据。未包含原始 JAR、PNG、OGG，也未创建或发布新版 Mod。

## 任务 002：Forge 1.20.1 最小工程

[工程与启动说明](forge-1.20.1/README.md) · [完成报告与实测边界](forge-1.20.1/TASK_002_REPORT.md) · [完整构建/测试日志](forge-1.20.1/logs/task-002) · [开发测试 JAR](deliverables/task-002/mfqm-reborn-0.0.2-dev.jar)

仅包含开发方块与工程基础；没有流沙物理。默认使用 Minecraft 自带沙纹理，不包含旧作者图片/音频。

## 任务 003：三核心材料与服务端陷落机制

[完成报告与验证边界](forge-1.20.1/TASK_003_REPORT.md) · [证据追踪/差异表](forge-1.20.1/docs/task-003/EVIDENCE_TRACEABILITY.md) · [重现步骤](forge-1.20.1/docs/task-003/REPRODUCE.md) · [日志](forge-1.20.1/logs/task-003) · [开发测试 JAR](deliverables/task-003/mfqm-reborn-0.0.3-dev.jar)

普通流沙、泥浆、松软流沙具有独立接触/阻力/支撑行为；服务端聚合状态、耗氧、伤害和生命周期。属于任务001静态证据指导下的近似实现，未取得1.7.10实机曲线，不宣称原版数值一致。默认占位为 Minecraft 自带16×16风格；没有使用AI生成贴图。任务004未开始。

## 任务 003.5-B1：运动观测、候选陷落与落地修复

[中文完成报告](forge-1.20.1/docs/task-0035-b1/COMPLETION_REPORT.zh-CN.md) · [自动化与实测结果](forge-1.20.1/docs/task-0035-b1/TEST_RESULTS.md) · [双客户端/延迟/低TPS](forge-1.20.1/docs/task-0035-b1/NETWORK_RESULTS.md) · [原始证据](forge-1.20.1/docs/task-0035-b1/evidence/INDEX.md) · [候选测试JAR](deliverables/task-0035-b1/mfqm-reborn-0.0.3.5-b1-candidate.jar)

提供默认关闭的限时诊断、首次入射限制、材料持续下沉与受控落地历史处理。参数仍待玩法验收；间歇性Y轴抽搐未被证明修复。保留旧测试断言，完成23项JUnit/20项GameTest，以及有明确证据范围的真实玩家、自然猪、双客户端和低TPS测试。没有开始船只修复或任务004/005。

## Reconstruction R0

工程重整数据库入口：[reconstruction/README.zh-CN.md](reconstruction/README.zh-CN.md)。本轮状态PARTIAL；完整字节索引不代表内容或玩法全部恢复。[R0报告](docs/reconstruction/COMPLETION_REPORT.zh-CN.md) / [未闭合项](docs/reconstruction/KNOWN_GAPS.md)。
