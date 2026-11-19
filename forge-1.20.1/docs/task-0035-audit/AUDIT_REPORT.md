# MFQM Reborn 003.5-A审计总报告

**本次仅审计，没有修复。** 基线为已合并Task003的main `0c3295161b0dae91ee2a12ccaeebdd6770776469`，独立分支`codex/mfqm-task-0035-audit`。日期2026-11-18（北京时间）；目标仍为Minecraft1.20.1 / Forge47.2.0 / Java17 / modid mfqm。运行时代码、资源、参数、原JAR、历史研究与Task003交付均不改。B/C、004/005未开始，后续须用户审核。

## 执行摘要

审计不是把已知用户反馈换个说法列一遍：除OBS-01..14与新增Boat项，还核对了三材料完整进入/退出、形状、更新/重力、采集、装备、非Living、特殊免疫、氧气、状态/显示等路径；从任务001全类/注册/资源盘点建立后续归属。发现旧同类Soft层叠填满、QS/Soft条件移块、旧采集/丝触/挖掘限制等不能被“通用减速已经通过”覆盖的差异。还逐指令核对了同名quicksandIDS数组：AirEvent使用EntityRope的4/17/29三核心索引，不能误用渲染数组的4/15/26推断Soft被排除。

重要的已证事实：

1. 旧Soft在上方同类时下层bounds=1.0，当前模型/outline恒0.85；同类缝隙有直接几何原因。
2. 旧QS/Soft具有条件随机向下移块，不是FallingBlock实体；Mud无相同自有下降分支。当前三者普通Block都没实现对应更新。不能把用户“沙式重力”目标当作三材料共同旧规则。
3. 当前Boat不进Living专用采样/solver/capability；三块又无可划船FluidState。QS/Soft无碰撞支撑时得不到水的浮力，继续Boat自身重力。Mud须按实际形状区分支撑/下沉。旧MFQM没有找到专用Boat浮力分支，通用非Living web存在；旧船实机漂浮/缓沉仍未证。
4. FOV补偿、眼部专用遮挡、原生气泡栏显示、覆盖等级/洗净/渲染、气泡/流沙声音触发均有明确未完成部分。它们不是单凭改一张纹理即可恢复。
5. OBS-07/09/11可能共享现代运动时序/预测/纠偏问题，但没有证据认定同根。Y抽搐仍为**间歇性待复现**。现CSV缺两端fallDistance/correction count/sound事件，不能宣布定位或修复。

## 统计口径与遗漏数量

以[audit-index.csv](audit-index.csv)的**51个互斥计数单元**为准：38个核心/跨机制单元、12个全局内容/架构单元、1个Boat单元。它们粒度不同，数量不是bug数量或完成百分比；三材料交叉表、14个OBS、人工参数组合、161类与302资源不再叠加计数。`已实现且有证据`仅指该单元限定合同有源码/历史证据，不代表旧版逐数值一致或用户验收。

| 状态 | 单元数 | 本次含义 |
| --- | --- | --- |
| 已实现且有证据 | 7 | 注册、限定Mud几何/碰撞、模式豁免、聚合、finite/属性清理、生命周期等已有证据 |
| 部分实现 | 14 | 有功能但缺原分支、状态、资源范围或组合验证 |
| 未实现 | 21 | 明确缺少相关功能路径/内容；包括Boat当前兼容路径 |
| 实现但行为疑似错误 | 2 | C10层叠几何、C29入射/实际速度；前者结构性差异明确，后者反馈与时序仍需运行定位 |
| 待验证 | 4 | 内部射线、纠偏稳定、落地声、延迟多人等，不能靠静态定案 |
| 原版规则不明 | 1 | G11代表五个未完整结构化生成方法的精确拓扑缺口 |
| 不适用（有证据） | 2 | 不复刻旧未调用反射路径、危险Watcher/全局槽/协议语义 |
| 合计 | 51 | 不按类/表格重复累计 |

**明确未完整实现的功能单元35个=21未实现+14部分。** 另有2疑似、4待验证、1旧规则不明，共7个待定位/补证单元；总计42个需处理或补证，不等于42个已确认缺陷。2个不适用是有意现代化/死路径排除，不计功能遗漏。统计由只读脚本输出[audit-check.json](evidence/audit-check.json)，不是手写完成率。

## 最高优先级问题与证据定位

| 优先级 | 项目 | 已证事实与假设边界 | 入口 |
| --- | --- | --- | --- |
| P0 | OBS-07 / C28：Y抽搐 | N-SRC：END写速度+条件teleport；U：偶发、最近未复现。H：预测/包批次/表面切换耦合。没有新复现，不写已修复 | [SinkEngine L63](../../src/main/java/art/tiary/mfqm/physics/SinkEngine.java#L63)、[L117](../../src/main/java/art/tiary/mfqm/physics/SinkEngine.java#L117)、[SinkMath L20](../../src/main/java/art/tiary/mfqm/physics/SinkMath.java#L20) |
| P0 | OBS-09 / C30：池底落地音效 | N-SRC：只在server END清fallDistance；Vanilla move/落地伤害/音效可先发生。H：两端历史/处理顺序；声音是否伴随伤害尚无现场 | [ENGINE L89](../../src/main/java/art/tiary/mfqm/physics/SinkEngine.java#L89)、[Vanilla方法hash](evidence/vanilla-methods.json)、[专项](PHYSICS_AND_INTERACTION_AUDIT.md) |
| P0 | OBS-11 / C29：快速入沙 | N-SRC：首次active前不做玩家预算，快降再叠近似netY。H：哪些因素导致用户觉得过快仍待测；water不是旧数值证据 | [MATH L34](../../src/main/java/art/tiary/mfqm/physics/SinkMath.java#L34)、[QS历史CSV](../task-003/traces/phase2/quicksand_fast_fall_13024_14.csv) |
| P1 | OBS-04 / C10：同类层叠 | O-BC：上同类下层填满；N-SRC：恒0.85。跨材质连接规则仍未证 | [旧Soft L92](../../../research/task-001/evidence/BlockSoftQuicksand.analysis.txt#L92)、[对应字节码](../../../research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockSoftQuicksand.bytecode.txt#L66)、[模型](../../src/main/resources/assets/mfqm/models/block/soft_quicksand.json) |
| P1 | OBS-12 / C11：内部放置 | N-SRC：outline非空、无内部交互特殊规则；H：内部hit面/纠偏眼位置。不能未测就让所有射线穿透 | [SinkingBlock L30](../../src/main/java/art/tiary/mfqm/physics/SinkingBlock.java#L30)、[交互专项](PHYSICS_AND_INTERACTION_AUDIT.md#2-方块形状堆叠与内部射线obs-04--12) |
| P1 | OBS-13 / C12：重力 | O-BC：QS/SS条件移块、概率/调度门控；Mud无相同自有路径；N-SRC全缺该更新 | [QS原指令L1299](../../../research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockQuicksand.bytecode.txt#L1299)、[Soft原指令L1514](../../../research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockSoftQuicksand.bytecode.txt#L1514) |
| P1 | MFQM-003.5-BOAT-01 | 当前船体被排除、无水支持路径是代码事实；某次沉底时刻/速度与旧船漂浮仍需复现/旧证。不能给Boat套玩家solver | [ENGINE L29](../../src/main/java/art/tiary/mfqm/physics/SinkEngine.java#L29)、[SAMPLE L13](../../src/main/java/art/tiary/mfqm/physics/ContactSampler.java#L13)、[船只专项](BOAT_COMPATIBILITY_AUDIT.md) |
| P1 | C22/C23：储气合同与原生气泡栏 | O-BC：三核心索引4/17/29均参与，旧客户端min联动/可自绘图标；N-SRC现在文本HUD。水交互、最大气息与非默认配置需规格，不应虚构Soft排除项 | [实际数组指令核对](evidence/legacy-air-map.json)、[旧UI L50](../../../research/task-001/evidence/CustomRenderOverlayEvent.analysis.txt#L50)、[状态专项](STATE_AUDIO_VISUAL_AUDIT.md) |

OBS-01创造/旁观/无敌豁免是003目标中的正常行为，不当作故障。OBS-02/03/05/06/08/10的未完成项与根因假设在[USER_OBSERVATIONS](USER_OBSERVATIONS.md)逐条列明，OBS-14通过全量目录扩展，不只搜索13个关键词。

## 本次实际执行了什么

| 类型 | 本次结果 | 不能据此声称 |
| --- | --- | --- |
| 原JAR只读复核 | SHA256仍为`2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`；463文件hash、161类/1955声明方法元数据、247PNG一致 | 原版游戏已经运行或机制已还原 |
| 全量目录 | 161类、302非class、49Block/43显式Item/16实体/13Fluid静态注册均有去向 | 每个方法1955条路径均完整语义验证；有条件注册实际成功 |
| Vanilla/Forge对照 | 只读缓存Forge47.2.0映射字节码及官方sources中的Boat补丁/IForgeBoat；方法hash入档 | Boat/客户端新测试已经通过；旧版Boat也使用同一算法 |
| 历史003日志/CSV | 核对18JUnit/15GameTest和真实回环280配对的已有日志；重新只读统计CSV | 用户已亲测通过；本轮重做了这些运行测试；Boat/音频/高延迟已有证明 |
| 文件范围核查 | 546个既有跟踪文件按原Git检出过滤逐字节比较，未变；新增/变动都在本审计目录 | 这是新运行时构建验证 |
| 文档/引用/矩阵校验 | 必需9份报告、51单元、14观察、相对引用与人工空白结果由脚本核查；见evidence输出 | 人工空白栏等于通过 |
| 新build/新游戏会话 | **0 / 0**（本任务只审计，不改运行代码） | 本轮修复或实机验收完成 |

范围证明含`git diff --stat`及`git status --short`见[evidence/git-scope.txt](evidence/git-scope.txt)。首版审计器直接比blob触发已有gradlew.bat CRLF误报，改为既有检出过滤后重跑；[记录](evidence/auditor-notes.md)。没有修改wrapper或通过重写原文件规避检查。

## 证据缺口与不可计成100%的部分

- 原始材料缺失项：本次JAR与任务001全部索引可用，文件级缺失为0；**旧实例实机轨迹、最终registry/recipe dump、配置/可选mod运行矩阵仍未取得**，不能把“文件齐”当“行为全知”。
- 五个CustomWorldGen方法未完整结构化：generateAOADimGardencia、generateWLD、generateABC2、generateNether、generateSurface。此为5个具体方法缺口、1个计数单元；其余全局系统本轮按类别/元数据/已有指令入口盘点，不声称1955方法逐路径验证。
- 13项具体用户反馈无本轮现场复现资料；Y抽搐明确仍待复现。既有CSV没记录落地声/纠偏/两端fallDistance，原音频设备失败也使声音验收无效。
- 当前无Boat测试代码、无Boat实机轨迹、无旧Boat漂浮证明；三材料+水的空/载客/延迟预期在专项中标为候选，不是已通过结果。
- 私有三静态纹理的003显示结果不能代替48动画、SS变体或异常32×304播放验证。未经授权素材/反编译源码未上传，无AI图。

## 可直接用于下一轮的任务建议

[IMPLEMENTATION_ROADMAP](IMPLEMENTATION_ROADMAP.md)已给每个B/C包输入、依赖、具体交付、风险与自动/人工回归：先B-OBS与B-MOTION/LANDING，再几何/射线/条件移块、Boat独立路径、AIR与掉落依赖；C分为局部FOV、遮挡、原生风格气泡栏、覆盖状态/渲染、气泡音效与资源/HUD。

需要用户审核D1..D7，尤其**气息水交互、QS/Soft下降与Mud边界、Boat“旧阻力”还是“新增漂浮”、内部射线、掉落依赖与数值容差**。本次交付已完成审计范围；等待用户确认下一轮规格后再写修复代码，不自动开始003.5-B/C或004。
