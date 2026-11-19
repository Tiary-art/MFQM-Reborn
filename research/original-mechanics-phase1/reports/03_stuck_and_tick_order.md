# 阻碍、坐标与tick顺序

## 不能把旧k当现代浸没比例

Quicksand/Mud玩家计算 `k=entity.posY-blockY-1`，非玩家为`entity.posY-blockY+.5`；Soft在此基础上减.2。`km=max(k,0)`与上一帧k独立保存。若上面连续两格同材料，只把k改成.001，**km没有重算**，所以后续分支选择与分母可以使用不同的量。

旧玩家坐标框架尤须谨慎：官方1.7.10 EntityPlayer的SRG `func_70047_e`（obf yz.g）返回.12，构造/复位中yOffset字段field_70129_M有1.62的赋值；不能把它直接当作现代玩家脚部Y+1.62。此为外部Vanilla参考，具体客户端/服务端玩家子类、姿态和Forge补丁仍需运行确认。测量时必须同时记posY、AABB.minY、eyeHeight和eyeWorldY，不能把posY列直接命名“脚部Y”。

## mr不共用一条曲线

三式均是碰撞分支的局部基础值，后面还会被深区强制值/装备规则覆盖：

- QS：`min(5+floor(max(0,100*(1.5-km))),145)`。
- Soft：`(int)min(5+floor(max(0,pow(12.5*(1.5-km),1.75))),175)`。
- Mud：`(int)min(5+floor(max(0,pow(4*(1.5-km),1.5))),145)`。mtdkof在该路径为2，不是QS的10。

Soft/Mud当km>1.5时非整数次幂底数负，Java NaN沿Math.max/floor/min传播，最终转int为0。不是先夹底数为0得到5。独立Java算术核查已验证；这不证明实际碰撞中该输入频率，也不决定新版应否复制旧边界行为。

QS/Soft/Mud在k<.45且isTrulySink时另强制145/175/145。`isTrulySink`对玩家返回world.isRemote，对非玩家返回true。原版部分阻碍只在客户端写，不能把现代服务端权威协议冒充旧事实。

## 真正移动限制由CustomPotionEvent实施

每次LivingUpdate先移除固定UUID `73A49882-85A3-4896-AD2D-8C591E24AA62`旧modifier。若Level>0，p=Level-5；水平碰撞时c=0，否则c=1：

```
jumpMovementFactor /= max((1+p*(1+c*2.5)/1000)^8,1)
speed=max(1/(1+p*(1+c/2)/50)^2,.02)
```

p>=250时jumpMovementFactor=0、speed=.02；算后jumpMovementFactor<.005置0。然后添加operation2、amount=speed-1、不保存的移动属性修饰器，Level置0；未续期下一次0→-1。PotionStuck.save/load为空。MFQM.setStuckEffect直接委托setter，并非全世界统一取最大值；多个接触回调和boots脚本的次序可能改变最终Level。

静态算术表在static-stuck-arithmetic.csv，其中jump起值.02是明确的探针输入，**不是测到的每tick起始值**；表未执行深区强制值、web或装备逻辑。它只能展示表达式的数值，不是运动模型。

## 必须保留的次序约束

三类先保存旧Y/上一Y/旧motionY，再识别动作。QS先清X/Z再Y耗散；Soft先X/Z×.71再Y耗散；Mud无靴着地先×.1，但mtd0分支会提前return，后面的×.71和Y/10并不总执行。特殊生物/兼容实体还可能提前返回。

声音/泡泡代码在多条后续物理随机判断前消费同一个World RNG。删除一段“纯特效”代码，或改成独立Entity RNG，可能改变后面的吸力/web/着地结果，不能只保持表面概率就宣称重放一致。

吸力不是固定挣扎加速：`VelY=max(prevMotionY*10,.25)`，客户端穿靴条件再缩放，然后time取模与nextInt(5)筛选。这里不是abs(prevMotionY)；负的入射速度会被.25下限替代。碰撞中的jump使用ΔY>.2，另有ΔY>.001的上升分支；按住跳键由末端antiHoldJumpScript处理，不是同一个条件。负重每32刻刷新缓存，armor/boots/heavy命名还影响阻碍与Y补偿。

典型正增量.075/.0735/.0725是修改motionY的浮力补偿，**不是每刻位移**。web、重力、碰撞、ground状态、位置回退和事件先后仍影响净运动。Soft在1.2<=k<1.3的路径先加.0735补偿，之后某分支给局部a1赋.0725；本次字节码中该赋值在已执行的dadd后，不能追溯改变那次补偿（偏移1465–1526与1627–1630）。

本轮没有测原版净下沉曲线，不认定“净速度必然严格随深度单调减小”。可以确认B2的线性深度增益无法表达这些原分支，但不能直接反向造一条递减曲线作为还原。
