# MFQM Reconstruction：唯一事实来源

本目录建立证据→对象→现代实现→验收的数据库。总体 **R0 PARTIAL**。全量字节索引完成不等于完整注册/深度语义/游戏复原。任务原文在 reports/TASK_R0.md；本轮治理见根 AGENTS.md。

权威关系：manifest/原始身份和现代清点 → mapping/RESTORATION_MATRIX.csv（原版每文件/类/成员/可识别注册调用都有行） → ORIGINAL_TO_MODERN.csv（多对多身份边） → 现代文件清点/全文件审计（含现代额外与未知）。按 original_id 正向查，按 modern_id/modern_path 反查；现代没有映射的项保留 UNKNOWN 或有理由的 MODERN_BRIDGE/DEV_ONLY，不能自动当死代码。

## 状态与证据标准

BYTECODE_CONFIRMED：只证明实际字节/签名/offset/引用；DECOMPILED_INTERPRETATION：CFR解释，非作者源码；DYNAMIC_ORACLE_CONFIRMED：限定实际运行域；RESEARCH_ONLY：历史证据未在本轮重放；INFERRED/UNKNOWN保留疑问。不得将签名确认提升为行为确认。

MISSING=已知需要的现代目标不存在；UNREGISTERED=存在实现但无注册；PLACEHOLDER=明确占位；APPROXIMATION=有现代近似、未证明原版一致；MISMATCH=具体证据表明差异；PARTIAL=仅部分分支/身份闭合；MATCHED_VERIFIED=相应维度同输入验证通过；NOT_APPLICABLE_PROVEN=有证据不适用；UNKNOWN=证据不足；BLOCKED=已知阻塞。REGISTERED、VISIBLE、ASSET_MATCHED、BEHAVIOR_PARITY、MULTIPLAYER_VALIDATED独立，不互相推出。

本轮注册清点为**调用点候选和显式metadata子集**，不是全旧运行时注册表。现代153项为 DeferredRegister literal+循环源解析，动态注册dump NOT_RUN。深度类全语义数保守为0，第一批6模块静态链为PARTIAL。完整旧metadata、创作栏栈和行为案例宇宙仍UNKNOWN，不用子集当真总数。

## 字段与外键

ID=kind:SHA256(UTF8 identity)前24位；方法identity含owner#name+JVM descriptor，字段含owner#name:descriptor。稳定于当前JAR版本；碰撞会被校验拒绝。CSV UTF-8/LF；分号分隔多值。source/target/class/member外键保留；CALL_GRAPH的offset为十进制。外部或继承虚派发未解边单列，不标UNREACHABLE。

RESTORATION_MATRIX含任务§9.1全部字段；各验收维度未知不填PASS。现代全文件审计包含§9.2全部字段；301行是全文件静态分拣，不声称301份人工深度审查。12个重点代码决策另有已审差异。完整依赖调用图、注解值、所有反射入口仍PARTIAL。

## 重放

Python3.9+，安装 `python -m pip install -r reconstruction/tooling/requirements.txt`；Java17/Forge构建需要已有依赖或联网。将私人原JAR留在仓库外。工具命令显式 --repo-root / --out-dir，不依赖开发机绝对路径：

```sh
python reconstruction/tooling/inventory_original.py --input-jar "/私人原版.jar" --repo-root . --out-dir reconstruction
# 先在 forge-1.20.1 运行 clean test build，再取编译后完整描述符
python reconstruction/tooling/inventory_modern.py --repo-root . --out-dir reconstruction
python reconstruction/tooling/build_database.py --repo-root . --out-dir reconstruction
python reconstruction/tooling/curate_audit.py --out-dir reconstruction
python reconstruction/tooling/resource_graph.py --repo-root . --out-dir reconstruction
python reconstruction/tooling/validate_database.py --repo-root . --out-dir reconstruction --verify
python reconstruction/tooling/report_coverage.py --out-dir reconstruction
```

缺少原JAR为显式错误，绝不输出假空成功。--verify校验现有表，原输入重读用inventory_original；输出到临时目录可比较身份表哈希，类文档仍按repo-root生成，不建议并发修改同一数据库。所有权清理不是这些工具功能，工具不删除输入或游戏源码。Windows文本使用UTF-8；本轮Windows运行NOT_RUN。原版/现代正式安装NOT_RUN，现有JUnit/GameTest结果见 checks/。

每个后续PR必须同时更新证据、实现、对应测试和矩阵；不能仅修改报告数值。清理门槛是证据/替代/同输入/安全/无重复执行/迁移/回滚/独立验收八项；未满足保持KEEP_TEMPORARILY。R0-E不执行。
