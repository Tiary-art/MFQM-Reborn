# Phase 6 两个纯组件实施报告

结论：**PASS（仅任务书授权的两个纯 Java 组件及声明测试域）**。不代表原版完整物理或世界生成恢复。基线是已合并 Phase5 PR #11 的 main `184eacb`；沿用仓库本身，不需要重新上传 ZIP。

## 修改与算法

新增 `forge-1.20.1/src/main/java/art/tiary/mfqm/legacy/`：

- `LegacyRandom.java`：注入 nextInt/nextDouble；测试包裹同一个 java.util.Random（48-bit）实例，不重新播种。
- `LegacyBlock.java`、`VoxelPort.java`：只表达原块身份和即时有序读写，不混入 metadata；OTHER 仅表示本测试未进一步区分的非 AIR/非 Dry 身份，不是材料物理 profile。
- `DryQuicksandCore.java`：generateSoftSand → DryQuicksand。保留 double 计算次序、Java 整除、i/j/e 包含端点循环、全部噪声、三连写与 flags3/meta0、重复与失败写、有序侵蚀和短路重复读取。负 extent 仍消费初始 nextDouble。
- `StuckLease.java`：Contact 最后覆盖；Update 先查并删固定 UUID，再判断属性是否存在；按 double c/2 计算速度与 operation2/savedfalse；Level>0 消费到0，下次无续期转-1。端口约定：一次 Update 内同 UUID 无外部重入修改。
- `package-info.java`：标明未接入玩法。

新增测试 `PureComponentsTest.java`、`src/test/resources/phase6/`、本目录工具/报告/证据。没有更改已有生产代码、资源、构建配置或运行依赖。生成的本地 JAR 沿用旧候选版本名，未分发、未当作玩法候选验收。

## 验证结果

`logs/gradle-clean-test-build.log`：`clean test build --offline` 成功，11 tasks executed；Java17，Forge47.2.0，Gradle8.1.1。`logs/junit-summary.json`：45 tests，0 failures/errors/skipped；其中新组件22 tests（19 Dry 动态测试+3 Stuck 测试），原物理23 tests。

19 Dry 样本：extent -1/0/1/4/5/10/18 × seed0/1；空网格extent10；完全拒绝、部分拒绝、SoftQuicksand 保护块 fixture；自然父调用seed38。每条逐项比较全部 RNG API、getBlock、write，包括返回失败、重复/同状态写；测试网格真实保存接受的写入。seed38先验证父调用前缀 RNG，再在同一个 Random 上执行子方法。保护块并不表示 Dry 会保护它：原 Dry 写入阶段可覆盖 SoftQuicksand，不能移植 Mire 的保护条件。

Stuck：先重验原 native/oracle 123事件一致，再把其中48条 Tick/属性/Level接口事件自动投影为 Java 向量；8次回调逐事件对照。原123事件中的字节码分支、helper边界、jump/snapshot不属于纯组件输出，**没有声称 Java 组件输出123事件**。112数学向量全数校验 amount（1e-12），不测试被排除的 jumpMovementFactor。另测已有 UUID、属性缺失先清理、其他 UUID 保留、负 Level 保持和无续期。

Phase2静态、Phase3 trace、Phase4的112数学向量、Phase5全部62组保存的 native/独立VM轨迹回归通过；写证据的历史测试在临时副本运行。补充三条 native 方法体/独立VM全事件对照分别2050/2268/2204事件通过。见 logs 和 TEST_MATRIX。

调用隔离检查：547个已有Forge文件与基线的Git规范化blob相同（Windows gradlew.bat检出换行需规范化），52个核心外Java文件无调用；纯核心可用空依赖 classpath javac 单独编译。B1 高速入沙、Y稳定、落地音效、同步及客户端预测均未修改。

## 复现

从仓库根目录执行，Python3.12、JDK17；Gradle依赖首次可联网下载，已缓存时可用 --offline：

```sh
python -B docs/phase6/tools/convert_vectors.py
cd forge-1.20.1
./gradlew clean test build --offline --console=plain
cd ..
python -B docs/phase6/tools/check_isolation.py --javac "$JAVA_HOME/bin/javac"
```

转换脚本只读取已提交的压缩事件证据，不需要旧 JAR、Minecraft 或 `/tmp` 文件；`vector-sources.json`记录来源hash。数值文本会出现 Python小写科学记数法与Java大写E的差别，测试按同一个解析后double规范化文本，**不放宽 RNG 数值误差**。字节码分支不属于接口事件，未加入生产代码以迎合日志。

若要重新执行原方法体而不只是消费保存的证据，先按 `research/original-phase5/REPRODUCE.md` 准备私有旧 JAR 和临时 harness；研究方法元数据来自Phase1。然后：

```sh
python -B docs/phase6/tools/add_native_cases.py --java "$JAVA_HOME/bin/java" --jar "$MFQM_LEGACY_JAR" --harness /tmp/mfqm-phase5
python -B docs/phase6/tools/check_supplemental_oracle.py --methods /tmp/mfqm-phase5/oracle-methods.json
python -B docs/phase6/tools/run_regressions.py --methods-work /tmp/mfqm-phase5
python -B forge-1.20.1/tools/verify_project.py
python -B forge-1.20.1/tools/verify_task003.py
python -B forge-1.20.1/tools/audit_b2_resources.py
```

本次环境 `JAVA_HOME=/workspace/work/task002-tools/jdk-17.0.21+9`，`GRADLE_USER_HOME=/workspace/work/task002-tools/gradle-home`。完整Gradle/JUnit/历史回归与补充方法调用命令和结果在logs、evidence/native-cases.json。临时回归目录用后删除，可通过run_regressions.py重建。

## 开发失败与真实边界

- 初轮Java对照在extent5/侵蚀读事件不一致，原因是简化邻居读取，恢复原第二次getBlock解决；未删输入。
- 接着extent10 seed0的事件1282仅科学记数法文本不同，解析后的double相同；加入精确double文本规范化，未改期望数值。
- deny补充fixture曾误以为默认是砂地/石地；原World是y66水、其余AIR。修正Java网格及本阶段独立VM的明确fixture子类；旧Phase5 VM/证据未改。失败日志仍保存。
- 隔离检查初次直接比较gradlew.bat遇到检出CRLF；改为Git clean-filter blob校验，不修改该文件。

所有本轮 native 均是原方法体+Phase5声明的模拟API/JVM；原版Minecraft1.7.10实机、现代客户端/专服/视觉/净下沉统计一律 **NOT_RUN**。完整Surface仍0/25，不因本阶段纯Dry实现而增加。完成本轮后停止，正式接入必须另获授权。
