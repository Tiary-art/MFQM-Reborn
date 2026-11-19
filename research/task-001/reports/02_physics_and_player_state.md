# 02 — 陷落物理与玩家状态

本报告为 2026-11-17 静态分析。原始 JAR 未执行，未启动 Minecraft，未验证运行时表现。高置信度表示归档/指令直接支持；中置信度表示反编译控制流与旧版 SRG 名称解释，仍需旧版实机复核；设计建议不代表旧版事实。所有方法描述符与十进制字节码偏移见 `evidence/*bytecode.txt`；`*.analysis.txt` 是 CFR 0.152 反编译的带行号分析文本，不是原始源码，也不是新版实现。

## 解读约定

SRG 字段：`field_70159_w/70181_x/70179_y` 为 motionX/Y/Z，`field_70163_u/70167_r` 为当前/上次 Y，`field_70122_E` 为 onGround，`field_70143_R` 为 fallDistance，`field_72995_K` 为 isRemote。`func_149670_a` 是实体方块碰撞入口；`func_149668_a` 返回碰撞 AABB；`func_70110_aj` 是旧版 setInWeb。这些语义使用旧版 SRG 常用对应关系解释，数值和分支可从指令直接核对，运行时坐标差异仍需旧环境验证。

**kof1 不是可直接跨版本复用的“浸没深度”**：Quicksand/Mud 玩家分支 k = entityY − blockY − 1；非玩家 k = entityY − blockY + 0.5；SoftQuicksand 再减 0.2。km = max(k,0)。因此 k 越小通常越深，但旧版玩家坐标、眼高与新版不同。真正窒息检查另外使用眼高和表面。正的 motionY 增量是浮力/抵消重力，不是正的“下沉速度”；净移动还受 Minecraft 重力、web、碰撞、移动更新先后影响。

## 核心证据表

| 类/方法 | 字节码/反编译证据（具体方法见 evidence） | 行为结论 | 置信度 |
| --- | --- | --- | --- |
| BlockQuicksand.func_149670_a | motionX=0, motionZ=0；motionY>-0.1 时置0，否则 /=2；mr=min(5+floor(max(0,100*(1.5-km))),145) | 强横向阻力，快速下落减半；黏滞级别随 k 变小增强 | 高（指令），净轨迹待测 |
| BlockQuicksand.func_149668_a | aconst_null; areturn | 无实体碰撞 AABB，不代表无碰撞回调 | 高 |
| BlockQuicksand.func_149670_a | jump: ΔY>0.2；moving: abs(ΔX/Z)>0.0015 或转向；movKofDiv=1+distance/2 | 运动/转向/跳跃参与浮力与挣扎 | 高 |
| BlockSoftQuicksand.func_149670_a | motionX/Z *=0.71；移动阈值0.001；movKofDiv=1+distance*2；mr 上限175 | 先阻尼，深区另清零并向方块中心牵引 | 高 |
| BlockSoftQuicksand.func_149668_a | aconst_null; areturn | 无 AABB；渲染顶面0.85不能当实体支撑面 | 高 |
| BlockMud.getMudDepth/getMudSafe | 同层8邻居、±2/±3四方向；材料 liquid/solid 判定 | 深度等级受池形与上覆液体影响；安全边缘可降级 | 高 |
| BlockMud.func_149668_a | f=0.3；meta1 f=0.5；meta2 f=0.75；深层返回null，受上方方块条件约束 | 碰撞高度依分支为0.7/0.5/0.25或空 | 高 |
| BlockMud.func_149670_a | 无靴且 onGround 时 X/Z*=0.1；后续 X/Z*=0.71；Y快降 /=10 | 分层黏滞与靴子特判；两个阻尼可能同时发生 | 高 |
| 三类 checkEntityUnder + MFQM.isDrowning | 眼高包围测试；alive、!isRemote；max(maxHealth*0.1,2)*DmgMul | 服务端窒息伤害，频率受氧气开关/时钟控制 | 高 |
| MFQM.isTrulySink | 玩家返回 world.isRemote；非玩家 true | 部分玩家 stuck 处理发生在客户端，不能假设旧系统完全服务端权威 | 高 |
| MFQM.suctionWorldCheck | VelY=max(prevVel*10,0.25)；time % floor(max(10*VelY²,1)) ==0 且 nextInt(5)==0 | 吸力受入射速度与时钟随机条件控制；靴子可修改VelY | 高 |
| MFQM.antiHoldJumpScript/jumpKey | 本地玩家读取键位；末端 jumpKey=true 时 onGround=false；另有盔甲/库存/靴子分支 | 持续跳跃、装备与负重参与阻碍；不得简化成一个恒定系数 | 高（分支存在），精确平衡待测 |
| CustomVarPlayer.get*/set* | idiv256/iand255；idiv65536；iand255；按位or写Watcher | type/level/time打包在一个32位整数 | 高 |
| MuddyEvent.onLivingDeathEvent | setMuddyLevel(0) → setMuddyType(-1) → setMuddyTime(0) | 意图清理；实际有符号/位运算可能留下level=255，见下文 | 高 |
| PotionStuck.save/loadNBTData | 仅return；Level构造为-1、TarTreads为0 | 不保存这些短期状态到NBT，也未见该类自带同步 | 高 |
| CustomPotionEvent.onLivingUpdateEvent | 移除固定UUID旧Modifier；operation=2；setStuckLevel(0)，下次0→-1 | 每tick续期式短时减速，不是注册的自定义药水 | 高 |
| AirEvent.onLivingUpdateEvent | 服务端覆盖时-1，脱离时+min(5,300-gma)；客户端夹到原生air | 独立氧气槽，客户端HUD/原生air联动 | 高 |

逐方法原始指令文件以 `MoreFunQuicksandMod__main__blocks__类名.bytecode.txt` 命名。带行号分析文本同名 `类名.analysis.txt`。证据表保留旧字段名与常量，便于定位；不把 CFR 变量名当原作者命名。

## Quicksand 主流程伪代码

```text
保存旧Y、prevY、prevVelY；计算 k、km、上一帧k
若 LivingEntity:
  检查眼部覆盖和窒息；若Player则服务端更新污泥覆盖
  jump=(Y-prevY>0.2)；splash=(原motionY<-0.1)
  moving=(水平位移超过0.0015或转向)
  distance=hypot(ΔX,ΔZ); div=1+distance/2（moving时）
  mr=min(5+floor(max(0,100*(1.5-km))),145)
  motionX=motionZ=0
  motionY=0 if motionY>-0.1 else motionY/2
  处理音效/气泡、SandBlob或兼容生物例外（可能提前return）
  若上方无同类块，或上方两格均同类:
    上方两格均同类时只将k置0.001（km保持旧值）
    若jump且suctionWorldCheck: motionY-=0.05*(min(0.75,km)+1)
    若k>=1.2且非splash:
      a=0.07485 if time%4==0 else 0.075
      motionY+=a/max((div-1)*max(km-0.5,0.75)*1.6,1)
                  /max(km/1.25,1)^2
      onGround=false; fallDistance=0；附加概率web/着地
    否则:
      有上升位移且随机/吸力满足时再施加-0.035*10*(min(0.75,km)+1)
      k>=0.9: 类似浮力，tick周期2，施加mr级Stuck
      k<0.9: a2约1.01/1.05，按k>=0.5等条件选择
             0.0725或0.075的浮力增量；moving再除(div+0.075或0.025)
             web、Stuck、概率onGround；k<0.45可设145级Stuck
    若原生inWater且motionY>0: motionY/=4
  否则: setInWeb；深处分支施加Stuck
  antiHoldJumpScript(entity,k,true)
否则若k<1.45: setInWeb
```

这不是可直接使用的新版 tick 实现；声音、随机数调用顺序、EntitySandBlob 的再生/浮起和兼容免疫仍需按原指令保留测试样本。不能仅依伪代码声称所有实体拥有同样轨迹。

## SoftQuicksand 差异

- k 相对 Quicksand 减 0.2；`mr=min(5+floor(max(0,pow(12.5*(1.5-km),1.75))),175)`。注意负数底数做非整数次幂会产生 NaN；不能未经验证把它改写为先 clamp 底数的等价算法。
- X/Z 初始乘 0.71，Y 快降减半；movKofDiv=1+distance*2，转向另加 mr*0.002。
- k≥1.3 时不进入 k∈[1.2,1.3) 的浮力子分支；该子分支浮力常量0.0735、分母含17.5、km/1.475，横向再乘 clamp((k−1.25)*4,0,1)。
- k∈[0.9,1.2) 施加 Stuck；玩家按 time%floor((k+0.1)^5) 调节0.0715/0.0735与web，非玩家会纠正水平位置。
- k<0.9 时清零水平速度；距方块中心0.075≤r<0.5，添加 `(center−pos)/max(10,km*50)` 的中心吸引。k∈[0.5,0.9) 运动时浮力分母 div*4+0.075，k<0.5 时 div*16+0.025；深区 Stuck 可175。
- 空 AABB；图标 meta 0→SoftQuicksand1、1→SoftQuicksand0、2→SoftQuicksand2，其他 meta 夹在0..2。

证据：BlockSoftQuicksand.analysis.txt 的 func_149670_a、func_149691_a、func_149651_a，以及同类原指令。

## Mud：池形、安全性与靴子

```text
getMudDepth:
  上面一格材料为液体 =>3
  上面一格为this且上面两格材料为液体 =>3
  同层八邻居不全为this =>0
  八邻居全为this，但±2轴向四格不全为this =>1
  再满足±2四格，但±3轴向四格不全为this =>2
  以上全部满足 =>3；异常=>0
getMudSafe:
  若上述上覆液体条件满足 =>0
  否则四方向存在非this且材料非solid的邻居 =>1
  其余/异常=>0
有效mtd = metadata<3 ? max(metadata,depth) : metadata
若mtd>0且safe>0 => mtd=0
```

AABB 默认顶面0.7；mtd>0 且（上方不是本块或上方meta>2）时，mtd1顶面0.5、mtd2顶面0.25、其余返回null。因此 meta 不是唯一深度来源，紧邻空气的“安全”与窒息安全是不同条件。

mtd0 有浅层处理与非玩家浮起；更深分支用 mtdkof=2、mr上限145。无靴着地先0.1横向阻尼，后0.71；Y初始>−0.1置零，否则/10。k≥1.3 分支浮力约0.075、周期8修为0.07485，分母含 `(div/3−1)*max(km−0.5,0.75)*1.6*mtdkof*17.5`。真正的 WadingBoots 在特定浅度可用0.085/0.1浮力，k<1.3又取消 bootsIsFloat。其他分支另有 web、Stuck、非玩家位置回退、兼容维度毒性与生物免疫。

这说明不能把 Mud 简化为“换颜色的 Quicksand”。边缘、池宽、上覆液体、metadata、靴子、实体类型和维度都影响结果。具体分支以 BlockMud.analysis.txt/bytecode 为准。

## 窒息、伤害与污泥覆盖

`MFQM.isEntityInsideOfBlock` 用 `entityY+eyeHeight` 取样；BlockFluidClassic 部分情况加0.15，Moss有向上偏移；S变体眼部再减0.2，L同时检查脚部，M变体检查眼部取样之上一格。不能用单一“碰到方块就掉血”代替。

`AirEvent` 按玩家QSAir/其他生物QSMAir分别启用，DataWatcher初值300。服务端遍历 EntityRope.quicksandIDS，跳过索引6/7/13/15/21；22走M变体，其他走普通覆盖检查。覆盖时 gma>−1 则减1并return；脱离恢复最多5/tick至300。客户端只在自定义air小于原生air时下调原生air。索引定义逐项保存在 EntityRope.analysis.txt 静态初始化部分，不能把跳过索引误解释为全部免疫伤害。

`isDrowning`：对应氧气开关关闭直接true（所以不等于关闭窒息伤害）；开启时无敌玩家false；服务端 gma<0 且 time%16==0 时将air置0并true；客户端 gma<1 为true。三个核心块在眼部覆盖、存活、服务端条件成立时造成 `max(maxHealth*0.1,2)*DmgMul` 的 drown 伤害。实际血量降低还受原生hurt-resistance、事件、免疫等影响。未将每次伤害调用直接换算DPS。

覆盖 `getMuddyLevel` 以眼高减blockY取分段：<0.7→10，<1.04→9，<1.1→8，<1.21→7，<1.32→6，<1.53→5，<1.67→4，<1.98→3，<2.14→2，<2.4→1，否则0。覆盖块比较 `preLevel*(maxOpacity/1000)` 与 `oldLevel*(oldTime/1000)` 决定是否更新；type来自 quicksandIDS 索引，time 按incOpacity增加并夹至maxOpacity。

## 玩家状态、NBT、同步与清理

CustomVarPlayer 的 EXT_PROP_NAME=`PlayerMuddyControl`，保存到复合NBT下的整数 `MuddyLevel`。Watcher ID来自MFQM.MuddyLevel（默认25），初始化冲突生成CrashReport。名义打包：低8位type、中8位level、高位time。实际读取使用整除而非无符号移位：

```text
type = data & 255
level = (data / 256) & 255  // Java整数除法向0截断
time = data / 65536
setLevel(l): data=(data/65536*65536) | (l*256) | (data&255)
setTime(t): data=(data&65535) | (t*65536)
setType(t): data=(data/256*256) | t
```

各 setter 不验证范围，也未将type mask到8位。`setType(-1)` 会把整个data置−1。死亡回调依次 level=0,type=−1,time=0，最终 data=65535，读到 **type=255、level=255、time=0**；这是对已确认指令的离线整数演算，尚未在游戏中验证视觉后果。报告不能只写“死亡完全清零”。

MuddyEvent 只在 QSCover 时注册：constructing 注册属性；服务端更新污泥时间；湿润 `func_70026_G`（旧版isWet）且不在两种LiquidMire时，每tick减 `5+time/100`、夹0，每16tick且level>5减1；干燥时每1024tick且time<1000/level>5减level，每2tick time高于类型残留阈值时减1。type>=0在getter总返回0..255，不能把它当有效索引校验。`getLastMuddyType` 用 `>` 而非 `>= length`，边界等于length会越界；有效期外type、数组长度与负数写入应在新版显式约束。

NBT加载直接取复合字段，没有缺失/类型保护；Watcher提供旧版实体追踪同步，未见覆盖专用消息。死亡事件存在，未发现显式 PlayerEvent.Clone/重生复制处理；不能保证跨重生保持或完全清理。氧气通过另一个Watcher同步，AirEvent本身不持久化该自定义氧气值。

PotionStuck：EXT_PROP_NAME=`MiredStuckEffect`；Level=−1，TarTreads=0；save/load为空。CustomPotionEvent在实体构造注册或DoInit。每tick先删除UUID `73A49882-85A3-4896-AD2D-8C591E24AA62` 的旧移动属性修饰器；若Level>0，p=Level−5，c=0若isCollidedHorizontally否则1：

```text
若p<250:
  jumpMovementFactor /= max((1+p*(1+c*2.5)/1000)^8,1)
  speed=max(1/(1+p*(1+c/2)/50)^2,0.02)
否则 jumpMovementFactor=0, speed=0.02
低于0.005的jumpMovementFactor置0
添加不保存的 operation=2 修饰器 amount=speed−1
Level=0；下个未续期tick 0→−1
```

这类状态没有独立NBT/数据包持久化协议；服务器、客户端各自碰撞/事件可能写它。客户端FOV处理读取该状态。新版须定义服务端状态权威、同步快照、重生和维度迁移规则，不能直接照搬 Watcher 数字。

## 其他陷落块的覆盖盘点

下表由每个实际覆盖 `func_149670_a` 的块类提取分支内赋值示例；是可追溯的实现差异，**不是对整类净速度的概括**。完整算法、AABB、under/damage 与状态选择均有该类分析文本及指令附录；未逐一实机标定。没有独立覆盖者可能继承父类行为，父类见 classes.csv。

| 类 | 分支内赋值示例 | 调用到的机制 | 证据 |
| --- | --- | --- | --- |
| BlockBog | entity.field_70159_w *= 0.25;；entity.field_70179_y *= 0.25;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 5.0);；entity.field_70181_x = kof1 > 1.25 ? (entity.field_70181_x += 0.085) : (entity.field_70181_x += 0.1); | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockBog.analysis.txt: func_149670_a；对应bytecode |
| BlockSinkyLiquid | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x = 0.0; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect | BlockSinkyLiquid.analysis.txt: func_149670_a；对应bytecode |
| BlockAcid | entity.field_70181_x = Math.min(entity.field_70181_x / 1.25, -0.05);；entity.field_70181_x = 0.0;；entity.field_70179_y = 0.0;；entity.field_70159_w = 0.0; | antiHoldJumpScript | BlockAcid.analysis.txt: func_149670_a；对应bytecode |
| BlockSand | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x = 0.0; | checkEntityUnder、antiHoldJumpScript、setStuckEffect | BlockSand.analysis.txt: func_149670_a；对应bytecode |
| BlockLiquidChocolate | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x -= 0.05 * (Math.min(0.75, kof1m) + 1.0); | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockLiquidChocolate.analysis.txt: func_149670_a；对应bytecode |
| BlockLiquidMire | entity.field_70181_x = Math.min(entity.field_70181_x / 1.25, -0.05);；entity.field_70181_x = 0.0;；entity.field_70181_x += 0.08;；entity.field_70181_x += 0.1; | checkPlayerMuddy、antiHoldJumpScript | BlockLiquidMire.analysis.txt: func_149670_a；对应bytecode |
| BlockSlurry | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 1.5);；entity.field_70181_x = 0.0; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockSlurry.analysis.txt: func_149670_a；对应bytecode |
| BlockSlime | entity.field_70159_w *= 0.91;；entity.field_70179_y *= 0.91;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x = 0.0; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockSlime.analysis.txt: func_149670_a；对应bytecode |
| BlockJungleQuicksand | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x = 0.0; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockJungleQuicksand.analysis.txt: func_149670_a；对应bytecode |
| BlockTar | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x = 0.0; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockTar.analysis.txt: func_149670_a；对应bytecode |
| BlockMucus | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x = 0.0; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockMucus.analysis.txt: func_149670_a；对应bytecode |
| BlockHoney | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 1.5);；entity.field_70181_x = 0.0; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockHoney.analysis.txt: func_149670_a；对应bytecode |
| BlockStableLiquidMire | entity.field_70181_x = Math.min(entity.field_70181_x / 1.25, -0.05);；entity.field_70181_x = 0.0;；entity.field_70181_x += 0.08;；entity.field_70181_x += 0.1; | checkPlayerMuddy、antiHoldJumpScript | BlockStableLiquidMire.analysis.txt: func_149670_a；对应bytecode |
| BlockMoss | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x -= Math.min(0.05 * (Math.min(0.5, kof1m) + 1.0), 1.0); | checkEntityUnder、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockMoss.analysis.txt: func_149670_a；对应bytecode |
| BlockSoftSnow | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x += a1 / Math.max(1.0, 5.0 - kof1); | checkEntityUnder、antiHoldJumpScript、setStuckEffect | BlockSoftSnow.analysis.txt: func_149670_a；对应bytecode |
| BlockMeatHole | entity.field_70181_x = 0.0;；entity.field_70159_w += (xx - entity.field_70165_t) / Math.max(5.0, kof1m * 25.0);；entity.field_70179_y += (zz - entity.field_70161_v) / Math.max(5.0, kof1m * 25.0);；entity.field_70181_x /= 4.0; | checkPlayerMuddy、antiHoldJumpScript、suctionWorldCheck | BlockMeatHole.analysis.txt: func_149670_a；对应bytecode |
| BlockSwallowingFlesh | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x = 0.0; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockSwallowingFlesh.analysis.txt: func_149670_a；对应bytecode |
| BlockBrownClay | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 1.5);；entity.field_70181_x -= 0.025 * (double)mtdkof * (Math.min(0.75, kof1m) + 1.0); | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockBrownClay.analysis.txt: func_149670_a；对应bytecode |
| BlockSinkingWool | entity.field_70159_w *= 0.71;；entity.field_70179_y *= 0.71;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x = 0.0; | checkEntityUnder、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockSinkingWool.analysis.txt: func_149670_a；对应bytecode |
| BlockTent | 见方法内速度/位置操作 | 见独立方法逻辑 | BlockTent.analysis.txt: func_149670_a；对应bytecode |
| BlockWax | entity.field_70159_w /= (double)(mtd * 100 + 1);；entity.field_70179_y /= (double)(mtd * 100 + 1);；entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockWax.analysis.txt: func_149670_a；对应bytecode |
| BlockBlossomSlab | entity.field_70179_y = -0.15;；entity.field_70159_w = 0.15;；entity.field_70179_y = 0.15;；entity.field_70159_w = -0.15; | 见独立方法逻辑 | BlockBlossomSlab.analysis.txt: func_149670_a；对应bytecode |
| BlockMorass | entity.field_70159_w *= 0.5 / (double)mtdkof;；entity.field_70179_y *= 0.5 / (double)mtdkof;；entity.field_70159_w *= 0.5;；entity.field_70179_y *= 0.5; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockMorass.analysis.txt: func_149670_a；对应bytecode |
| BlockVoreHole | entity.field_70181_x = 0.0;；entity.field_70159_w += (xx - entity.field_70165_t) / Math.max(5.0, kof1m * 25.0);；entity.field_70179_y += (zz - entity.field_70161_v) / Math.max(5.0, kof1m * 25.0);；entity.field_70181_x /= 4.0; | checkPlayerMuddy、antiHoldJumpScript、suctionWorldCheck | BlockVoreHole.analysis.txt: func_149670_a；对应bytecode |
| BlockMire | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x = 0.0; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockMire.analysis.txt: func_149670_a；对应bytecode |
| BlockSolidHoney | entity.field_70181_x = 0.0;；entity.field_70181_x += 0.08 + Math.min((0.9 - kof1) / 100.0, 0.005);；entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0; | 见独立方法逻辑 | BlockSolidHoney.analysis.txt: func_149670_a；对应bytecode |
| BlockWetPeat | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 1.5);；entity.field_70181_x -= 0.05 * (double)mtdkof * (Math.min(0.75, kof1m) + 1.0); | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockWetPeat.analysis.txt: func_149670_a；对应bytecode |
| BlockMeat | entity.field_70159_w *= 0.9;；entity.field_70179_y *= 0.9;；entity.field_70179_y = 0.1;；entity.field_70159_w = 0.1; | 见独立方法逻辑 | BlockMeat.analysis.txt: func_149670_a；对应bytecode |
| BlockSinkingClay | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 1.5);；entity.field_70159_w *= (double)0.91f; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockSinkingClay.analysis.txt: func_149670_a；对应bytecode |
| BlockCorruptedSand | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x -= 0.025 * (double)mtdkof * (Math.min(0.75, kof1m) + 1.0); | checkEntityUnder、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockCorruptedSand.analysis.txt: func_149670_a；对应bytecode |
| BlockGas | 见方法内速度/位置操作 | 见独立方法逻辑 | BlockGas.analysis.txt: func_149670_a；对应bytecode |
| BlockBlossom | entity.field_70159_w *= 0.9;；entity.field_70179_y *= 0.9; | 见独立方法逻辑 | BlockBlossom.analysis.txt: func_149670_a；对应bytecode |
| BlockMoor | 见方法内速度/位置操作 | 见独立方法逻辑 | BlockMoor.analysis.txt: func_149670_a；对应bytecode |
| BlockDenseWeb | entity.field_70159_w *= 0.91;；entity.field_70179_y *= 0.91;；entity.field_70181_x = 0.0;；entity.field_70181_x += 0.08; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockDenseWeb.analysis.txt: func_149670_a；对应bytecode |
| BlockSoftGravel | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = 0.0;；entity.field_70159_w -= 0.2 * mul; | checkEntityUnder、checkPlayerMuddy、antiHoldJumpScript、setStuckEffect、suctionWorldCheck | BlockSoftGravel.analysis.txt: func_149670_a；对应bytecode |
| BlockLarvae | entity.field_70159_w = 0.0;；entity.field_70179_y = 0.0;；entity.field_70181_x = entity.field_70181_x > -0.1 ? 0.0 : (entity.field_70181_x /= 2.0);；entity.field_70181_x /= 4.0; | antiHoldJumpScript、setStuckEffect | BlockLarvae.analysis.txt: func_149670_a；对应bytecode |

## 未解决问题与下一步

- 上述为静态行为恢复，未测每种方块、不同体型/装备/维度的时间—浸没曲线；不能宣称旧版平衡已完全复现。
- 旧版玩家坐标、web、重力、碰撞与LivingUpdate执行顺序决定净下沉速度；建立逐tick轨迹基线后再迁移。
- 随机数分支、兼容生物免疫、Mud所有metadata、暂停/低TPS、玩家重生/切维度的边界须补运行实验。
- 死亡打包溢出、type数组边界和非整数幂NaN应作为兼容性决策记录；新版建议修复并写明行为差异，不能无意保留。
- 建议下一步先按报告05的旧版基线矩阵验证，再经授权启动任务002。
