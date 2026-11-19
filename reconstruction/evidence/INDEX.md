# 证据索引

原始JAR不公开，hash及实际文件闭环在 checks/ORIGINAL_INPUT.json。每类class SHA及 archive path 在 ORIGINAL_CLASSES，bytecode文本指向 research/task-001/evidence；每个方法descriptor和代码SHA在 ORIGINAL_METHODS。CALL_GRAPH的offset为十进制，CFR行号与字节偏移不是同单位。

当前源码清单含逐文件SHA；baseline旧main与新import提交在 R0_BASELINE.json。原文/CFR不冒充作者源码；历史native向量不记本轮运行。旧阶段索引/任务映射见 reports/BASELINE_AND_REUSE.md；首批纵深分析见 reports/DEEP_FIRST_BATCH.md。所有161类在 docs/reconstruction/original/CLASS_DOSSIER_INDEX.csv 可导航。

clean-build-gametest.log.gz为本轮原始日志；.log仅去行尾空白。5份JUnit XML为本轮46项实际结果，原始日志含43 GameTests逐批记录及所有warning/error，保留Forge配置清理错误/离线鉴权异常而非删除。build退出0、测试46+43通过，不以此推断原版一致。

工具首次提取失败记录：jawa2.2.0在自动实例化ConstantValue属性时抛 AttributeError: 'int' object has no attribute 'index'（jawa/attributes/constant_value.py:16）；修正为读取raw attribute table中的属性名，不猜属性值，全部方法体已成功读出。字段ConstantValue语义/注解值仍待深度解析，不能宣称已完整证明。

TOOL_TESTS保留缺输入、非法外键的预期失败stderr及确定性重跑结果；这些不是删掉的失败用例。原始私有输入哈希最后再校验，无字节写入。Windows和正式安装NOT_RUN。
