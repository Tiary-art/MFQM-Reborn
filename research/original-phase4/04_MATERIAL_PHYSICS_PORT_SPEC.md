# 全量物理族的本轮进展与准入边界

仍以全部49对象、12 Fluid定义及实际metadata证据为范围，不能把它们视为对应数量的独立物理。Phase3的39contact入口、37指令指纹只是候选分组，不等于已证明37个物理族。本轮没有宣称任何完整物理族PORT_READY。

## 剩余10个入口继续追踪

`ten-contact-inheritance.json`逐对象给父链、obf/SRG和独立javap。HPeat/HardenedClay/Honeycomb/ChocolateBlock/WaxWood等从Block，SandstoneTrap从BlockSandStone，Lure从BlockContainer，LilyPad/Bush系沿各自父链，最后解析到Vanilla `aji.a(Lahb;IIILsa;)V` offset0 return（对应Block.func_149670_a）。这是STATIC_VERIFIED父链，不是只看本类缺方法。

Forge1.7.10补丁和外部事件未核对；Trap下落、植物/TileEntity/碰撞形状等其他入口仍可能有玩法。不能写成“这10种无陷落/无效果”。原官方client与SRG的hash及逐父类字节码已附，仅文本证据，不分发Vanilla jar。

## 可执行数值接口：共享stuck核

原`CustomPotionEvent#onLivingUpdateEvent(Lnet/minecraftforge/event/entity/living/LivingEvent$LivingUpdateEvent;)V`：55..87读取Level-5与horizontalCollision；90..162计算，167..200阈值，217..252添加operation2 modifier并Level置0。原指令在Phase1/2 CustomPotionEvent文本；本轮stuck-kernel-callers.csv给实际材料调用者与offset，范围不是固定三材料。

```
p=Level-5; c=horizontalCollision ? 0 : 1
if p<250:
  jump=(float)(jump/max((1+p*(1+c*2.5)/1000)^8,1))
  speed=max(1/(1+p*(1+c/2)/50)^2,.02)
else: jump=0; speed=.02
if (double)jump<.005: jump=0
modifier(operation=2, amount=speed-1); Level=0
```

PhysicsVectors.java与独立Python数学测试112组输入，包括1/4/5、254/255阈值、水平碰撞、float .005附近。速度容差1e-12、float字符串输出比较1e-7；这是**MODEL_TESTED数值表达式**，没有执行原LivingUpdateEvent完整事件/属性生命周期。probe Level1..4可算出speed>1，但这不证明这些Level自然可达；不能用测试输入反推游戏默认行为。float .005f转换double后略小于.005，边界也不能按十进制直觉替换。

## 深度、动作与安全层

原各材料的k/km、正Y补偿/绝对赋值/回退、web/ground与不同实体/装备/随机路径须沿Phase3每类入口继续闭环。这里的stuck强度随Level变化，不直接证明所有材料Level随深度单调，也不决定净Y。原版净下沉可能变慢的用户观察仍需条件分层实测，当前NOT_RUN，没有编造统一减速公式。

原算法层给逐回调状态意图；B1网络/高速扫掠/耗散/Y同步/着地层保留，不能为套旧公式删除安全层。本轮未改速度、未合并物理profile、未新增现代JAR。首批只可使用上述数值接口规格审阅，完整物理族准入仍BLOCKED。

已定位到共享stuck调用的对象（仅调用路径集合，非同一物理profile）：Bog, BrownClay, CorruptedSand, DenseWebbing, DryQuicksand, Honey, JungleQuicksand, Larvae, LiquidChocolate, Mire, Morass, Mucus, Mud, Quicksand, SinkingClay, SinkingRug, SinkingSlime, SinkyLiquid, Slurry, SoftGravel, SoftQuicksand, SoftSnow, SwallowingFlesh, TangleRootMoss, Tar, Wax, WetPeat。每个入口/offset见stuck-kernel-callers.csv。
