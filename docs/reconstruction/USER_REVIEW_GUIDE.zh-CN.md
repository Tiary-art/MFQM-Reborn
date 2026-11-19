# 如何检查这次成果

下载PR完整ZIP，先看 reconstruction/README.zh-CN.md 和 checks/R0_VALIDATION.json。按类名查 docs/reconstruction/original/CLASS_DOSSIER_INDEX.csv，进入对应类文档查看不同字段/方法descriptor及字节码定位；重点链看 reconstruction/reports/DEEP_FIRST_BATCH.md。

查“原版有、新版缺”：RESTORATION_MATRIX按modern_ids为空/semantic_mapping=UNKNOWN筛选；查“新版有但原版对应不明”：NEW_PROJECT_INVENTORY与UNVERIFIED_MODERN；查“哪些近似要换”：AI_APPROXIMATION_AUDIT按KEEP_TEMPORARILY/REPLACE_FROM_ORIGINAL筛选。ORIGINAL_TO_MODERN同original_id多行支持一对多，按modern_id反向查；身份映射不证明等价。

重放命令在README。Python安装jawa2.2.0；原JAR私人路径仅供--input-jar，不上传。validate_database/report_coverage能独立运行；重新现代成员清点需要先Java17 clean test build。Windows实机未测，runner提供cmd.exe /c路径与二进制日志，不能当通过。

若要帮助关闭缺图问题，请提供实际私有JAR SHA256、具体block/item ID和state、资源包列表、复现位置、截图及latest.log。U-01..05当前都是OPEN；无需为了阅读报告重新上传原JAR。带原素材的包/截图仅私下提供，不放公开仓库。本次不要求安装新玩法JAR，不开始下一阶段。
