# 全材料污染、眼部遮挡、镜头与原始素材

01的每个对象都带污染适用性：有直接调用为CONDITIONAL_DIRECT_CALL，无直接调用仍UNKNOWN_INHERITED_OR_EXTERNAL。污染类型表达式复用Phase2逐材料表；所有实际checkPlayerMuddy调用在material-instruction-sites.csv对应完整方法/offset。不能把“干沙”名称当成不污染的证据，也不能让全部材料共用Mud规则。逐变体触发阈值完整追踪仍PARTIAL。

33污渍类型、20张64×32遮罩的文件名/hash/UV映射和材质清单从Phase1读取，只复制文本索引。所指是**MFQM自身原始素材**，不是minecraft:sand/mud占位；本轮没有PNG/OGG/JAR公开嵌入，也不以原版Minecraft占位作为资源还原验收。

沿用已定位样本：QS type4(5000/+100)、Soft17(2000/+100)、Mud实际Mire type9(1000/+50)；覆盖按旧玩家posY+eyeHeight-blockY阈值分level10..0，详见Phase2污渍报告。level1/2两族遮罩只腿，Mud族6级/Slime族7级首次头部UV。alpha=min(1,time/1000)，非触碰即全身覆盖。64×64/Alex/盔甲不能套旧共享镜像64×32UV，需独立重映射验收。

MuddyEvent共享清洗服务端分支：湿润且不在两种LiquidMire L检测内，每次time减5+time/100夹0，worldTime%16且旧level>5降级；干燥worldTime%1024且time<1000才降高level，%2且time>类型残留阈值才减time。饱和污渍可干燥保留。逐材料残留参数见coating-type-map，不能当统一最终清零。

第一人称眼部命中与第三人称相机裁剪分开：原overlay走玩家位置/eyeHeight-.2而非独立相机，原图标深色RGB.1、alpha1；具体数组不是全部49对象同序。镜头仅进入、玩家在外不应冒充玩家浸没；旧Vanilla射线可击中空实体碰撞箱块的outline。现代visual shape与第一人称遮挡分别设计，不能加实心碰撞解决镜头。

声音以原playSound调用的事件、volume/pitch和clock/RNG门为证据，逐材料索引沿用Phase1；JAR自有OGG只有bee两项，不能要求每种沙有自有OGG。原声音与泡泡可能先于后续物理消费World RNG，删特效会改随机序列。FOV、air、雨水、设备、跨维与死亡都需原版/现代分开测试，当前全NOT_RUN。
