# 原机制全量目录与后续归属

口径：以任务001归档的161类、1955个声明方法、463个文件为封闭输入集合；本次重读原件并校验hash。**目录覆盖整个集合，不声称每个方法的每条路径都已语义验证。** 旧实例实测为0，配置/随机/兼容分支的运行结果仍有证据缺口。状态定义及51个独立计数单元见[audit-index.csv](audit-index.csv)，OBS反馈不是额外计数项。

## 清单覆盖

| 输入类别 | 数量 | 定位与处理 |
| --- | --- | --- |
| main基础/事件/网络/生成等 | 26类 | [逐类目录](CLASS_COVERAGE.md)、C18–C38/G03/G07–G12 |
| blocks（含ItemBlock实现） | 39类 | 三核心深入核查，其余归G01/G06；不能以只有三种已注册推断旧版只有三种 |
| liquids（方块和Fluid类） | 25类 | G02；旧核心Quicksand/Mud/Soft本身不是这些Fluid类 |
| items | 30类 | G02/G03/G04；还有MFQM中直接构造的普通Item/ItemFood，不只这30类 |
| entity | 16类 | G03/G05/C33；含救援实体、气泡、投射物，不是16个自然生物 |
| client | 18类 | C23/C24/C31/C32/C33/G12；不是仅纹理文件 |
| Tileentity | 7类 | G06；注册调用与类存在分别记录，不假设全部有独立注册字符串 |
| 非class文件 | 302 | [逐资源目录](evidence/resource-coverage.csv)：247PNG、48mcmeta、2语言、2OGG、sounds.json及其余元数据；仅列路径/hash，不复制内容 |
| 静态注册调用 | 49个Block、43个显式Item、16个mod实体、13个Fluid | [注册归属附录](REGISTRATION_COVERAGE.md)，有条件调用不等于实际加载成功；ItemBlock与循环配方不重复计入43项 |

两个完整附录与原[classes.csv](../../../research/task-001/evidence/classes.csv)/[methods.csv](../../../research/task-001/evidence/methods.csv)/[archive_entries.csv](../../../research/task-001/evidence/archive_entries.csv)逐项相连，没有把自然生成、其他材料、装备、救援或特殊实体排除在未来计划之外。

## 机制类别、原证据与移植归属

| 类别 / 审计单元 | 旧类及方法 / 资源证据 | 当前状态与后续归属 | 置信度与边界 |
| --- | --- | --- | --- |
| 注册、方块物品与变体 C01/G12 | MFQM.preInit/Init/postInit；[注册调用](../../../research/task-001/evidence/registration_calls.txt)；ItemMud/ItemMeta/ItemMetaColor | 三核心与dev块已注册；全量旧变体/多语言部分实现；003.5-B/C及未来 | O-BC高：调用存在；有效registry dump未取得 |
| 核心碰撞、XZ/Y、吸力、转向 C02–C09 | 三类func_149670_a/func_149668_a；MFQM.suctionWorldCheck/antiHoldJumpScript | 当前近似，不是原版净曲线；003.5-B | O-BC分支高，净轨迹/旧坐标含义中，旧实机未测 |
| 堆叠/选中/放置 C10/C11 | Soft.func_149719_a；Block默认射线，三类是否覆盖选择函数见methods.csv | 同类下层填满缺失；内部命中待复现；003.5-B | 同类填满分支高；跨材质没有同等规则证据 |
| 重力/液体邻接/更新 C12/C15 | QS.func_149674_a/func_149726_b/func_149695_a；Soft同名方法；MFQM.LiqFixer | QS/Soft随机条件移块与岩浆转换未移植；003.5-B；Mud无自有同名下降分支 | 高：直接setBlock+remove；不等于FallingBlock实体 |
| 采集、掉落、挖掘 C13/C14 | QS/Soft.func_149636_a丝触与沙子；Mud.func_149650_a/quantityDropped/MudBallID；func_149737_a | 统一self掉落和标准挖掘只部分；003.5-B | O-BC高，丝触/配置条件须旧实机核对 |
| 非Living与船 C16/BOAT | 三碰撞入口非Living的func_70110_aj；无显式EntityBoat常量池引用 | 非Living web未恢复；Boat不进当前求解器；B单独决策，非“已证旧版船漂浮” | 通用web分支高，旧船净行为待证 |
| 装备与负重 C18 | MFQM.antiHoldJumpScript/jumpKey；ItemWadingBoots/PreWadingBoots/ItemLifeJacket/ItemGasMask | 裸装近似；已有依赖未移植，未来装备包；B只定义接口和回归，不顺手加装备 | O-BC分支高，重量和装备平衡待测 |
| 特殊实体/兼容免疫 C19/G05/G08 | 三核心中的EntitySandBlob/EntityMuddyBlob和TBL/ABC/AOA/WLD/EUD；[配置](../../../research/task-001/evidence/config_and_compatibility.txt) | 当前统一Living策略与通用免疫；未来生物/兼容包 | 高：判断存在；现代mod生态匹配未做 |
| 聚合/有限值/黏滞 C20/C21 | PotionStuck、CustomPotionEvent.onLivingUpdateEvent；旧每块碰撞写入；新SinkEngine/MATH | 新聚合、finite、自有modifier已有证据；不复刻旧负数幂NaN、Watcher危险语义 | 静态/历史测试高，不能等同所有mod兼容 |
| 氧气/窒息/原生UI C22/C23 | AirEvent引用EntityRope数组，三核心索引4/17/29均参与；MFQM.isDrowning、CustomRenderOverlayEvent.renderAirGUI；独立Watcher | 最小链部分、文本HUD；C原生风格呈现，B先明确水/气息配置合同；不混用渲染数组 | 高：300/-1/+5/16tick及实际数组owner；UI实机未验收 |
| 覆盖与洗净 C24/C25 | CustomVarPlayer.get/set/save/load，MuddyEvent.onLivingUpdateEvent；MudModelRenderer/CustomRenderPlayerEvent；textures/entity/mudOverlays | 当前仅残留type/ticks，无level/洗净/渲染；003.5-C | O-BC高，原死亡位污染不复制 |
| 生死/存档/同步 C26/C27 | 原Watcher/ExtendedProperties；旧Rope/Hook/Rescue消息；当前Capability/Snapshot/lifecycle | 核心新生命周期有历史通过，旧救援协议不是生理同步协议；B回归+004救援网络另做 | 高：字段/事件；旧重生完整保证不存在 |
| 预测/速度/落地 C28–C30/C36/C37 | 旧web/onGround/fallDistance多写点；新END tick/netY/teleport预算；Vanilla travel/move | 疑似入沙问题与间歇抽搐/声音待实测；003.5-B最先 | N-SRC路径高，具体反馈根因H，不冒称修复 |
| FOV/遮挡 C31/C32 | CustomPotionEvent.onFOVUpdateEvent；CustomRenderOverlayEvent.RenderOverlay/renderInsideOfBlockR | 两套独立视觉逻辑均未移植；003.5-C局部补偿/材质overlay | O-BC高，不应全局禁FOV/强制切第一人称 |
| 气泡/声音 C33/C34 | EntityBubble/RenderBubble；三块碰撞与QS/Soft.func_149734_b；MFQM.spawn*Bubble；sounds.json只两蜂声 | 全部触发逻辑未实现；003.5-C | 高：调用/条件；Mud不能凭QS环境气泡代码推断空池也必冒泡 |
| 原图/动画 C35/G12 | 162块PNG、54物品、25实体、5盔甲、1Logo；48mcmeta；2语言 | 公开占位+私有3静态，动画未验；C/未来资源包独立授权 | 资源hash高，不是渲染成功证据 |
| 其他块 G01 | BlockBog/Sand/Mire/Moor/Morass/Moss/Tar/Slime/Mucus/SoftSnow/Clay/Wax/Peat/Wool/Meat等，详见完整类/注册附录 | 未实现；未来材料批次，不能默许塞入004救援或B | O-BC声明/注册高，具体曲线只按单类取证，不能套三材料 |
| 流体/桶 G02 | 13Fluid，BlockFluidClassic派生类，Item*Bucket，CustomBucketEvent/CustomMaterial* | 未实现；未来流体包；不为修船把核心三块变水 | 类型/注册高，流动/置换需独立运行矩阵 |
| 救援 G03 | EntityRope/Hook/Rescue/LongStick；三Message及Handler；HandEvent；ItemCable/LongStick/GrapplingHook | 未实现；004，按UUID/权限/有限值/维度/断线设计 | O-BC高，不复制全局64槽、String引用比较、直接任意float |
| 物品食品装备经济 G04 | MFQM的ItemFood构造、ItemCranberry/Potion/SPotion/Fertilizer/WaxPiece等；CustomFuelHandler；recipe_calls | 未实现；未来装备/内容/配方任务 | 注册调用高，43显式Item不等于43种配方 |
| 生物/投射物 G05 | 四Blob/Slime、Bee；Tentacles/MudTentacles/SlimeHole/TarTreads；LiqBall/SPotion | 未实现；未来实体包，气泡仅视觉部分可归C | O-BC高，追踪实体与自然刷怪分开 |
| 植物/陷阱/BE G06 | Blossom/BlossomSlab/Larvae/Lure/Meat、SandstoneTrap；TileEntity*及renderer | 未实现；未来陷阱/植物包 | 类型/方法高，未将渲染器误计为可放置内容 |
| 世界生成 G07/G11 | CustomWorldGen.generate*，CustomWorldGenLakes，GenerateDesertTombs/GenerateMucusBlossom，CustomGenerationEvent | 未实现；005；五个未结构化方法逐条字节码+旧固定种子补证 | 注册入口高，精确拓扑规则不明，不能声明100%还原 |
| 第三方兼容 G08 | BoP/TF/TBL/ABC/WLD/AOA/EUD探测、反射/tag前身、外部图标与配方分支 | 未实现；未来兼容包，不引入旧硬依赖 | 分支存在高，现代替代API待确认 |
| 旧反射与危险状态 G09/G10 | CustomRegister具备替换分支但未发现调用；CustomVarPlayer负type/Watcher25；64槽网络 | 不适用（有证据）：保留研究，不照搬；有意现代化记录 | O-BC高，非“必须恢复的缺失功能” |

## 有界的遗漏口径

计数以51个机制/验收单元为准，不以类、函数、材质交叉表格重复累计。登记了全部任务001类别，但尚缺旧实机与五处生成语义补证，不能将“归属表没有空行”解释为全量机制已验证。当前未移植的其他材料/装备/特殊生物只是**后续依赖项**；不属于本轮可写代码的范围。
