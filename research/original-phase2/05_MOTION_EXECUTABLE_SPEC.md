# 三核心运动逐tick规格：局部可执行，完整等价仍PARTIAL

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
