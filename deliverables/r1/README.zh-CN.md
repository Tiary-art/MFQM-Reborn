# R1 安装与私有材质构建

公开安装文件为同目录的 **mfqm-reborn-r1-public.jar**。Minecraft 1.20.1 / Forge 47.2.0 / Java 17。ARTIFACTS.json 记录源提交、Forge 工程树与成品哈希；SHA256SUMS 可独立验证。GUI、专服和测试日志位于 logs。安装后的验收步骤见 [用户指南](USER_TEST_GUIDE.zh-CN.md)。

## 使用自己的旧 JAR 构建私有版

解压整个项目。安装 Python 3 和 JDK 17，设置 JAVA_HOME。首次运行 Gradle 需要访问 Minecraft、Forge、Gradle 及 Maven 依赖服务。Windows 在项目根目录的 PowerShell 运行以下命令，将引号内路径替换成自己的文件路径。

```powershell
.\deliverables\r1\tools\build-private-windows.cmd --jar "D:\我的模组\MoreFunQuicksandMod-1.1.1-1.7.10.jar"
```

Linux 或 macOS 在项目根目录执行以下命令。

```sh
python3 deliverables/r1/tools/build_private.py --jar "/path/to/original.jar"
```

离线且已缓存所需依赖时可追加 `--offline`。成功后将 `local-original-assets/r1/mfqm-reborn-r1-private.jar` 放入测试实例的 mods。构建脚本会核对指定旧 JAR 的 SHA，再逐一检查私有 JAR 内生成项的哈希。校验自己的现有私有产物可追加 `--verify-only`。本机的 `local-original-assets/r1/ARTIFACTS.json` 记录私有 SHA 与每个受控文件的摘要。需要排查构建问题时查看同目录 build.log。Windows 批处理使用带引号的脚本路径和 Python UTF-8 模式；Windows 实机和中文用户名未实测。

## 重放公开构建及数据库校验

在 forge-1.20.1 运行 `./gradlew clean test build runGameTestServer --console=plain`（Windows 用 gradlew.bat）。输出是 build/libs/mfqm-reborn-0.1.0-r1-content.jar。开发环境 GameTest 会在 run/gameTestServer 写入 r1-runtime.json。运行时采样采用默认 feature flags 和 operator 权限。

在仓库根目录执行以下命令。重建静态清单需先编译 Java 类，安装 reconstruction/tooling/requirements.txt 中的依赖。先把本次 GameTest 导出的 JSON 复制到 deliverables/r1/logs/r1-runtime.json。发布新私有版本时同步更新无像素的 private-entry-hashes.json。

```sh
python3 reconstruction/tooling/r1/content_database.py
python3 reconstruction/tooling/inventory_modern.py --repo-root . --out-dir reconstruction
python3 reconstruction/tooling/build_database.py --repo-root . --out-dir reconstruction
python3 reconstruction/tooling/r1/method_evidence.py
python3 reconstruction/tooling/curate_audit.py --out-dir reconstruction
python3 reconstruction/tooling/resource_graph.py --repo-root . --out-dir reconstruction
python3 reconstruction/tooling/validate_database.py --repo-root . --out-dir reconstruction --verify
python3 reconstruction/tooling/report_coverage.py --out-dir reconstruction
python3 reconstruction/tooling/r1/test_validation.py -v
python3 reconstruction/tooling/r1/validate.py
python3 reconstruction/tooling/check_delivery.py --repo-root . --out-dir reconstruction
```

最后的 R1 包审计可传 `--private 私有JAR路径 --original 原始JAR路径`，缺少相应输入时该部分显示 NOT_RUN。已有 ZIP 中直接校验公开交付物只需最后一条命令。
