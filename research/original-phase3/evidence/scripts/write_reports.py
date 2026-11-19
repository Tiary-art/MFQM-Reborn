#!/usr/bin/env python3
import argparse,json,csv,collections,hashlib
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);a=ap.parse_args();r=a.root

def out(name,s):(r/name).write_text(s.strip()+'\n')
def read(name):return list(csv.DictReader((r/name).open()))
materials=[x for x in read('01_ALL_SINKABLE_MATERIALS.csv')if x['metadata_variants'].startswith('PARTIAL:')];chains=read('evidence/indexes/surface-all-chains.csv');summ=read('evidence/indexes/five-method-summary.csv');tombs=json.loads((r/'evidence/indexes/tombs-blueprint-summary.json').read_text())
links='\n'.join(f"|{x['order']}|`{x['condition'].replace('|','∣')}`|{x['configs'] or 'setup'}|{x['direct_product_fields']}|[{x['source']}]({x['source']})|{x['config_bytecode_offsets']}|"for x in chains)
family=collections.defaultdict(list)
for x in materials:family[x['contact_algorithm_hash']].append(x)
famtext=[]
for index,(key,items)in enumerate(family.items(),1):
 famtext.append(f"### 候选组 {index}: "+', '.join(x['legacy_registration']for x in items))
 famtext.append('UNKNOWN：未在模组继承链找到contact覆盖，不能证明无陷落。'if key=='NONE'else'碰撞指令规范化指纹 `'+key+'`。仅支持同指纹入口候选复用；未证明构造参数/metadata/外部事件等价。')
 for x in items:famtext.append(f"- `{x['legacy_class']}`；入口 `{x['formula_entry']}`；[{x['evidence'].split(';')[0]}]({x['evidence'].split(';')[0]})；父类 `{x['parent']}`；污渍 `{x['coating']}`。")
familytext='\n\n'.join(famtext)
modeltable='\n'.join('|'+x['method']+'|'+x['semantic_closed_blocks']+'/'+x['total_blocks']+'|'+x['model_exercised_blocks']+'/'+x['total_blocks']+'|UNRESOLVED|'for x in summ)
out('00_EXECUTIVE_SUMMARY.zh-CN.md','''# 原版机制研究 Phase 3 — 证据与离线模型交付

**总体PARTIAL；未完成移植，未达到完整语义闭环。** 本批优先交付P0真实索引和可运行离线工具，P1/P2保留明确缺口。没有更改forge-1.20.1玩法、原JAR或素材，没有候选游戏JAR。

用户说明MFQM-main (6).zip就是仓库文件打包。本轮基线为实际fetch核对的main `1f320442e0196319af24e40073cce6631cd7ec48`，已合并Phase2 PR8；不把该ZIP视为另一份缺失资料。Phase2指定报告/矩阵/未解块和Phase1证据均复用。原JAR重新校验SHA-256 `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

## 已完成的证据与工具

- 覆盖49个注册Block对象，发现39个自身/模组继承的碰撞入口，另外10个入口语义待核对。**不把它们称为49种独立陷落机制，也不将全部归并为三种profile。** 主矩阵49个块范围行、47条可追溯常量metadata写入记录及12个独立Fluid定义；Fluid定义有参数调用偏移和名称，不能当作12种独立陷落物理；784个存储metadata覆盖格另表，绝非已证明784种可达变体。
- 261个metadata读取点、750个瞬时motion分量写入点、2816个相关指令点已索引。它们是证据覆盖，逐材料完整公式仍PARTIAL；没有无接触入口就判定“不陷落”。
- Surface索引26个外层区域（1个BoP准备区、25个生成分支），保留全部可读表达式、配置字节码偏移和有序源片段。未完成25分支的全部语义等价证明。
- 受限字节码解释器执行Gardencia原指令控制流，在显式mock条件下输出5组MODEL_TRACE；覆盖90/100基本块，但语义闭环仍0/100。
- 墓室六段连续链提取8489条直接写入，坐标/metadata/写序与独立CFR字面解码器逐项相同；宝箱/刷怪笼15次helper调用内部没有执行，不能称最终世界完整蓝图。
- JavaRandom实现与官方java.util.Random的840个输出精确对照，含nextInt1和拒绝采样；有预期失败案例、确定性重放及blockGen失败副作用检查。全为MODEL_TESTED，不是原版实机。

## 未完成及运行边界

五大方法完整语义闭环数量全部0；未解offset/B块逐条保留，不能拿90块模型覆盖替代证明。WLD结构路径尚未进一步闭环；Surface复杂群系/辅助形状、逐变体运动公式、外部模组、原版运行统计均未完成。完整材料行为矩阵仍含UNKNOWN，故P0的“全量已验证变体/全生成语义”仅PARTIAL。

所有1.7.10客户端/专服/视觉/净下沉曲线实机测试 **NOT_RUN**。首次离线测试暴露两处工具/解析问题，修复及失败记录保留。下一步最小任务是消除Gardencia剩余10块覆盖缺口并进入helper真实执行，再关闭Surface每个实际材料链；不启动004/005。
''')
out('02_MECHANISM_FAMILIES.md','''# 机制族：按代码入口与行为轴分组

证据：01主矩阵、material-instruction-sites.csv、metadata-read-sites.csv及逐类javap。所有定位均带完整方法descriptor和十进制offset。下面是**候选复用组**，不是已证实的物理族全集；不能凭名称或三核心样本确定族数。

39个contact入口产生37个指令指纹；10个没有找到模组contact覆盖的对象列未知组。指纹去除常量池编号但保留操作数/调用目标；指纹不同不能证明算法完全不同，指纹相同也不能证明构造参数、metadata、外部事件等价。两个共享入口对象可能是继承，需独立核对注册构造参数和状态。

机制分类采用多轴：直接Y补偿/位置回退、水平阻碍/web、窒息/伤害、黏污、流体更新、生态/结构触发。这些轴可重叠。已有setStuck/air/hurt/motion字段写入的位置只证明入口存在，不能自动证明玩家在任何深度必定触发。流体类与普通Block不能仅因都减速就共用旧物理profile。

## 复用准入

共享原版算法必须同时关闭：同输入域/坐标框架、实体例外、metadata、装备、RNG消费、事件顺序及副作用。仅数值不同的参数化分支还要从构造/注册实参定位。无证据时保持独立，现代B1安全层可共用，算法层不强行合并。

注册却没有陷落能力的**确定名单尚未形成**；未知组不能冒称非陷落。可选模组和配置分支从各类常量引用/调用图进一步追踪，未闭环不作默认行为。原始材料名（包括流体、装饰、植物、结构）全部保留如下，不按英语名称猜测。

'''+familytext)
out('03_SURFACE_WORLDGEN_ALL_MATERIALS.md','''# Surface全部材料相关生成链

范围来自49对象/字段反查，不预先只选三种。原入口：`MoreFunQuicksandMod.main.CustomWorldGen#generateSurface(Lnet/minecraft/world/World;Ljava/util/Random;III)V`，CFG B0起，完整1054块见Phase2同名CFG。

`surface-all-chains.csv`有26个外层区域，首区是BoP兼容/探测准备，后25区按原代码顺序。每段保留单独第二反编译器源码片段、原配置字段读取offset和所有局部数值/门/循环/退出表达式。配置offset可能在嵌套或其他段重复，不将它冒充该整段唯一的精确边界；指令定位以方法+CFG为准。

|顺序|原始外层条件|配置（含嵌套）|直接产品字段|全部表达式与写序|配置读取offset|
|---|---|---|---|---|---|
'''+links+'''

## 精度与不可省略部分

dHeight=height-62，wordSizer=height/62f。height配置默认62不是高度偏移。Surface顺序包含墓室、废坑、蜡树、蜂巢、黏液、网、幼虫、软雪/软沙、植物、QS/JQS、砾石、Morass/Moor、Tar、SQS族、Moss、Bog、LiquidMire、Clay组、Mire/Mud与末尾硬黏土分支。这里名称只是导航；真正生成物ID/metadata及辅助算法按主矩阵字段与子调用追踪。未在片段直接出现产品字段的链仍标UNKNOWN/helper-produced，不能据名填块ID。

前序失败仍可留下写入；blockGen不等于成功放置数。Slime/Moss等不统一受!blockGen约束；某些门前已经采样count/radius。完整条件、Y、概率、数量、半径、短路都在每段表达式中原样保留，**尚未全部转成已证明等价的语义规格**。没有为未解参数补现代默认值。

可证实的局部事实继承Phase2：Tombs浮点门nextFloat()*750>749；一次扫描70+d下到>60+d后构建Y-8-nextInt9，返回值不阻止blockGen=true。Wax/Honey成功终止、Slime独立门/高度拒绝、Clay/Mud嵌套都有各自条件。完整偏移/RNG调用查Phase2 rng-call-sites/write-and-subgenerator-sites；本批MODEL_TRACE只执行Gardencia和墓室直线指令，不执行Surface，所有Surface运行均NOT_RUN。

尚未闭环1054/1054块，逐块列five-method-block-status.csv。下一步应先按产品字段把外层链拆为实际材料子链，用读/写/RNG差分记录失败副作用；不能把“25段全部列到”宣称“25段算法已完成”。
''')
out('04_GARDENCIA_WLD_STRUCTURES.md','''# Gardencia、WLD与五大方法状态

精确原签名、B块起止、对应CFG文件在five-method-block-status.csv；复用Phase2原始CFG。下表闭环与模型覆盖分列：

|方法|语义闭环/总块|MODEL exercised/总块|其余状态|
|---|---:|---:|---|
'''+modeltable+'''

## Gardencia本批推进

受限解释器读取原方法675条指令，执行其分支、循环、locals、RNG及直接World写入。LocalVariableTable明确blockGen位于slot11（Phase2 worldgen-javap-v.txt中本方法LocalVariableTable），故BLOCKGEN_STORE事件不凭变量名猜测。

固定origin(-16,0)：Mud seed0只开GenMud，mock validWater在Y66、validSolid只在Y70，故65与60..64均可写，得到16×16×6=1536条写入（水65 meta0、泥60..64 meta3）。入口只消费两个nextInt16。这是fixture结果，不是自然世界平均分布。

JQS seed10、Blossom seed384、Moor seed10、LiquidMire seed1分别进入其门；合并覆盖90/100块。validGround/solid/liquid/free/flat/groundNear的返回由工具明确给定，并记录FIXTURE_PREDICATE。生成helper只记录调用和返回fixture，不执行其内部读写或RNG；因此后续父方法随机序列不代表真实生成后的World RNG。

Blossom stub返回false，原调用者仍写blockGen=1，离线测试专门断言此副作用。JQS成功后循环未因blockGen停止也能从轨迹观察；这些都是指定fixture下的原控制流执行，不能上升为全方法/全输入证明。

未覆盖10块及已覆盖但语义仍未证明的90块均列offset，没有删去。需要增加Tar/地面拒绝/Flat/scan中止/锚点坐标0等反例并实际执行helper才能关闭。

## WLD保留缺口

原方法466块，本批没有执行。Phase2已定位沙漠QS及±3区块金字塔查找、底部采样、k20向0的截面和刷怪笼多级随机替换。父区块存在检查不等于所有实际半径写入都在区块内；跨区块加载、读不存在邻区、边界metadata和已写后失败均待复核。完整旧片段与CFG引用不丢失，仍PARTIAL，不虚报本批完成。

Nether131块/ABC2 135块也全部保留原证据和未解表。本批未替换其旧成果或宣称获得完整闭环。01字段→生成引用可导航这些额外维度中实际材料。
''')
tombrows='\n'.join(f"|`{k}`|{v['writes']}|{v['bbox']}|{v['metadata']}|"for k,v in tombs['methods'].items())
out('05_DESERT_TOMBS_BLUEPRINT.md','''# 墓室连续拼装蓝图（直接写入已差分）

原类`MoreFunQuicksandMod.main.GenerateDesertTombs`；六方法共同签名`(Lnet/minecraft/world/World;Ljava/util/Random;III)Z`。func_76484_a→generate2→generate3→generate4→generate5→generate6顺序执行，非六选一。

`evidence/indexes/tombs-direct-write-blueprint.csv`逐条记录类/方法、调用offset、相对XYZ、原字段/metadata、flags和坐标0锚点下区块号。原方法指令在trace-methods.json及Phase2同名CFG。直线方法中每次literal坐标加法/取字段/setBlock调用由受限解释器执行，未手写8489条坐标。

|段|直接写数|XYZ相对范围|metadata字面值|
|---|---:|---|---|
'''+tombrows+f'''

共8489次直接写入，{tombs['unique_positions']}个不同坐标；**必须按序保留覆盖**，不能仅当无序体素集合。所有坐标相对输入锚点。跨chunk区间由floor division计算，负坐标不能使用向0截断。origin(-16,40,0)示例trace与origin0蓝图分开，不能混合两者坐标。

独立CFR文本字面解析器逐项对比全部8489次坐标、块、metadata及顺序，完全相同（MODEL_TESTED）。它是独立提取路线的差分，不是两个反编译器输出相似就宣称证明整个Minecraft行为。

这六段没有输入旋转参数/旋转变换：以固定literal偏移和metadata摆放。metadata不自动等于现代facing，不能根据整数2/3/9统一旋转；各原方块映射尚待对应Vanilla/Forge状态语义核对。

## 不包含的内容

有15次宝箱/刷怪笼helper调用只记录位置、原方法及参数，内部没有执行；trace中的RNG计数0只指这六个直线调用体，不代表完整墓室生成无随机数。TileEntity写入、loot、额外block写入和世界更新尚未合并，故这不是最终完整结构存档。

Phase2源/字节码保留generateSpawner、generateChest/2。刷怪笼可见SpawnRange32、Count1、MinDelay400/Max1600/MaxNearby3及Skeleton/Zombie随机；宝箱混合ChestGenHooks和权重物品。继续逐helper核对World RNG顺序和下游写入，不能凭直接蓝图宣称完整结构已可移植。
''')
out('06_RNG_WRITE_TRACE_SPEC.md','''# 离线字节码驱动模型与轨迹规范

工具`evidence/scripts/trace_vm.py`依赖Python标准库与选择后的原指令JSON，不加载/改写原JAR，不启动Minecraft。输入JSON含675条Gardencia指令及墓室六段指令，原方法descriptor/offset都保留。其执行是**MODEL_TRACE**：真实原控制流在声明的世界/方法stub上求值，不是ORIGINAL_RUNTIME_TRACE。

## 有效范围

支持当前选定方法实际出现的受限opcode；未知opcode、未声明helper直接报错，绝不跳过假装成功。Java Random 48bit LCG和nextInt拒绝采样已与JDK官方840个结果核对，含负seed、nextInt1、非2幂和拒绝路径。浮点f32显式舍入。它不是通用JVM：对象/异常/完整Java整型溢出/任意大坐标和全部字节码未实现，当前测试仅声明的有界fixture输入；不能在任意旧类上执行后宣称等价。

mock判定及生成helper与原算法分开。所有FIXTURE_PREDICATE给出方法/offset/输入/输出；HELPER_NOT_EXECUTED列出缺失函数，不能用其false返回理解为原版真实失败。RNG只统计当前执行体，省略helper内部RNG会改变后续真轨迹，报告不得做全链随机一致性承诺。

## 轨迹列

每行seq/method/offset/event；RNG含bound/result/state_before/state_after/draws；WRITE含XYZ/metadata/flags/区块及cross_chunk；CONFIG_READ含开关；BLOCKGEN_STORE含slot11；BRANCH含目标/是否跳转。墓室BLUEPRINT_WRITE表示setBlock直写，不能代表宝箱TE的最终数据。

固定样本：Gardencia mud(seed0)、jqs(10)、blossom(384)、moor(10)、liqmire(1)，origin(-16,0)；墓室seed0、origin(-16,40,0)。完整命令在REPRODUCE。输出jsonl与summary均保留。五组只单独开启各开关，不代表全开原版配置的联合分布。

## 对照与失败案例

`test-trace.json`记录：840 RNG值精确匹配、nextInt1删除后下个值改变、Mud1536写入坐标/meta、负区块、全事件确定性重放、Blossom false返回仍blockGen true，以及8489墓室写入与独立CFR解码器比较。输入非法bound/未知opcode/未知helper均是预期失败测试。首次工具None上下文bug和漏解析(Block)cast导致77项差异，失败记录与修复说明保留，不当原版游戏故障。

静态方法选择/指令复制仅STATIC_VERIFIED来源；模型执行/差分为MODEL_TESTED；原版游戏运行状态均NOT_RUN，没有任何ORIGINAL_RUNTIME_TESTED条目。
''')
# Individual motion entries carry exact descriptor/offset reference for every material.
motionlist='\n'.join(f"|{x['legacy_registration']}|`{x['formula_entry']}`|{x['observed_metadata_write_values']}|[{x['evidence'].split(';')[0]}]({x['evidence'].split(';')[0]})|PARTIAL / NOT_RUN|"for x in materials)
out('07_MATERIAL_MOTION_SPEC.md','''# 全材料运动规格入口与逐路径缺口

范围包含全部49个注册对象及meta证据，不以三种早期样本为上限。01列各对象的父类、碰撞入口、stuck、水平分量、air/hurt、污染、声音、气泡及流体证据。261个metadata读取点含随后23条IR供追踪；750个motion分量写入各有前置20条IR。它们不是完整公式证明：栈可能来自更早分支，不可把局部窗口自动翻译成完整表达式。

|注册名|公式/碰撞入口和字节码范围|观察到的meta写入常量（不等于行为变体全集）|原指令|规格/运行|
|---|---|---|---|---|
'''+motionlist+'''

## 逐材料执行规格的统一记录接口（提案，不修改现代数值）

每条路径记录ActorClass/side/旧posY与AABB/prev位置/入射motion/输入/装备缓存/metadata/邻接拓扑/World RNG状态；输出分别是motion增量、绝对赋值、position回退、web/ground/fall、air/伤害、stuck续期和FX调用。不把正Y补偿当最终净Y速度，也不把最终净Y速度当深度。

后续解析应从各自入口按CFG顺序完整执行而非套统一profile；完整源推断也保留在evidence/source。每个路径状态需单列进入、浅层、深层、退出、装备和实体例外，未完成部分保持UNKNOWN。这里只完成全量定位、分量写入证据和样本旧公式复用，**尚未交付49对象全部路径可直接执行的物理模型**。

## 已有三样本事实仅作样本

Phase1/2的39主要分支继续有效：QS/Mud玩家k=posY-blockY-1，非玩家+.5；Soft再-.2。km=max(k,0)，顶部连两同材把k改.001但km不重算。QS入口X/Z清0、下降/2，Soft横向*.71和下降/2；Mud浅meta提前返回可绕过深层/10。mr三式不同，且CustomPotionEvent的非线性jump/移动阻碍在另一事件续期。精确偏移沿用Phase2 phase1-core-motion-decisions.csv，对应原指令已包含本包。

这些事实不能推广给Tar、Honey、Slurry、Acid、Moor、Mire等。接触入口相同也须追踪参数/状态/外部事件；注册无contact的10对象不能直接写“不能陷落”。

## 深陷用户观察

尚无原版逐tick实机轨迹，不能证明所有材料净下沉随深度严格单调减小。静态分段/web/stuck支持部分深区行动受限，但确切适用材料/深度/装备/input和净速度仍UNKNOWN。现代B2 MotionMath深度正增益是候选近似，与原分支存在差异，本轮没有调反其斜率。

## 与B1安全层接口

原版算法层只计算按旧语义转换后的状态意图；B1现代权威/预测层继续负责高速扫掠接触、耗散预算、Y同步和条件着地。允许复用安全层，不意味着复用所有材料的算法。可观测验收层分别记录motion前后、净位移、深度/横向/跳跃和回调次序；原版/模型/现代实测日志不得混用。没有更改forge源码，也没有重跑或重新宣称B1测试通过。
''')
out('08_COATING_CAMERA_TEXTURE_SPEC.md','''# 全材料污染、眼部遮挡、镜头与原始素材

01的每个对象都带污染适用性：有直接调用为CONDITIONAL_DIRECT_CALL，无直接调用仍UNKNOWN_INHERITED_OR_EXTERNAL。污染类型表达式复用Phase2逐材料表；所有实际checkPlayerMuddy调用在material-instruction-sites.csv对应完整方法/offset。不能把“干沙”名称当成不污染的证据，也不能让全部材料共用Mud规则。逐变体触发阈值完整追踪仍PARTIAL。

33污渍类型、20张64×32遮罩的文件名/hash/UV映射和材质清单从Phase1读取，只复制文本索引。所指是**MFQM自身原始素材**，不是minecraft:sand/mud占位；本轮没有PNG/OGG/JAR公开嵌入，也不以原版Minecraft占位作为资源还原验收。

沿用已定位样本：QS type4(5000/+100)、Soft17(2000/+100)、Mud实际Mire type9(1000/+50)；覆盖按旧玩家posY+eyeHeight-blockY阈值分level10..0，详见Phase2污渍报告。level1/2两族遮罩只腿，Mud族6级/Slime族7级首次头部UV。alpha=min(1,time/1000)，非触碰即全身覆盖。64×64/Alex/盔甲不能套旧共享镜像64×32UV，需独立重映射验收。

MuddyEvent共享清洗服务端分支：湿润且不在两种LiquidMire L检测内，每次time减5+time/100夹0，worldTime%16且旧level>5降级；干燥worldTime%1024且time<1000才降高level，%2且time>类型残留阈值才减time。饱和污渍可干燥保留。逐材料残留参数见coating-type-map，不能当统一最终清零。

第一人称眼部命中与第三人称相机裁剪分开：原overlay走玩家位置/eyeHeight-.2而非独立相机，原图标深色RGB.1、alpha1；具体数组不是全部49对象同序。镜头仅进入、玩家在外不应冒充玩家浸没；旧Vanilla射线可击中空实体碰撞箱块的outline。现代visual shape与第一人称遮挡分别设计，不能加实心碰撞解决镜头。

声音以原playSound调用的事件、volume/pitch和clock/RNG门为证据，逐材料索引沿用Phase1；JAR自有OGG只有bee两项，不能要求每种沙有自有OGG。原声音与泡泡可能先于后续物理消费World RNG，删特效会改随机序列。FOV、air、雨水、设备、跨维与死亡都需原版/现代分开测试，当前全NOT_RUN。
''')
out('09_OPEN_QUESTIONS_AND_PORT_READINESS.md','''# 缺口、可移植性与逐项验收

|要求|实际产物|状态|
|---|---|---|
|49对象及全量材料范围|49块范围行、字段/继承/39碰撞入口与10未知入口|STATIC_VERIFIED索引；行为PARTIAL|
|metadata变体|47常量写入记录、169精确写入点、261读点、784存储域覆盖格|PARTIAL；可达变体及其独立机制未全部确定|
|Surface全部相关链|26外层区=1准备+25生成条件，原表达式及offset索引|索引完成；语义闭环PARTIAL|
|Gardencia核心|5固定seed轨迹、90/100模型块覆盖|MODEL_TESTED；语义闭环0/100|
|至少一个可复现trace|Mud1536写入、RNG配置blockGen及其他fixture；完整输出|MODEL_TESTED|
|五方法闭环/未解块|逐块B/end及闭环/模型覆盖双列|全部语义UNRESOLVED，不虚报|
|WLD结构推进|保留原结构片段/CFG与边界风险|PARTIAL，本批未新闭环|
|墓室蓝图|8489直接写入与独立CFR解码逐项一致|MODEL_TESTED；15 helper未执行|
|逐材料运动、污染和机制族|全对象入口及指令点、独立候选组、素材文本映射|PARTIAL；不能作为全量可执行移植批准件|
|原版运行/分布/净速度曲线|测试边界与原计划保留|NOT_RUN|
|现代玩法、候选JAR、004/005|没有修改或实施|未启动|

## 每材料/生成器的准入门

01每行的modern_gap/confidence/runtime和Surface各段status为实际就绪度，全部未达到完整移植准入。常量写入meta只证明该分支静态操作数，不证明自然世界可达或该meta有不同物理。37个碰撞指纹也不是37种已证明物理族。

最小下一研究：先为Gardencia未覆盖的10块增反例fixture，同时真正执行MireO/OD、LiquidMire、Morass等helper并比较写入/RNG。再逐一关闭Surface 25生成支路和实际产品字段映射，不能只再次扩大索引数。墓室的下一最小范围是15次helper内部和metadata旋转含义，不重新抄8489写入。

P0真实证据与工具已交付，但“全变体机制闭环/全部Surface算法闭环”仍PARTIAL；P1/P2未完成内容不称通过。研究结束后停止，等待验收和下一阶段授权，不修改B1安全层或现代数值。
''')
print('10 requested reports/matrices present; semantics intentionally PARTIAL')
