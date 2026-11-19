# MFQM-003.5-BOAT-01：船只浮力及运动兼容性

状态：**未实现**（指当前MFQM船体接触/阻力/浮力专用路径）；优先级P1，归003.5-B独立审核包。U“快速沉底”尚无本轮实机复现；下面区分可直接证明的代码缺口、对观察的机制解释和待批准的新预期。没有改Boat、SinkingBlock、流体、玩家或网络代码。

## 1. 原版MFQM是否有船只漂浮机制

**未找到三核心材料的专用船只漂浮机制；也不能由此声称旧版实机船必定快速沉底。**

- 对原始JAR161类常量池UTF8做了只读全量检查，显式Boat/EntityBoat引用为0，原件463文件hash与任务001一致，见[audit-check](evidence/audit-check.json)。字符串不存在只能排除这类显式引用，不能排除继承、间接通用Entity逻辑或外部运行时介入。
- 深入核对三入口`func_149670_a(World,int,int,int,Entity)`：Living分支内才有分段支持/浮力；非Living分支调用旧`Entity.func_70110_aj()`（setInWeb）而不是提供船体上浮。证据：[QS L119/L336](../../../research/task-001/evidence/BlockQuicksand.analysis.txt#L119)、[QS原指令](../../../research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockQuicksand.bytecode.txt)、[Mud L549](../../../research/task-001/evidence/BlockMud.analysis.txt#L549)、[Mud原指令](../../../research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockMud.bytecode.txt)、[Soft入口及尾分支](../../../research/task-001/evidence/BlockSoftQuicksand.analysis.txt#L104)、[Soft原指令](../../../research/task-001/evidence/MoreFunQuicksandMod__main__blocks__BlockSoftQuicksand.bytecode.txt)。Mud/Soft另有触手调用，不是船浮力。
- 旧QS/Soft构造用`Material.field_151595_p`，Mud用`field_151578_c`，均extends Block，不是本mod的13种Fluid类；不能从“流沙外观像液体”推导Vanilla水浮力。旧SRG材质通常对应sand/ground，三者并未以water字段构造。
- 通用web可能改变非Living速度与运动历史，**这有别于恢复表面浮力**。本次未启动1.7.10、未审计旧Vanilla Boat全生命周期，旧空船/有人船净曲线仍待旧实例补证；不能为迎合新期望编造“旧版船一直漂浮”。

## 2. 当前三个组件是否处理Boat

| 组件 | N-SRC结论 | 影响 |
| --- | --- | --- |
| [SinkingBlock L13–31](../../src/main/java/art/tiary/mfqm/physics/SinkingBlock.java#L13) | 普通Block；QS/Soft碰撞始终empty，不分CollisionContext实体；没有entityInside船分支/FluidState覆盖 | 无专用支撑/阻力；只有outline高度不产生船浮力 |
| [MudBlock L43](../../src/main/java/art/tiary/mfqm/physics/MudBlock.java#L43) | 依池几何和DEPTH返回碰撞，无Boat例外 | 船可能落在0.7/0.5/0.25或下层支撑，也可能在空形状处继续下沉；不能概括全部Mud都沉底 |
| [SinkEngine L28–29](../../src/main/java/art/tiary/mfqm/physics/SinkEngine.java#L28) | 只对LivingEntity执行settle | Boat继承Entity，不是LivingEntity，根本不会进入现有solver |
| [ContactSampler.sample L13](../../src/main/java/art/tiary/mfqm/physics/ContactSampler.java#L13) | 参数限定LivingEntity，并使用体高/眼点 | 没有可直接给船复用的船底/船顶/体积接触合同 |
| [SinkCapability.attach](../../src/main/java/art/tiary/mfqm/state/SinkCapability.java#L31) / [Snapshot](../../src/main/java/art/tiary/mfqm/network/SinkNetwork.java#L36) | 仅Living挂载/同步 | Boat没有该状态，现HUD/trace/280快照证据都不能覆盖船 |
| [ModBlocks](../../src/main/java/art/tiary/mfqm/registry/ModBlocks.java#L19) | copy(SAND/MUD/RED_SAND)没有定义可划船FluidState | Boat检查的不是块名/方块水标签或视觉纹理 |
| 玩家作为乘客 | ENGINE没有isPassenger/vehicle运动分流 | 乘客仍可能被当独立玩家写速度、减速/teleport；是否实际造成脱船/回拉是H，待测 |

## 3. 与1.20.1原版水中Boat比较

只读了任务003缓存的**Forge47.2.0官方映射构建字节码**，方法签名/Code hash见[vanilla-methods.json](evidence/vanilla-methods.json)。对照官方[Forge47.2.0 sources JAR](https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.1-47.2.0/forge-1.20.1-47.2.0-sources.jar)中的`patches/net/minecraft/world/entity/vehicle/Boat.java.patch`、`net/minecraftforge/common/extensions/IForgeBoat.java`。未上传Minecraft反编译源码，下面为语义摘要，不是新实测。

| 路径 | Vanilla / Forge水行为 | 当前MFQM三材料 |
| --- | --- | --- |
| getStatus | 先船顶isUnderwater，再船底薄片checkInWater，再ground friction，否则IN_AIR | 空FluidState不满足水/可划船流体检测；QS/Soft无支撑时通常IN_AIR；Mud支撑时可ON_LAND |
| 水判定 | Vanilla以FluidTags.WATER为基础；Forge补丁改为canBoatInFluid(FluidState)，再委托state.supportsBoating/FluidType | 只给Block加water tag也不够；未定义FluidType/非空FluidState，不能自动走此路 |
| 浸没检测 | AABB底部约0.001薄片求waterLevel；顶面+0.001判断水下、source/flowing分支 | 当前Living眼点/脚深合同与之不同，不能用玩家immersion直接当船排水量 |
| floatBoat | 默认重力约−0.04；IN_WATER水平惯性系数0.9，按水位/船高算支持；正支持项含0.06153846并乘0.75 | ENGINE没有给Boat添加该支持或材料阻尼，Boat原来重力继续工作 |
| 水下/流动水 | UNDER_WATER惯性0.45、支持0.01；UNDER_FLOWING_WATER下向项约−0.0007；水下累计60tick可逐出乘客 | 无MFQM对应状态/入没/逐出规则，不能直接假冒全局water来顺带触发 |
| 入水惯性 | 从IN_AIR进入水分支可调整到水面、清该转换的垂直速度 | 空FluidState不会触发；所以快速入沙不会自动获得水的入水缓冲 |
| 运动权威 | 空船/本地控制实例与有人驾驶不同；tick以isControlledByLocalInstance决定float/control/move，驾驶客户端发送船移动/划桨信息 | 只在服务器END给Boat setDeltaMovement未必约束驾驶客户端位置；不能重复玩家速度包方案的旧失误 |
| ground | 检查船底与实际collision交叠并取friction；无支撑则非ON_LAND | Mud形状可产生实际着陆；是否沉到底取决于整列形状和meta，不仅池宽 |

水的这些系数是引擎对照，不是旧MFQM数值，不能直接复制后宣称旧版船只恢复。

## 4. 快速沉底的根本路径与尚待验证因素

**可以由当前代码确定的缺口链：Boat被Living过滤排除 + 核心块无可划船FluidState + QS/Soft空碰撞 → 无MFQM船体支持/阻力，也进不了水的浮力/入水转换路径，继续走船原有重力，直到碰到真实支撑。** 这不是普通玩家浮力常量设置太小，也不是贴图/AI资源问题。

针对用户某一次“快速沉底”的精确速度、触底时刻及Mud情况仍是H，需记录Boat.status、waterLevel、hull AABB、server/client Y/vy、控制者、相邻水、DEPTH/shape、RTT及乘客修正。载客时玩家自身纠偏可能是第二个耦合因素；仅凭静态代码不能宣称它已导致脱船。旧版通用web未恢复可能使当前比旧版非Living下降更快，但没有旧船轨迹，不能量化差距。

## 5. 不破坏玩家陷落的修复设计（待批准，不实施）

### 先决定目标

- **A：忠实性优先候选。** 补回三材料针对非Living的有限阻力/接触语义，再用旧实例确认Boat是否仅缓沉/触底；不许把缺少旧表面浮力证据写成已恢复。
- **B：新增船兼容候选（若用户要表面漂浮，建议单独开关/明确新规则）。** 船体在三材料取得有阻尼的表面支持、材料间有差异；与旧版等价性无承诺。下表给出B的定性预期，数值/开关默认及是否支持各Mud状态需审批。

### 推荐边界

1. 提取不依赖Living/眼高的只读`MaterialContact`合同：船底足迹、顶面、材料表面、覆盖比例、柱连续性、碰撞支撑、相邻原生水；Living physiology仍复用现有独立眼部采样，不能重写其系数。
2. 增加独立Boat动力学路径与临时状态，不把Boat伪装Living，也不给它氧气、stuck属性或污泥等级。有限入射阻尼+浸没相关支持+材料XZ/转向阻尼，禁止NoGravity常开、永久vy=0或硬塞一块碰撞平台给所有实体。
3. 明确驾驶客户端预测与服务端校验/同步，覆盖Vehicle移动包时序；一次tick只裁决一次船，不复制原生水浮力再额外加一份。不得简单在每个接触格累加浮力。
4. **乘客只分流运动，不能跳过生理。** 被支持的Boat乘客不做独立玩家teleport拉扯/船体速度叠加；乘客眼真的被覆盖时仍按批准的air规则耗氧/伤害。下船立即恢复正常玩家接触/陷落，不清空气息以制造“上下船补满气”漏洞。
5. 保持三核心块FluidState与玩家collision不变。把它们全部改成water/FluidType会连带改变游泳、眼部水判定、声效、流动、桶、实体路径、Mud深度和原生air，不是低风险船只补丁。若最终选择真实流体重构，须另立任务。
6. 只在船接触材料范围生效，离池/拆船/换维度/重进清理，不改原生水/陆地/空中船；兼容ChestBoat和乘客、混合接触、观众/服务器加载；材质依赖不引入旧素材。

## 6. 三材料测试矩阵与预期行为

均在生存，空橡木船/一人/两人/ChestBoat分别测，11×11池、1/3/17层，静置600tick、前进/后退/转向、0/3/10格落入、上/下船、离池至水/陆地。当前列是代码推定，**不是新测试结果**；B列是待批准设计目标，不是合格结果。实际结果栏留空。

| 材料 | 当前预期（N-SRC推定） | A忠实候选预期 | B新增浮力候选预期 | 人工结果 |
| --- | --- | --- | --- | --- |
| Quicksand | 无水浮力/无块支撑时走空中下降至池底；相邻真水可能改变Boat.status | 非Living阻力按旧分支补证，不保证表面漂浮 | 入射减速后在表面附近形成稳定支撑，强水平阻力；驶出后恢复Vanilla，不能改变旁边徒步玩家陷落 | |
| SoftQuicksand | Boat同样不进入Living物理路径；0.85 outline不是船支撑 | 旧通用web/触手依赖单列；船净轨迹待旧实例 | 按0.85顶表面支持，较QS不同阻尼；同类连续柱不得把船误抬到更高空面；不直接套玩家深区中心吸力 | |
| Mud | 可能在0.7/0.5/0.25或下层Mud碰撞支撑；整列空shape才可继续落底；默认depth0堆叠与全depth3不同 | 保留真实几何支撑并补非Living阻力；没有旧专用船浮力证据 | 安全边缘仍守实际碰撞；深Mud的部分浸没/支持强度另定，禁止穿过实体支撑，禁止无差别水上快艇体验 | |
| 原生水对照 | 应走水状态/浮力（须本机实测） | 不变 | 不变，入水过渡不重复加支持/不双重扣气 | |

追加情形与建议采样：

| ID | 场景 | 预期不变量 / 待定指标 | 结果 |
| --- | --- | --- | --- |
| B-01 | 三材料空船/载客各静置600tick | 坐标速度有限；稳定浸没区间/最大振幅/收敛时限须先定容差；不以永久锁Y达标 | |
| B-02 | 三材料落入0/3/10格及1/3/17层 | 比较首次接触穿透、vy峰值、触底/稳定时间；入沙前真实坠落仍受正常规则 | |
| B-03 | Mud全depth0、1、2、3，上覆Mud/液体，中心/边缘 | 与Mud碰撞面一致，明确Boat.status是ON_LAND还是材料支持；不得把默认堆叠当全空形状 | |
| B-04 | 三材料→水、陆地、混合边界→三材料 | 支持源一次结算，不重复浮力、无无限抬升；原生水功能保留 | |
| B-05 | 生存上下船、两乘客、一人眼覆盖 | 徒步陷落不变；乘客运动不被独立拉回；真实眼覆盖仍耗氧，换座/上下船不刷气 | |
| B-06 | 真专服，两客户端和观众，RTT0/50/150/300ms | 船位置/支持状态可配对、不会持续纠偏/脱船；低TPS观察单列 | |
| B-07 | 拆船、死亡、换维度、卸载/重进 | 无临时支撑或玩家modifier遗留；驾驶权与UUID不会错配 | |
| B-08 | 同池旁边玩家/猪/掉落物与船并行 | 玩家原003基础回归仍通过；非Living和Living分流不相互改变 | |

本轮没有现成Boat测试代码或Boat日志证据；原15项GameTest和280条Living快照不能为上述任何空白结果背书。
