#!/usr/bin/env python3
import json,csv
from pathlib import Path
r=Path(__file__).resolve().parents[2];ev=r/'evidence/results';repo=r.parents[1];summary=json.loads((ev/'summary.json').read_text());cases=json.loads((ev/'cases.json').read_text());branches=list(csv.DictReader((ev/'surface-25-audit.csv').open()));blocks=list(csv.DictReader((ev/'gardencia-block-audit.csv').open()))
def out(n,s):(r/n).write_text(s.strip()+'\n')
out('00_EXECUTIVE_SUMMARY.zh-CN.md',f'''# Phase 4：原指令执行、局部闭环与准入

**总体PARTIAL；没有完成全量移植或本轮全部验收。** 本轮从Phase3的跳过helper模型推进到读取原始class并在Java17执行实际方法体；内存插入日志，原JAR文件只读。所有环境是声明的mock，绝非Minecraft1.7.10实机。

基线main `37d18a17a1d6cdc679c4b8182c8621df97024c57` 已合并Phase1–3。原JAR SHA-256前后保持 `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。没有修改旧报告、Forge1.20.1代码、原素材，没有候选游戏JAR，没有启动004/005。

## 本轮真正推进

- Gardencia实际指令模型覆盖**99/100基本块**；Phase3未覆盖10块逐块解释。剩余B694有局部循环界证明：最多10次增量，无法通过countBlock>10；不伪造执行该块。
- **GenMud片段B0..190的14个块在明确API合同下局部闭环**：14组独立手工控制流实现与JVM执行的完整有序事件（含分支/helper/config/RNG/读写）及最终方块状态一致。包括开关关闭、无水、混合支撑、拒绝写入、不同seed及负坐标。这个结论有范围限制，不是Gardencia全方法闭环。
- MireO、MireOD、LiquidMire、Morass、Water及相关检测helper执行的是原方法体；Java JVM承担int/long、类型/返回/异常语义，不再跳过这些helper。仍有2条Morass模型在PlantingThis类型边界失败，完整错误/写入前缀保留。
- 共{summary['cases']}组模型：{summary['completed_model_cases']}组正常结束，1组预期非法bound异常，2组未解环境异常。**不把65组称作全部通过**。
- Surface25分支逐条有验收行、原条件/参数/offset、依赖与实际seed0轨迹；QS和GenSSand（SandBlock / DryQuicksand，不是SoftQuicksand）另有放置正例，QS无地面负例。**完整分支闭环0/25**，全部整支路准入仍BLOCKED。
- 剩余10个碰撞入口追到Vanilla父链的Block方法offset0 return；明确Forge补丁/外部事件未闭环，不宣称这些对象没有玩法。
- 112组受困数学核数值向量、247个原始资源路径/hash的现代目标提案和私有导入工具。Phase3回归、官方840项Java RNG对照保持通过。

## 现在可以移植什么

该片段仅属于原`world.dimension==MFQM.AOADimGardencia`路由内的Y60..66水底泥层变换，**不能当成主世界通用泥浆生成规则**；现代AoA/Gardencia维度映射未明确前不能挂载自然生成。可作为首批实现依据的是**GenMud局部算法控制流与纯水/固体检测接口**，前提是现代适配保持已声明API/材料语义、调用顺序和RNG边界；不是整套自然分布已验收。受困数值公式可按证据编写接口，但完整事件/材料物理族尚未准入。资源仅提供路径映射与私有导入方案，不能据此公开分发旧图。

## 仍不可以声称什么

Gardencia完整方法、Surface25完整支路、所有物理族、Tombs完整结构和WLD结构都没有整体PORT_READY。Tombs15 helper本轮未执行，WLD端到端结构本轮未完成；其旧证据未丢失，精确缺口见03/07。原版客户端/专服/净速度/视觉/生成分布**全部NOT_RUN**。研究交付后停止，等待验收。
''')
missrows='\n'.join('|'+x['block']+'..'+x['end']+'|'+x['condition_or_counterexample']+'|'+('PROVED_UNREACHABLE'if x['block']=='B694'else'MODEL_TESTED')+'|'for x in blocks if x['previous_phase3_miss']=='True')
out('01_GARDENCIA_CLOSURE.md','''# Gardencia：覆盖、局部闭环和未解分别统计

原方法`MoreFunQuicksandMod.main.CustomWorldGen#generateAOADimGardencia(Lnet/minecraft/world/World;Ljava/util/Random;II)V`。100块的原CFG在Phase2；本轮逐块`gardencia-block-audit.csv`含原B起止、真实覆盖用例和闭环范围。

|度量|结果|不能推导的结论|
|---|---:|---|
|实际原方法体的mock模型执行|99/100|不是99块语义闭环|
|GenMud片段局部闭环（API合同限定）|14块 B0..190|不包括其他生成分支与真实Minecraft调度|
|B694不可达的结构证明|1块|没有伪造该块执行轨迹|
|全Gardencia语义闭环|未完成|不能把99+1说成完整算法已验证|

## Phase3遗留10块逐项处理

|原块范围|原因与反例/证明|本轮状态|
|---|---|---|
'''+missrows+'''

JQS Flat seed114、OD seed10执行真实MireO/OD及LeavesAround；LiquidMire seed1 water-island fixture执行真实填充；Blossom seed384执行原GenerateMucusBlossom构造算法。Moor seed2132在第一次合适点选择Water分流，后续Morass仍可能失败。99块覆盖包含两条失败样本在ERROR之前已经执行的前缀；这不是两条样本完整通过。完整大轨迹为gzip **分析日志**（非原始素材），可解压逐事件审阅；并保存raw SHA及独立coverage。

## GenMud局部闭环定义与证据

调用范围：原generate路由以`MFQM.AOADimGardencia`选择本方法并用LiqFixer作用域；本轮反射直接调用helper，不证明该路由/现代维度映射。条件：GenMud开/关，其他四个开关关闭；世界API遵守tools/World.java定义的纯读、按坐标写入/返回applied、material属性与biome合同，原helper不另消耗RNG。独立reference_mud.py不是trace_vm/ASM解释器：手工导出循环/分支表、独立LCG、独立世界状态，以原javap offset标记事件。

原0..49先消费两次nextInt16、查biome、blockGen置0。51..190：16×16列，读water66；非固体65写water0/flags2；y60..64逐格非固体写Mud3/flags2。失败返回值不改变循环或blockGen；固体/无水跳过对应写入。14块与两个小谓词的逐跳转条件直接对应原指令，无额外隐藏生成helper。最后其他开关关闭后退出，原RNG顺序保持。

`independent-mud-diff.json`有14个完整逐事件/最终状态对照：3seed×4环境、配置关闭及全部局部布尔布局；不是只比1536个计数。all-layouts一组在256列中枚举水66的1位、固体65和60..64的6位共128种局部布尔布局，再用第8位分成功/拒绝写入。原片段不跨列读取，所有写返回值立即pop且不分支；因此这覆盖了每列局部判定域，结构对应而非只挑相似地形。正常mud写1536格；mixed、empty、deny各自按合同改变，deny的写调用与真正应用状态分开。这个**SEMANTICALLY_CLOSED有合同限定**；它不证明任意Forge补丁、副作用/异步/世界载入与现代API等价。

## B694证明

精确指令在b694-control-instructions.json。601..606令Y=70+dHeight，619..620计数0；625..632仅当Y>60+dHeight循环；684计数最多+1；697 Y-1；700回625。689..691判断count<=10，否则落入694。因此最多10次增量，count>10不可能。dHeight在此前没有变动；后续Moor赋值不回跳入该段。callee不能写调用者局部变量，异常也不会增加迭代。prove_b694.py校验这些控制指令并保留证明，非模型伪造覆盖。

## 尚未闭环的helper边界

运行在mock API上而非World真实引擎；MireO/OD/LiquidMire/Morass/Water未有各自完整独立oracle。Morass原`generateMorass(...FI)V@801`执行对BlockMorass的cast/PlantingThis时，MFQM mock字段仍是普通Block，因此ClassCastException；这是**模型类型不完整，不是原版bug**。两个失败用例已记录前缀写入、World RNG与错误，不能截去错误计为成功。下一步需类型正确的原生态回调环境/替代独立oracle；不能用跳过PlantingThis的假成功关闭它。
''')
rows='\n'.join(f"|{x['branch']}|`{x['original_condition'].replace('|','∣')}`|{x['anchor_interval_not_semantic_ownership']}|{x['seed0_write_calls']}|{x['positive_fixture'] or '未具备'}|BLOCKED|"for x in branches)
out('02_SURFACE_25_BRANCH_CLOSURE.md','''# Surface25分支逐项验收

原签名`CustomWorldGen#generateSurface(Lnet/minecraft/world/World;Ljava/util/Random;III)V`，25支路来自Phase3原序列。完整表`evidence/results/surface-25-audit.csv`逐行包含群系/配置/高度/半径等原表达式、原字段→注册名映射、callee descriptor/offset、实际trace、block/meta结果、独立验证与阻碍。

下面范围是**按外层配置锚点划分的审查区间**，不是证明每块只属于该分支；跳转/公共准备以原CFG为准。所有未闭环offset均保留在对应区间与Phase2 CFG中。

|分支|外层原条件|锚点offset区间|seed0写调用|另有正例|整支路准入|
|---|---|---|---:|---|---|
'''+rows+'''

## 运行内容与边界

25条都在原generateSurface字节码中实际运行，仅启用表中配置，种子0、dimension调用上下文/height62、mock desert biome与沙地；配置/群系/概率拒绝也是真实原分支结果。部分自然概率不会触发，不能将该负例当整条正例通过。涉及BoP/AoA配置默认未安装/关闭，未伪装成外部模组实机。

QS追加seed10 desert正例与empty无地面负例；GenSSand追加seed38 desert正例；它调用generateSoftSand，写原SandBlock（注册DryQuicksand），不能误认成SoftQuicksand。使用原generateMire/generateSoftSand等共用helper指令及真实Random，完整按序RNG/读写/分支/配置/blockGen日志保留。观测到的块/meta只证明该fixture里的结果；不是穷尽全部变体或自然群系分布。

## 逐条关闭条件

每条目前都缺少所有路径/变体/外部环境的独立读写oracle，因此**完整语义闭环0/25、整支路PORT_READY全BLOCKED**。表内给出每条精确锚区间、全部callee位置与源表达式，待关点不是一条空白UNKNOWN。配置门/已执行正负例属于MODEL_TESTED，不冒充SEMANTICALLY_CLOSED。

下一批优先QS与GenSSand（DryQuicksand）的独立helper oracle，然后共享Mire/Mud/Bog/Moor等依赖。保留各材料实际字段，不统一三种profile。Waxes/蜂巢/Web/幼虫/Clay等依然各有独立条件；模板化PlacedFeature不能改原有顺序或假设失败无副作用。
''')
out('03_TOMBS_WLD_CLOSURE.md','''# Tombs与WLD：本轮未完成部分

**P1未完成，UNRESOLVED。** 本轮将资源优先投入Gardencia真实helper与独立对照；没有再抄8489条已比对直接写入。

`tombs-15-helper-audit.csv`逐一列原调用方法签名/offset/目标helper。全部15次（6刷怪笼、9宝箱）内部本轮NOT_RUN；仍缺NBT、TileEntity、ChestGenHooks与WeightedRandom的忠实mock及独立抽奖/写序oracle。原GenerateDesertTombs#generateSpawner、generateChest/2完整字节码/源片段沿用Phase2。

原六段连续func_76484_a→generate2→3→4→5→6、相对坐标/固定metadata以及跨区块布局沿用Phase3已核验8489直接写入。没有输入旋转参数不等于每种方块metadata可直接转成现代facing；宝箱/刷怪笼附加写入/保护/失败仍可能影响最终世界。不能称最终完整结构一致。

WLD `CustomWorldGen#generateWLD(Lnet/minecraft/world/World;Ljava/util/Random;II)V` 的466块保留Phase2 CFG和Phase3缺口，本轮没有完成所要求的结构路径端到端模型。原±3区块金字塔搜索、底部探测、截面重写/刷怪笼随机替换都是未解依赖，不用本轮QS普通地形模型冒充WLD结构通过。

下一最小P1任务：先一个Tombs spawner helper的NBT/World RNG/TileEntity空值与正常值对照，再ChestGenHooks固定表；WLD先定义邻区存在/Chunk storage合同后关闭一个真实结构分支。当前两项均BLOCKED。
''')
stuck_names=sorted({x['legacy_id'] for x in csv.DictReader((ev/'stuck-kernel-callers.csv').open())})
out('04_MATERIAL_PHYSICS_PORT_SPEC.md','''# 全量物理族的本轮进展与准入边界

仍以全部49对象、12 Fluid定义及实际metadata证据为范围，不能把它们视为对应数量的独立物理。Phase3的39contact入口、37指令指纹只是候选分组，不等于已证明37个物理族。本轮没有宣称任何完整物理族PORT_READY。

## 剩余10个入口继续追踪

`ten-contact-inheritance.json`逐对象给父链、obf/SRG和独立javap。HPeat/HardenedClay/Honeycomb/ChocolateBlock/WaxWood等从Block，SandstoneTrap从BlockSandStone，Lure从BlockContainer，LilyPad/Bush系沿各自父链，最后解析到Vanilla `aji.a(Lahb;IIILsa;)V` offset0 return（对应Block.func_149670_a）。这是STATIC_VERIFIED父链，不是只看本类缺方法。

Forge1.7.10补丁和外部事件未核对；Trap下落、植物/TileEntity/碰撞形状等其他入口仍可能有玩法。不能写成“这10种无陷落/无效果”。原官方client与SRG的hash及逐父类字节码已附，仅文本证据，不分发Vanilla jar。

## 可执行数值接口：共享stuck核

原`CustomPotionEvent#onLivingUpdateEvent(Lnet/minecraftforge/event/entity/living/LivingEvent$LivingUpdateEvent;)V`：55..87读取Level-5与horizontalCollision；90..162计算，167..200阈值，217..252添加operation2 modifier并Level置0。原指令在Phase1/2 CustomPotionEvent文本；本轮stuck-kernel-callers.csv给实际材料调用者与offset，范围不是固定三材料。

```
p=Level-5; c=horizontalCollision ? 0 : 1
if p<250:
  jump=(float)(jump/max((1+p*(1+c*2.5)/1000)^8,1))
  speed=max(1/(1+p*(1+c/2)/50)^2,.02)
else: jump=0; speed=.02
if (double)jump<.005: jump=0
modifier(operation=2, amount=speed-1); Level=0
```

PhysicsVectors.java与独立Python数学测试112组输入，包括1/4/5、254/255阈值、水平碰撞、float .005附近。速度容差1e-12、float字符串输出比较1e-7；这是**MODEL_TESTED数值表达式**，没有执行原LivingUpdateEvent完整事件/属性生命周期。probe Level1..4可算出speed>1，但这不证明这些Level自然可达；不能用测试输入反推游戏默认行为。float .005f转换double后略小于.005，边界也不能按十进制直觉替换。

## 深度、动作与安全层

原各材料的k/km、正Y补偿/绝对赋值/回退、web/ground与不同实体/装备/随机路径须沿Phase3每类入口继续闭环。这里的stuck强度随Level变化，不直接证明所有材料Level随深度单调，也不决定净Y。原版净下沉可能变慢的用户观察仍需条件分层实测，当前NOT_RUN，没有编造统一减速公式。

原算法层给逐回调状态意图；B1网络/高速扫掠/耗散/Y同步/着地层保留，不能为套旧公式删除安全层。本轮未改速度、未合并物理profile、未新增现代JAR。首批只可使用上述数值接口规格审阅，完整物理族准入仍BLOCKED。
''')
physics=r/'04_MATERIAL_PHYSICS_PORT_SPEC.md'
physics.write_text(physics.read_text()+'\n已定位到共享stuck调用的对象（仅调用路径集合，非同一物理profile）：'+', '.join(stuck_names)+'。每个入口/offset见stuck-kernel-callers.csv。\n')
out('05_COATING_CAMERA_ASSET_PORT_SPEC.md','''# 污渍、镜头与MFQM原资源规格核对

沿用Phase3的逐对象/变体证据；没有将无直接污染调用的材料改判成不沾污，也没有把干沙统一套Mud规则。33类型与20张64×32分级遮罩、Muddy Type/Level/Time和更新/清洗的精确offset依旧指向Phase1/2证据。逐材料完整污染路径尚未全部闭环，状态UNRESOLVED部分保留。

湿润且不在两类LiquidMire L检测中，time减5+time/100夹0，按worldTime门逐渐降高level；干燥有类型残留阈值与time<1000条件，不保证最终自动清白。等级选mask，不是触碰后全身alpha。旧Biped64×32/Alex现代左右独立UV/盔甲遮挡仍需独立映射和实测，不能把它写成完成。

原第一人称overlay来自玩家眼部位置-.2采样，原RGB .1、alpha1与原图不透明证据沿用；第三人称相机射线与玩家眼部触发分开。镜头在内玩家在外不能激活玩家浸没遮挡。空实体碰撞体不等于空视觉shape，不加实心碰撞修相机。旧音效/粒子随机消耗次序不能删除后声称物理RNG一致。

## 新增可复核资源映射与私有方案

`original-asset-path-map.csv`列247原资源路径/hash/尺寸/动画sidecar及**现代目标提案**，没有复制像素。`original-audio-path-map.csv`另列仅有的2份原JAR附带的bee OGG路径/hash/现代别名提案；没有给每种沙编造专有OGG，也没有音频听验。`mfqm:legacy/...`是建议的逻辑sprite/纹理标识，目标文件路径在另一列；现代渲染注册/UV还没实施。源指MFQM1.1.1自己的资源，不是minecraft:sand/mud；不生成AI图、不重绘、不缩放。

private_assets.py默认只写文本映射，验证整个原JARhash；只有显式--extract --out才提取到非Git工作树的私有目录。原PNG字节与sidecar保持不变，逐图hash核对；所有Git祖先路径拒绝。当前**pixels_extracted=false**，未运行实际提取或渲染。

原图有动画条、32像素宽纹理、64×32污渍mask等不同用途，不因16×16美术方向就擅自缩放所有图。原始贴图与声音授权未确认前不可公开分发，现代资源代码本轮不改。私有导入是计划/工具，不是素材授权或渲染验收通过。
''')
out('07_OPEN_QUESTIONS_AND_USER_ACTIONS.md','''# 精确缺口与用户事项

|缺口|精确定位|本轮证据与下一步|
|---|---|---|
|Gardencia非GenMud全语义|gardencia-block-audit.csv各B起止|99块执行不是闭环；为各helper建独立oracle|
|Morass生态回调类型|CustomWorldGen#generateMorass(IIIILnet/minecraft/world/World;Ljava/util/Random;FI)V@801|两失败trace保留ClassCastException及前缀状态；修mock BlockMorass身份并执行PlantingThis，不能跳过|
|LiquidMire非法参数|generateLiquidMire(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;I)V@325|isWL76令nextInt(75/76)=nextInt0，预期失败；不当自然默认参数|
|Surface25完整链|surface-25-audit.csv每条锚区间及callee descriptor/offset|0/25整支路闭环；先QS/SoftSand独立oracle，再Mire/Clay/环境兼容|
|Tombs15 helper|tombs-15-helper-audit.csv每次调用offset|全部NOT_RUN；NBT/loot/TE/World RNG合同|
|WLD结构|原generateWLD descriptor、Phase2 CFG全部466块|端到端结构未完成，不能拿Surface QS代替|
|10父链的Forge语义|ten-contact-inheritance.json|Vanilla noop已核对，补Forge patch/事件覆盖|
|物理/污染全变体与净轨迹|Phase3逐材料入口、metadata读点|不套统一profile，逐材料事件/装备/侧重与真实轨迹|

当前没有必须由用户补交资料或截图才能继续的静态研究阻塞，已有原JAR与仓库足够继续下批工具研究。**不重复索要已说明是仓库快照的ZIP，也不重复请求此前已同意的EULA。**

后续若要取得ORIGINAL_RUNTIME_TESTED，必须运行合法MC1.7.10+匹配Forge+原JAR/可选mod环境并记录版本/hash/配置/seed/逐tick或存档；本批没有这样的真实运行。USER_ACTION_REQUIRED仅在需要用户提供其私有原版环境日志或视觉观察时才成立：给出对应固定seed/配置/坐标的小场景，导出原始日志/截图，不让其阻塞无人工依赖的工作。现在不将此作为必须确认的请求。

研究交付点停止。下一最小研究建议：关闭Morass PlantingThis类型边界及一个Mire helper完整独立oracle；之后再验收Surface正/负/边界支路。任何新版玩法修改另待授权。
''')
print('Phase4 reports written; whole-generator/whole-physics readiness remains blocked')
