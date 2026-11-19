# MFQM原版机制研究第一阶段交付

本轮重新核对原始1.1.1 JAR，**未修改模组代码、未制作新候选、未启动1.7.10游戏**。重点是三核心运动分支、阻碍、分级污渍和相机/声音证据；没有把静态结论或B2测试冒充旧版实测。

- [总报告](COMPLETION_REPORT.zh-CN.md)
- [范围/来源/等级](reports/01_scope_and_evidence.md)
- [39条三核心主要运动分支](reports/02_core_motion_branches.md)
- [坐标、Stuck及tick顺序](reports/03_stuck_and_tick_order.md)
- [污渍类型/等级/UV/清洗](reports/04_coating_state_uv.md)
- [相机/氧气/声音/原图](reports/05_camera_air_audio_resources.md)
- [B2偏差与修复约束](reports/06_port_differences.md)
- [未执行的旧版测量计划](reports/07_original_runtime_measurement_plan.md)

索引：161类、1955方法、29276调用位置、14169跳转位置；methods-with-instructions.json保留方法描述符和完整指令。所有类的方法结构已列出，但**不是1955方法完整语义恢复**。UNKNOWN/PARTIAL明确保留。

输入/工具/哈希见manifest.json、evidence/external/provenance.json。ZIP只含文本、JSON/CSV和研究脚本；原JAR、PNG/OGG、官方客户端二进制都不在交付包里。可以在私有环境按原JAR复核资源名和像素统计，不把报告里的UV统计当新贴图。
