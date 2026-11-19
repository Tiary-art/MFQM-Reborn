# Gardencia：覆盖、局部闭环和未解分别统计

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
|B254..255|Flat=true, passed seed/gate; old fixtures only used Flat=false|MODEL_TESTED|
|B387..390|valid solid ground but isAboveFreeSpace=false; ceiling fixture|MODEL_TESTED|
|B393..396|Tar early break; tar fixture|MODEL_TESTED|
|B406..406|solid/free rejection countBlock>10; ceiling fixture|MODEL_TESTED|
|B459..479|Flat path executes generateMireO; seed114|MODEL_TESTED|
|B684..684|MucBl ground valid but space blocked; sand-ceiling|MODEL_TESTED|
|B694..694|UNREACHABLE: ten Y positions, countBlock<=10, guard>10|PROVED_UNREACHABLE|
|B1014..1034|Moor nextInt100==0 executes generateWater; seed2132|MODEL_TESTED|
|B1246..1246|LiquidMire water but overhead blocks; alternating water/solid|MODEL_TESTED|
|B1256..1256|LiquidMire scan rejects >10 water layers; alternating fixture|MODEL_TESTED|

JQS Flat seed114、OD seed10执行真实MireO/OD及LeavesAround；LiquidMire seed1 water-island fixture执行真实填充；Blossom seed384执行原GenerateMucusBlossom构造算法。Moor seed2132在第一次合适点选择Water分流，后续Morass仍可能失败。99块覆盖包含两条失败样本在ERROR之前已经执行的前缀；这不是两条样本完整通过。完整大轨迹为gzip **分析日志**（非原始素材），可解压逐事件审阅；并保存raw SHA及独立coverage。

## GenMud局部闭环定义与证据

调用范围：原generate路由以`MFQM.AOADimGardencia`选择本方法并用LiqFixer作用域；本轮反射直接调用helper，不证明该路由/现代维度映射。条件：GenMud开/关，其他四个开关关闭；世界API遵守tools/World.java定义的纯读、按坐标写入/返回applied、material属性与biome合同，原helper不另消耗RNG。独立reference_mud.py不是trace_vm/ASM解释器：手工导出循环/分支表、独立LCG、独立世界状态，以原javap offset标记事件。

原0..49先消费两次nextInt16、查biome、blockGen置0。51..190：16×16列，读water66；非固体65写water0/flags2；y60..64逐格非固体写Mud3/flags2。失败返回值不改变循环或blockGen；固体/无水跳过对应写入。14块与两个小谓词的逐跳转条件直接对应原指令，无额外隐藏生成helper。最后其他开关关闭后退出，原RNG顺序保持。

`independent-mud-diff.json`有14个完整逐事件/最终状态对照：3seed×4环境、配置关闭及全部局部布尔布局；不是只比1536个计数。all-layouts一组在256列中枚举水66的1位、固体65和60..64的6位共128种局部布尔布局，再用第8位分成功/拒绝写入。原片段不跨列读取，所有写返回值立即pop且不分支；因此这覆盖了每列局部判定域，结构对应而非只挑相似地形。正常mud写1536格；mixed、empty、deny各自按合同改变，deny的写调用与真正应用状态分开。这个**SEMANTICALLY_CLOSED有合同限定**；它不证明任意Forge补丁、副作用/异步/世界载入与现代API等价。

## B694证明

精确指令在b694-control-instructions.json。601..606令Y=70+dHeight，619..620计数0；625..632仅当Y>60+dHeight循环；684计数最多+1；697 Y-1；700回625。689..691判断count<=10，否则落入694。因此最多10次增量，count>10不可能。dHeight在此前没有变动；后续Moor赋值不回跳入该段。callee不能写调用者局部变量，异常也不会增加迭代。prove_b694.py校验这些控制指令并保留证明，非模型伪造覆盖。

## 尚未闭环的helper边界

运行在mock API上而非World真实引擎；MireO/OD/LiquidMire/Morass/Water未有各自完整独立oracle。Morass原`generateMorass(...FI)V@801`执行对BlockMorass的cast/PlantingThis时，MFQM mock字段仍是普通Block，因此ClassCastException；这是**模型类型不完整，不是原版bug**。两个失败用例已记录前缀写入、World RNG与错误，不能截去错误计为成功。下一步需类型正确的原生态回调环境/替代独立oracle；不能用跳过PlantingThis的假成功关闭它。
