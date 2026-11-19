# Phase8 安装产物

安装文件：**mfqm-reborn-phase8-controlled.jar**。适用 Minecraft1.20.1 / Forge47.2.0 / Java17；客户端和专服安装同一文件，先移走旧的MFQM Reborn JAR，避免相同modId重复加载。测试前备份世界。

此文件由最终Phase8源码干净重建并reobfuscate，不是重命名的B2：新增类、实际字节码调用链及与旧B2差异见jar-verification.json与BUILD_VERIFICATION.zh-CN.md。项目内部版本字符串仍为旧candidate，不能用模组列表版本名鉴别；请核对SHA-256。

```sh
cd deliverables/phase8
sha256sum -c SHA256SUMS
```

Phase8仍为PARTIAL：普通流沙的受控非玩家Contact子链已接入，玩家自动映射仍BLOCKED；实验开关默认关闭，未开启自然生成。玩法和开关说明见../../docs/phase8/USER_TEST_GUIDE.zh-CN.md。本次只补齐构建交付，没有修改机制。

完整重建日志/46项JUnit XML在logs；本次没有重新执行游戏实测或新增Phase9功能。原1.7.10JAR和原始贴图/音频不包含在此产物中。
