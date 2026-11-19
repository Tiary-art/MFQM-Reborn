# MFQM Reborn R1 完成报告

**状态 PARTIAL。** R1 交付可安装的 Minecraft 1.20.1 / Forge 47.2.0 模组，新增 91 个物品 ID，默认材料栏实际显示 153 个栈。80 个新增物品是可拿取和查看的收藏样本，其旧版使用或放置功能仍待复原。

|交付|位置|
|---|---|
|公开 JAR、SHA 与私有版构建入口|[安装与构建](../../deliverables/r1/README.zh-CN.md) · [公开 JAR](../../deliverables/r1/mfqm-reborn-r1-public.jar) · [文件清单](../../deliverables/r1/ARTIFACTS.json)|
|逐 ID 内容与剩余缺口|[差异矩阵](../../reconstruction/mapping/CONTENT_PARITY_MATRIX.csv) · [旧对象和现代注册统计](../../reconstruction/checks/REGISTRY_COUNT_RECONCILIATION.json)|
|创造栏顺序、类型、名称及 NBT|[实际导出](../../reconstruction/manifest/MODERN_CREATIVE_RUNTIME.csv)|
|测试结果与原始记录|[场景结果](../../reconstruction/checks/R1_TEST_RESULTS.json) · [日志、探针和 JUnit XML](../../deliverables/r1/logs)|
|Windows 玩家验收|[一页操作指南](../../deliverables/r1/USER_TEST_GUIDE.zh-CN.md)|

仓库 Tiary-art/MFQM-Reborn，分支 reconstruction-r1-content。基线 `790ddadeeb364057969488aabfa30db2003c1160`。两次运行时实现提交为 `05b65ae`、`68296e6dc3cc578e209e67d6b9b7457b27347090`。交付 JAR 对应后者，Forge 工程树 `ffd93033b1f77aa044075469fe65ba99bef6aace`。后续提交包含清单、脚本、日志和成品。原版只读输入 SHA-256 为 `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

## 原版证据与现代内容

R0 的 210 行拆为 131 个注册相关调用点和 79 个显式栈用途。另检出直接构造的 tabMFQM，原版现有 132 个候选身份、174 个已识别栈。67 个静态 append 中有 18 个属于 int 参数重载。原版运行时创造栏总数未知。174 个旧栈中 153 个已有现代表示，21 个仍缺，涉及棕黏土深浅、蜡木方位、泥沼 9、沼泽草和卷须。现代 Forge 有 244 个 mfqm 注册对象，其中物品 154 个。153 个 R0 身份均保留。六种计量口径分别有自己的证据。

新增的稳定 ID 覆盖工具和装备样本、食品、药水与按旧 damage 展开的物品模型；六种食物使用已查证的食物属性。Mud 的三种额外深度复用既有物品及 BlockStateTag。旧版英文 addName、语言文件和现代名称分列，部分对象的两种旧证据互相冲突。当前简中为项目翻译。

## 构建与实际测试

|场景|结果|
|---|---|
|Java 17 clean test build、Forge GameTest|PASS。46 个 JUnit、44 个必需 GameTest 全通过。比 R0 多出的 1 个 GameTest 实际枚举注册对象、构造创造栏、验证新增物品类型和每个栈的 NBT 往返。|
|公开成品 JAR|PASS，SHA-256 `ddb1636a189686e79f57e6dc454af3e681664c17ed338b2d0449145cd94488ee`。独立打开并核对版本、实现类、目录及模型引用，包含 210 个模型、0 个 PNG、0 个 OGG。|
|私有成品 JAR|本地构建和包内校验 PASS，SHA-256 `0e61774ae553fc9b736298a5cb4d5ca465d130a4145bb4bfe7035e9352fb028d`。289 个导入项的哈希已核对，含 119 个 PNG。公开交付中只有路径、哈希、脚本及无像素日志。|
|Linux Forge 开发客户端|公开版单人、私有版单人及一台私有客户端连接本机离线专服，均进入世界、绘制 153 个栈、执行资源重载并退出。每次资源重载后缺失模型和缺失 particle 均为 0。|
|旧世界|打开并保存了早期 Phase9 测试世界副本。旧玩家真实背包、所有历史状态和跨整合包迁移 NOT_RUN。|
|原版 1.7.10、Windows 正式启动器、正式安装 JAR 启动、其他模组组合、逐件人眼对版|NOT_RUN。专服日志包含 Forge 数字 ID 调整；离线环境出现 Mojang 公钥请求错误，GameTest 退出还记录了 Forge 配置跟踪器移除警告，Linux 客户端没有音频设备。|

旧 Phase9 日志记录 mucus 流动纹理帧尺寸无效，影响物品模型和世界 level=8。R1 保留原 PNG，修正生成的动画元数据为 32×16。私有客户端在重载前后均读到 19 帧。用户此前报告的所有紫黑对象仍需对照实际 ID 和资源包；U-01、U-02、U-03 均为 PARTIAL。

## 详细证据

- [注册路径、反射与条件](../../reconstruction/reports/R1_ORIGINAL_REGISTRY_DEEP_DIVE.md)
- [metadata、创造栏和名称](../../reconstruction/reports/R1_METADATA_CREATIVE_AND_NAMES.md)
- [资源、动画、模型与渲染](../../reconstruction/reports/R1_ASSET_MODEL_AND_RENDER_AUDIT.md)
- [实现与 R0 台账变动](../../reconstruction/reports/R1_IMPLEMENTATION_DIFF.md)
- [兼容测试范围和回退](../../reconstruction/reports/R1_COMPATIBILITY_AND_ROLLBACK.md)
- [21 个未映射栈及下一项验证](../../reconstruction/reports/R1_UNRESOLVED_AND_NEXT_STEPS.md)
