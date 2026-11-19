# 两个可直接实施的纯组件规格（下轮建议，本轮不实施）

目标Java17/MC1.20.1/Forge47.2.0；只准入下面边界，不等于完整模组/世界生成准入。原方法、seed、native/oracle trace和diff在cases、method-provenance及summary中。

## A. DryQuicksand有序体素事务核心

原`CustomWorldGen#generateSoftSand(IIIILnet/minecraft/world/World;Ljava/util/Random;)V`，完整字节码范围见method-provenance。不是SoftQuicksand。

```java
interface LegacyRandom { int nextInt(int bound); double nextDouble(); }
interface VoxelPort {
  LegacyBlock blockAt(int x, int y, int z);
  boolean write(int x, int y, int z, LegacyBlock block, int metadata, int flags);
}
void generateDry(int x, int y, int z, int extent, VoxelPort world, LegacyRandom rng);
```

接口必须按执行次序立即应用状态，再返回写入是否接受；写失败或写相同状态也不能擅自删掉调用。后续查询读实际结果。禁止将结果先去重、无序并行写入或同时侵蚀。

固定映射：SandBlock→mfqm:dry_quicksand的默认meta0状态；field_150322_A→minecraft:sandstone默认态；field_150350_a→AIR。判断同块忽略meta，等价state.getBlock身份。1.20 cave_air/void_air在适配层明确归为Legacy AIR，这是新增世界状态的兼容决定，不是原1.7.10事实。

原flags3对应邻更+客户端更新意图；算法核心不包含真实Level更新/掉落/落体回调。运行Adapter需另审，不可先注册天然Feature。VoxelPort由算法测试网格提供，无Minecraft依赖即可实现；实际DryQuicksand物理未完成不影响这个纯组件的接口验收，但阻止其天然玩法集成。

数学与顺序：

```
cof=max((double)extent/10,1)
a=rng.nextDouble()+.5
b=((1-a)+.5)+.5                  // 保留运算顺序
for i=0..extent, j=0..extent, e=0..extent:  // 此嵌套次序
  p=(x+i-extent/2(int), y-j, z+e-extent/2(int))
  dis=sqrt(pow(x-p.x,2)*a+pow(y-p.y,2)+pow(z-p.z,2)*b)
  threshold=((double)extent/2)/(1+abs(a-b)/3)
            +(rng.nextDouble()*cof-cof/2)
  if dis<threshold:
    write(p,SandBlock,0,3)
    write(p.y-1,SandBlock,0,3)
    write(p.y-2,Sandstone,0,3)
if extent>4 && (extent<10 || rng.nextInt(2+extent/2)==0):
  for i=0..extent, j=0..extent+1, e=0..extent:
    p=(...)
    if j<extent/3 && blockAt(p)==SandBlock:
      wall = any neighbor in order(-x,+x,+z,-z,-y)
             whose block is neither AIR nor SandBlock
      if !wall: write(p,AIR,0,3)
```

extent不是球半径。每个体素点都抽噪声，初始draw在空/负extent时仍发生；不能优化为仅内球抽样。整数除法为Java截断，double算式保留旧序；LegacyRandom用48bit java.util.Random兼容序列，注入同一个协调器实例，不换新seed、不假定所有RandomSource等价。不要删nextInt1。

验收：native与独立VM完整分支/读取/RNG/写入一致；独立几何/有序侵蚀oracle的事务与最终网格一致。边界extent -1/0/1/4/5/10/18、seed0/1、空网格、自然父调用seed38、概率/无地面/写拒绝和组合配置均有用例。语义闭环仅限声明域；其它世界副作用/所有seed统计不宣称实机通过。

## B. Stuck属性租约/Level状态reducer

原`CustomPotionEvent#onLivingUpdateEvent(LivingUpdateEvent)V`，原body与clinit指令指纹相同。准入的是属性/Level子组件，不含旧air factor字段及整体事件挂接。

输入：可选Stuck属性状态（初始Level=-1）、当前Level int、horizontalCollision、固定UUID现有modifier；AttributePort保证当前调用内无其它mod重入改同UUID。

```
Contact(level): pendingLevel=level     // 覆盖，不是max
Update:
  查询固定UUID；若存在先移除
  若属性不存在: return
  若Level>0:
    p=Level-5; c=horizontalCollision?0:1
    speed= p>=250 ? .02 : max(1/(1+p*(1+c/2)/50)^2,.02)
    再次查询UUID；若仍无则加operation2,amount=speed-1,saved=false
    Level=0
  否则若Level==0: Level=-1
  其它负Level保持
```

现代映射：Attributes.MOVEMENT_SPEED；UUID 73a49882-85a3-4896-ad2d-8c591e24aa62；removeModifier(UUID)；addTransientModifier(AttributeModifier(..., MULTIPLY_TOTAL))。其它修饰符不删除，不能改base speed；状态不写持久NBT。0代表本轮已消费但本帧modifier仍有效，下次无续期才移除、变-1。

8次实际旧事件体、123事件的独立reducer对照、Phase4的112数学向量提供验收。材料接触函数本轮没实机/原方法执行，不把测试的Contact输入伪装碰撞测量。原jumpMovementFactor是空气控制，不是motionY；现代映射仍BLOCKED。Global Forge tick与碰撞的时序尚待验证，所以当前只能实现纯reducer及模拟测试，不能接正式事件。

## 集成前保留的闸门

两组件先作为可复现算法/状态单元实施，单独测试；不要注册PlacedFeature或改B1网络/运动代码。完整Surface协调器、原块更新语义、空气控制、材料Level产生路径、FOV/视觉、现代NBT与真实MC对照另行授权与验收。
