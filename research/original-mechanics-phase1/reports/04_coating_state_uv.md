# 污渍：类型、等级、时间、UV和洗净

## 状态与持久化

CustomVarPlayer将type/level/time打包一个DataWatcher整数，属性名PlayerMuddyControl，NBT名MuddyLevel。低8位type；level是`(data/256)&255`；time是有符号整除65536。setter没有完整范围约束，不能等同于安全的三字段现代结构。

MuddyEvent死亡序列setLevel(0)→setType(-1)→setTime(0)会产生data=65535，读到type255/level255/time0。独立Java算术检查通过；没有验证旧游戏视觉/重生结果。渲染有mt>50门槛，所以不能只根据异常level推断死亡后全身显污。getLastMuddyType用`>`而非`>= length`、MudModelRenderer用`<= colors.length`均有边界风险；这是未来迁移需明确修复/兼容的旧行为，不应机械照搬。

## 三核心污染更新实际不同

|材料|type来源|覆盖比较|时间上限/增加|干燥残留阈值|
|---|---|---|---|---|
|Quicksand|quicksandIDS首次匹配本块：4|preLevel×(maxOpacity/1000) > oldLevel×(oldTime/1000)|5000 / +100|type4：1000|
|SoftQuicksand|本块：17|同上|max2000 / +100|type17：1000|
|Mud|明确调用getMuddyType(MFQM.MireBlock)：9，**不是Mud自身索引29**|preLevel > oldLevel×(oldTime/1000)|硬编码1000 / +50|type9：1000|

QS/Soft参数由MFQM注册处mudMax/Last/IncOpacity数组传入；Mud的更新器硬编码，不能误用数组index29的max2000/inc100。覆盖等级使用玩家posY+eyeHeight-blockY阈值，从<.7→10、<1.04→9、<1.10→8、<1.21→7、<1.32→6、<1.53→5、<1.67→4、<1.98→3、<2.14→2、<2.4→1，其余0；边界等号落在下一档。坐标须先按旧玩家框架核对，不能原样当现代脚部Y差。

完整33类型色值/默认数组/遮罩族见coating-type-map.csv。quicksandIDS里BrownClay出现两次，getMuddyType首次返回23，不能据表给同一块同时配23/24两个运行身份。每个Block的直接checkPlayerMuddy调用见material-coating-call-index.csv；无直接调用不等于继承或外部路径一定没有污渍。

## 洗净不是统一倒计时

QSCover开关控制MuddyEvent注册和方块更新。服务端玩家type>=0、time>0时：

- 湿润isWet，且不处于两种LiquidMire的L检测中：time每次减`5+time/100`并夹0；time%16==0且旧level>5时level减1。
- 干燥：time%1024==0且level>5、time<1000才降1级；time%2==0且time>该类型lastOpacity才减1。

这里“time%16”等周期条件指worldTime，非污渍time字段。QS/Soft可以逐步降到1000后停止干燥时间衰减；Mud硬编码上限1000而type9残留1000，饱和时干燥不会继续减。time恰1000也不满足level降级的`time<1000`条件。**在这些状态条件下，干燥可以保留污渍；不是必然最终洗白。**未饱和、被其它类型覆盖、湿润和异常打包路径需分别测量。

## 遮罩选择与绘制

MudModelRenderer读取type/level/time：mt>50、level>0且类型通过检查后绘制。颜色由mudTypesColors[type]的RGB乘到纹理；alpha=`min(1,mt/1000)`，所以time1000以后alpha已饱和，5000的时间上限并不是alpha5。level选择`textures[level-1]`，不是一个整身透明量。

type {0,1,3,6,7,8,15,19,20,21,25,28,31}用SlimeOverlay；其余用MudOverlay。三核心QS4、Soft17、Mud实际9均用MudOverlay。两族各10张64×32，遮罩原图未打包进本报告。

CustomRenderPlayerEvent.scanChilds遍历`renderer.field_77109_a`的ModelRenderer/ModelBox，复制原UV起点和box几何，膨胀.2并挂child。手部RenderHandEvent也安装该树。官方旧RenderPlayer+SRG确认该字段是主模型，g/h两个独立盔甲模型不是此处遍历目标。因此目前证据支持主身体/手部模型附层，**不支持“旧代码此路径必然覆盖所有盔甲”**。盔甲遮住身体层的实际表现仍需原版实测。

旧标准Biped为64×32：腿UV[0,16)×[16,32)，躯干[16,40)×[16,32)，双臂共享/镜像[40,56)×[16,32)，头[0,32)×[0,16)，帽壳[32,64)×[0,16)。从官方客户端ModelBiped构造器和SRG字段核对，详见外部文本附录。不能把这套UV无转换套现代64×64、Alex或自定义盔甲。

下表是各区域alpha>0像素数，非三维表面积百分比；完整逐级数据见coating-uv-body-map.csv。两族级别逐对比较均未发现上一等级非透明像素被删或alpha下降，证实是逐级扩张的遮罩，而非单靠提高整身alpha。

|遮罩族/等级|腿|躯干|手臂|头|帽壳|
|---|---:|---:|---:|---:|---:|
|MudOverlay / 1|94|0|0|0|0|
|MudOverlay / 2|160|0|0|0|0|
|MudOverlay / 3|219|111|55|0|0|
|MudOverlay / 4|224|172|93|0|0|
|MudOverlay / 5|224|228|135|0|0|
|MudOverlay / 6|224|297|192|25|0|
|MudOverlay / 7|224|343|218|111|0|
|MudOverlay / 8|224|352|224|176|0|
|MudOverlay / 9|224|352|224|263|0|
|MudOverlay / 10|224|352|224|385|0|
|SlimeOverlay / 1|62|0|0|0|0|
|SlimeOverlay / 2|126|0|0|0|0|
|SlimeOverlay / 3|195|70|37|0|0|
|SlimeOverlay / 4|218|125|77|0|0|
|SlimeOverlay / 5|218|181|107|0|0|
|SlimeOverlay / 6|218|241|152|0|0|
|SlimeOverlay / 7|218|297|194|42|0|
|SlimeOverlay / 8|218|347|221|92|0|
|SlimeOverlay / 9|218|351|224|165|0|
|SlimeOverlay / 10|218|351|224|320|0|

Mud在等级6首次出现头UV非透明像素；Slime在等级7首次出现头UV像素；等级1/2两族均仅腿区域有像素。帽壳区域20张图均无非透明像素。实际动画姿态/装备遮挡/现代左右独立UV重映射未验证。
