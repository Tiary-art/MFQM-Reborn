# R0 工程重整报告

总体 **PARTIAL**，不表述为MFQM全部移植完成。目标仓库为 Tiary-art/MFQM-Reborn；旧main `1db85f8` 的已跟踪快照导入新main `8814a448`，R0在独立 reconstruction-r0 分支。输入/工具/构建身份见 reconstruction/checks/。

| 子阶段 | 状态 | 实际结果 |
|---|---|---|
| R0-A 字节/基线索引 | PASS（字节身份范围）/PARTIAL（动态内容） | 独立读原463文件、161类、1955方法、721字段、300资源；基线冻结、所有原始条目去向；动态注册/全部变体尚不闭合 |
| R0-B 类档案与纵深 | PARTIAL | 161类各有不同成员档案；6重点模块的静态链、现代差异与测试方案见DEEP_FIRST_BATCH，10类入口已连；未宣称所有语义深度完成，完整深度类数保守记0 |
| R0-C 新旧矩阵/清理 | PARTIAL | 3510原对象主表、2364未映射行；现代301文件、1021编译成员、153源解析注册对象；双向身份映射、资源使用、全文件分拣及12重点决策。反射/完整动态调用/全文件深审待完成 |
| R0-D 工具与当前回归 | PASS（已覆盖范围） | 数据唯一键/外键/路径/全文件覆盖校验通过；确定性、缺输入失败、错误外键拒绝实测；clean构建46 JUnit/43 GameTests通过 |
| R0-E 可选运行时清理 | NOT_ATTEMPTED | 没有足够成对oracle/迁移/无双执行证明，不强改；运行时替换0、删除0 |

原版方法调用/字段指令边54811，未闭合内部声明目标3377（继承/虚派发等仍未知，不判死代码）。现代编译直接调用/字段边6596，配合import图，非完整反射/动态调用图。旧注册表210行是调用点与79显式metadata用途的子集，不是完整旧运行时条目总数；现代153也含dev block/source/flow/type，不能混淆分母。

具体定位：CoatingLayer统一vanilla全身纹理+min(.65,residueTicks/500)与原类型mask/level/time清洗有静态差异；MaterialProfile/LegacyBlocks等为待逐材料验证近似；StuckLease/Adapter的UUID与一次更新/清理属于有证据或现代必要职责，不直接删除。核心k/km、独立幂指数、Mud metadata安全分支、Soft图标选择、SSand/QS RNG顺序详见深度报告。

用户Windows紫黑、名称、数量、物理偏差独立登记U-01..04，污渍差异为U-05，全部OPEN。具体出错ID/hash/截图/log仍UNKNOWN，不用历史Linux截图或JUnit关闭。原JAR只读、未公开PNG/OGG/原JAR/私人构建；R0是分析工具交付，不发新玩法JAR。实际重建公开基线JAR SHA仍为 `13b0a9365fe56bac159c4864017c1c0d71719c141568df92f09f4e8cd188cc6d`，仓库原deliverables/phase9保留。

实际命令：forge-1.20.1内Java17.0.21/Gradle8.1.1，`./gradlew clean test build runGameTestServer --offline --console=plain`，退出0，2m6s，17任务全执行；5份JUnit XML共46通过/0失败/0跳过，GameTests43 required全部通过。原始日志gzip、可读日志、预期失败工具测试和校验JSON随仓库。原版1.7.10运行、本轮独立普通专服手工连接、Windows、正式启动器JAR安装、真实多人/整合包/迁移/完整视觉均NOT_RUN；GameTest专服启动不冒充这些体验验收。

后续按依赖执行R1-REG与一个具体R1-ASSET复现，再推进单材料R2、R3污渍、R4世界生成和R5兼容。R0-C全部人工深审、R0-B全部重要分支与原动态注册仍欠证据，故总体PARTIAL。此处停止，不自动开始R1。
