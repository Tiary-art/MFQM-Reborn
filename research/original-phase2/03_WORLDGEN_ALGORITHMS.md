# 世界生成算法、CFG与未解分支

证据优先顺序：同一原JAR的javap指令、保守CFG、CFR0.152与Vineflower1.11.2交叉读。`evidence/pseudocode/CustomWorldGen.vineflower.txt`是第二反编译器推断，未运行、未声称源码。第一次整JAR反编译在巨型墓室方法OOM；第一次单类运行因输出目录缺失保存失败；创建目录后成功。日志均保存，失败没有当成功。

CFG节点名B后数字为**方法内字节码偏移**，json含精确指令/异常边，五个方法另有dot和标签IR。后向边不等于已证明的自然循环。异常边是保守近似。IR不是高层语义验收的替代品。

|方法签名|基本块|边|后向边|异常表项|状态|
|---|---:|---:|---:|---:|---|
|`generateAOADimGardencia(Lnet/minecraft/world/World;Ljava/util/Random;II)V`|100|156|10|0|PARTIAL：结构化输出可用；全块等价未证明|
|`generateWLD(Lnet/minecraft/world/World;Ljava/util/Random;II)V`|466|732|40|0|PARTIAL：结构化输出可用；全块等价未证明|
|`generateABC2(Lnet/minecraft/world/World;Ljava/util/Random;II)V`|135|213|9|0|PARTIAL：结构化输出可用；全块等价未证明|
|`generateNether(Lnet/minecraft/world/World;Ljava/util/Random;II)V`|131|214|8|0|PARTIAL：结构化输出可用；全块等价未证明|
|`generateSurface(Lnet/minecraft/world/World;Ljava/util/Random;III)V`|1054|1735|65|0|PARTIAL：结构化输出可用；全块等价未证明|

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
