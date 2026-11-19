# Phase9 构建交付验证

公开版 `mfqm-reborn-phase9-public-source.jar` 已放入本目录并纳入 Git，下载本分支完整 ZIP（合并后 main ZIP）即可找到。它是 **PUBLIC_SOURCE_BUILD，不含原版素材**，不是原版纹理完整恢复包。需要原版材质时，从完整项目运行本目录 `build-private-local.py --jar <私人原版JAR>`，输出留在忽略的 `deliverables/phase9-private/`。

| 产物 | 大小 | SHA-256 | 分发状态 |
|---|---:|---|---|
| mfqm-reborn-phase9-public-source.jar | 303806 | 13b0a9365fe56bac159c4864017c1c0d71719c141568df92f09f4e8cd188cc6d | Git 中公开交付；无原版 PNG/OGG |
| ../phase9-private/mfqm-reborn-phase9-original-textures-local.jar | 472014 | 1a457d746456a26c917ffe7b5b6ce3df56f453fd1741f9a58789d491e777e07d | PRIVATE_ORIGINAL_ASSETS_BUILD；PRIVATE_ARTIFACT_NOT_DISTRIBUTED，本地存在但不进入公开 ZIP |

实现源码内容对应提交 `022983116600f9a5a281da06ed3f3cdc58dd6582`。构建在该内容提交前启动、提交后完成；未改代码，已与实现提交核对。基线为 main `6a44d6f7f0403dfce67f597c8fc6b5edd5911317`。交付报告提交不改变源码。完整元数据见 ARTIFACTS.json、../../docs/phase9/ARTIFACTS.json。

Java17.0.21 / Gradle8.1.1 / Forge47.2.0 / MC1.20.1，Linux。公开实际命令（forge-1.20.1 内）：

```sh
./gradlew clean test build runGameTestServer --offline --console=plain
```

退出0，46 JUnit（0失败/0跳过），43 GameTests（0失败），2m10s。使用现有 Gradle 依赖缓存，clean 删除工程 build 输出；不是空依赖缓存离线安装测试。私有 builder 实际执行 clean test build，并验证最终 reobf JAR 全部88生成条目的哈希。原 JAR、PNG、动画侧文件未重编码或改动。详细日志和原始 gzip 见 docs/phase9/logs/。

公开 JAR：364 ZIP 条目、169 个非目录 assets/mfqm 资源条目、PNG0/OGG0/私有marker0。已确认包含 OriginalTextureBindings、Phase9RenderProbe、OriginalContactBridge、StuckLease、DryQuicksandCore 新旧类，mods.toml 为 `0.0.9-phase9-resources`。SHA 与 Phase8 的1480c274…以及旧 B2 的beef245f…不同，非改名旧包。公开 quicksand 模型引用 minecraft:block/sand，mud 引用 minecraft:block/mud；这是明确占位，不冒充 MFQM。

私有最终 JAR：429 ZIP 条目、231 个非目录 MFQM 资源条目、36 PNG、无OGG；quicksand 模型引用 mfqm:block/original/quicksand，mud 引用 mfqm:block/original/mud，soft 引用 mfqm:block/original/softquicksand1；实际 PNG、mcmeta 和模型清单详见 docs/phase9/evidence/private-final-jar.json（仅元数据）。真实开发客户端世界/物品栏与 atlas 已检查；正式启动器安装该最终 reobf JAR 尚未实测，不能将内容校验写成已安装测试。

私有→公开不带 clean 切换的 processResources 回归也通过（36→0 PNG，marker清除）；公开交付 JAR再次独立扫描通过。SHA256SUMS 包括公开 JAR及构建入口，不列未分发的私有二进制为可下载项。Git archive 交付与隐私检查见 docs/phase9/evidence/archive-verification.json。
