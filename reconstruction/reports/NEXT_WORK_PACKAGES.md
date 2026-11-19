# 按依赖与用户问题安排的工包

本表是后续入口，不授权现在启动。每PR同时改证据、实现、测试与矩阵；退出后以对象ID关闭缺口，不以阶段号计进度。

| 次序/工包 | 输入证据/具体改动目标 | 验证与退出门槛 | 风险与依赖 |
|---|---|---|---|
| R1-REG-0 原registry闭合 | ORIGINAL_REGISTRY、MFQM/CustomRegister/ItemMeta/ItemMetaColor；补动态registry/metadata/creative/name结构行，不先改ID | 条件场景旧Forge dump、现代dump、逐damage原名；所有未解标明 | 反射/可选依赖；先于任何内容注册修改 |
| R1-ASSET-0 缺图复现 | U-01具体JARhash/物品ID/log；RESOURCE_REFERENCE_GRAPH与RESOURCE_USAGE；检查blockstate/model/item/parent/texture/atlas/finalJar | Windows正式安装重现至少1例，私有包逐条校验+截图/reload；公开包不含素材 | 用户原问题证据待补；优先于宣称材质完成 |
| R1-CONTENT-1 内容/名称 | R1-REG闭合表；ModBlocks/Items/Tabs、lang/item模型；有证据才补安全条目 | 注册/visible/name/assets独立验收；已有存档ID不变 | 不把占位当行为parity，不同时开改ID分支 |
| R2-QS-0 单材料 | core接触descriptor、BEHAVIOR_CASES、MotionRuntime/SinkEngine/OriginalContactBridge | 原/新同输入ordered contact/RNG/Y轨迹，多接触/退出/低TPS，B1防抖无退化 | 先单材料，再Mud/Soft；不得整包替换 |
| R2-BOAT | LegacyFluids supportsBoating(false)与原核心非Living分支；原生水中Boat浸没检测/阻力/浮力对照 | QS/Soft/Mud分别空船/载人/流动/出入边界矩阵；玩家机制不变 | 根因未闭合不填PASS，不凭近似密度调参 |
| R3-STATE-0 污渍/清洗 | MuddyEvent/CustomVarPlayer/原mask与UV；SinkState、SinkEngine、network、CoatingLayer/Hands | 独立type/level/time、湿润/干燥/残留与NBT迁移；同步后才切渲染 | 保留residue旧键并测回滚；可在R1证据后先做分析 |
| R3-VISUAL | 状态闭合、私有原图；相机/FOV/声音与资源入口 | 第一/三人称、Alex/盔甲/遮罩、重载及多玩家 | 不套旧UV，不以开发类路径代正式包 |
| R4-WORLDGEN | Phase5有限oracle、DryQuicksandCore、surface共享blockGen/RNG、墓室/WLD | seed/写块flags/拒写/跨区块，先离线与隔离世界，再默认策略 | 不能把测试纯core当真实生成，禁用未知生态 |
| R5-COMPAT | 以上包对象矩阵、冻结清单与旧存档 | 正式JAR/专服/联机/升级回滚/整合包/性能，独立结果 | 真实体验验收不能被JUnit替代 |

每包通过前将不确定分支留在总表分母。R0已完成的数学事实直接消费历史向量；历史有冲突或输入域不匹配才重测，不从头重复全部解码。
