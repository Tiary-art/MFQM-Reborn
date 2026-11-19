# Phase9 安装入口

本目录 `mfqm-reborn-phase9-public-source.jar` 是可安装公开构建，**没有原版材质**。安装要求 Minecraft1.20.1 / Forge47.2.0 / Java17，mods 目录只保留一份 MFQM。

查看原版材质需用自己的原版 JAR 私下生成：在解压后的完整项目根目录运行 `python3 deliverables/phase9/build-private-local.py --jar "/私人原版.jar"`。输出为 `deliverables/phase9-private/mfqm-reborn-phase9-original-textures-local.jar`，不会提交/公开分发。Windows 命令及测试细节见 [用户指南](../../docs/phase9/USER_TEST_GUIDE.zh-CN.md)。

总体 PARTIAL；已肉眼检查核心三种方块及 acid/bog，桶和旧变体等仍待完成。完整 [报告](../../docs/phase9/COMPLETION_REPORT.zh-CN.md)、[构建验证](BUILD_VERIFICATION.zh-CN.md) 和 ARTIFACTS.json/SHA256SUMS 随项目交付。
