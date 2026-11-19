# 重现任务003

基线：main `f9a6fc7`；Java17、Gradle8.1.1、ForgeGradle6.0.24、Minecraft1.20.1、Forge47.2.0。版本未升级。公开包只引用 Minecraft 的 sand/mud/red_sand 占位纹理。

在 `forge-1.20.1`：

```sh
./gradlew --no-daemon --console=plain clean build
./gradlew --no-daemon --console=plain runGameTestServer
python3 tools/verify_project.py build/libs/mfqm-reborn-0.0.3-dev.jar
python3 tools/verify_task003.py build/libs/mfqm-reborn-0.0.3-dev.jar
./gradlew --no-daemon --console=plain -PtraceSnapshots runClient
./gradlew --no-daemon --console=plain -PtraceSnapshots runServer
```

依赖必须能访问官方 Maven。这里使用的代理/JDK/Gradle缓存绝对路径只属于测试环境，不属于工程要求。专服首次运行须自行阅读并接受 Minecraft EULA。本次沿用任务002中用户明确同意的本地测试 EULA；不把已接受的 eula.txt 提交仓库。联机只在127.0.0.1测试，无正版认证链路验证，不应用测试用 offline-mode 配置部署公网。

## 实机试验（会覆盖测试世界坐标，须用新建测试世界）

单人创建开启命令的超平坦测试世界。设置 `doMobSpawning false`；三核心材料各执行：

```
/mfqm trial quicksand still
/mfqm trial quicksand walk
/mfqm trial quicksand jump
/mfqm trial quicksand hold_jump
/mfqm trial quicksand fast_fall
/mfqm trial quicksand edge
/mfqm trial quicksand single_layer
/mfqm trial quicksand multi_layer
```

将 quicksand 分别替换 mud、soft_quicksand。trial **不会代替键盘输入**：walk按W约2.5秒，jump按Space约0.12秒，hold_jump按住Space约3秒；其余不输入。每项应至少等10秒（200server ticks），受卡顿影响实际墙钟可能更长。CSV在运行目录 `mfqm-traces`；`/mfqm status` 输出服务器权威字段。默认试验为11×11三层池，中心0.5/0.5，顶格Y64；edge从X4.75开始；fast_fall初始表面上3格、初速−1；单层为1层。Mud的碰撞可能阻止眼部覆盖，这属于材料差异。

安全平台X6..10/Y64/Z−3..3。先 `/spawnpoint @s 8 65 0`，否则死亡重生可能重新选择池内。`/tp @s 8.5 65 0.5` 是**指令辅助退出**，不能据此声称玩家自行逃脱。`/mfqm trace start exit_label`记录400ticks；覆盖下气息耗尽后退出，观察material=none、stuck=0、air以5/tick恢复及移动恢复。`deep_oxygen`从眼部刚覆盖处开始，记录420ticks，可能导致死亡。

以活跃状态 `/kill @s` 后真实点击重生；进入另一维度后status；活跃状态保存退出并重进，确认重新采样和新气息而非持久stuck。专服须实际用客户端连接，操作同样命令，并以UUID+tick配对MFQM_SYNC_SERVER/CLIENT日志。

```sh
python3 tools/analyze_task003_traces.py run/client/mfqm-traces --output summary.json
```

统计器只汇总实际观测，不会填补未观测脱离时间。CSV速度为求解器输出，位置为服务器接受的位置；玩家的Vanilla网络运动与生物不同，不能只看速度推断净轨迹。

## 私有原始纹理

复用 `tools/private_legacy_pack.py --help`。`--core` 将原始JAR中三个静态16×16PNG原样打入已忽略的本地包，不上传、不重绘、不缩放。三者没有对应mcmeta；工具在其他带mcmeta的条目中保留其原始字节。动画实测与三个静态纹理实测须分开标记。原JAR SHA256必须为 `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。
