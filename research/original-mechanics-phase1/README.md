# MFQM 原版机制研究：第一阶段

本 PR 仅提交研究文档和完整证据包；不修改模组源码或原始 JAR。B2 对比基线为研究时的提交 `03a6a20`，本 PR 基于随后合并 B2 的 main `9a0c127`。

- **[下载完整研究包 ZIP](MFQM-Original-Mechanics-Phase1-research.zip?raw=true)**（约6.8 MiB，230个文件）
- [ZIP 的 SHA-256](MFQM-Original-Mechanics-Phase1-research.zip.sha256)
- [总报告](COMPLETION_REPORT.zh-CN.md)
- [范围与证据等级](reports/01_scope_and_evidence.md)
- [三核心运动分支](reports/02_core_motion_branches.md)
- [Stuck 与 tick 顺序](reports/03_stuck_and_tick_order.md)
- [污渍类型、分区 UV 和清洗](reports/04_coating_state_uv.md)
- [相机、空气、声音和原图](reports/05_camera_air_audio_resources.md)
- [B2 偏差清单](reports/06_port_differences.md)
- [旧版实机测量计划](reports/07_original_runtime_measurement_plan.md)
- [复核说明](REPRODUCE.md)

本目录展示可在线阅读的报告；全部类/方法/调用/跳转索引、逐类字节码、关键反编译文本、UV/资源元数据、研究脚本与校验日志均在完整 ZIP 内，保持原交付包不变。

已索引161类、1955方法，并人工核对三核心39条主要运动分支。**结构索引不等于全部方法语义还原；1.7.10实机轨迹未执行，90个待测场景标为NOT_RUN。**没有将离线算术或B2运行数据冒充原版实测。

研究包不包含原始模组/官方客户端二进制或PNG/OGG素材；没有AI贴图或重新绘制的素材。原始JAR哈希复核未变。本 PR 不启动后续移植开发。
