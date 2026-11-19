# 首批纵深分析：证据、现代差异与退出门槛

状态 **PARTIAL**，不是六个模块全部闭合。以下是本轮逐段核对的具体链条；历史 oracle 结果只标 RESEARCH_ONLY，本轮未启动原版游戏。类的完整 descriptor/member_id 从 ORIGINAL_METHODS.csv 按 owner/name 查询；字节码文件在各类档案，按 METHOD+descriptor 和十进制 offset 定位。反编译文件中 `n:` 为 CFR 行号，**DECOMPILED (not original source)**。本报告与所有类档案双向链接，不用本报告代替成员目录。

## 1. 注册、独立物品、名称与旧变体

来源：research/task-001/evidence/MFQM.analysis.txt:602–605、954–1013、1380–1480、1848–1866；CustomRegister.analysis.txt:35 起。MFQM.preInit 初始化方块/流体字段，registerBlock 会指定 ItemMud/ItemMeta 等 ItemBlock；LanguageRegistry.addName 另给 ItemStack damage 命名。典型 Mud 明列0..3同名；SoftSnow0="Soft Snow"、1="Soft Ash"；Morass 循环0..<8，BrownClay数组8项中后4项为 Mineral Clay。不能将同一个 block registry ID 的多个可见 ItemStack 当成一个“已复原物品”。独立 Emptycomb/HoneycombItem/WadingBoots 等通过 registerItem 注册，与 BlockItem 不同。

CustomRegister 操作反射/原全局注册容器，不只是 GameRegistry 的别名。因此原表只自动提取带点的调用表达式，包含条件路径和动态参数，**不是完整运行时注册表**。ORIGINAL_REGISTRY 保留每次调用、明确 metadata常量和原表达式；循环变量、条件可见性、getSubItems/getSubBlocks、反射与注册替换均仍需闭合。Entity注册与配置条件、TileEntity、网络0/1/2、WorldGenerator也进入表，不用49方块代替全内容。

现代对照：registry/ModBlocks.java、ModItems.java、ModTabs.java、content/LegacyCatalog.java。目录循环注册 block 与对应 BlockItem；LegacyFluids 为每族另注册 bucket/source/flow/type。现有独立原版工具/装备并未因有63 Item源解析条目就恢复。现代153个源解析注册对象包含dev_test_block与流动Fluid，不能与原版51个调用候选做数量减法。英文名需逐原ItemStack/damage比对；中文名不由英文直译当作原版名称。

行为规范：构造→字段赋值→注册→名称/配方/创造栏，各自可能受可选模组和配置门控制；稳定ID必须保存大小写旧名，迁移到mfqm的小写映射另建行。测试计划：隔离旧Forge可选依赖场景枚举registry及可见栈，再与新Forge registry运行时dump和creative tab逐项对照；本轮动态枚举 NOT_RUN。下一步R1-REG，保留全部现有ID，不贸然补注册。

## 2. 三种核心接触与Y运动

证据：BlockQuicksand.analysis.txt:88–140、288–332；BlockMud:199–247、483–545；BlockSoftQuicksand:104起、265–333。共同入口 func_149670_a 的 descriptor 为 `(Lnet/minecraft/world/World;IIILnet/minecraft/entity/Entity;)V`。这是真实逐实体碰撞路径，不是一个每tick共同的 SinkMath 曲线。

QS首先读posY/prevPosY/motionY。玩家k=posY-y-1，非玩家k=posY-y+.5；km先夹零。LivingBase 路径先checkEntityUnder，再玩家checkPlayerMuddy，然后识别动作。WLD怪物有排除；非Living/特殊实体分支不能直接套玩家路径。Soft相同坐标框架还有-.2偏移。旧posY和现代脚部/AABB/eye坐标不能无测量直接等同。

QS基础mr为 min(5+floor(max(0,100*(1.5-km))),145)；Soft是12.5倍差值的1.75次幂，Mud是4倍差值的1.5次幂；深区还会强制145/175/145。Soft/Mud负底数的NaN→int行为见历史报告，不能先夹底数改变语义。Mud先读metadata，必要时getMudDepth取max，再getMudSafe可能归零；装备、特殊生物、外部兼容分支会提前return。

顺序证据与完整限制见 research/original-mechanics-phase1/reports/03_stuck_and_tick_order.md：QS先清XZ，Soft乘.71，Mud无靴与metadata0提前返回；浮力补偿不是净位移。原World RNG中的特效调用影响后续随机消费，不能只拷贝最终概率。

现代：physics/MaterialProfile.java 自述 bounded approximations，统一surface/retention/buoyancy与三类枚举；SinkEngine、MotionRuntime/Math 与 CoreSinkingBlock 的随机搬块是现代有限适配。integration/OriginalContactBridge 仅开启受控非玩家QS域。明确差异：目前profile无法表达上述全部条件；不是可立即删除的死代码。测试：已有 MotionMath/SinkMath/MudGeometry 与43 GameTests本轮通过，只证明现有稳定性。旧碰撞native向量/净Y曲线/玩家坐标实测本轮NOT_RUN。R2按单材料成对轨迹替换，不调整B1防抖以伪装原版。

## 3. Stuck setter → 属性更新 → 现代租约

MFQM.analysis.txt:2641–2644：`PotionStuck.get(elb).setStuckLevel(level)`，直接写最后一次level，非全世界max聚合。CustomPotionEvent和PotionStuck具体签名、字段写入见各自档案/CALL_GRAPH。历史报告03明确：LivingUpdate先删固定UUID 73A49882-85A3-4896-AD2D-8C591E24AA62；level>0计算p=level-5、collision决定c；speed=max(1/(1+p*(1+c/2)/50)^2,.02)，p>=250特殊；operation2非保存modifier，level→0，未续期下一次→-1。旧 jumpMovementFactor另有8次幂限制，本轮未证明现代跳跃等价。

现代 legacy/StuckLease.java contact直接赋值、update先删UUID、添加瞬态MULTIPLY_TOTAL，保留lease转换；integration/StuckAdapter.java update每实体每gameTime至多一次，先SinkEngine.removeModifier以交接所有权，离开/死亡/禁用清理。OriginalContactBridge限定生产者，不把所有entityInside都传入。现代服务端权威与旧玩家客户端写入存在工程差异，需标MODERN_BRIDGE，不假装原版。

风险：StuckAdapter.managed 与 SinkEngine/ClientMotionPrediction所有权条件决定是否双重减速；仅看函数名相似不能MERGE_DUPLICATE。必须测试同tick双接触顺序、无接触续租、死亡/跨维、卸载、旁观/乘客、禁用后属性不存在，再删旧路径。现有PureComponentsTest及GameTests通过，覆盖域之外仍未知。保持B1 Y保护不变；R0-E不执行。

## 4. 纹理、metadata与紫黑缺失案例

BlockSoftQuicksand.analysis.txt:350–351返回 icon[clamp(meta,0,2)]；现代FILLED是几何状态，不是旧meta1/2。Mud:618起含可选模组维度图标，不只一个mud.png。Phase9 importer用原字节生成小写现代路径，流体still/flow绑定由client/OriginalTextureBindings读取私有marker，公开构建仍vanilla占位。copied PNG/JSON存在不等于世界/物品正确。

案例U-01（OPEN）：用户Windows报告私有Phase9仍紫黑。本轮未得到出错物品ID、截图/位置、实际JAR hash和日志，因此**不能断定是大小写、漏资源还是模型错误**。排查链固定为 registry→blockstate模型→item模型/parent→texture→atlas/reload→资源包覆盖→最终JAR条目。RESOURCE_USAGE保留旧绑定证据，未继承旧视觉PASS。U-02名称、U-03数量分别建案，不能用核心三块历史截图关闭它们。新增RESOURCE_REFERENCE_GRAPH对所有JSON引用保留外部vanilla/需私有导入/缺失状态；未引用候选也不判死资源。

已知源差异：流体bucket仍water_bucket；cube库存几何不证明原版自定义renderer；multiface/动态纹理不能扁平化为all。R1-ASSET先复现一个具体缺图ID，再补模型与打包验收；正式启动器与Windows本轮NOT_RUN。

## 5. 污渍状态、视觉与清洗

来源：BlockQuicksand.checkPlayerMuddy:540起、MFQM.<clinit>:2650起的原遮罩数组；research/original-phase3/08_COATING_CAMERA_TEXTURE_SPEC.md 与原MuddyEvent/CustomRenderPlayerEvent/CustomVarPlayer字节码。历史证据为33类型/20张64×32mask，QS type4、Soft17、Mud实际Mire type9，触发参数/UV阈值不同，alpha=min(1,time/1000)。湿润清洗 time减5+time/100，%16条件降level，干燥%1024/%2与残留阈值分别控制；并非统一计时最终清空。旧64×32 UV不能直接冒充现代Alex/64×64/盔甲覆盖正确。

现代client/CoatingLayer.java实际用vanilla sand/red_sand/mud贴图，对整个玩家模型renderToBuffer，alpha=min(.65,residueTicks/500)，另套盔甲模型；state/SinkState.java只residueType/residueTicks的持久化框架，不是33类level/time状态机。此为**已定位静态MISMATCH**，而不是用户感觉不对。CoatingHands/SinkHud与网络包的视觉权威还需逐链审查。

R3先引入兼容旧NBT键的附加污渍状态，再成对验证水/雨/退出/死亡/维度/保存和客户端同步，后改渲染层，不直接删现存residue存档字段。原版动态污渍、现代视觉/清洗实测本轮NOT_RUN；当前不宣布资源导入已恢复污渍。

## 6. 自定义世界生成与现代边界

原入口 MFQM.analysis.txt:1480注册CustomWorldGen优先级9999999；CustomWorldGen.generate/CustomGenerationEvent与湖泊、墓室辅助类有分派。research/original-phase5/02_SURFACE_BRANCH_CLOSURE.md定位 generateSurface descriptor与offset0..14261：SSand先于QS、共享blockGen；dry helper写SandBlock而非SoftQuicksand；extent不是数学半径。概率门、噪声、拒绝写入及反复写入flags必须保序，不能只比最终去重体素。

历史native/栈机/事务oracle只在报告列明沙漠、配置、种子和拒写域闭合；完整25个surface分支报告仍0/25全域闭合。现代legacy/DryQuicksandCore和测试world适配是纯核心/受控集成，不是生产PlacedFeature已注册；墓室、WLD可选依赖/群系生态尚无完整现代实现。不可为“内容数量完整”默认开启自然生成。

R4先复用cases.json有限向量并验证RNG/读写事件；按真实现代注册入口、seed/邻块更新/跨区块拒绝路径逐项集成，保留存档与配置冻结。原1.7.10游戏及现代自然生成本轮NOT_RUN。

## 结论与验证层次

上述是有定位、有差异、有测试计划的第一批链条，**每个模块仍PARTIAL**。成员签名/边独立提取为BYTECODE_CONFIRMED；CFR条件为DECOMPILED_INTERPRETATION；历史oracle为RESEARCH_ONLY；本轮现有回归为现代测试PASS；没有新DYNAMIC_ORACLE_CONFIRMED或完整BEHAVIOR_PARITY。覆盖工具保守将完整深度类数记0，而不是按本报告出现类名提高完成率。
