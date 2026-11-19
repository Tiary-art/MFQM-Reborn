# 状态、原生气泡栏、FOV、遮挡、气泡与声音

所有旧机制结论来自字节码/分析或归档资源，未做1.7.10实机。当前事实直接核对源码，任务003旧日志只作HIST。本轮未改变状态、网络协议、客户端事件、贴图或声音文件。

## 1. 旧空气槽与“原版气泡栏”不是同一个概念

[AirEvent.onLivingUpdateEvent L122](../../../research/task-001/evidence/AirEvent.analysis.txt#L122)先分玩家QSAir/生物QSMAir；server读取独立Watcher气息，覆盖−1、脱离最多+5至300。[MFQM.isDrowning L2598](../../../research/task-001/evidence/MFQM.analysis.txt#L2598)根据air负值与16tick时钟返回伤害条件；关闭储气开关不是关闭所有窒息伤害。

客户端在自定义气息低于原生air时把原生air压低（AIR L128）；[CustomRenderOverlayEvent.renderAirGUI L50](../../../research/task-001/evidence/CustomRenderOverlayEvent.analysis.txt#L50)也做min并可按QSCAir取消默认AIR事件，用Vanilla图标绘制气泡。这证明“独立生理储气+原生样式显示联动”，不能据此说旧版仅依赖原生water air，也不能在新服务端对两个储气槽同时扣减。

**同名数组必须按实际调用者展开：** AIR跳过索引6/7/13/15/21，但它引用的是[EntityRope静态数组L85](../../../research/task-001/evidence/EntityRope.analysis.txt#L85)：QS=4、Soft=17、Mud=29，三者均不在排除集合；15实际是MeatHole。渲染器的另一张数组才是Soft=15/Mud=26。已按[AirEvent字节码L286](../../../research/task-001/evidence/MoreFunQuicksandMod__main__AirEvent.bytecode.txt#L286)的实际字段owner及两张数组的初始化指令核对，见[evidence/legacy-air-map.json](evidence/legacy-air-map.json)。本轮草稿曾混用两数组而推测Soft不扣气，已更正；不把错误草稿转成用户需要批准的功能差异。新[SinkEngine L95](../../src/main/java/art/tiary/mfqm/physics/SinkEngine.java#L95)对三核心扣气有旧分支支持，但眼判定/坐标/非默认开关/水交互仍不等于完整复刻。

### 当前与拟议C-AIRUI

- 当前[SinkState.air](../../src/main/java/art/tiary/mfqm/state/SinkState.java)独立；[SinkHud](../../src/main/java/art/tiary/mfqm/client/SinkHud.java#L18)是文本，ClientSinkState不写Vanilla air。003默认耗氧/伤害有历史自动与实机证据，但原生气泡栏**未实现**。
- 1.20.1 Gui.renderPlayerHealth按`eye in water 或 air<max`判断原生气泡显示；ForgeGui/VanillaGuiOverlay的AIR_LEVEL布局也必须核对。缓存方法hash见[vanilla-methods](evidence/vanilla-methods.json)。不能只在server把air设低就默认兼容所有HUD。
- 建议保留server独立储气与单伤害时钟，仅在客户端AIR_LEVEL层用Vanilla资源表达有效气息。水/沙同时覆盖的显示预算可提案`min(vanillaAir, customAir)`并使用各自max归一化；**这是待批准的显示决策**，不是未经验证把server两个系统合并。
- 不永久覆盖原生server air，不全局取消其他HUD；只在本模组确实呈现时处理重复栏，离池/断线/死亡/维度后恢复。测试水呼吸、气息附魔、最大气息修改、第三方HUD、两系统伤害时钟，确保无双伤害或空气恢复跳变。

## 2. 仅消除MFQM减速带来的FOV缩放

旧[CustomPotionEvent.onFOVUpdateEvent L158](../../../research/task-001/evidence/CustomPotionEvent.analysis.txt#L158)在stuck时使用缓存SIFOV，再处理弓拉伸。新[SinkEngine.setModifier L152](../../src/main/java/art/tiary/mfqm/physics/SinkEngine.java#L152)添加MULTIPLY_TOTAL的自有减速modifier，当前没有FOV事件处理。

1.20.1 AbstractClientPlayer.getFieldOfViewModifier使用约`(movementSpeed / walkingSpeed + 1) / 2`因子，并有飞行、弓、望远镜和Forge hook。Forge47.2.0有`ComputeFovModifierEvent`，其结果还涉及用户FOV效果强度。N-SRC证明存在导致FOV变化的路径；实际变化幅度仍须用户环境测量。

### C-FOV建议（待实现）

目标：在本地玩家实际被MFQM自身modifier影响且有有效材料状态时，重建**仅移除本模组modifier的反事实移动FOV分量**，保留疾跑、其他属性、药水、弓、望远镜、飞行、用户选项和其他监听器结果。

若自有乘数m=1+amount且范围未夹取，属性反事实可用A/m；但实际RangedAttribute夹取/其他modifier组合可能使简单相除不精确，完整实现应在只读计算副本上去除该UUID并重算，再按Vanilla FOV的正确阶段补偿。属性只占`(A/w+1)/2`，**不能直接把整个FOV除m**；FOV效果强度插值也不能忽略。w为0、非有限值、属性包与快照先后到达时回退安全值。

禁止：全局FOV effects=0、固定每帧FOV=1、冻结进入前全部FOV、渲染时临时移除服务器/客户端真实modifier。旧缓存冻结逻辑也不能不加分析照搬，因为它可能吞掉期间其他效果。建议纯函数测试叠加modifier/夹取/选项强度，再人工验收进出池、拉弓/望远镜、速度/缓慢、骑乘及其他FOV插件。

## 3. 眼部遮挡与摄像机

旧[RenderOverlay L93](../../../research/task-001/evidence/CustomRenderOverlayEvent.analysis.txt#L93)检查S变体、取方块图标，再绘制暗色遮挡；配置可强制第一人称。原生体感遮挡与伤害眼部采样是两套入口，不能混为相同阈值。

现[SinkingBlock L17](../../src/main/java/art/tiary/mfqm/physics/SinkingBlock.java#L17)禁用suffocating/viewBlocking，且没有专门overlay。因此OBS-03可从当前路径解释：既没用默认视野遮挡，也没有移植旧替代。1.20.1 ScreenEffectRenderer.getOverlayBlock也检查viewBlocking，不能以“块有贴图”期望自动遮挡。

C-VISION建议：共享但分层的材料表面/摄像机采样、采用Minecraft占位材质atlas、明确第一/第三人称、睡眠/旁观/无敌及摄像机在外身体在内的规则；只绘制，不让渲染决定伤害。不得强制改用户视角或开放旧素材。SS层叠几何先修，防止眼面与模型脱节。

## 4. 污泥状态、覆盖、洗净与生命周期

原[MFQM.getMuddyLevel](../../../research/task-001/evidence/MFQM.analysis.txt#L2035)按眼高分0..10；三类checkPlayerMuddy比较现有level/time与新覆盖，记录类型/不透明计时。CustomVarPlayer把type/level/time打包Watcher并存NBT；[MuddyEvent L42](../../../research/task-001/evidence/MuddyEvent.analysis.txt#L42)湿润时减`5+time/100`、每16tick减高级level，干燥时有1024/2tick与类型残留规则，排除两种LiquidMire。

[CustomRenderPlayerEvent](../../../research/task-001/evidence/CustomRenderPlayerEvent.analysis.txt#L39)/[MudModelRenderer](../../../research/task-001/evidence/MudModelRenderer.analysis.txt)覆盖模型/第一人称手，资源有mudOverlays。原死亡setType(-1)导致位污染是任务001离线算术发现，不当作必须兼容行为。

当前只有residueType/ticks：active每tick+5至10000、离池−1；NBT只存这两项，Snapshot也**不包含残留字段**。这不是旧level/time系统，没有清水/雨洗、类型残留或外观渲染；“Capability存在/存档通过”不等于“弄脏玩家已实现”。

C-COVER须先确定新字段schema、范围/迁移、湿润源、类型优先级与帧率无关时钟；server更新、跟踪首次/增量同步，再加玩家RenderLayer/手层，不替换全局模型实例。死亡/重生/维度/卸载/跟踪退出单独测试，观察者与本地手持/盔甲不污染其他玩家。旧资料仍是静态；覆盖参数/私有素材授权与公共占位策略需批准。

## 5. 环境气泡、身体气泡与音效不能混为一项

| 原路径 | 已证条件/差异 | 当前与后续 |
| --- | --- | --- |
| QS.func_149734_b | 顶部空气，概率环境气泡；SOFT有相应显示tick | 没有display/animateTick实现；C-FX按材料规划 |
| Mud.func_149670_a L380–411 | 快落/走/跳等动作概率body bubble，深Mud32tick/随机分支 | 未实现；**没有找到Mud自己的同名环境显示tick覆盖**，不能承诺无人空池一定冒泡 |
| MFQM.spawnQSBubble L2446 | client侧/QSBubble；可实体泡或blockcrack fallback；还播放liquid.lavapop | 需要现代粒子/受限事件路径与sound映射；不要每格每tick无限生成 |
| EntityBubble/RenderBubble | 携材质/meta/尺寸/时长等，属于非生物显示实体 | 可设计现代Particle替代，但注明实现差异，不默认加入完整旧实体系统 |
| 三块动作声 | game.player.swim、mob.slime.attack；Mud还有mob.silverfish.step、liquid.water等 | 当前只有复制Block soundtype，缺触发；C-AUDIO按语义映射现代原生SoundEvent，旧键不能原样当1.20.1 ID |
| 原JAR自有声音 | sounds.json只定义bee.hurt/say，2OGG都是蜂 | “没有旧OGG”不能解释全部流沙声音；旧蜂声属于未来生物包且未授权素材不得上传 |

历史003客户端OpenAL启动失败（[日志16](../../logs/task-003/16-final-client.log)），因此旧实机证据不能验收声音；用户当前听到落地声也不能反证旧swim触发已存在。新人工音频验收必须使用可播放设备并记录声音事件ID/数量/位置，随机效果采用样本窗口与触发统计，不以一次无泡无声断定概率错误。

## 6. 资源/动画边界与新旧状态迁移

原247PNG、48mcmeta、2OGG本轮hash复核不变，未复制到新目录。003私有工具只实测三静态16×16；SS的meta0/1/2纹理、多帧加载、异常32×304没有通过证据。C只可用清楚标记的Minecraft占位/授权私有字节不变测试包，不生成AI纹理，不把metadata复制成功当动画播放成功。

现death/server clear与respawn sync有历史验证；死亡画面暂留上一条HUD快照是003已记录的显示缺项，不代表服务器stuck泄漏。C应专测死屏/断线/新UUID/换维度显示清理，B仍保留服务器生命周期保障。将来加入level/time或Boat状态需要明确schema/协议版本和未知字段回退，本轮不提前修改协议。
