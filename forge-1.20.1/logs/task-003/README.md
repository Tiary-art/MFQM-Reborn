# 任务003原始日志索引

原始进程日志时间为UTC；北京时间=UTC+8。本次日期均为2026-11-18。保留失败尝试，不用通过日志覆盖失败日志。

| 文件 | 结果/用途 |
| --- | --- |
| 01-compile.log | 初次编译成功 |
| 02-first-build-tests.log | 初次clean build，17JUnit成功 |
| 03-first-gametest.log | 首次14项GameTest中4失败，保留原输出 |
| 04-first-client.log | 玩家只发速度包的错误轨迹；不是最终通过证据 |
| 05-gametest-corrections.log | 剩2个测试网络fixture失败 |
| 06-gametest-player-fixtures.log | 改无socket玩家fixture，14GameTest成功 |
| 07-private-core-pack.log | 本地三静态PNG字节/尺寸/hash复核，无PNG内容 |
| 08-first-dedicated-server.log | 较早构建仅专服启动，未联机 |
| 09-position-budget-regression.log | 18JUnit/14GameTest通过 |
| 10-corrected-client.log | 位移预算版本，24场景、退出恢复；也含换维度失效现场与SIGQUIT线程转储 |
| 11-corrected-dedicated.log | 句柄修复前构建，启动/stop成功，没有客户端联机 |
| 12/13-resource-audit*.json | 位移预算构建资源审计 |
| 14-dimension-thread-dump.txt | jcmd受沙箱/proc限制失败；成功SIGQUIT转储在10中 |
| 15-final-clean-build-gametest.log | 最终clean build、18JUnit、15GameTest全部通过 |
| 15-final-gametest-runtime.log | 同次最终GameTest运行目录的原始日志 |
| TEST-*.xml | 最终JUnit原始XML，0失败/0跳过 |
| 16-final-client.log | 最终客户端：单人换维度/重新陷落/活跃重进、私有静态包加载/卸载、真实专服连接/退出/死亡重生 |
| 17-final-dedicated.log | 最终真实socket登录、三材料、/kill、正常断开及stop保存，BUILD SUCCESSFUL |
| 18/19-final-*-resource-audit.json | 最终默认/核心资源链与Java17审计 |
| 20-final-dedicated-sync.json | 仅客户端连接标记之后的快照配对，280匹配、0字段差异 |
| 21-final-integrity.json | 原JAR/247PNG/最终JAR审计 |

16客户端日志截取到测试完成并返回多人菜单；客户端应用留在菜单，不将它说成已取得JVM正常退出码。原始日志中的音频设备错误、Forge版本提示/空metadata警告和性能落后警告均保留，详见完成报告边界。

CSV在docs/task-003/traces；phase2与最终构建分目录。无观测到的自救/脱离时间不由统计程序补写。截图来自实际窗口，公开截图均为Minecraft占位资源；原始贴图的私有截图没有提交。
