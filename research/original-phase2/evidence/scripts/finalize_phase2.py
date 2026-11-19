from pathlib import Path
import json,csv,re,shutil,hashlib
import argparse
ap=argparse.ArgumentParser();ap.add_argument('--phase1',type=Path,required=True);ap.add_argument('--cfr',type=Path,required=True);ap.add_argument('--work',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--original-jar',type=Path,required=True);a=ap.parse_args()
r=a.out;p=a.phase1;w=a.work;cfr=a.cfr

def out(name,s): (r/name).write_text(s.strip()+'\n')
def table(name,rows):
 with (r/name).open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');wr.writeheader();wr.writerows(rows)
methods=json.loads((p/'indexes/methods-with-instructions.json').read_text()); calls=list(csv.DictReader((p/'indexes/calls.csv').open()))
idx=list(csv.DictReader((r/'evidence/indexes/generator-methods.csv').open()))
(r/'evidence/indexes/worldgen-parameter-expressions.csv').write_bytes((r/'02_WORLDGEN_GENERATOR_MATRIX.csv').read_bytes())
shutil.copy(w/'vineflower-targeted/CustomWorldGen.java',r/'evidence/pseudocode/CustomWorldGen.vineflower.txt')
for f in w.glob('*.log'): shutil.copy(f,r/'evidence/logs'/f.name)
for f in ['core-motion-decisions.csv','material-coating-call-index.csv','coating-type-map.csv','coating-masks.csv','coating-uv-body-map.csv','material-sound-sites.csv','original-runtime-cases.csv','classes.csv','material-behaviors.csv','legacy-sounds.json']:
 shutil.copy(p/'indexes'/f,r/'evidence/indexes'/('phase1-'+f))
# Keep extra callers and motion/effects evidence individually; do not publish assets.
extra=['MFQM','BlockBlossom','BlockQuicksand','BlockSoftQuicksand','BlockMud','CustomPotionEvent','CustomVarPlayer','MuddyEvent','MudModelRenderer','CustomRenderPlayerEvent','CustomRenderEvent','AirEvent']
for m in methods:
 if m['class'].split('.')[-1] not in extra:continue
 src=p/'evidence/bytecode'/(m['class'].replace('.','__')+'.txt')
 if src.exists():shutil.copy(src,r/'evidence/bytecode'/src.name)
# Exact callsite index for registrations, blossom regeneration and motion/effect dependencies.
related=[x for x in calls if x['caller_class'].split('.')[-1] in extra or x['target_class'].split('.')[-1] in extra]
table('evidence/indexes/related-call-edges.csv',related)
# Each method is a separate record. No inferred biome/radius is silently promoted to fact.
rows=[]
for x in idx:
 if x['method']=='<init>':continue
 cs=[v for v in calls if v['target_class']==x['class'] and v['target_method']==x['method'] and v['target_descriptor']==x['descriptor']]
 rows.append(dict(chain=x['slug'],kind='method / helper; chain semantics PARTIAL',legacy_class=x['class'],method=x['method'],descriptor=x['descriptor'],bytecode='0..'+x['last_offset'],callers=';'.join(f"{v['caller_class']}.{v['caller_method']}@{v['offset']}" for v in cs),product_metadata='UNKNOWN: inspect getstatic and write-and-subgenerator-sites.csv',dimension_biome='caller-dependent; see dispatch and source',y='exact expressions indexed; semantic bounds PARTIAL',attempts_probability_rng='rng-call-sites.csv + worldgen-parameter-expressions.csv; no aggregate rate inferred',size_depth_shape='PARTIAL; source + CFG',replacement_support_neighbors='PARTIAL; source + CFG',failure_retry='PARTIAL; early return and loop edges in CFG',cross_chunk='NOT assumed chunk confined',config_order=';'.join(v for v in x['mfqm_fields'].split(';') if v.startswith('Gen'))+'; caller order required',evidence=x['source_file']+'; evidence/cfg/'+x['slug']+'.json',status='PARTIAL',runtime='NOT_RUN'))
# Curated chains supplement, rather than hide, incomplete inventory.
def chain(id,method,product,dim,y,attempts,shape,conditions,retry,cross,config):
 x=next(z for z in idx if z['method']==method and z['class'].endswith('CustomWorldGen'))
 rows.append(dict(chain=id,kind='curated branch; static specification PARTIAL',legacy_class=x['class'],method=method,descriptor=x['descriptor'],bytecode='0..'+x['last_offset']+'; exact calls in indexes',callers='CustomWorldGen.generate',product_metadata=product,dimension_biome=dim,y=y,attempts_probability_rng=attempts,size_depth_shape=shape,replacement_support_neighbors=conditions,failure_retry=retry,cross_chunk=cross,config_order=config,evidence=x['source_file']+'; evidence/pseudocode/CustomWorldGen.vineflower.txt; RNG/write offsets indexed',status='PARTIAL_STATIC_CROSSCHECK',runtime='NOT_RUN'))
chain('GARD-MUD','generateAOADimGardencia','MudBlock meta3; vanilla water meta0','AOA Gardencia dimension route','test66; water65; fill60..64','16*16 columns; no gate','per-column replacement','validWater66 && !validSolid at each write','skip solid cells','within origin16x16 for direct writes','GenMud first; does not set blockGen')
chain('GARD-JQS','generateAOADimGardencia','JungleQuicksandBlock; leaf ring','AOA Gardencia','scan96 down while >68','count50+nextInt(10); nextInt(10)==0 gate; nextInt(10)==0 Flat; each attempt x/z nextInt16 then radius6+nextInt6','generateMireO vs generateMireOD(meta0); leaves radius+3','reject Tar; solid && no liquid above && free; flatSolid at Y and Y+1','countBlock>10 abort scan; continues attempts after success','helper radius may cross chunks','GenJQS&&!blockGen; sets blockGen')
chain('GARD-BLOSSOM','generateAOADimGardencia','Blossom/Lure construction','AOA Gardencia','scan70 while >60; invoke at Y-6','50 attempts; nextInt100==0','origin x-3,z-3; generator literal layout','ground/free/no liquid above; flat at Y-1,Y','stop when blockGen; ignores generator boolean','layout may cross chunks','GenMucBl&&!blockGen')
chain('GARD-MOOR','generateAOADimGardencia','Morass or water','AOA Gardencia','66','50+nextInt30; nextInt15==0; water nextInt100==0','radius20+nextInt10; water min(radius,7); morass18/max(distance,1)','water/free/isGroundQS(round(radius*1.5))','continues after success; anchor uses BGPX==0 sentinel','x/z origin-16+nextInt64 plus radius','GenMoor independent of blockGen')
chain('GARD-LIQMIRE','generateAOADimGardencia','LiquidMire (mode1)','AOA Gardencia','scan96 while >66','20+nextInt10; gate nextInt2==0; radius10+nextInt10','generateLiquidMire material water mode1','vanilla water/free; isGroundNear(round(radius*1.5))','count>10 abort; continues attempts','radius may cross chunks','GenLiqMire&&!blockGen')
chain('NETHER-TAR','generateNether','TarBlock meta0 lake','dimension-1; Tar biome classifier and optional nearby fallback','nextInt128','type4: nextInt1==0 && nextInt3==0; otherwise nextInt8==0 && nextInt5==0','CustomWorldGenLakes.generate mode0','lake shell validation','caller sets blockGen even when lake returns false','x/z origin+nextInt16+8 then lake origin-8','GenTar first; consumes nextInt1')
chain('NETHER-CSAND','generateNether','CSandBlock','dimension-1; getCSandsType','start30+nextInt98; scan >30','type1 count20+nextInt20 else10+nextInt10; gate1/5; radius7+nextInt7','generateMire sand material','validCS/free/no lava above; flat at Y,Y+1','countBlock>50 abort scan','radius crosses chunk','GenCSand&&!blockGen')
chain('ABC2-MOSS','generateABC2','JungleQuicksand via generateMossQS','ABCDim2; ABCBiomes[11] DreadForest','scan96 while >60','count10+nextInt10; gate1/7; radius6+nextInt6; Flat nextInt10 consumed','MossQS helper','nonTar solid/nonliquid/free; flatY,Y+1','continues on success','radius crosses chunk','GenMoss&&GenJQS&&!blockGen')
chain('ABC2-FLESH','generateABC2','SwFleshBlock + blood + tendrils','ABCDim2; ABCBiomes[9] or[10]','scan96 while >60','count5+nextInt2; gate1/3; radius6+nextInt6','generateBlood called THREE times at radius*2; Mire2; tendrilsY+5 radius*2','solid/free; flatY,Y+1 radius+1','countBlock>10; continues','radius*2 crosses chunk','GenMeatS (not gated by !blockGen)')
chain('SURFACE-TOMBS','generateSurface','desert tombs literal structure chain','dim0 normal terrain; desertType1/6 or vanilla desert','scan70+dHeight while >60+dHeight; build Y-8-nextInt9','one try; nextFloat()*750>749','func_76484_a -> generate2 ->3 ->4 ->5 ->6 (sequential, not alternatives)','validSolid center; downstream structure writes','blockGen true even if returned false','large multi-chunk footprint; exact writes indexed','GenDesertTombs&&!blockGen; first feature')
chain('SURFACE-SLIME','generateSurface','Slime','dim0 normal terrain','scan96+dHeight while >16','75+nextInt10 attempts, realCount1; gate1/75; radius7+nextInt10; rejects nextInt(floor((Y/4)/wordSizer))==0','genSlime','validSlime/free/no water above/isInCave; flatY-1,Y,Y+1','stop realCount<=0','radius crosses chunk','GenSlime independent of !blockGen')
table('02_WORLDGEN_GENERATOR_MATRIX.csv',rows)
# Explicit unresolved basic blocks. All five have structured output, not all have semantic equivalence proved.
unresolved=[]; summary=[]
for name in ['generateAOADimGardencia','generateWLD','generateABC2','generateNether','generateSurface']:
 d=json.loads((r/'evidence/cfg'/('CustomWorldGen__'+name+'.json')).read_text())
 for b in d['blocks']:unresolved.append(dict(method=name,block='B'+str(b['start']),end=b['end'],status='SEMANTIC_EQUIVALENCE_NOT_PROVED',next_step='compare Vineflower/CFR stack dataflow, preserve RNG/write ordering; differential mock-world trace'))
 x=next(z for z in idx if z['method']==name)
 summary.append(f"|`{name}{x['descriptor']}`|{x['basic_blocks']}|{x['edges']}|{x['backward_edges']}|{x['exception_handlers']}|PARTIAL：结构化输出可用；全块等价未证明|")
table('evidence/indexes/unresolved-five-method-blocks.csv',unresolved)
# Per-material applicability never converts absence of direct calls into verified absence.
coat=list(csv.DictReader((p/'indexes/material-coating-call-index.csv').open()))
for x in coat:
 x['applicability']='CONDITIONAL_DIRECT_CALL' if x['contact_call_present']=='True' else 'UNKNOWN_INHERITED_OR_EXTERNAL'
 ms=[m for m in methods if m['class'].split('.')[-1]==x['class']]
 sites=[]
 for m in ms:
  for i in m['instructions']:
   if 'checkPlayerMuddy' in i['args']:sites.append(m['name']+'@'+str(i['offset']))
 x['bytecode_calls']=';'.join(sites);x['runtime']='NOT_RUN'
table('evidence/indexes/coating-applicability-49.csv',coat)
# Full class coverage is a gap inventory, not semantic completion.
gaps=[]
for x in csv.DictReader((p/'indexes/classes.csv').open()):
 ms=[m for m in methods if m['class']==x['class']]
 gaps.append(dict(mechanism=x['class'],kind=x['kind'],legacy_entry=';'.join(m['name']+m['descriptor']+'@0..'+str(m['instructions'][-1]['offset']) for m in ms if m['instructions'])[:12000],evidence='Phase1 methods-with-instructions.json; evidence/bytecode/'+x['class'].replace('.','__')+'.txt in Phase1 archive',modern_location=x['modern_location'],port_status=x['modern_status']+' (Phase1 inventory; registration does not prove behavior)',evidence_grade='PARTIAL_SEMANTICS',risk='unresolved lifecycle/RNG/side/metadata equivalence',effort='UNKNOWN until per-method semantic review',depends='original runtime measurements; worldgen helper specification',sequence='worldgen -> motion -> coating/effects -> entities/items/TE',runtime='NOT_RUN'))
table('07_FULL_MECHANISM_GAP_MATRIX.csv',gaps)
# Baseline source hashes and original read-only input.
jar=a.original_jar
manifest={'baseline_main':'88b9ad1a53dd34a2322b7bb78ce0f5dc52d0a69c','original_sha256':hashlib.sha256(jar.read_bytes()).hexdigest(),'original_bytes':jar.stat().st_size,'runtime':'NOT_RUN','worldgen_methods_indexed':len(idx),'worldgen_chains_complete':0,'worldgen_chains_partial_or_inventory_only':len(rows),'five_methods_fully_semantically_closed':0,'status':'STAGED_RESEARCH_PARTIAL','generation_note':'Primary matrix contains method/helper inventory plus explicitly curated branches; not all distinct generation paths yet normalized.'}
out('evidence/manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
out('00_EXECUTIVE_SUMMARY.zh-CN.md',f'''# 原版机制研究 Phase 2 — 分阶段研究交付

状态：**PARTIAL，尚未满足全部算法闭环验收**。本批提供独立研究 PR，不能作为任务 005 实装依据的完整批准件。原版实机全部 **NOT_RUN**，本轮未改动现代玩法源码、原 JAR 或素材，也未构建新 JAR。

基线实际核对为 main `88b9ad1a53dd34a2322b7bb78ce0f5dc52d0a69c`（包含 B2 和 Phase1）。原 JAR SHA-256 `{manifest['original_sha256']}`，1,644,655 字节，与任务书一致。Phase1 报告01–07、类/方法/调用/跳转、49方块和90待测场景均复用；其公开原包在 `../original-mechanics-phase1/`。

已取得五个生成类的213方法索引、7243基本块、1189随机调用点、9080写入/子生成调用点及14040相关调用边。计数是索引覆盖，**不是213个算法已还原**。主矩阵同时列方法/辅助函数和人工细化分支，不得把行数作为独立自然生成器数量。

关键发现：常规生成权重9999999；另有 PopulateChunkEvent.Post 邻区存储转换；BlockBlossom 随机刻再次生长；沙漠墓是连续 generate2→6 的结构写入链。`blockGen` 非全局互斥，部分调用失败仍置 true；`nextInt(1)`仍消费随机数。直接套现代独立 PlacedFeature 会改变顺序和分布。

CFR失败的五个方法均有 javap -v、CFG、第二反编译器结构化输出和报告伪代码。**5/5已恢复可读结构，0/5已完成全基本块语义等价证明**；未解块逐行列于 `evidence/indexes/unresolved-five-method-blocks.csv`。Gardencia、ABC2、Nether 的主分支已人工解释，WLD/Surface 仍有大段复杂地形/辅助函数缺口。不能用“反编译成功”替代算法完成。

运动沿用Phase1的39条已定位主要分支，明确 k/km、事件顺序与净速度区别。污渍提供49材料直接调用适用性审查，未找到直接调用仍标 UNKNOWN。全机制矩阵覆盖161类，条目是缺口登记，不是假定每类只有一个机制。

未完成：所有生成链精确参数的规范化、WLD大结构/Surface群系分支全闭环、墓室全部写入蓝图语义、原版世界生成统计及逐tick轨迹、现代API真实验证。下一阶段顺序见09；本批未启动任务004/005。
''')
out('01_WORLDGEN_ENTRY_CALLGRAPH.md','''# 入口、注册与调用链

以下是静态事实或明确标注的推断；全程未运行1.7.10。精确调用偏移见 `evidence/indexes/related-call-edges.csv` 与 `worldgen-call-edges.csv`，原始指令见 `evidence/bytecode/`。方法名/descriptor消除重载歧义。

```mermaid
flowchart TD
 P[MFQM.preInit] --> E[EVENT_BUS register CustomGenerationEvent]
 I[MFQM.Init: FMLPostInitializationEvent] --> R[registerWorldGenerator weight 9999999]
 R --> D[CustomWorldGen.generate]
 D --> N[generateNether dimension -1]
 D --> S[generateSurface or generateCustom dimension 0]
 D --> O[TF/TBL/WLD/ABC/AOA dimension routes]
 S --> H[terrain helpers: generateMire variants / slime / tar / clay]
 S --> T[GenerateDesertTombs.func_76484_a then generate2 through generate6]
 S --> B[GenerateMucusBlossom.func_76484_a]
 N --> L[CustomWorldGenLakes.generate]
 E --> X[PopulateChunkEvent.Post neighbor storage conversion]
 K[BlockBlossom random tick] --> G[checkCanGrow]
 G --> B
 Q[MFQM.CanBeMudTentacles] --> A[CustomWorldGen.isAboveSky]
 H --> W[World.setBlock / setAir]
 L --> W
 T --> W
 B --> W
 X --> Z[ExtendedBlockStorage direct block/meta writes + World writes]
```

`generate`先按维度路由：-1 Nether；0由 CWG 决定 Surface/Custom，传入 AltitudeShift；1 End（空方法）。TF传 generateCustom(height32)，TBL/WLD/ABC和AOA各用配置维度及对应方法。完整有序分派代码保存在 `evidence/source-methods/CustomWorldGen__generate.cfr.txt`，不要仅凭上图推定维度优先级；维度ID冲突时先匹配分支生效。

每次路由设置 `MFQM.LiqFixer=true`，调用在try/finally中，finally清false。它是全局可变状态，可能影响流体/方块更新，不是一个 Feature 参数。现代异步生成须消除共享状态或明确串行等价上下文。

`AltitudeShift`配置文字是 Water level (62 Default, 144 TerraFirmaCraft)，实际默认62；Surface 用 `dHeight=height-62`、`wordSizer=height/62f`。不能把输入再当增量加62。42项配置声明索引见 worldgen-config.csv；getBoolean(false)是读取API兜底，不能据此把get(...,true)默认误读成关闭。

## 邻区后处理

Populate Post与常规生成分开。维度0扫描3×3邻区、各16存储段、每段16³格。GenTempleQS识别原版TNT及上方砂岩，写Quicksand0、SandstoneTrap0及垂直基础。BoP mud依旧meta与群系分型转换为Mud/草/土/砂；其中换Block不一定同步清meta。

Nether且GenHoney2：3×3邻区BoP蜂蜜/固体蜂蜜转换为MFQM对应块meta0。Betweenlands维度：5×5邻区，TBLMud→Mud3，Tar保留meta，Sludge→Mire0并补下方Mire12/Peat，含跨存储段边界分支。边界逻辑原样保留在populateChunk证据，尚未证明所有局部Y条件符合设计意图。重复Post可能重复扫描；生成顺序、邻区可用性和重入需实测。

## 扩展搜索边界

调用图不是五类封闭图：额外包括MFQM注册/配置/触手判定、BlockBlossom随机刻、World/Chunk/ExtendedBlockStorage、ChestGenHooks、刷怪笼TileEntity、方块更新副作用。Tombs/MucusBlossom虽实现IWorldGenerator，其接口generate方法为空；不能仅根据接口宣称被独立注册。未证明反射/其他模组动态调用全部覆盖。

注册和配置的字节码保存在 MFQM 文本中；每个调用精确偏移可从相关调用CSV按 `target_method=registerWorldGenerator`、`register`、`isAboveSky`过滤。生成开关在同一方法多次使用，必须保留源程序顺序，不是互不影响的概率表。
''')
out('03_WORLDGEN_ALGORITHMS.md','''# 世界生成算法、CFG与未解分支

证据优先顺序：同一原JAR的javap指令、保守CFG、CFR0.152与Vineflower1.11.2交叉读。`evidence/pseudocode/CustomWorldGen.vineflower.txt`是第二反编译器推断，未运行、未声称源码。第一次整JAR反编译在巨型墓室方法OOM；第一次单类运行因输出目录缺失保存失败；创建目录后成功。日志均保存，失败没有当成功。

CFG节点名B后数字为**方法内字节码偏移**，json含精确指令/异常边，五个方法另有dot和标签IR。后向边不等于已证明的自然循环。异常边是保守近似。IR不是高层语义验收的替代品。

|方法签名|基本块|边|后向边|异常表项|状态|
|---|---:|---:|---:|---:|---|
'''+ '\n'.join(summary)+'''

所有五方法未闭环块的B起止范围已逐块登记 `unresolved-five-method-blocks.csv`。这张表保守地包含全部基本块：局部人工解释没有升级为全块等价。下一步应逐块进行值来源/短路次序检查并差分mock-world写入/RNG轨迹；不能从删除无用变量的反编译输出直接推论随机调用被删除。

## Gardencia（局部高层恢复，PARTIAL）

```
probe biome using random x,z; blockGen=false
if GenMud: for h,v in [0,16): if water at66:
  if !solid65: write water0 at65
  for y60..64: if !solid: write Mud3
if GenJQS && !blockGen:
  count=50+nextInt10; if nextInt10==0:
    Flat=(nextInt10==0)
    repeat count: choose x,z in16; radius6+nextInt6
      scan96 while y>68; rejectTar; accept solid+free+no liquid above
      break scan if countBlock>10
      if accepted and flatSolid(y,y+1): MireO if Flat else MireOD(meta0)
        leaves(y+3,radius+3); blockGen=true  // does not terminate loop
if GenMucBl && !blockGen: gate1/100; up to50 while !blockGen
  scan70>60, ground+free+no liquid above; flat(y-1,y)
  call blossom(x-3,y-6,z-3); blockGen=true // result ignored
if GenMoor: count50+nextInt30; gate1/15; repeat:
  center x,z=origin-16+nextInt64; y66; radius20+nextInt10
  water+free+groundQS; first anchor when BGPX==0
  nextInt100==0 -> water(radius min7), else Morass(18/max(distance,1))
if GenLiqMire && !blockGen: count20+nextInt10; gate1/2
  scan96>66 for water+free; radius10+nextInt10; groundNear(round(radius*1.5))
  LiquidMire(water,mode1); blockGen=true
```

每行底层调用的精确偏移按方法过滤rng/write索引取得。`BGPX==0`哨兵在真实坐标0附近可能重复选锚；作为旧逻辑记录，不擅自修复。

## ABC2（主分支恢复，PARTIAL）

按ABCBiomes[9]/[10]识别Dreadlands，[11]DreadForest，[12]Purified。顺序是Moss/JQS→LiquidMire→SwallowingFlesh→Tar。Moss门1/7、次数10+nextInt10、半径6+nextInt6；Flat的1/10随机数即使不影响最终选择仍消费。LiquidMire门1/10，类似扫描96>60，flatOrLMire，mode0。

Dreadlands GenMeatS不受!blockGen约束；门1/3、次数5+nextInt2、半径6+nextInt6。接受地面后先调用三次generateBlood(radius*2)，再判断flatSolid半径+1、生成Mire2(SwFlesh)与Y+5触须。前置血液写入可能存在，即使后置平坦判定失败。

Purified Tar：次数20+nextInt10，radius10+nextInt5，realCount10+nextInt20，门1/4；首个合适foundation只设aDetBlock，后续才canGen。首次成功记录FX/FY/FZ并把genCount改750；簇半径floor(30*min(1,realCount/20d))，之后围绕锚点采样。外围岩块次数genSand*10+T_real+nextInt(T_real/2)，T_real=初始realCount*4。连续条件会覆盖rrad，不能简化成互斥等概率选型。精确岩块及地面辅助函数语义仍待闭环。

## Nether（主分支恢复，PARTIAL）

Tar先执行；type4门nextInt1==0 && nextInt3==0，其他nextInt8==0 && nextInt5==0。nextInt1仍推进RNG。选origin+nextInt16+8、Y nextInt128，调用Lake mode0；返回false也blockGen=true。

CSand仅!blockGen：type1次数20+nextInt20，否则10+nextInt10，门1/5，radius7+nextInt7。Y30+nextInt98下扫>30，validCS/无熔岩上盖/free，countBlock>50中止；flatY/Y+1后generateMire(sand,CSand)。

Flesh族仅!blockGen进入：血群系次数40+nextInt20/门1/4，其他30+nextInt10/门1/50，BoP可再乘100。无BoP时坐标正弦场影响门分母，保留源式不可替换为统一概率。GenMeatS先血液三次；GenMeat与nextInt5决定肉坑/吞噬肉分流。genHole后GenMeat最多2*count尝试，生成前isVorePlace与flatVore；GenMeatAss再有1/(genPos+5)门，最多count*40直到real=count/4耗尽，以上次成功点为锚，执行ClearArea2、Blood2、flatSlurry、Mud2、Slurry和条件Ass。吞噬/排泄结构辅助写入和各短路路径未全部语义证明。

## WLD（未完整恢复，明确PARTIAL）

已结构化全部方法，未完成人工全分支核对。WLDBiomes[0..5]分别forest/desert/snow/tainted/ashes/volcan。首支沙漠QS次数2+nextInt5，门1/10，radius5+nextInt7，Y96>60，flatY/Y+1再Mire(QS)。随后还有±3区块搜索金字塔材料及大范围结构改写；原版邻区exists探测、随机寻找底部、k20下降到0的水平截面以及刷怪笼多级随机替换不能忽略。

**尚未闭环**：该结构改写全部metadata/支撑、后续群系生成支路、跨区块读写范围及flat/helper短路。具体B列表见未解CSV中generateWLD全部行，具体源分支见第二反编译器方法8042起（以文件内容为准）。下一步从调用/写入偏移向上做数据流分段，不能将这个方法当普通QS Feature直接移植。

## Surface（未完整恢复，明确PARTIAL）

height默认62；dHeight=height-62；wordSizer=height/62f。顺序为Tombs→WastePit→Wax→Honey→Slime→Web→Larv→SSnow→SSand→MucBl→QS→JQS→Gravel→Morass→Moor→Tar→SQSF→SQS→Moss→Bog→LiqMire→Clay组→Mire/Mud→HClay→HPClay及条件SClay；嵌套分支/配置仍以源程序为准。Slime/Moss/Moor等不统一受!blockGen控制。

Tombs门为nextFloat()*750>749，不是nextInt750；一次扫描70+d>60+d，地面后调用Y-8-nextInt9，调用结果不决定blockGen。WastePit先消费dep=nextInt10==0，再按BoP群系门1/75，30+nextInt30尝试、半径10+nextInt10，MireD/Mire分流。Wax门1/85最多52次，只有成功才置blockGen并break。Honey门1/175最多50次，半径采样在门前，蜂巢近邻拒绝可终止尝试。Slime独立门1/75，最多75+nextInt10、真实成功预算1；洞内扫描96+d>16，有“nextInt(floor((Y/4)/wordSizer))==0就拒绝”的高度偏置。

**尚未闭环**：Surface剩余各群系链的具体条件/概率/metadata、局部变量复用、clay/泥浆反复地表改写。逐块缺口全部登记。主矩阵相关记录明确UNKNOWN/PARTIAL，没有用现代默认参数填空。

## 湖泊（具体算法，静态恢复但未实测）

CustomWorldGenLakes.generate：x/z各减8；从输入Y向下寻非空气直到>5，否则Y<=4失败；mode!=2时Y再减4。16×16×8布尔体，4+nextInt4个椭球，直径分别nextDouble*6+3、*4+2、*6+3；中心按剩余边距随机。内部循环局部x/z1..14、y1..6，归一化距离平方和<1置mask。

对未mask且六邻接mask的壳：上半y>=4遇液体失败；下半必须solid或同blockIndex否则失败。验证后对mask写入：上半空气、下半目标块meta0/flag2，**同样的选择还写到该格Y-1**。这不是普通单层lake模板。表层土依biome.topBlock和天光替换草/菌丝。mode1另作石衬与随机条件；非mode1另尝试结冰。完整排除材料见generate.cfr与指令，映射现代时须显式决定此双写/结冰是否保留。

## 墓室与植物

墓室不是六选一：func_76484_a连续调用generate2→3→4→5→6。大量literal坐标/metadata在源码与9080调用点索引中；本批未把每个写入整理成验收蓝图。刷怪笼写SpawnRange32、Count1、Skeleton/Zombie随机、MinDelay400/Max1600、MaxNearby3；宝箱混用ChestGenHooks及自定义权重，消费World RNG，不能与传入Random合并。

MucusBlossom接口generate为空，func_76484_a实际构造Blossom/Lure、metadata及向下列。checkCanGrow遍历i0..8，在y-i+1取中心/四角/四边共9点半径3检测；i>3改dirt允许条件，force可绕过检查。BlockBlossom随机刻可再次调用，属于生态更新，不仅是地形初始化。具体literal形状及validMaterial条件见对应单方法证据，尚未完成全部蓝图验收。

## RNG约束

随机调用CSV保留每个调用descriptor/offset与前置指令，常量表也有精确offset。传入Random与World.field_73012_v分别保留；计数/半径常常在门之前采样，失败也可能消耗RNG或留下部分写入。nextInt1不能删。共享World RNG可能与粒子/实体/其他生成交错；本批没有证明旧Forge全部执行调度，故不能声称跨版本固定种子逐块复现。
''')
print(json.dumps({'primary_matrix_rows':len(rows),'unresolved_blocks':len(unresolved),'gap_classes':len(gaps),'coating_rows':len(coat)}))

out('04_WORLDGEN_PORT_SPEC_1_20_1.md','''# 1.20.1 Forge 适配规格（提案，未实施/未编译验证）

现代源码基线88b9ad1；worldgen目前只有包占位，不能把49方块注册视作生成完成。原版参数只取02/03与指令证据；本文件新增设计一律是 **PROPOSED_MODERN_ADAPTATION**。

|原版链|候选机制|语义差异与需决定事项|验收|
|---|---|---|---|
|Surface/Custom/Nether内有序地形斑块|一个编排Feature封装各旧算法，ConfiguredFeature参数化，PlacedFeature控制入口，Forge biome modifier挂载|独立PlacedFeature会打乱blockGen/共享RNG与失败副作用；先保持编排顺序，再决定是否拆分|相同mock地形+相同随机序列的写入/调用轨迹差分；实际世界只比较统计|
|Mire/MireD/MireOD等形状|Feature内确定性体素算法，使用RandomSource适配|nextInt1保留；Java Random与新版RNG不可默认序列一致；先允许显式legacy RNG策略|半径/深度/支撑/空洞边界fixture；失败前后写入差分|
|CustomWorldGenLakes|自定义Feature，不直接套现代LakeFeature|双写Y-1、壳验证、mode1衬层/结冰、原版材料分类和meta语义不同|16×16×8mask及实际写入范围、液体泄漏拒绝、边界位移|
|Tombs连续大结构|Structure+StructurePiece或模板化pieces，宝箱LootTable/刷怪笼BE|旧入口概率浮点门、跨区块一次直写、初始化顺序与piece按区块写不同；还未整理完整蓝图不能开始实现|结构锚点/每piece边界/metadata映射/宝箱刷怪笼数据；多区块重复生成与保存重载|
|MucusBlossom首次生成|Feature；生态再生另用block randomTick|checkCanGrow的force/dirt和调用偏移要保留；不可只做初次Feature|初生、破坏、邻接、强制放置、随机刻再生分别验收|
|Populate Post替换TNT/BoP/TBL|兼容模组专用Feature或安全区块后处理队列，待调度验证|没有可直接宣称等价的同名现代事件；禁止在异步生成中随意加载3×3/5×5邻区、直改section漏光照/高度图/脏标记|原邻区可用性重放；区块不额外加载；状态/光照/保存一致|
|TF/WLD/ABC/AOA维度与整数群系数组|ResourceKey/Tag可配置路由，软依赖检测|旧mod不存在时不能仅照抄整数ID；需要明确用户选择的现代对应模组；缺失依赖不生成、不崩溃|依赖存在/不存在/群系tag为空/维度冲突|
|MFQM.LiqFixer全局标记|显式局部GenerationContext，作用域finally清理|不能保留跨线程共享boolean；哪些流体更新抑制必须先追踪消费者|并发区块生成、异常回滚后无标记泄漏|

旧meta须逐块映射为BlockState属性，Mud3/Mire12等不能被统一默认状态吞掉。物品掉落、碰撞、液体source判定必须在材料规格闭环后决定。全局高度不应机械把旧62改成新版海平面：先提供legacy高度策略，再以现代地形高度作为用户可选适配。两种均不能伪装旧事实。

## 保真与统计验收门

第一层是纯算法：mock-world记录每次RNG调用类型/界限/顺序、读取坐标、写入块/状态/flags、提前退出；不要求运行Minecraft即可检查局部语义，但本批尚未实现该harness。

第二层是1.7.10参考实测：08中固定种子和坐标，分维度/群系/配置统计尝试、门通过、地面拒绝、成功斑块及部分写入。第三层是现代同类地形分层样本；不要求跨版本逐方块地形一致。报告每组样本量、按群系/高度分层的密度、连通面积/深度/失败率、置信区间和原始分布。

验收容差尚未指定：须先获得原版基线和误差/多次运行方差，再写入后续任务书。不能现在编造“相差5%即可”冒充历史要求。任务书授权的船兼容性增强与旧世界生成保真分开验收。
''')
out('05_MOTION_EXECUTABLE_SPEC.md','''# 三核心运动逐tick规格：局部可执行，完整等价仍PARTIAL

**本文件不能直接当作完整物理实现批准件。** 39主要分支静态定位已完成（复用Phase1），全部嵌套路径的可执行闭环未完成，旧版运行NOT_RUN。精确十进制偏移、方法descriptor及作用见 `evidence/indexes/phase1-core-motion-decisions.csv`；原指令在对应Block/CustomPotionEvent字节码。下面只对已确认表达式给伪代码，未知helper不填假系数。

## 状态与事件顺序

状态最少包括旧posY/prevPosY/AABB.minY/eyeWorldY、oldMotion、k/km/prevk、mtd、mr、动作位、装备缓存、ground/web、水状态、worldTime、RNG。旧玩家posY不等价现代feetY；QS/Mud玩家k=posY-blockY-1，非玩家k=posY-blockY+.5，Soft再减.2。km=max(k,0)。连续上两块同材时k=.001，**km不重算**。

```
旧一次碰撞回调:
  保存旧位置和速度；区分玩家/生物/非生物
  计算k、km、prevk、metadata/泥深和动作标志
  按材料/特殊实体路径早退或阻尼
  先执行原本位于物理前的声音/泡泡（可消费World RNG）
  执行特殊实体分支、拓扑修正、跳跃吸力
  按原k分段执行补偿/web/ground/阻碍/位置回退
  执行inWater/堵顶/antiHoldJump等尾部
另一次LivingUpdate:
  移除固定UUID旧modifier
  读取stuck Level，非线性调整jumpMovementFactor和移动属性
  重置Level，等待碰撞续期
```

这不是保证Forge事件全局顺序的声明；LivingUpdate相对多方块碰撞、客户端/服务端的实测顺序仍UNKNOWN。重放需逐回调序号，不能每tick合并为一个接触事件。多个接触会覆盖setter，不是统一max。

## Quicksand

偏移0–184坐标；246–568动作/mr；568–615入口；615–1097FX；1098–1395特殊实体早退；1396–1579拓扑/吸力；1580–2418分段；2419–2514尾部。

```
mr=min(5+floor(max(0,100*(1.5-km))),145)
vx=0; vz=0; vy=(vy>-.1 ? 0 : vy/2)
if EntitySandBlob或兼容例外: 专用.08/.1补偿，reset fall/ground，return
if above1 && above2同材: k=.001 // km仍旧值
执行条件跳跃吸力
if k>=1.2 && !splash: 原分母正Y补偿+随机web/ground
else:
  若k<1.2且ΔY>.001且RNG/helper通过: 额外负Y吸力
  if .9<=k<1.2: 正补偿、setStuck(mr)、清fall、随机web/ground
  else if k<.9: tick改变a2和side-specific stuck
    if .5<=k: .0725/.075由web选择；移动时分母div+.075
    else: web；移动分母div+.025；k<.45且isTrulySink强制mr145
尾部: 水中正vy/4；堵顶web/stuck；antiHoldJump；非生物k<1.45 web
```

上述“原分母”不是省略后仍完整可执行的承诺：详式及helper闭环仍PARTIAL，下一阶段按1580–1755、1876–2060等逐块翻译。不能据此擅自写统一目标速度。

## SoftQuicksand

偏移0–219坐标；220–542动作；542–603阻尼；603–1218FX/例外；1219–1438拓扑；1439–2773各深度；2774–2882尾部。

`mr=(int)min(5+floor(max(0,pow(12.5*(1.5-km),1.75))),175)`；div=1+2*distance+rotation项。先vx/vz乘.71，vy>-.1清0否则/2。SandBlob早退，后续还有触手路径。

1.2<=k<1.3且!splash先加.0735支撑，横向乘clamp((k-1.25)*4)。后面局部a1=.0725赋值不追溯重加（1465–1526与1627–1630）；k>=1.3跳过此子分支。.9<=k<1.2时玩家tick选.0735/.0715+web，非玩家位置回退，支撑分母2*div-1。k<.9且中心径向距离在[.075,.5)时清X/Z并向中心吸引，除max(10,km*50)，足够强时会改变moving/div。更深区.5<=k<.9移动分母4*div+.075；k<.5分母16*div+.025，k<.45且side eligible强制175。尾部水中正Y/4、堵顶web/stuck、antiHold、非生物触手另行处理。

## Mud

偏移0–582 metadata/装备；582–914动作；914–1023浅泥早退；1024–1814例外/FX；1815–1884阻尼；1885–2267拓扑/吸力；2268–3408深区；3409–3522尾部。

meta<3时mtd结合几何深度，安全边界可能重置0；涉水靴可改变路径。`mr=(int)min(5+floor(max(0,pow(4*(1.5-km),1.5))),145)`，div=1+5*distance+rotation项。无靴且onGround先vx/vz*.1；**mtd0提前返回，不能总执行/10**。正常mtd>0路径vx/vz*.71，k<1.3清bootsFloat，vy>-.1清0否则/10。

k>=1.3 !splash：周期8选.075/.07485；靴子.085/.1，否则分母含/3与mtdkof*17.5；web或非玩家回退。.9<=k<1.3：setStuck(mr)，周期4，mtd>2时groundfalse；k<.9 a2=1/.95与web；.5<=k<.9随机.0725/.075、移动分母div+.25；k<.5若水中/上方水a2=1.01，否则k<.475时1.05、移动分母div+.025，k<.45 eligible强制145。尾部inWater正Y清0再-.01；antiHold只在正常拓扑分支；非生物触手分开。

## 真正移动阻碍与数值边界

CustomPotionEvent：每次LivingUpdate先移除UUID `73A49882-85A3-4896-AD2D-8C591E24AA62`。Level>0时p=Level-5，水平碰撞c=0否则1：

```
jumpMovementFactor /= max((1+p*(1+c*2.5)/1000)^8,1)
speed=max(1/(1+p*(1+c/2)/50)^2,.02)
if p>=250: jumpMovementFactor=0; speed=.02
if jumpMovementFactor<.005: jumpMovementFactor=0
添加operation2、amount=speed-1、不保存modifier
Level=0; 未续期下次0 -> -1
```

Soft/Mud负底数的非整数幂会NaN，最终转int0，不是先clamp底数得5；移植是否修复须显式决定。isTrulySink对玩家返回world.isRemote，对非玩家true。装备每32tick缓存，浮力/boots/armor/heavy不能当成纯装饰。

吸力VelY=max(prevMotionY*10,.25)，不是abs；ΔY>.2的jump判定、ΔY>.001上升分支和antiHoldJump三个不同入口。正Y .075等是速度增量而非净位移；不可与重力简单抵消后宣布已测曲线。

## 深陷反馈与B2差异

现代 `physics/MotionMath.java::velocity` 是 `-min(terminal,base+depthGain*min(1,depth/2)+movingExtra+struggleExtra)`。这是深度增加会加快的候选目标速度；原版分段支撑、web/ground、非线性阻碍和事件次序不能由该式表达。用户观察“深陷净速度减慢”是待逐tick验证的行为假设；没有证据证明三种材料所有输入均严格单调。本批没有把斜率倒过来当还原。

## B1安全层边界（现代适配提案）

原版算法层输出旧坐标转换后的状态增量和事件意图；现代权威层保留ContactSampler预测扫掠、高速入沙耗散预算、Y同步和条件着地处理。不要删除安全层来复刻旧碰撞时序；避免安全层在原版补偿后再次盲目覆盖速度。B1既有测试结果保留其原报告范围，本批未重新实测。

后续验收层分别跑局部公式、逐回调RNG trace、现代server/client轨迹及高速入沙/落地音效回归。原版深度×初速度×输入×装备轨迹用08计划获取，全部NOT_RUN。
''')
out('06_COATING_VISUAL_AUDIO_SPEC.md','''# 污渍、视觉、声音与基础交互规格

证据主要继承Phase1报告04/05及本批拷贝的精确索引；所有运行行为仍NOT_RUN。49材料审查见 `evidence/indexes/coating-applicability-49.csv`，有直接checkPlayerMuddy调用的为条件触发；无直接调用标UNKNOWN（继承/外部入口未排除），没有凭空把全部干沙判为不污染。每个发现的调用附方法@字节码偏移。

## 污渍规则

|核心|实际type|更新上限/增加|残留|
|---|---:|---|---:|
|Quicksand|4|5000/+100|1000|
|SoftQuicksand|17|2000/+100|1000|
|Mud|getMuddyType(Mire)=9|1000/+50硬编码；不是Mud数组29|1000|

33类型、20张64×32遮罩的文件名/哈希与映射分别在phase1-coating-type-map/masks索引。没有上传原图。BrownClay重复索引以首次匹配为准。原版污渍不是“触碰即全身”：按玩家posY+eyeHeight-blockY的阈值依次 `<.7→10, <1.04→9, <1.10→8, <1.21→7, <1.32→6, <1.53→5, <1.67→4, <1.98→3, <2.14→2, <2.4→1`，其余0。等号进入下一档；旧坐标转现代尚待运行核对。

QS/Soft覆盖比较 `preLevel*(maxOpacity/1000)>oldLevel*(oldTime/1000)`；Mud为 `preLevel>oldLevel*(oldTime/1000)`。服务端湿润且不在两种LiquidMire的L检测内时，time每次减5+time/100夹0；worldTime%16==0且旧level>5时level减1。干燥时worldTime%1024==0且level>5、time<1000才降级，worldTime%2==0且time>该type残留阈值才减1。因此饱和泥污可干燥残留，不是必然自动洗白。雨/水应分别记录isWet、LiquidMire排除、worldTime，不能只按进入水体立即清零。

渲染门mt>50、level>0及type检查；alpha=min(1,mt/1000)，level选择textures[level-1]。Mud族level1/2仅腿，level3起躯干/手臂，level6起头；Slime族level7起头；帽壳20图均未发现非透明像素。索引的像素数不等于三维覆盖面积。现代CoatingLayer残留整层表现尚未达到旧逐级UV语义。

原版扫描主Biped模型/手部复制UV并膨胀.2；不证明此路径必然涂全部盔甲。现代64×64左右独立四肢及Alex需重映射，盔甲遮挡另测。DataWatcher打包边界和死亡255异常是兼容/修复决定，不能机械复制成安全现代字段。

## 遮挡、镜头与FOV

原版眼部触发取玩家眼位置偏移-.2，暗色RGB .1、alpha1不透明；这是玩家浸没触发，不是摄像机进入就触发。第一人称遮挡和第三人称相机方块射线/visual shape分开建模；第三人称镜头进入而玩家在外，不能错误激活第一人称污屏。旧方块射线/选框不等于实体实心碰撞；禁止给全部流沙加实心collision来修镜头。

FOV须记录原版事件缓存/恢复条件；现代状态按本地玩家与生命周期隔离，退出/死亡/换维/断线必须恢复。局部模组FOV处理不能全局改原版基础设置。AirEvent/原版气泡栏与现代NativeAir的证据/差异参照Phase1报告05和B2源码，本批未做回归测试。

## 声音与随机数

`evidence/indexes/phase1-material-sound-sites.csv`按材料列具体playSound调用，`phase1-legacy-sounds.json`仅记录模组自有bee声音注册；前一CSV保留反编译参数表达式；调用点精确偏移可在对应块字节码过滤func_72908_a等核对。旧Minecraft内置swim/slime/water/silverfish等事件与模组自有bee OGG区分，不能为每种沙编造专有OGG。声音音量/音高/动作门/clock门必须逐调用取原表达式，不统一为MudStep。

声音/泡泡常在吸力web判定前消耗World RNG；若现代FX改独立RNG，要把轨迹不再逐调用相同写成兼容决定。本批声音索引是调用覆盖，尚未把全部表达式规范化为逐事件可执行调度，状态PARTIAL。没有打包OGG，没有生成或重绘贴图。

## 其他交互：事实/现状/方案/测试

|机制|原版证据边界|现代入口|拟后续工作与场景|
|---|---|---|---|
|原生air/气泡栏|AirEvent与块内窒息调用；不能用自绘条宣称原生|NativeAir/SinkHud|头进出、creative、死亡、服务端扣气同步；NOT_RUN|
|内侧放置|旧可替换/射线与更新链须区分|SinkingBlock/CoreSinkingBlock|沙中脚边/头顶/不同物品/邻接多格；PARTIAL|
|泥堆叠/形状|meta+几何深度/mtd安全分支|MudGeometry/MudBlock|1/2/3层、边缘、保存重载；不是注册即完成|
|条件下落|块随机刻/邻更与LiqFixer相互作用|SinkingBlock|失去支撑/液体/跨区块边界；各材料独立查证|
|船|核心非生物web等路径未证实专用浮船算法|BoatMotion/ContactSampler/MotionRuntime|用户指定兼容增强；不可称旧版复刻。空船/载客/冲入/跨界/保存重载分别测|
|泥浆泡泡|旧SpawnBodyBubble/表面泡泡及开关、RNG|现代粒子/音效路径|不同meta/深度/玩家与非玩家，频率及穿顶；NOT_RUN|

船测试矩阵必须独立列Quicksand、SoftQuicksand、Mud：预期为用户定义“稳定受浮力支撑、保留有限阻力/可移动、载客时不污染玩家独立陷落状态”，此为增强提案，具体浮面高度/阻尼数值未定。水中Boat浸没检测不能直接从水tag推到流沙；原版没有证实的行为保留UNKNOWN。其他实体逐类处理，不能把Boat修复套给所有非living。
''')
out('08_ORIGINAL_RUNTIME_TEST_PLAN.md','''# 原版运行与测量计划

状态：**NOT_RUN**。本轮仅静态读取JAR和运行分析脚本，没有启动1.7.10客户端/专服，没有原版世界存档、截图或逐tick实测数据。旧90场景索引逐项复用，不能据此前现代B1测试推导原版通过。历史用户EULA同意不代表此次已跑服。

## 环境与采样（以下全部是本研究选择的测量参数，不是旧算法常量）

私有安装MC1.7.10/相应Forge/原JAR，首次日志记录Java、Forge版本、mod列表和配置hash。资源仅从合法持有JAR加载，不加入公开repo。选种子0、1、-1、987654321为研究样本；每个配置新建存档，不在同存档来回切配置。先分别只开一个生成开关，再全开原默认，必要可选模组分别装/不装。

对各维度在区块中心(0,0)、(32,32)、(-32,-32)附近各取16×16区块窗，按固定Z行/X列顺序触发生成；另重复反向顺序，检查邻区后处理差异。这里16×16是采样预算，绝非旧每feature次数。群系不足时记录缺样而不改群系冒充自然样本；补充已查明群系坐标并保留发现过程。结构稀有时扩大样本，不能把零事件样本解释为无机制。

每chunk记录seed/dim/chunk/生成次序/群系配置/入口次数/门通过/地面拒绝/部分写入/最终材料meta计数；每斑块记录连通体ID、面积、体积、最高最低Y和深度；结构记录锚点、bbox、宝箱与spawner数据。失败率须instrument门通过和实际失败，不能从最终方块计数反推出尝试失败率。重复加载与已生成邻区分别测试，避免把Post转换多次算新生成。

## 非修改原版的测量方式

优先外部观察/存档扫描：每次生成前后复制世界，读取Anvil区块快照做材料/meta差分；原JARhash前后相同。需要入口/RNG/tick细节时使用独立Javaagent/调试器只记录方法边界、局部值、Random调用；工具尚未实现，状态PLANNED，不能声称已有可运行探针。不要为了测量直接改原JAR。记录instrumentation开关和性能影响，做未插桩对照。

## 运动样本

三材料分别设置均匀池/混合边界/1-3+层Mud；固定初始AABB与原posY，入射vy=0、-.1、-1、-3作为探针输入。输入静止/行走/冲刺/单跳/持续跳/转身分别跑，靴/重甲/无装备、玩家/生物/非生物分层；水上盖/堵顶分别测。每组至少重复若干World RNG状态，先报告原始轨迹再决定统计样本量。

每tick列worldTime/side/callbackSeq/entityID/posY/prevPosY/AABB.minY/eyeY/motion前后/k/km/mtd/mr/ground/web/fall/输入/装备/RNG调用序。深度按实际表面与AABB定义，先验证旧坐标转换；比较净ΔY曲线及水平/跳跃能力，不能用某一次正Y补偿冒充净速度。深陷减速是否成立按材料、姿态与初速度分别回答，允许非单调结果。

## 视觉和交互

49材料的污渍直接调用与UNKNOWN分别测；各等级边界等号、饱和/未饱和、雨/水/LiquidMire、死亡重生、盔甲、第一/三人称和换维。眼部跨界与仅相机进入分别截图；FOV退出/重连/断线恢复；内侧放置、stack、支撑移除和泡泡独立测试。

船按三材料×空船/载人×静置/冲入/跨边界×单机/专服列矩阵。原版观察仅描述实际；现代用户浮力增强另有预期，不修改参考数据迎合目标。旧水中船作对照，记录状态枚举、浸没高度/速度/阻力而非只看截图。

## 输出规范

保存commands.log含退出码、原始CSV、环境manifest、存档hash及截图索引。行状态NOT_RUN/FAIL/PASS/INCONCLUSIVE分开；空数据不是通过。静态脚本的exit0只表示索引检查通过。本批不含任何伪造测量CSV。
''')
out('09_IMPLEMENTATION_ROADMAP.md','''# 后续研究与开发路线（草案，不实施）

本次仅研究阶段提交，任务004/005没有启动。以下依赖必须按证据闭环推进，不把文档存在当作规格完整。

1. **研究批次A：关闭世界生成缺口。** 按unresolved-five-method-blocks逐块核对Vineflower/CFR/栈数据流；优先Surface三核心链与WLD结构改写。把主矩阵UNKNOWN逐条换成带offset的精确参数，抽出墓室连续pieces完整蓝图。交付RNG/写入mock trace harness；所有213方法分别给完成/未完成列表，不能只删未解行。
2. **研究批次B：原版可复现测量。** 依08建立私有旧环境和只读存档差分；先小样本验证工具，再世界生成统计与深陷轨迹。未具备环境继续NOT_RUN；不得先拟合目标曲线。确认用户观察的适用范围。
3. **规格批次C：物理闭环。** 将39主分支扩成逐路径执行规格，审阅坐标和NaN/side/装备策略；确认原版算法层与B1安全层接口。独立文档PR可以先合并，不改速度。依赖A的helper知识及B的轨迹。
4. **规格批次D：材质/视觉/声音。** 49材料逐个排除继承/外部污染入口，声事件参数规范化，64×64/Alex及盔甲策略、眼部与镜头分别写验收。素材授权未确认前只用名称/hash映射，不上传旧PNG/OGG。
5. **经用户后续授权的实现批次。** 生成先编排Feature和少量核心材料、再结构与兼容模组；运动单独PR并保留B1回归；污渍视觉分开；实体/TE/物品与用户船增强单列。先说明行为/验收/风险再开始，不自动实施本路线。

建议下一任务书明确：只关闭Surface三核心生成及Gardencia全部B块，交付完整精确参数和mock-world随机写入差分；不要求一次实现161类。随后再指定旧运行测量任务及合法私有环境。当前不能给出可信工时：复杂旧结构/可选模组和测试可用性尚未知。

可合并性：本批为独立研究分支，全部变更限制在research/original-phase2，无现代runtime差分。PR应保留PARTIAL标签/说明；接受阶段文档并不表示全部Phase2验收通过。
''')
print('specifications written')
