# Phase 1–8 历史交付审计

main 输入基线 `6a44d6f`，审计快照 HEAD `0229831`，不覆盖或改写旧报告。细项见 HISTORICAL_DELIVERY_AUDIT.csv（1062 行）及 history-audit-details.json。PRESENT_VERIFIED 在文件行表示存在、跟踪、当前哈希可核验，不代表重新执行了历史全部玩法。16 份已有 SHA 清单共 1950 条，缺失 0、哈希不符 0；未以研究阶段没有安装 JAR 判失败。

| 阶段 | 证据路径 | 结论 | 严重程度 / 处理 |
|---|---|---|---|
| Task001 研究 | research/task-001/ | PRESENT_VERIFIED；347 条校验匹配 | 无新增缺口 |
| 原版机制 Phase1 | research/original-mechanics-phase1/ | 当前研究文件跟踪；未重新运行全部反编译工作 | 历史运行仅文档证据 |
| Task002 / Task003 | deliverables/task-002/、task-003/ | 安装 JAR 存在；Task003 清单已由前次补交修复 | 旧缺口已修复，本次不重造旧 JAR |
| B1 / B2 | deliverables/task-0035-b1/、task-0035-b2/ | 二进制跟踪；保留历史测试边界 | 不宣称旧版玩法现已全部实现 |
| Original Phase2 | research/original-phase2/ | 493 条校验匹配，研究报告/工具存在 | 无新增缺口 |
| Original Phase3 | research/original-phase3/ | 196 条校验匹配，当前映射引用其 CFR 证据 | 无新增缺口 |
| Original Phase4 | research/original-phase4/ | 261 条校验匹配 | 无新增缺口 |
| Original Phase5 | research/original-phase5/ | 332 条校验匹配 | 无新增缺口 |
| Phase6 | docs/phase6/；legacy/StuckLease、DryQuicksandCore | 59 条校验匹配；独立发布 JAR NOT_REQUIRED | 任务/报告没有承诺独立发行，不推断遗失 |
| Phase7 | docs/phase7/；integration/StuckAdapter | 62 条校验匹配；独立发布 JAR NOT_REQUIRED | 报告明示未分发新 gameplay JAR |
| Phase8 | docs/phase8/；integration/OriginalContactBridge；deliverables/phase8/ | 78 条清单匹配；最终受控 JAR 已跟踪 | 过去仅 workspace 产物缺失为高严重度，PR15/edeb2f1 已修复，SUPERSEDED |

Phase8 当前交付 JAR：`deliverables/phase8/mfqm-reborn-phase8-controlled.jar`，SHA `1480c2746cdc64fb93563e652114769cbf0501a24baf71473c0469e3ce001a77`。docs/phase8/ARTIFACTS.json 记录最终源码 da9af36、补交重建 EXACT_MATCH；JAR 含 Phase8 实际类，不是改名 B2。其内部版本字符串仍旧 B2，是中等标识风险，保留历史二进制并解释。Phase9 已独立采用 `0.0.9-phase9-resources`，不靠文件名辨认阶段。

当前存在 Phase6–8 核心类；本次重新运行基线及候选 43 个 GameTests、候选干净构建 46 个 JUnit（基线 JUnit 沿用缓存 XML，未冒充重新执行） 验证现有受控边界，包括 B1/B2 运动、Stuck 租约、自动碰撞域。源码比较证明这些代码未改。研究报告中的未移植项、Phase8 的玩家/全部材料/垂直物理/自然生成缺口仍然存在，属于功能边界，不是本次交付遗漏。

扫描 16 个可访问历史 Git 工作树：未发现被遗漏的未跟踪项目路径。忽略的 build/run、原版私人输入、临时依赖缓存不等同于应公开项目交付。`/workspace/outputs/MFQM-Phase8` 当前可访问的副本已列哈希，均分类为 SUPERSEDED 工作区副本。无法证明本环境之外、未提供的旧 ZIP/已销毁工作区完整性，记为 NOT_VERIFIABLE，不推断丢失。用户所称 `MFQM-main (13).zip` 本轮未作为独立字节输入取得，使用实际 Git main 基线，未伪称审计过该 ZIP 的全部字节。

本次没有发现还需重建的可信历史必需产物；无需用户补旧文件。Phase9 本身补充仓库内公开 JAR、SHA、构建入口及 Git archive 检查，防止再次仅留工作区。私有素材 JAR 不进入公开 ZIP 属于授权边界，已给本地脚本。

扩大审计还逐项列入当前 Forge 源码/配置/资源/测试、旧 gameplay 报告与工具及 Task002/003/B1/B2 安装目录。共 1062 行，16 份历史清单1950条均匹配；日志 history-audit.json 的516行/1828条为初次范围，已由 history-audit-expanded.json 的扩大范围取代，非哈希不符。旧审计 evidence/SHA256SUMS 按原报告父目录解析，其他按清单所在目录，不通过猜测文件名隐藏缺失。
