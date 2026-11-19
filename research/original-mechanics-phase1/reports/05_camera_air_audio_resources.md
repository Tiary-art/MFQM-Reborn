# 相机、遮挡、FOV、氧气、气泡、音效与原图

## 眼部遮挡：已可进一步验证的原版路径

CustomRenderOverlayEvent.RenderOverlay遍历其**自己的30元素数组**（不是EntityRope的33元素同序数组），传入Minecraft.thePlayer到MFQM.isEntityInsideOfBlockS。该方法用`player.posY+eyeHeight-.2+overCor`，按方块位置/上沿判断；部分BlockFluidClassic有.15修正，Moss有上移采样。它没有传入独立摄像机坐标。

命中后取图标；该overlay数组i==19特判图标side1，此处19是Moss，不是EntityRope数组的SwallowingFlesh索引19，不能混用索引。QSThirdPerson配置名实为“Force camera to firstperson in deep”，config.get声明默认true（代码另有getBoolean(false)读取fallback）；启用时将thirdPersonView写0。随后仅视角0且renderViewEntity的func_70608_bn为false时画inside quad。应保留原SRG条件，不把它未经核对解释为任意“相机未被方块挡住”。

renderInsideOfBlockR绑定原方块atlas图标，glColor4f(.1,.1,.1,1)，在identity矩阵下画全屏quad。直接测JAR内三核心材料对应的五份默认/变体图标原图alpha均为255，故对这些原图该绘制输入是**不透明深色遮挡**，与B2的半透明.78占位不同。实际渲染事件/其它mod相互作用尚未运行核验。

## 相机裁剪与实体碰撞是两条路径

官方1.7.10 EntityRenderer.func_78467_g（blt.h）第三人称有8条±.1偏移射线，用World.func_72933_a。World该重载调用总方法(false,false,false)，因此不因“忽略无碰撞箱”而先跳过空实体AABB；Block.canCollideCheck默认允许，再调用Block.collisionRayTrace，它会更新Block bounds并求轮廓交点。QS/Soft没有重写canCollideCheck/collisionRayTrace；Soft更新bounds为顶.85/内层1。**空实体碰撞箱不代表旧相机射线也为空。**这是Vanilla原始类+mod覆盖方法的静态链，不是已测旧Forge摄像机轨迹；Forge补丁/第三方事件仍未穷尽。

现代1.20.1 Camera.getMaxZoom使用ClipContext.Block.VISUAL，BlockBehaviour.getVisualShape默认返回getCollisionShape。B2 SinkingBlock空实体碰撞且未覆盖visual shape，因此视觉射线沿用空形状；B2 SinkHud随后只看MainCamera.position，造成“玩家在外而第三人称相机进沙也遮挡”的代码路径。修正需分开研究视觉shape/相机裁剪，以及玩家眼部触发overlay，不应靠把流沙做成实心碰撞体解决。

## FOV

旧CustomPotionEvent缓存MFQM.SIFOV：不受stuck时更新缓存，stuck Level>=0时event.newfov回到缓存；拉弓另乘弓系数。它并不是数学上逐个排除MFQM UUID，所以可能连其他时变FOV也冻结。B2定向排除自身速度modifier属于现代兼容决策，不应标成旧代码直接复刻；还应分别验证正常FOV、冲刺、药水、飞行、弓/望远镜和其它mod。

## 氧气与伤害

AirEvent服务端按EntityRope数组检测：跳过6/7/13/15/21，22用M采样，其余普通采样；覆盖时自定义Watcher air大于-1则减1并return，离开最多补5到300。客户端只在自定义air更少时向下夹原生air。CustomRenderOverlayEvent在AIR事件也向下夹原生air，QSCAir开启会取消默认并自行画原版图标。

MFQM.isDrowning在对应氧气开关关闭时直接true，不表示“关闭伤害”；开启时服务端gma<0且worldTime%16==0则置0并返回true。三核心再按眼部、存活、服务端检查调用max(maxHealth*.1,2)*DmgMul的drown伤害。真实掉血频率仍受hurt resistance/其它事件影响，不能把调用次数直接算DPS。

因此“原生气泡UI”并非原版完全无关的创新，但B2的服务端native-air共享预算/水肺处理是不同实现/现代产品方案。旧代码的WaterBreathing、Respiration、与水切换整体效果本轮未测，不能据B2测试反证旧版。

## 三核心音效与泡泡

原JAR自有sounds.json只有mob.bee.hurt、mob.bee.say，两份对应OGG。三核心所读路径大量使用旧Minecraft事件名：game.player.swim、mob.slime.attack、mob.magmacube.jump、mob.silverfish.step、liquid.water；Soft还用step.sand/step.grass/dig.sand。原版使用Vanilla声音是直接事实；B2 block.mud.step等不同事件并不能据此算对应还原。须保留事件、volume/pitch表达式、时钟和随机调用次序。

|材料|原代码中主门控/例子|泡泡差异|
|---|---|---|
|QS|time%128，移动按movCof，跳跃%8，splash；swim音高rand*.25+.1；跳跃slime attack|入沙玩家nextInt2三泡，移动nextInt5一泡；另%16且nextInt10 body bubble|
|Soft|静止%4，移动movCof/2，跳跃%8；silverfish+沙/草组合|本回调无QS式BodyBubble调用，但调用SpawnMudTentacles，不能据此宣称全局无任何效果|
|Mud|mtd0提前return；更深用%128/移动/跳跃/入沙门控；pitch与QS有差异|splash nextInt3两泡、移动nextInt7一泡、跳跃nextInt5三泡；mtd>2且%32、nextInt20的环境泡还在外层门控内，不能当独立1/640每刻事件|

源码各播放点在material-sound-sites.csv；随机调用顺序在core-random-call-sites.csv。spawnBodyBubble/Random内部有实体/客户端/表面/配置等附加条件，调用出现不保证每次实际生成。此阶段未听验、未跑原版粒子帧率，不把事件存在写成实测。

## 原图与授权

QS实际注册morefunquicksandmod:quicksand；Soft metadata0→SoftQuicksand1、1→SoftQuicksand0、2→SoftQuicksand2；Mud默认mud，兼容维度还可能改取外部模组图标。这是精确资源名，不能用minecraft:sand/red_sand/mud冒充MFQM原图。core-texture-map.csv和全部247纹理清单/48动画JSON保留原始大小写和哈希。

原图并不全为16×16静态文件：有32像素宽、纵向动画条，以及20张64×32污渍遮罩。整套block/item/entity/armor/overlay映射需按用途区分。当前B2三核心只用Vanilla占位，是资源偏差；本次仅输出名称/尺寸/哈希/统计和文本证据，没有拷贝原PNG/OGG/JAR进交付包，也没有AI生成或重绘。独立纹理目录ZIP缺失不妨碍对JAR内真实文件做静态清点。
