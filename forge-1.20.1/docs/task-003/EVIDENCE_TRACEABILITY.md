# 原证据 → 现代实现 → 差异 → 验证

所有旧版结论来自任务001的静态字节码研究，未取得1.7.10实机轨迹。下表中的“保留”只描述具体机制/常量，绝不代表整体数值等价。对应证据文件均在仓库research/task-001/evidence；*.analysis.txt原有行号保留，*.bytecode.txt包含类SHA256、完整方法描述符及十进制偏移。

| 原始证据（类/方法/分析行） | 现代实现 | 明确差异/不确定性 | 验证入口 |
| --- | --- | --- | --- |
| BlockQuicksand.func_149670_a 151–163；bytecode同方法 putfield field_70159_w/field_70179_y | SinkMath: QUICKSAND横向速度清零，独立速度属性因子 | 属性因子与现代移动包共同作用，未复制旧web/onGround；不能推断旧净行走速度 | SinkMathTest；quicksandRealMobTrajectory；真实玩家CSV |
| BlockQuicksand.func_149670_a 255–321；0.075/0.07485、挣扎0.05/0.035；MFQM.suctionWorldCheck | MaterialProfile.buoyancy=0.075；SinkMath深度支持/运动惩罚/0.05吸力；SinkEngine8tick挣扎冷却 | 用现代表面-脚部深度d与体高归一化，不使用旧k。新支持公式=buoyancy/(1+0.08*d²)/movementPenalty，明确减去0.08作为净速度近似；不恢复随机微扰或旧随机序列。0.035附加随机吸力未移植 | JUnit深度/运动/挣扎；真实单人静止/走/跳/连跳/快速落入 |
| BlockQuicksand.func_149668_a 341–343 aconst_null/areturn | SinkingBlock.getCollisionShape为空 | 非LivingEntity只保留普通碰撞结果，不恢复掉落物web特例 | Live注册/放置；无碰撞资源实测 |
| BlockSoftQuicksand.func_149670_a 148、171–173；0.71阻尼、stuck175 | 独立SoftProfile，0.71，buoyancy0.0735，stuck上限175 | 不是Quicksand换色。旧k阈值和非整数幂替换为有限的归一化深度；没有NaN继承 | SinkMathTest；softQuicksandDeepCenterPull；玩家CSV |
| BlockSoftQuicksand.func_149670_a 284–298；0.075≤r<0.5，(center−pos)/max(10,km*50) | SinkMath软沙深区中心牵引，保留环带/分母常量，以现代depthBlocks代替km | 深区界限现代immersion≥0.5，不声称等于旧k<0.9；生物体高不同使用各自当前AABB/眼高 | JUnit环带边界；真实tick Pig中心距离变化；玩家样本 |
| BlockSoftQuicksand渲染顶面0.85和空AABB | 单独0.85模型与采样表面、空实体碰撞 | 暂不恢复旧meta0/1/2纹理变化；默认占位统一red_sand。内部连续列的生理表面查询覆盖相邻单元，列扫描最多16格 | JSON审计；客户端显示；映射草案 |
| BlockMud.getMudDepth 76–147；8邻格，±2/±3轴向，上方液体 | MudGeometry.poolDepth，MudBlock.grid | 核心离散分支保留；现代“液体”用非空FluidState，“固体”用BlockState.isSolid，第三方方块材料语义可能不同 | MudGeometryTest逐缺口；liveMudPoolGeometryAndShapes |
| BlockMud.getMudSafe 149–174 | MudGeometry.safeEdge，液体覆盖优先取消安全边缘 | 安全只降低Mud有效深度，不是免疫所有窒息/伤害 | JUnit/Live几何；mudCenterAndSafeEdgeHaveDifferentSupport |
| BlockMud.func_149668_a 176–196 | depth0..3 BlockState；0.7/0.5/0.25/空碰撞面，保留上方Mud深度条件 | 不沿用旧数字metadata ID；属性默认0、池几何可提升、边缘可降级 | JUnit四碰撞高度/堆叠分支；Live世界shape |
| BlockMud.func_149670_a 313–325、416–421 | 0.71水平阻尼；着地另乘0.1；快降除10 | 装备/负重/涉水靴未实现：本阶段所有无免疫LivingEntity按裸装处理；不虚构已移植靴子 | JUnit与真实Pig/玩家轨迹 |
| MFQM.isEntityInsideOfBlock 2077–2105；三个checkEntityUnder | ContactSampler眼点覆盖独立于身体接触；SinkEngine服务端伤害 | 使用现代eyePosition和局部表面，不复制旧玩家+1/非玩家−0.5等坐标偏移；仅三种核心材料 | 混合接触/空气GameTest；deep_oxygen玩家记录 |
| AirEvent.onEntityConstructing 49/60；onLivingUpdateEvent 134–151；bytecode sipush300 | Capability.air默认300，覆盖−1/未覆盖+5至300 | 不改原生水中air，HUD显示独立槽；仅本阶段三种材料，无旧quicksandIDS数组 | oxygenDamageThenExitRecoversAndPreservesForeignModifier；S2C字段配对 |
| MFQM.isDrowning 2598–2618；各块checkEntityUnder伤害 max(maxHealth*0.1,2)*DmgMul | 眼部覆盖、气息耗尽后每16tick最多一次服务端drown请求；配置倍率 | 原版关氧气开关会直接判true并由每碰撞回调请求伤害；现代关开关保留眼部伤害但固定16tick以避免多块重复。Vanilla hurt免疫/其他mod可取消实际扣血 | drowningDamageRequestCannotRepeatWithinOneTick；空气/退出GameTest |
| CustomVarPlayer get/set/NBT；MuddyEvent死亡setType(-1)位污染 | Entity Capability，独立字段；版本1NBT仅residueType/residueTicks | 不保存stuck/air/active；不复制负数打包溢出。污泥覆盖仅保留非视觉残留计时，旧10级覆盖/洗净/渲染未恢复 | actualEntityNBTStoresResidueButNoTransientState；死亡/重生/重进 |
| PotionStuck.save/load空；CustomPotionEvent 122–153 固定UUID、移除旧属性、瞬时续期 | 仅一个本模组UUID的TransientModifier，逐tick更新、退出/无敌/死亡/失效时移除 | 现代操作不改其他modifier，不复刻旧jumpMovementFactor或客户端FOV修正。与其他模组组合只做“外来modifier保留”测试，未做Mod生态联测 | 属性退出GameTest；NBT无残留；deathAndRemovalInvalidateTransientState |
| MFQM.isTrulySink玩家返回isRemote；原客户端重量/按键逻辑 | 服务端LevelTick END聚合、C2S仅boolean意图、S2C只读副本、原生velocity/属性同步 | 架构有意修正：不恢复客户端自行结算生理状态，不做自定义反作弊器。快照每5tick/进入退出发送，包含维度/实体UUID/服务器tick | 同tick多同种/混合单次结算；真实联机快照比对 |
| 原始逻辑未定义跨材料边界优先级 | ContactSampler按接触体积评分、同分Soft>Quicksand>Mud | 显式现代确定规则，不声称来自旧版；所有触碰块只有一套生理结算 | sameAndMixedCellsSettleOncePerEntityTick |

## 尚未完成的忠实性项目

- 真实玩家额外使用服务端每tick位移预算：水平上限max(0.02,组合移动属性×1.3)，下降上限max(0.015,min(0.35,abs(上次垂直决策)×1.5+0.003))，上升上限0.05（浅Mud为0.5）。这是修复现代客户端位置批处理绕过速度包的明确现代策略；玩家与生物可能具有不同净轨迹，延迟时可能出现位置校正。未取得旧版曲线，未做高延迟联机或第三方传送模组联测；小于16格且不发Forge传送事件的直接移动API可能被校正。

- 未恢复旧版周期/随机气泡音效、web频率、所有onGround伪装和客户端FOV；没有装备/背包负重、特定旧生物或旧维度免疫逻辑。
- 未恢复旧污泥覆盖视觉与完整NBT兼容；仅版本化新残留字段。旧存档转换不在范围。
- 未测1.7.10曲线，绝不能称“数值完全一致”。近似公式和归一化边界今后必须按旧实例轨迹校准；目前没有被掩盖的旧版等价断言。
- 物理列扫描最多16格、体积采样限制到实体中心±4格/向上4格，超大非标准实体需扩展/实测。
- 私有三核心材质是静态16×16PNG；动画资源与异常32×304是否加载成功单独登记，不能用静态材质结果代替。
