# Phase8 构建交付补齐与验证

结论：**构建、精确哈希复现、Phase8包内字节码核验通过**。此前确实漏把JAR提交进仓库：ARTIFACTS.json只记了`/workspace/outputs/...`，因此GitHub合并项目ZIP不包含它。本次将实际二进制提交至`deliverables/phase8/mfqm-reborn-phase8-controlled.jar`，不是仅修改链接。

## 源码与构建

最终Phase8提交：`da9af361b3f21f466edd813377fb3969aedd11f0`；本次干净检出其合并提交`c02c5c9`。两者Forge工程树一致。本次没有修改forge-1.20.1中的源码、资源、构建配置或玩法。

JDK17.0.21+9、Gradle8.1.1、Forge47.2.0，执行：

```sh
JAVA_HOME=/path/to/jdk17 GRADLE_USER_HOME=/path/to/gradle-cache \
  bash forge-1.20.1/gradlew -p forge-1.20.1 clean test build --offline --console=plain
```

实际执行使用已有JDK17/Forge依赖缓存；完整原始输出`logs/clean-test-build.log.gz`，可读副本仅移除行末空白。结果`BUILD SUCCESSFUL in23s`，11tasks全部执行；46JUnit、0failure/error/skipped。最终构建包括`reobfJar`，复制的是build/libs输出。

## SHA-256 对照

原ARTIFACTS.json记录与本次干净重建、仓库交付JAR三者均为：

`1480c2746cdc64fb93563e652114769cbf0501a24baf71473c0469e3ce001a77`

这是实际逐字节重建匹配，不是把新哈希覆盖旧值后声称一致。ARTIFACTS.json保留原工作区位置、原哈希及EXACT_MATCH对照，并新增仓库路径、最终源码与重建检出提交。

旧B2 SHA为`beef245fd6f642fe2510548a9f1ec668eafa6bde28757dedaa853d44d8c22355`，与本JAR不同。JAR内部Implementation-Version仍为历史`0.0.3.5-b2-candidate`，这解释了旧输出文件名；本次不改源码版本，以免偏离用户指定的最终Phase8源码。

## 包内实际功能确认

`tools/verify_jar.py`核验交付JAR，而非工作区dev classes：

- OriginalContactBridge、QuicksandContacts、StuckAdapter、DryWorldAdapter、Phase7Commands、Phase8ClientTrace、Phase8GameTests及Phase8TestIsolation均在包内；旧B2没有这些要求的类。
- 反汇编确认`SinkingBlock→OriginalContactBridge.inside→QuicksandContacts.emit/StuckAdapter.automaticContact→StuckLease.update`实际调用链，以及命令对disableAll的调用和forcedDisabled锁存字段。
- CoreSinkingBlock.surfaceHeight读取FILLED状态，未调用BlockGetter查询，包含Phase8的线程安全修复。
- mods.toml、49材料目录、中文语言资源存在；所有class为Java17版本61；没有打包PNG/OGG。

完整反汇编和结构化结果见`logs/phase8-delivered-jar.javap.txt`、`jar-verification.json`。复核命令：

```sh
python deliverables/phase8/tools/verify_jar.py --java-home "$JAVA_HOME"
```

本次没有重新做安装版JAR实机/整合包测试，不把包内验证冒充运行测试；Phase8原实测范围与PARTIAL/BLOCKED限制保持不变。原游戏机制、默认关闭开关、原始JAR/素材均未更改。

## 旧阶段交付检查

Task002、Task003、B1、B2的4个历史JAR都已被Git跟踪，会进入项目ZIP。002/B1/B2的既有哈希均匹配；003的JAR也存在，但没有独立SHA256SUMS，本次新增该清单，不替换历史JAR。详情见prior-deliverables-audit.json。

Phase6明确声明仅纯组件、未分发候选JAR；Phase7也明确没有发布新玩法候选JAR，因此未把它们记为“承诺交付却丢失的二进制”，也没有擅自生成历史版本。研究Phase1–5是研究资料，不是可安装版本。本次确认的仓库漏交是Phase8。

提交后使用git archive再次检查项目ZIP确实包含本JAR并验证其字节哈希；PR合并后main项目ZIP才包含此次补交。无需启动Phase9。

另外核查研究Task001/Phase2–5及docs/Phase6–8的8份既有文件清单，共1,828个条目，均存在且哈希匹配（Phase8本次ARTIFACTS.json变更的校验项已对应更新）。这不涵盖没有列入公开清单的私有输入文件。详情见prior-manifests-audit.json。
