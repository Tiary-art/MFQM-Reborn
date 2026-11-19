# 三材料完整差异矩阵

旧版栏均为O-BC/O-AN静态证据，**不是旧版实机结果**。当前栏为N-SRC；TEST/TRACE只表示任务003历史证据，不是本轮重测。状态逐单元对应[audit-index.csv](audit-index.csv)，来源键可点击展开于[README](README.md#证据键csv用此表展开)，人工验收M-Cxx见[矩阵](MANUAL_ACCEPTANCE_MATRIX.md)。

| 单元 / 状态 | 原版 Quicksand / SoftQuicksand / Mud | 当前实现与差异 | 证据与验收 |
| --- | --- | --- | --- |
| C01 已实现且有证据 | 三独立Block与ItemBlock，Mud有meta0..3 | 三稳定小写ID/BlockItem、独立资源/名称/创造栏；Muddepth0..3可用但普通放置默认0 | REG；CoreMaterialGameTests.registeredMaterialsPlaceAndDrop；M-C01 |
| C02 部分实现 | 玩家与非玩家有不同旧Y/k；上方同类分支；Mud池形 | 三者统一现代AABB/脚深；SAMPLE中心±4/上4、连续列16上限；超过边界可能截断，不是旧k公式 | QS.func_149670_a L88；SOFT L104；MUD L199；SAMPLE L18；M-C02 |
| C03 部分实现 | checkEntityUnder与MFQM.isEntityInsideOfBlock*眼部；渲染S变体另偏移 | 眼点独立于身体；SS连续列补覆盖，但采用单点和现代0.85表面；不同眼型/第三人称未普测 | SAMPLE L58；MFQM.isEntityInsideOfBlock/S/M/L；M-C03 |
| C04 部分实现 | QS横向0；位移/转向判定参与movKofDiv和mr | QS速度0；移动只看水平接受位移，转向未参与；移动惩罚用输入velocity，不等于旧位移惩罚 | QS L145–163；MATH L36；ENGINE L80；M-C04 |
| C05 部分实现 | QS0.075等分段支持；跳跃/上升位移/随机时钟吸力；原生web混合 | 固定深度公式、8tick意图吸力，无旧随机/第二吸力/web/onGround规则；不是旧净浮力曲线 | QS L255；MFQM.suctionWorldCheck；MATH L39；M-C05 |
| C06 部分实现 | SS0.71阻尼，多个0.0715/0.0735段，mr175；Mud深区0.71/着地0.1、快降/10 | SS独立profile但单条支持曲线；Mud也用近似曲线。旧Mud mtd0在L321–328提前返回（非玩家额外浮起），现mtd0仍走全solver/stuck。SS旧硬度2.0、现1.0亦未说明为忠实恢复 | SOFT L171；MUD L317；MATH L40；REG；M-C06 |
| C07 部分实现 | SS深区中心环带0.075≤r<0.5，分母max(10,km*50) | 保留环带/方向，触发换为immersion≥0.5；Pig用例与玩家正中心样本不能互相代替 | SOFT L284；MATH L46；softQuicksandDeepCenterPull；M-C07 |
| C08 已实现且有证据 | Mud8邻、±2/±3、上液体、安全边缘；QS/SS无该池深 | 离散几何及形状支撑有JUnit/live GameTest证据；现代FluidState非空/isSolid与旧Material语义需兼容回归 | MUD L76/149；MUDGEOM；liveMudPoolGeometryAndShapes；M-C08 |
| C09 已实现且有证据 | QS/SS碰撞null；Mud顶0.7/0.5/0.25/空，受上Mud约束 | 对应空形状/离散Mud形状已存在且有自动证据；不代表射线/视觉/所有实体行为恢复 | QS L341；SOFT L345；MUD L176；SHAPE；M-C09 |
| C10 实现但行为疑似错误 | SS上方同类时下层bounds=1，否则0.85；QS不矮；Mud碰撞与视觉分开 | SS模型和getShape恒0.85，state无连接属性；生理列补满不能补渲染缝。跨材质连接未获旧规则支持 | [旧SS L92](../../../research/task-001/evidence/BlockSoftQuicksand.analysis.txt#L92)；SHAPE L30；MODEL；M-C10 |
| C11 待验证 | 三块继承选择/交互路径；不能用空碰撞推断射线穿透 | getShape仍非空，Mud选择满格；内起点可能先命中所在/头顶沙，BlockItem按命中面邻格放置；纠偏也可能移动视点 | SHAPE；VANILLA BlockGetter.clip/BlockItem.place；M-C11 |
| C12 未实现 | QS随机1/5、SS1/2在下方条件满足时setBlockBelow+removeSelf，LiqFixer门控；Mud无相同自有下降方法 | 三者均extends Block，copy(SAND)只复制属性，未继承FallingBlock，也未实现旧条件移块。不能将Mud一并强制FallingBlock | [QS L350](../../../research/task-001/evidence/BlockQuicksand.analysis.txt#L350)、[SS L354](../../../research/task-001/evidence/BlockSoftQuicksand.analysis.txt#L354)；REG；M-C12 |
| C13 部分实现 | QS/SS普通采集给原版沙，丝触自身；Mud可按MudBallID掉4球 | 现三者统一self loot；不是旧生存获取链。未移植MudBall/配置，B需决定等价替代或保留差异 | QS L472；SOFT L467；MUD L586；LOOT；M-C13 |
| C14 未实现 | QS/SS未onGround时极慢挖掘；Mud返回−1；与旧伪ground耦合 | 没有对应挖掘速度门控；不能直接复制旧onGround黑箱 | 三类func_149737_a；SHAPE继承普通Block；M-C14 |
| C15 未实现 | QS邻岩浆→MFQM.SandBlock；SS→Blocks.sand；fizz/smoke，加入/邻变调度 | 无scheduled/random tick转换；QS旧转换目标尚未移植，不能悄悄替成同一种材料 | QS L398–436；SS L402–440；M-C15 |
| C16 未实现 | 三者非Living低阈值setInWeb；Mud/SS还有触手处理调用 | ENGINE只遍历LivingEntity；物品和Boat完全不进采样/阻力路径。普通碰撞仍可能支撑Mud | QS L336；MUD L549；SOFT末尾；ENGINE L29；M-C16 |
| C17 已实现且有证据 | 原版模式相关处理与本轮目标不同，不能称逐条件等价 | 创造/旁观/无敌跳过生理和运动是003明确策略；Mud实体碰撞仍存在，创造≠对全部Mud形状noclip | ENGINE.exempt；creativeSpectatorAndInvulnerableAreExempt；M-C17 |
| C18 未实现 | 三者调用antiHoldJumpScript，Mud有真靴分支，负重/盔甲/救生衣 | 统一裸装近似，未实现装备依赖；未来包，不顺手加入B | MFQM L2236；MUD L283；M-C18 |
| C19 未实现 | 三类有材料专属Blob、兼容维度/生物豁免或再生 | 新通用免疫非这些旧特例；生物内容未注册，兼容待独立计划 | QS/SS/MUD Living分支；M-C19 |
| C20 已实现且有证据 | 旧逐块碰撞；跨材料顺序受引擎影响 | 新每tick守卫、体积分数主材料，同分SS>QS>Mud；这是有意现代规则，有混合用例，不冒称旧版优先级 | ENGINE L44；SAMPLE L45；sameAndMixedCellsSettleOncePerEntityTick；M-C20 |
| C21 已实现且有证据 | 旧PotionStuck瞬时状态与固定UUID；负幂/打包危险分支 | finite夹取、一个自有临时modifier、清理且保留外来modifier；不复制旧bug | POTION；MATH；ENGINE L147；TEST；M-C21 |
| C22 部分实现 | AirEvent引用EntityRope数组：QS4/Soft17/Mud29均参与，排除15实际是MeatHole；damage另查air | 三者眼覆盖−1/恢复+5及16tick链有旧机制依据；现代眼坐标/采样、关开关时钟/非默认组合仍有差异或未验，不混用渲染数组 | [AirEvent L135](../../../research/task-001/evidence/AirEvent.analysis.txt#L135)、[实际数组L85](../../../research/task-001/evidence/EntityRope.analysis.txt#L85)、[指令核对](evidence/legacy-air-map.json)；ENGINE L95；M-C22 |
| C23 未实现 | 旧客户端min(customAir,vanillaAir)，QSCAir控制原生图标自绘 | 当前只文本HUD且不联动原生air；003目标最小链通过不等于用户气泡栏需求完成 | AIR L128；OVERLAY L50；HUD；M-C23 |
| C24 部分实现 | 三材料checkPlayerMuddy + level/type/time，Mud有单独规则 | 仅residueType/ticks，没有覆盖等级和外观同步；生理air同步不等于污泥同步 | QS L540；SOFT L491；MUD L669；STATE；M-C24 |
| C25 未实现 | 湿润减时、分级清洗、干燥类型残留、LiquidMire排除 | 仅离池residueTicks递减，无湿润/等级/类型阈值 | MUDDY L42；ENGINE L109；M-C25 |
| C26 已实现且有证据 | 旧ExtendedProperties/Watcher，死亡有位污染，重生迁移保证不全 | 现短期不存NBT，death/clone/dimension/logout/invalidate重建；历史最终实机有证据，非所有异常均测 | STATE；最终15/16/17日志；M-C26 |
| C27 部分实现 | 生理依赖Watcher；救援另3C2S消息 | 当前专用方向/UUID/维度/tick快照与boolean意图；历史280配对只比较5字段，未验全部眼字段/旁观流 | NETWORK；20-final-dedicated-sync.json；M-C27 |
| C28 待验证 | 原端侧/重力/web混合，不能直接作新版权威方案 | END速度包+每tickteleport预算，多决策源可能打架；OBS-07最新未复现，CSV无correction_count不可证明根因 | ENGINE L63/L117；MATH L20；M-C28 |
| C29 实现但行为疑似错误 | QS/SS快降/2；Mud深区/10后再分段支持 | 新netY夹−0.25，但活跃前不做位置预算；已落下的位移不会靠速度包倒回。入沙深、玩家积分/包批次与终端曲线需补测 | MATH L34–41；ENGINE顺序；TRACE fast_fall；M-C29 |
| C30 待验证 | 旧在多个分段写fallDistance/ground；不是全局取消坠落 | 当前只服务端END统一清fallDistance；client move/碰撞声音可能先触发，缺两端前后顺序证据 | ENGINE L89；VANILLA LivingEntity.causeFallDamage；M-C30 |
| C31 未实现 | 旧onFOVUpdateEvent在stuck时保留历史FOV并单独处理拉弓 | 当前移动属性参与Vanilla FOV，无局部补偿；不能通过全局FOV effects=0解决 | POTION L158；ENGINE L159；VANILLA；M-C31 |
| C32 未实现 | renderInsideOfBlockR材质遮挡、S变体眼检，配置可强制第一人称 | 现isViewBlocking=false且无自定义遮挡，缺少视野遮挡有直接代码原因；不应同时恢复强制视角副作用 | OVERLAY L93；SHAPE L18；M-C32 |
| C33 未实现 | QS/SS有环境显示tick，Mud有身体/动作/深区气泡；随机、client、QSBubble门控 | 没有粒子/EntityBubble注册或触发。Mud空池环境泡的旧规则不能由QS复制推断 | QS L448；SOFT.func_149734_b；MUD L380–411；MFQM L2446；M-C33 |
| C34 未实现 | swim/slime/silverfish/water/lavapop等原生键 + 蜂自有OGG | 当前没有对应触发；复制Minecraft soundtype仅普通脚步/落地，不是原MFQM声音。历史OpenAL失败另列限制 | ASSETS/sounds.json；三块原碰撞；REG；M-C34 |
| C35 部分实现 | 三静态PNG及SS三metadata纹理；全mod48动画 | 当前公开vanilla占位；私有3静态历史加载过，动画及SS变体未恢复/未验 | MODEL；私有工具；07/16日志；M-C35 |
| C36 待验证 | 旧端侧系统不等于延迟稳定 | 只有回环单客户端，50/150/300ms、两客户端、低TPS/观众/乘客未测 | NETWORK；TRACE；M-C36 |
| C37 部分实现 | 同类上方与两格、不同材料阈值，不是统一连续介质 | 当前同block列最多16、体积限制、混合确定优先级；长柱/跨材质眼面/邻块更新未完整测试 | SAMPLE L35；M-C37 |
| C38 部分实现 | 多项氧气/覆盖/气泡/装备/伤害/透明等配置 | 仅player/mob oxygen和damageMultiplier；非默认组合未实测，其余没有 | CONFIG；M-C38 |

Boat另列[专项](BOAT_COMPATIBILITY_AUDIT.md)，不把空碰撞、水中外观或Living轨迹当作船只兼容证据。新人工步骤均未执行，历史通过仍按原构建阶段标明。
