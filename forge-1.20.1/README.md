# MFQM Reborn — Forge 1.20.1

Minecraft **1.20.1** · Forge **47.2.0** · Java **17** · ForgeGradle **6.0.24** · Gradle **8.1.1** · modid **mfqm**

当前开发版本：**0.0.3.5-b1-candidate**。包含普通流沙、泥浆、松软流沙及 B1 候选入射/持续下沉/落地历史修复。运动参数待用户玩法验收，不宣称与 1.7.10 数值等价。使用 Minecraft 内置材质与 16×16 风格，无 AI 贴图或未授权旧图片/音频。

[003.5-B1 中文完成报告](docs/task-0035-b1/COMPLETION_REPORT.zh-CN.md) · [测试结果](docs/task-0035-b1/TEST_RESULTS.md) · [诊断与人工操作指南](docs/task-0035-b1/MANUAL_TEST_GUIDE.md) · [已知限制](docs/task-0035-b1/KNOWN_GAPS.md)

## 构建与测试

设置 `JAVA_HOME` 为 JDK17，进入本目录：

```sh
./gradlew --no-daemon --console=plain test runGameTestServer build
```

Windows 使用 `gradlew.bat`。首次运行需要下载依赖。构建执行 `reobfJar`，可安装文件为 `build/libs/mfqm-reborn-0.0.3.5-b1-candidate.jar`。当前套件共23项JUnit、20项Forge GameTest；这些自动测试与真实图形/网络测试分别报告。

## 客户端与专服

```sh
./gradlew --no-daemon --console=plain runClient
./gradlew --no-daemon --console=plain runServer
```

专服首次启动由运行者阅读 Minecraft EULA 并决定是否接受。不要将本地 EULA 文件或世界提交仓库。测试客户端与专服使用相同版本的本模组；B1 通道协议为 `2-b1`。`runObserver` 是第二开发客户端，用户名 Observer；仅限本地测试。开发运行 JVM 上限1GiB，Gradle内存可自行调整。

诊断默认关闭。操作员在可丢弃的允许作弊测试世界中使用 `/mfqm motion diag 260 label` 记录自己；`trial`、`suite` 和 `pigsuite` 会创建并替换测试池，具体范围、命令和字段见操作指南。`mfqm motionload` 是单独显式的限时负载夹具，不属于观测开关。

## 历史工作

[任务002工程基础报告](TASK_002_REPORT.md) · [任务003核心材料报告](TASK_003_REPORT.md) · [003.5-A审计](docs/task-0035-audit/README.md)

Task004/005、船只浮力、几何/方块交互和额外效果不在 B1 范围。
