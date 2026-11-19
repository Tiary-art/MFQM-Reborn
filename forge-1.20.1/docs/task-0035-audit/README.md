# MFQM Reborn 003.5-A：机制完整性审计

本次**只审计，没有修复**。基线是任务003合并后的 `main 0c32951`（完整SHA见[evidence/audit-check.json](evidence/audit-check.json)），独立分支 `codex/mfqm-task-0035-audit`。日期2026-11-18（北京时间）。本目录以外文件不改变；Minecraft1.20.1、Forge47.2.0、Java17、modid=mfqm保持不变。003.5-B/C须用户审核后另行开发，004/005未开始。

## 导航

1. [全量原机制目录](ORIGINAL_MECHANICS_INVENTORY.md)、[161类归属附录](CLASS_COVERAGE.md)
2. [三材料差异矩阵](THREE_MATERIAL_GAP_MATRIX.md)
3. [OBS-01至14用户观察](USER_OBSERVATIONS.md)
4. [运动与方块交互专项](PHYSICS_AND_INTERACTION_AUDIT.md)
5. [状态、音效及视觉专项](STATE_AUDIO_VISUAL_AUDIT.md)
6. [新增船只项MFQM-003.5-BOAT-01](BOAT_COMPATIBILITY_AUDIT.md)
7. [003.5-B/C实施路线](IMPLEMENTATION_ROADMAP.md)
8. [人工验收矩阵（结果空白）](MANUAL_ACCEPTANCE_MATRIX.md)
9. [审计总报告及统计](AUDIT_REPORT.md)、[51个计数单元](audit-index.csv)

## 证据等级与限制

- **O-BC**：原JAR指令/资源事实；O-AN为旧反编译分析辅助解释，不是旧版实机。原始字节码优先于任务001/003报告中的概括。
- **N-SRC**：当前源码/模型事实；**HIST**：任务003历史日志/CSV，不是本轮重测，也不代表用户验收。
- **U**：附件列明的用户观察；BOAT项包含“快速沉底”观察。没有用户逐tick轨迹、坐标/配置/录像，不能从反馈直接确定根因。
- **H**：技术假设/设计建议，必须人工验证；本轮新游戏会话和新build均为0。人工结果栏空白。

原JAR私有可读，复核463个文件hash和161类/1955个声明方法元数据；247PNG保持不变。没有公开JAR/PNG/OGG或新增反编译源码，也没有生成贴图。161类和302个非class文件全部列入归属表，**这只是枚举覆盖，不能写成1955方法完整语义审计或100%行为还原**；三材料及指定跨机制深入核查，其他系统以已有指令/注册清单做类别盘点，生成算法五处仍不明确。

## 证据键（CSV用此表展开）

| 键 | 源码/原始证据入口 |
| --- | --- |
| QS | [BlockQuicksand分析](../../../research/task-001/evidence/BlockQuicksand.analysis.txt#L88)、[原指令](../../../research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockQuicksand.bytecode.txt)；碰撞func_149670_a、更新func_149674_a、采集func_149636_a |
| SOFT | [BlockSoftQuicksand分析](../../../research/task-001/evidence/BlockSoftQuicksand.analysis.txt#L92)、[原指令](../../../research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockSoftQuicksand.bytecode.txt)；形状func_149719_a、碰撞/更新/采集 |
| MUD | [BlockMud分析](../../../research/task-001/evidence/BlockMud.analysis.txt#L76)、[原指令](../../../research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockMud.bytecode.txt)；getMudDepth/getMudSafe/func_149668_a/func_149670_a |
| MFQM | [MFQM分析](../../../research/task-001/evidence/MFQM.analysis.txt#L2035)、[原指令](../../../research/task-001/evidence/MoreFunQuicksandMod__main__MFQM.bytecode.txt)；getMuddyLevel/isEntityInsideOfBlock*/antiHoldJumpScript/spawn*Bubble/isDrowning |
| AIR | [AirEvent](../../../research/task-001/evidence/AirEvent.analysis.txt#L122)、[原指令](../../../research/task-001/evidence/MoreFunQuicksandMod__main__AirEvent.bytecode.txt) |
| OVERLAY | [CustomRenderOverlayEvent](../../../research/task-001/evidence/CustomRenderOverlayEvent.analysis.txt#L50)、[原指令](../../../research/task-001/evidence/MoreFunQuicksandMod__main__client__CustomRenderOverlayEvent.bytecode.txt) |
| POTION | [CustomPotionEvent](../../../research/task-001/evidence/CustomPotionEvent.analysis.txt#L122)、[原指令](../../../research/task-001/evidence/MoreFunQuicksandMod__main__CustomPotionEvent.bytecode.txt) |
| MUDDY | [CustomVarPlayer](../../../research/task-001/evidence/CustomVarPlayer.analysis.txt)、[MuddyEvent](../../../research/task-001/evidence/MuddyEvent.analysis.txt#L42)、[MudModelRenderer](../../../research/task-001/evidence/MudModelRenderer.analysis.txt)及各自bytecode |
| REG / LOOT | [ModBlocks](../../src/main/java/art/tiary/mfqm/registry/ModBlocks.java#L14)、[ModItems](../../src/main/java/art/tiary/mfqm/registry/ModItems.java)、[掉落JSON](../../src/main/resources/data/mfqm/loot_tables/blocks) |
| SHAPE / MODEL | [SinkingBlock](../../src/main/java/art/tiary/mfqm/physics/SinkingBlock.java#L16)、[MudBlock](../../src/main/java/art/tiary/mfqm/physics/MudBlock.java#L43)、[Soft模型](../../src/main/resources/assets/mfqm/models/block/soft_quicksand.json)、[状态JSON](../../src/main/resources/assets/mfqm/blockstates) |
| SAMPLE | [ContactSampler.sample](../../src/main/java/art/tiary/mfqm/physics/ContactSampler.java#L13) |
| ENGINE / MATH | [SinkEngine.settle/reconcilePlayer](../../src/main/java/art/tiary/mfqm/physics/SinkEngine.java#L39)、[SinkMath](../../src/main/java/art/tiary/mfqm/physics/SinkMath.java#L20) |
| MUDGEOM | [MudGeometry](../../src/main/java/art/tiary/mfqm/physics/MudGeometry.java) |
| STATE | [SinkState](../../src/main/java/art/tiary/mfqm/state/SinkState.java)、[Capability](../../src/main/java/art/tiary/mfqm/state/SinkCapability.java)、[生命周期](../../src/main/java/art/tiary/mfqm/state/SinkLifecycle.java) |
| NETWORK / HUD | [SinkNetwork](../../src/main/java/art/tiary/mfqm/network/SinkNetwork.java#L28)、[ClientSinkState](../../src/main/java/art/tiary/mfqm/client/ClientSinkState.java#L24)、[SinkHud](../../src/main/java/art/tiary/mfqm/client/SinkHud.java#L18) |
| TEST | [CoreMaterialGameTests](../../src/main/java/art/tiary/mfqm/gametest/CoreMaterialGameTests.java)、[FoundationGameTests](../../src/main/java/art/tiary/mfqm/gametest/FoundationGameTests.java)、[JUnit](../../src/test/java/art/tiary/mfqm/physics) |
| TRACE | [003原日志](../../logs/task-003)、[24场景原CSV](../task-003/traces/phase2)、[最终专服CSV](../task-003/traces/final-dedicated) |
| CONFIG | [旧配置调用](../../../research/task-001/evidence/config_and_compatibility.txt)、[SinkConfig](../../src/main/java/art/tiary/mfqm/physics/SinkConfig.java) |
| ASSETS | [463文件清单](../../../research/task-001/evidence/archive_entries.csv)、[162块纹理映射](../../../research/task-001/reports/04_texture_inventory.csv)、[私有包工具](../../tools/private_legacy_pack.py) |
| GLOBAL | [类清单](../../../research/task-001/evidence/classes.csv)、[1955方法](../../../research/task-001/evidence/methods.csv)、[注册调用](../../../research/task-001/evidence/registration_calls.txt)、[配方/燃料](../../../research/task-001/evidence/recipe_calls.txt)、[全量归属](CLASS_COVERAGE.md) |
| VANILLA / BOAT | [船只专项](BOAT_COMPATIBILITY_AUDIT.md)及[evidence/vanilla-methods.json](evidence/vanilla-methods.json)，记录本机Forge映射构建方法hash；未复制Minecraft反编译源码 |

## 可复现的只读核查

```sh
# 仓库根目录；输入JAR路径替换为自己的私有文件
python3 forge-1.20.1/docs/task-0035-audit/tools/audit_readonly.py \
  --baseline 0c32951 --original-jar /path/to/original.jar \
  --vanilla-jar /path/to/forge-1.20.1-47.2.0_mapped_official_1.20.1.jar
python3 forge-1.20.1/docs/task-0035-audit/tools/validate_documents.py
```

第一个脚本只输出本目录的索引/统计，逐字节比较基线全部受跟踪文件，拒绝本目录外的新增/修改；不启动游戏、不加载mod。缺少原JAR/映射构建可省略参数，对应项会标未提供，不能说完成原件复核。脚本输出见[evidence](evidence)，范围证明见[evidence/git-scope.txt](evidence/git-scope.txt)。本轮复用了任务003缓存的官方Forge映射构建，只在仓库外私有反编译辅助阅读，公开仅记录方法签名/hash/语义摘要。
