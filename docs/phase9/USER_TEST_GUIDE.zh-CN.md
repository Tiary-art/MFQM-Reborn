# 用户本地构建与验收

需要 Java17、Minecraft1.20.1、Forge47.2.0。先备份存档，建议用独立游戏目录/测试世界，不将本阶段当成完整原版物理移植。

公开项目 ZIP 的 `deliverables/phase9/mfqm-reborn-phase9-public-source.jar` 可以安装，但**不含原版素材**，仍是 vanilla 占位。要看原版材质，请在自己的电脑私下构建：

1. 下载 PR 分支（合并后 main）的完整 ZIP，解压。将自己的原始1.7.10 JAR 放到仓库外；不要公开上传原素材/私有生成包。
2. 在项目根目录运行（Python3、Java17 在 PATH；第一次 Gradle 需要联网下载依赖）：

   ```sh
   python3 deliverables/phase9/build-private-local.py --jar "/你的私人路径/MoreFunQuicksandMod-1.1.1-1.7.10.jar"
   ```

   Windows 可用 `py -3` 代替 `python3`，路径加引号；工具支持 gradlew.bat，但本轮 Windows 实机 NOT_RUN。也可用环境变量 `MFQM_ORIGINAL_JAR`，不要把私人绝对路径写入公开配置。离线依赖已齐时追加 `--offline`。
3. 成功后安装 `deliverables/phase9-private/mfqm-reborn-phase9-original-textures-local.jar` 到该游戏目录 `mods/`，只保留一个 MFQM 版本。此包仅本地使用；同时查看该目录新生成的 SHA256SUMS 和 ARTIFACTS.json。构建系统/时间戳差异可能改变整个 JAR 哈希，不能因此直接声称与本报告二进制一致；导入 PNG/mcmeta 必须与原输入逐字节一致。
4. 创造测试世界，放置/查看 `mfqm:quicksand`、`mfqm:mud`、`mfqm:soft_quicksand`；泥浆为深棕，普通/松软流沙为各自原图，世界与方块物品应一致。试泥浆 depth0–3 和松软流沙 FILLED；FILLED 不等于旧 metadata1/2。放置 acid/bog 源方块并留出流动空间，查看静止/流动面和动画；桶图标目前仍为原版水桶占位，是已知缺口。
5. F3+T 重载后重复查看。不能有紫黑格、白色缺图；leaves_pile 需用户进一步检查透明区域和遮挡，其余未逐个视觉验收的 ID 不标为已测。

导入可单独操作，均从根目录运行：

```sh
python3 docs/phase9/tools/asset_pipeline.py --jar "/私人原版.jar" --dry-run
python3 docs/phase9/tools/asset_pipeline.py --jar "/私人原版.jar"
python3 docs/phase9/tools/asset_pipeline.py --jar "/私人原版.jar" --verify
python3 docs/phase9/tools/asset_pipeline.py --clean-generated --dry-run
python3 docs/phase9/tools/asset_pipeline.py --clean-generated
```

清理仅删除所有权清单登记且未被用户改动的文件；有用户改动会整体拒绝，先自行备份，不强制覆盖。自定义资源包优先级沿用 Minecraft ResourceManager；可覆盖同名 mfqm 资源，但其他包兼容性本轮未实测。公开源码无需原 JAR：`cd forge-1.20.1` 后执行 `./gradlew clean test build`（Windows gradlew.bat）。

反馈时提供：实际安装 JAR SHA256、Forge/Java 版本、方块 ID/状态/维度、资源包列表与优先级、latest.log 相关段、重现步骤及截图。带原素材的截图/包只私下提供，不发公开 issue。无需现在补交历史研究文件。不要打开新物理/世界生成开关来“修复”材质。
