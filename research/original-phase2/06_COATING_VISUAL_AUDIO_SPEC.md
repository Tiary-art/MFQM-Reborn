# 污渍、视觉、声音与基础交互规格

证据主要继承Phase1报告04/05及本批拷贝的精确索引；所有运行行为仍NOT_RUN。49材料审查见 `evidence/indexes/coating-applicability-49.csv`，有直接checkPlayerMuddy调用的为条件触发；无直接调用标UNKNOWN（继承/外部入口未排除），没有凭空把全部干沙判为不污染。每个发现的调用附方法@字节码偏移。

## 污渍规则

|核心|实际type|更新上限/增加|残留|
|---|---:|---|---:|
|Quicksand|4|5000/+100|1000|
|SoftQuicksand|17|2000/+100|1000|
|Mud|getMuddyType(Mire)=9|1000/+50硬编码；不是Mud数组29|1000|

33类型、20张64×32遮罩的文件名/哈希与映射分别在phase1-coating-type-map/masks索引。没有上传原图。BrownClay重复索引以首次匹配为准。原版污渍不是“触碰即全身”：按玩家posY+eyeHeight-blockY的阈值依次 `<.7→10, <1.04→9, <1.10→8, <1.21→7, <1.32→6, <1.53→5, <1.67→4, <1.98→3, <2.14→2, <2.4→1`，其余0。等号进入下一档；旧坐标转现代尚待运行核对。

QS/Soft覆盖比较 `preLevel*(maxOpacity/1000)>oldLevel*(oldTime/1000)`；Mud为 `preLevel>oldLevel*(oldTime/1000)`。服务端湿润且不在两种LiquidMire的L检测内时，time每次减5+time/100夹0；worldTime%16==0且旧level>5时level减1。干燥时worldTime%1024==0且level>5、time<1000才降级，worldTime%2==0且time>该type残留阈值才减1。因此饱和泥污可干燥残留，不是必然自动洗白。雨/水应分别记录isWet、LiquidMire排除、worldTime，不能只按进入水体立即清零。

渲染门mt>50、level>0及type检查；alpha=min(1,mt/1000)，level选择textures[level-1]。Mud族level1/2仅腿，level3起躯干/手臂，level6起头；Slime族level7起头；帽壳20图均未发现非透明像素。索引的像素数不等于三维覆盖面积。现代CoatingLayer残留整层表现尚未达到旧逐级UV语义。

原版扫描主Biped模型/手部复制UV并膨胀.2；不证明此路径必然涂全部盔甲。现代64×64左右独立四肢及Alex需重映射，盔甲遮挡另测。DataWatcher打包边界和死亡255异常是兼容/修复决定，不能机械复制成安全现代字段。

## 遮挡、镜头与FOV

原版眼部触发取玩家眼位置偏移-.2，暗色RGB .1、alpha1不透明；这是玩家浸没触发，不是摄像机进入就触发。第一人称遮挡和第三人称相机方块射线/visual shape分开建模；第三人称镜头进入而玩家在外，不能错误激活第一人称污屏。旧方块射线/选框不等于实体实心碰撞；禁止给全部流沙加实心collision来修镜头。

FOV须记录原版事件缓存/恢复条件；现代状态按本地玩家与生命周期隔离，退出/死亡/换维/断线必须恢复。局部模组FOV处理不能全局改原版基础设置。AirEvent/原版气泡栏与现代NativeAir的证据/差异参照Phase1报告05和B2源码，本批未做回归测试。

## 声音与随机数

`evidence/indexes/phase1-material-sound-sites.csv`按材料列具体playSound调用，`phase1-legacy-sounds.json`仅记录模组自有bee声音注册；前一CSV保留反编译参数表达式；调用点精确偏移可在对应块字节码过滤func_72908_a等核对。旧Minecraft内置swim/slime/water/silverfish等事件与模组自有bee OGG区分，不能为每种沙编造专有OGG。声音音量/音高/动作门/clock门必须逐调用取原表达式，不统一为MudStep。

声音/泡泡常在吸力web判定前消耗World RNG；若现代FX改独立RNG，要把轨迹不再逐调用相同写成兼容决定。本批声音索引是调用覆盖，尚未把全部表达式规范化为逐事件可执行调度，状态PARTIAL。没有打包OGG，没有生成或重绘贴图。

## 其他交互：事实/现状/方案/测试

|机制|原版证据边界|现代入口|拟后续工作与场景|
|---|---|---|---|
|原生air/气泡栏|AirEvent与块内窒息调用；不能用自绘条宣称原生|NativeAir/SinkHud|头进出、creative、死亡、服务端扣气同步；NOT_RUN|
|内侧放置|旧可替换/射线与更新链须区分|SinkingBlock/CoreSinkingBlock|沙中脚边/头顶/不同物品/邻接多格；PARTIAL|
|泥堆叠/形状|meta+几何深度/mtd安全分支|MudGeometry/MudBlock|1/2/3层、边缘、保存重载；不是注册即完成|
|条件下落|块随机刻/邻更与LiqFixer相互作用|SinkingBlock|失去支撑/液体/跨区块边界；各材料独立查证|
|船|核心非生物web等路径未证实专用浮船算法|BoatMotion/ContactSampler/MotionRuntime|用户指定兼容增强；不可称旧版复刻。空船/载客/冲入/跨界/保存重载分别测|
|泥浆泡泡|旧SpawnBodyBubble/表面泡泡及开关、RNG|现代粒子/音效路径|不同meta/深度/玩家与非玩家，频率及穿顶；NOT_RUN|

船测试矩阵必须独立列Quicksand、SoftQuicksand、Mud：预期为用户定义“稳定受浮力支撑、保留有限阻力/可移动、载客时不污染玩家独立陷落状态”，此为增强提案，具体浮面高度/阻尼数值未定。水中Boat浸没检测不能直接从水tag推到流沙；原版没有证实的行为保留UNKNOWN。其他实体逐类处理，不能把Boat修复套给所有非living。
