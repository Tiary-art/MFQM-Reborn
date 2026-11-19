# Stuck生命周期与首批可实施接口

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
