#!/usr/bin/env python3
from pathlib import Path
import json,csv,hashlib,gzip,shutil,re,argparse
ap=argparse.ArgumentParser();ap.add_argument('--work',type=Path,default=Path('/tmp/mfqm-phase5'));a=ap.parse_args()
r=Path(__file__).resolve().parents[2];repo=r.parents[1];ev=r/'evidence/results';s=json.loads((r/'summary.json').read_text());cases=json.loads((ev/'cases.json').read_text())
def out(n,text):(r/n).write_text(text.strip()+'\n')
def table(n,rows):
 with(r/n).open('w',newline='')as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
# Keep only current named runs as canonical evidence. Old smoke errors remain separately labeled.
allow={c['tag']+suffix for c in cases for suffix in ['.jsonl.gz','.oracle.jsonl.gz']}
allow|={f'morass-parent-{seed}.jsonl.gz'for seed in [10,2132]};allow|={'stuck-lifecycle.jsonl.gz','stuck-lifecycle.oracle.jsonl.gz'}
manifest=json.loads((ev/'trace-manifest.json').read_text());retained=[]
for entry in manifest:
 path=r/entry['path']
 if path.name in allow:retained.append(entry);continue
 with gzip.open(path,'rt')as f:failed=any(json.loads(line).get('event')in ['ERROR','UNRESOLVED']for line in f)
 if failed:
  dest=r/'evidence/failures'/('old-smoke-'+path.name);shutil.move(path,dest)
 else:path.unlink()
(ev/'trace-manifest.json').write_text(json.dumps(retained,indent=2)+'\n')
# Source references, no new whole-JAR decompilation or registration claims.
methods=json.loads((a.work/'oracle-methods.json').read_text());selected={m['class']+'#'+m['name']+m['descriptor']:m for m in methods}
used=sorted({c['method']for c in cases}|{'MoreFunQuicksandMod.main.blocks.BlockMorass#func_149721_r()Z','MoreFunQuicksandMod.main.CustomPotionEvent#onLivingUpdateEvent(Lnet/minecraftforge/event/entity/living/LivingEvent$LivingUpdateEvent;)V'})
refs=[]
for key in used:
 m=selected.get(key);refs.append(dict(method=key,bytecode_range='0..'+str(m['instructions'][-1]['offset'])if m else'0..1 (copied predicate proof)',evidence='Phase1 method index + Phase2/3 bytecode + body-identity.log',status='STATIC_VERIFIED_ORIGINAL_METHOD_REFERENCE'))
table('evidence/results/method-provenance.csv',refs)
# Four collision families plus an intentionally distinct Honey path: static only, no fake original-entity execution.
sites=list(csv.DictReader((repo/'research/original-phase3/evidence/indexes/material-instruction-sites.csv').open()));mat=[]
expr={
 'Quicksand':'min(5+floor(max(0,(mtdkof*10f)*(1.5-km))),145); deep forced145',
 'DryQuicksand':'min(5+floor(max(0,pow((mtdkof*20f)*(1.5-km),1.5))),128); deep forced128',
 'Mud':'min(5+floor(max(0,pow((mtdkof*2f)*(1.5-km),1.5))),145); mtd0 may return; deep forced145',
 'Mire':'min(5+floor(max(0,pow((mtdkof*3f)*(1.5-km),1.6))),145); special branches request255',
 'Honey':'min(5+floor(max(0,pow((mtdkof*5f)*(1.5-km),1.5))),140); deep eligibility can force50, not145'}
for name,formula in expr.items():
 calls=[x for x in sites if x['legacy_id']==name and x['signal']=='stuck'];mat.append(dict(material=name,callback_methods=';'.join(sorted({x['method']for x in calls})),setter_offsets=';'.join(x['offset']for x in calls),source_level_relationship=formula,status='STATIC_VERIFIED_CALLS; expression decompile cross-reference PARTIAL; collision callback NOT_RUN',evidence='../original-phase3/evidence/source/'+{'Quicksand':'BlockQuicksand','DryQuicksand':'BlockSand','Mud':'BlockMud','Mire':'BlockMire','Honey':'BlockHoney'}[name]+'.cfr.txt',whole_physics_port_ready=False))
table('evidence/results/material-level-callbacks.csv',mat)
ready=[
 dict(component='Stuck attribute lease reducer',evidence='stuck-lifecycle.jsonl.gz + oracle + stuck-diff.json',level='PORT_READY',scope='pure callback-level UUID lease/Level reducer; atomic attribute-map contract; operation2 and transient mapping defined',not_in_scope='1.20 jump/air-factor hook, global Forge event order, material collision implementation or net Y',next='implement pure reducer + tests only before wiring approved callbacks'),
 dict(component='DryQuicksand voxel transaction core',evidence='generateSoftSand cases + independent VM + declarative mesh/erosion oracle',level='PORT_READY',scope='algorithm layer via ordered voxel/LegacyRandom interfaces; block identity/state mapping defined',not_in_scope='PlacedFeature registration, density/biome API, original block-update callbacks or actual DryQuicksand physics',next='implement exact ordered core and acceptance vectors; no independent placement decomposition'),
 dict(component='PlantingThis + func_149721_r',evidence='body-identity.log; 9 type-correct positive/refusal/null seeded cases',level='SEMANTICALLY_CLOSED',scope='declared Morass singleton/material and deterministic flower-provider contracts; bytecode unchanged before logging',not_in_scope='real biome flower provider, other BlockMorass methods, whole Morass parent equivalence',next='real API provider adapter before runtime placement'),
 dict(component='GenQS / GenSSand Surface selected input domains',evidence='positive/no-ground/probability/refused-write/composed cases; whole ordered event diff',level='SEMANTICALLY_CLOSED',scope='fixed declared Desert/BoP-off/height62/origin(-16,0)/seeds/config domains only',not_in_scope='all biome types, all configs, all world side effects; global 25-branch closure remains0',next='broader independent caller oracle before declaring whole branch PORT_READY'),
 dict(component='Shared generateMire target / protection / replacement',evidence='mire helper+MudBlock/protected/water-only cases',level='SEMANTICALLY_CLOSED',scope='specified finite stable terrain/material sentinel/target domain + independent transaction oracle',not_in_scope='full plant/snow replacement traits, Nether branch, all dynamic block updates',next='complete trait domain and dependent callers'),
 dict(component='Whole Gardencia Morass parents',evidence='morass-parent-10/2132 complete native logs',level='MODEL_TESTED',scope='both former class-cast failures now finish with actual original planting body',not_in_scope='no independent oracle for whole parent',next='parent-wide oracle, not more counting'),
 dict(component='Tombs spawner/chest vertical slices',evidence='8 seeded/null native-vs-independent VM/NBT/inventory comparisons',level='SEMANTICALLY_CLOSED',scope='specified empty initial NBT/fixed ChestGenHooks/27-slot/stack-count contracts',not_in_scope='real mod loot tables; chest2; all15 caller interleavings; modern Spawner NBT mapping',next='versioned NBT/loot adapter and whole structure sequence'),
 dict(component='WLD sparse pyramid lava transformation',evidence='wld-positive/reject/overlap full VM diff + sparse transaction oracle',level='SEMANTICALLY_CLOSED',scope='defined sparse storage/neighbor presence/biome arrays/seed0 and no implicit chunk loading',not_in_scope='whole466-block method, all pyramid blocks/spawners/puddles, live chunk loading/lighting',next='extend one structure predicate at a time'),
 dict(component='49 objects /12 Fluid / all visual behavior',evidence='unchanged Phase3 full material and Phase4 asset evidence',level='BLOCKED',scope='scope maintained; no claim49 independent mechanisms or3 universal profiles',not_in_scope='whole material physics and visual closure',next='individual collision and visual adapters; no new assets redistributed')]
table('06_PORT_READINESS_MATRIX.csv',ready)
# Preserve all 25 rows, updating only explicit bounded evidence; not a new completed-generator count.
old=list(csv.DictReader((repo/'research/original-phase4/evidence/results/surface-25-audit.csv').open()));status=[]
for x in old:
 candidate='GenQS'if x['original_condition'].startswith('if (MFQM.GenQS ')else'GenSSand'if x['original_condition'].startswith('if (MFQM.GenSSand ')else''
 status.append(dict(branch=x['branch'],condition=x['original_condition'],source_interval=x['anchor_interval_not_semantic_ownership'],status='SEMANTICALLY_CLOSED_DECLARED_FIXTURE_DOMAIN'if candidate else'BLOCKED',whole_original_branch_port_ready=False,case_prefix='qs-'if candidate=='GenQS'else'dry-'if candidate=='GenSSand'else'',evidence='../original-phase4/evidence/results/surface-25-audit.csv; cases.json',remaining='all untested biome/config/helper/block-update states retained'))
table('evidence/results/surface-25-status.csv',status)
base=list(csv.DictReader((repo/'research/original-phase3/01_ALL_SINKABLE_MATERIALS.csv').open()));table('evidence/results/material-scope-delta.csv',[dict(registration=x['legacy_registration'],legacy_class=x['legacy_class'],record_kind=x['record_kind'],scope='unchanged all registered objects/metadata evidence/Fluid definitions',new_evidence='algorithm/callback subset only'if x['legacy_registration']in ['DryQuicksand','Quicksand','Mud','Mire','Honey','Morass']else'none',full_physics_port_ready=False)for x in base])
s['ready_component_count']=2;s['surface_scoped_candidate_count']=2;s['whole_surface_all_biomes_closed']=0;s['material_callbacks_executed']=False;s['original_jar_sha256']='2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b';(r/'summary.json').write_text(json.dumps(s,indent=2)+'\n')
out('00_EXECUTIVE_SUMMARY.zh-CN.md',f'''# 原版研究 Phase5：已闭环的限定域与首批实施规格

**总体PARTIAL，但本轮有实质性新增闭环与两个可实施的算法组件规格。** 基线main `c8fa7214525dfecb6b66835a903edd25a19dfe9c`，即用户仓库快照，不要求重新上传ZIP/JAR。原JAR只读hash保持 `{s['original_jar_sha256']}`。没有改Forge1.20.1生产逻辑、原JAR或素材，没有候选游戏JAR、没有注册新世界生成。

本轮 {len(cases)} 组原方法体与独立Python栈机的**完整有序事件及最终状态**对照；其中 {sum(bool(c['declarative'])for c in cases)} 组另有不执行字节码的几何/事务或随机游走 oracle。原始/native和oracle日志完整gzip保存，没有采样裁剪。独立VM不是唯一的算法证明。

## 可以开始实施的两个小组件

1. **Stuck属性租约与Level状态reducer**：原事件体执行8次、123个有序事件与独立状态机一致；现代 UUID remove/addTransientModifier、MULTIPLY_TOTAL 映射和接口明确。只准入这个纯组件；jumpMovementFactor的现代空气控制映射、整体Forge时序、材料碰撞和净Y尚未准入。
2. **DryQuicksand体素事务核心**：原generateSoftSand（SandBlock / DryQuicksand，绝不是SoftQuicksand）有独立VM及几何/有序侵蚀oracle、边界和失败写入用例；旧块身份→现代资源/状态映射、LegacyRandom和顺序写入接口明确。只准入算法核心；不注册Feature，不宣称自然分布或DryQuicksand完整物理完成。

## 与Phase4的实际差异

- 修好Morass类型/对象关系：模拟类型装入**未改指令的原PlantingThis与原func_149721_r**，材料标识恢复原151583_m。复制前后指令/操作数/跳转指纹相同，原JAR不变；不是跳过回调或强制成功。两条旧失败seed10/2132现在均正常结束，父方法仍仅MODEL_TESTED。
- QS与DryQuicksand有正例、概率拒绝、无地面、拒绝写入、边界、组合配置对照。指定Desert/BoP关闭等测试域闭环；**整个25支路全群系闭环仍0/25**，不把有限域验证扩成全部完成。
- 真正执行原stuck事件生命周期；原碰撞材料回调本轮没有执行，Quicksand/Dry/Mud/Mire/Honey的Level关系仍按静态证据分列。
- Tombs完成spawner/chest正常、空Tile和不同World seed垂直切片；独立NBT/库存/随机对照。未再抄8489直接写入，15次父调用链/Chest2/现代NBT仍未闭环。
- WLD执行真正金字塔搜索与lava→Tar/基础支撑路径：正例38格、无邻区拒绝及重叠群系回归；完整原事件流与独立VM一致，另有稀疏几何事务oracle。整个466块方法没有完成。

保留失败：protected环境缺支路、WLD尝试次数在群系门前消费RNG、开放顶砂格先触发World RNG但不抽puddle概率等差异都已记录，失败输入仍在回归。Phase2/3/4回归在隔离副本运行，旧证据不覆盖。**所有真实MC1.7.10客户端/专服/视觉/净下沉统计仍NOT_RUN**。
''')
out('01_MORASS_MOCK_AND_PLANTING_CLOSURE.md','''# Morass类型与PlantingThis

原`CustomWorldGen#generateMorass(IIIILnet/minecraft/world/World;Ljava/util/Random;FI)V@801`先cast MFQM.MorassBlock再调用PlantingThis。Phase4字段是普通Block，违反类型和this身份合同；不是原方法本身抛错。

本轮是**受控模拟类型外壳**：保留原全名/Block父类、MFQM单例与World中对象身份。构造器是mock，只初始化本方法实际查询的material151583_m；原PlantingThis(World,Random,III)V与func_149721_r()Z方法指令完整复制进外壳。后者原返回false，不能只消除cast却继承错误的solid判定。其它原BlockMorass方法/字段没有声称完整加载。

BodyProof在日志插桩前比较原与外壳方法的操作码、操作数、目标/跳转指令序号；body-identity.log提供SHA。原JAR不写入。后续仅加入日志；不改条件、RNG、返回或跳过128次尝试。

合同：坐标(-16,70,0)、below<=70为同一Morass单例，花材/func_149721_r谓词、Biome花名与canPlant均显式native API。plant-ok、plant-refuse、plant-null×seed0/1/-1共9例。null表示花查找返回null，不是假定World可为null。花提供者固定且不额外消费RNG；真实Vanilla/其他mod花提供者不在此闭环域。

独立Python栈机逐事件校验所有BRANCH/HELPER/RNG/读写；独立随机游走事务模型按attempt号生成可达候选，不读取JVM trace，校验RNG和花写入/最终状态。原this身份、每步4个nextInt3、整数除2、支撑/上方谓词、nextInt8、元数据2和写入flags3均保留。

父Gardencia seed10/2132两例已经执行实际回调并返回，完整日志见morass-parent-*。**没有对整个父链宣称独立闭环**；只对PlantingThis的指定API输入域标SEMANTICALLY_CLOSED。真实Biome映射与整个Morass物理仍BLOCKED。
''')
out('02_SURFACE_BRANCH_CLOSURE.md','''# QS、DryQuicksand与共享Mire：限定域关闭

原`CustomWorldGen#generateSurface(World,Random,III)V@0..14261`，完整25行状态在surface-25-status.csv。源条件/参数/callee offset沿用Phase4同名审查表。主世界dim0、height62（dHeight0）、origin(-16,0)，BoP等可选模组关闭，原BiomeGenDesert、dT0；没有用原CF自我重放作为唯一oracle。

## 原条件与顺序

GenSSand先于GenQS。dT0时SSand次数1+nextInt2、门1/20、extent4+nextInt15；QS次数1+nextInt2、门1/15、extent5+nextInt10。均从96扫到>60，沙材/free space和平坦条件先通过才调用helper。isAboveFreeSpace消费单独World RNG。源rad是旧循环extent，数学半径约rad/2，不能将其误当球半径翻倍。

GenSSand调用generateSoftSand，写SandBlock（注册DryQuicksand）与砂岩；QS调用generateMire(F哨兵,QuicksandBlock)。SSand成功后blockGen使后续QS跳过；QS尝试循环与SSand停止规则不同。组合seed10/38回归及refused-writes保留共享blockGen、前置RNG、void helper返回后仍置状态等副作用；不拆成独立PlacedFeature。

## 验证域

QS和SSand分别有desert正例、empty地面拒绝、seed0概率拒绝、desert-refuse全部写返回false、组合配置；helper extent -1/0/1/4/5/10/18×seed0/1、空背景、SoftQuicksand保护、water替换拒绝、MudBlock目标等。全部有原native与独立栈机完整事件/最终状态；关键helper另有独立事务oracle。

Mire oracle以噪声体素筛选+目标写入+下方支撑事务定义；Dry oracle以三格竖印和**有序**浅层侵蚀定义，不共享字节码分派。genMire普通/目标Mud/保护/替换域已验证，但植物、雪、Nether及任意动态方块API未全闭环。旧helper即便extent<0仍消费初始nextDouble，不能优化掉。

每个点的噪声先消费，所有重复写入和metadata/flags保留；不能只对最终去重体素比对。独立栈机覆盖分支和读取，事务模型额外检查数学/写入语义。原helper写入可能拒绝，后续查询反映实际应用状态；refused-write用例不被删除。

**SEMANTICALLY_CLOSED仅用于cases.json中明确的有限环境/输入域**。全原支路的所有群系、配置和更新回调仍0/25闭环。只有Dry体素核心形成PORT_READY接口规格；整个Surface/天然生成注册仍BLOCKED。
''')
out('03_STUCK_AND_MATERIAL_PHYSICS_PORT_SPEC.md','''# Stuck生命周期与首批可实施接口

原`CustomPotionEvent#onLivingUpdateEvent(LivingUpdateEvent)V@0..272`及clinit复制指令与原文件完全一致，未加载/伪装其他spawn/FOV事件。Entity/属性/扩展属性API为明确mock；原碰撞函数本轮未执行。8次回调123事件，包括多次接触setter、无续期、0、255、null属性，完整native与独立状态reducer对照。

```mermaid
stateDiagram-v2
 [*] --> Idle: Level=-1
 Idle --> Pending: contact(L) overwrites
 Pending --> Active: update removes old UUID; add transient op2; Level=0
 Active --> Pending: later contact(L)
 Active --> Idle: no contact; next update removes UUID; 0 becomes -1
```

## 原语义及现代租约接口

0..32查询并移除固定UUID旧modifier，**早于**36..46的属性存在检查。Level>0：p=Level-5，horizontalCollision时c0否则c1；speed=max(1/(1+p*(1+c/2)/50)^2,.02)，p>=250则.02。添加amount=speed-1、operation2、saved=false，然后Level=0。下次无碰撞续期时先移除modifier，再把0改-1；0不是当前帧立即取消效果。多个setter是最后值胜出，非max。

PORT_READY的**纯属性租约reducer**接口：Contact(level)→overwrite；Update(optionalProperty, horizontalCollision, AttributePort)→LookupUUID/Remove/AddTransient/SetLevel命令。目标47.2.0/Java17映射：Attributes.MOVEMENT_SPEED，removeModifier(UUID)，addTransientModifier(new AttributeModifier(UUID,name,amount,Operation.MULTIPLY_TOTAL))；其它UUID保持不变，状态不跨存档持久化。限定AttributePort没有重入修改；异常/缺属性仍先清自己UUID。原UUID为73a49882-85a3-4896-ad2d-8c591e24aa62。

jumpMovementFactor旧float另按8次幂及.005阈值处理，**不是motionY或竖直跳跃初速**。1.20空气控制映射尚未确认，因此不在PORT_READY子组件内。旧/新Forge全局事件相对碰撞的顺序也未实测，运行挂接必须另验；B1高速扫掠、服务端同步、Y稳定与着地安全层保留，不再叠加一套无来源速度曲线。

## 分材料的调用者证据

material-level-callbacks.csv列Quicksand、DryQuicksand、Mud、Mire、Honey的原完整callback签名/setter offset及源公式。QS cap145，Dry为非线性cap128，Mud/Mire有不同指数/metadata与早退，Mire特殊请求255，Honey cap140而深区可请求50；不能统一三profile。这里是STATIC_VERIFIED调用点/源表达式审阅，不称真实碰撞轨迹MODEL_TESTED。

八次事件测试输入包含145→无续期、145再128（后值覆盖）、Honey样本50、饱和255和0；它们是外部接触请求输入，非伪造原碰撞执行。受困核强度和材料深度关系必须各自追踪，尤其Honey的深区请求不支持全材料统一单调规则。净Y速度和每tick深度实机均NOT_RUN。

下一轮可先实现纯租约reducer及测试，不接Forge事件、不修改VY。材料碰撞、jump空气控制、FOV/全局时序继续BLOCKED。
''')
out('04_TOMBS_WLD_VERTICAL_SLICES.md','''# 结构最小垂直切片

## Tombs

真实原`GenerateDesertTombs#generateSpawner(World,III)V`与`generateChest(World,IIII)V`已执行。spawner/chest各seed0/4096/-1和空Tile共8例；World随机种子等于case seed。原方法、分支、读取、NBT/库存/metadata与最终状态全部和独立Python栈机比较。

spawner正常：原@10置spawner0 flags2，@19查Tile，@45导出NBT，再写SpawnRange32/SpawnCount1、World nextInt2选Skeleton/Zombie、Min400/Max1600/MaxNearby3并导入。空Tile保留原stderr并正常返回，不伪造实体。合同初始NBT为空；真实Tile额外字段、现代SpawnData结构未纳入。

chest：固定ChestGenHooks返回一条fixture_token权重2，其后17条原字面loot仍由原方法构造；27槽，抽取量均可装为一堆。native逐项减权重实现与独立CDF查找对照，连nextInt1也消费；slot覆盖不合并。LOOT_TABLE/World RNG/INVENTORY_SET和最终slots均有日志。不是声称真实模组默认loot table或真实Vanilla WeightedRandom API已完整运行。

这是两个helper种类的有限域切片，不把6 spawner+9 chest的全部父调用次序减成“只剩13次”；15处父调用的交错RNG/最终完整结构仍未验证。Chest2表不同，本轮未闭环；8489直接写入保留不重抄。现代NBT版本转换仍BLOCKED。

## WLD实际结构路径

真实`CustomWorldGen#generateWLD(World,Random,II)V`执行。不是Surface替代。稀疏Chunk/World合同：仅首邻区存在；角点(-64,63,-48)为lava，底部探测候选(-69,63,-47)为sand，下两格stone，其它未写位置AIR；seed0，Desert-only WLDBiomes映射。没有隐式加载其它区块。

原搜索找到lava/底部后执行原截面改写：Tar2格及四向各9砂岩支撑，共38次/38格，跨3个区块。全有序事件和独立VM一致，另由稀疏几何事务规则独立预测RNG与38次写入及最终状态。无邻区拒绝和重叠ID回归也保留。

本轮查明两个易漏语义：Ashes后备支路在判断群系前已抽尝试次数；单一Desert即使不走Ashes也会消费该nextInt5。开放顶砂点先调用isAboveFreeSpace（World RNG），其否定条件不成立就**不抽**puddle概率。早期CFR未结构化片段不可当完整算法，修正有原CF/第二反编译器证据，失败oracle输入未删。

这个合同是globally sparse voxel存储+邻区存在接口，不等价真实Chunk加载、光照、邻更。只关闭该稀疏路径/输入域；整个466块WLD和完整金字塔仍BLOCKED。
''')
out('05_MATERIAL_AND_VISUAL_GAPS.md','''# 全量范围与视觉/物理缺口

material-scope-delta.csv完整保留Phase3的49对象范围、metadata写入证据与12 Fluid定义；不是49种物理，也不归并3个profile。新证据只更新明确候选，不把注册成功当机制完成。DryQuicksand/SandBlock与SoftQuicksand/SoftQuicksandBlock分开。

DryQuicksand原本类碰撞没有checkPlayerMuddy调用，不能擅自套Mud污染；继承与全局其它触发仍按旧证据边界。33类型、20分级身体UV遮罩、湿润逐步清洗、干燥残留规则继续引用Phase1–4。本轮没有新污渍/镜头闭环，不称所有干沙永远不沾污。

第一人称眼部不透明遮挡与第三人称相机射线仍分开。不能用相机进入代替玩家眼部条件，不用实心碰撞修镜头。音效/泡泡的World RNG与物理耦合不能丢弃。原材质专指MFQM1.1.1自带资源，不是Minecraft占位图。

继续沿用Phase4的247路径/hash与2原附带OGG映射和私有导入工具。没有提取/重绘/AI生成或公开再分发原资源，也没有现代渲染修改。实际Forge1.7.10客户端/专服/视觉/净下沉曲线本轮均NOT_RUN。
''')
out('07_OPEN_QUESTIONS_AND_USER_ACTIONS.md','''# 用户事项与停止点

**目前无必须用户操作。** 不要重传JAR/仓库ZIP，不需要预先截图。本轮输入足够复现所有离线检查，模型与原版实机分开。

未完成：真实BlockMorass全类环境/花提供者；Mire植物雪与其它维度/更新回调；全群系Surface25支路；Forge实际碰撞/更新顺序、1.20空气控制与完整物理；Tombs15处父调用交错、Chest2和现代NBT；完整WLD结构/真实chunk加载；全部视觉。原方法/offset见method-provenance、原Phase4矩阵与本轮cases，未说明项一律BLOCKED。

可选后续原版实机不是本轮前置条件。若再需要人工验收，应先建立MC1.7.10+经核对的匹配Forge+原JAR/可选mod环境，给出固定seed/坐标/配置/输入步骤和原始日志格式，再委托具体小场景，不把离线MODEL_TRACE当运行通过。

建议下一授权只实现两个纯组件规格：DryQuicksand体素事务核心、Stuck属性租约reducer及单元测试。先不注册世界生成、不接物理/网络事件；B1安全层保留。研究在本PR交付点停止，等待验收，不提前开始新版玩法。
''')
print(json.dumps({'cases':len(cases),'ready_components':2,'scoped_surface_candidates':2,'whole_surface_closed':0,'original_runtime':'NOT_RUN'}))
