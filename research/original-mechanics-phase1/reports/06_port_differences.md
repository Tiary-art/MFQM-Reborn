# 原版事实、B2差异与后续修复约束

对比基线为B2提交03a6a20，不是未经取得的MFQM-main (5).zip。下列“确认”均为本轮静态文件/表达式验证，运行状态另列。本轮没有改这些代码。

|项目|原版事实/证据|B2位置和差异|证据/运行状态|
|---|---|---|---|
|深度参数|玩家/非玩家k不同，Soft再-.2，km单独保存|ContactSampler通用depth/immersion；MotionMath随depth增大而加快目标下沉|静态确认；旧净曲线NOT_RUN|
|持续Y|多段正补偿+web+ground+随机，仍受旧引擎积分|MotionMath固定net目标，base+depth+moving+struggle|已实现现代提案，不是还原|
|入沙|QS/Soft快落/2，Mud特定路径/10；慢Y先0|MotionRuntime首步扫掠/.08穿入和3刻阻尼|现代安全适配，保留B1回归基线；不要直接删|
|横向|QS清零；Soft阻尼后深处清零+中心牵引；Mud浅层提前返回及boots差异|SinkMath通用profile/.5 immersion中心牵引门槛|部分相似，分段与坐标不等价|
|mr|QS线性k、Soft幂1.75、Mud幂1.5；深区强制值|SinkMath `round(5+(max-5)*immersion)`|明确不同，非只调max值可修复|
|实际阻碍|CustomPotionEvent碰撞corrector、8次幂jump衰减和threshold|SinkMath只给速度系数；MotionRuntime另抑跳|不能标成旧jumpMovementFactor等价|
|挣扎|ΔY判跳/上升、客户端持键、boots/负重、World RNG吸力|固定struggleExtra目标速度；意图包|现代协议可保留，效果不能当原公式|
|RNG与次序|FX与物理可消费同一World RNG；多回调/实体例外|中央预算+Entity RNG+最强Contact一次结算|现代预算/权威适配，旧精确轨迹不保真|
|污渍类型|33类型，Mud实际借Mire9；可覆盖比较|SinkState只有三核心profile residueType|丢失类型和污染更新差异|
|污渍等级|1–10分段阈值和level纹理|residueTicks整身alpha，无level|核心视觉差异|
|污渍时间|每材料max/inc/last不同，干燥可停在残留阈值|接触+5，离开-1到0，水雨-50|清洗/残留规律不等价|
|污渍纹理|两族20张64×32、type着色、mt/1000 alpha|CoatingLayer/CoatingHands使用Vanilla block纹理|占位，不是原始MFQM美术|
|盔甲|已追踪路径只装主Biped子模型；完整装备显示未测|B2主动加标准盔甲覆盖|现代新增行为，不能倒写为原版已证实|
|眼部遮挡|player eyes-.2 S检测；可强制第一人称；核心不透明RGB.1|SinkHud只按MainCamera.position，.78透明|触发对象和强度都不同|
|相机射线|旧Vanilla不跳过空实体AABB，求Block轮廓|现代VISUAL默认空collision，无专用visual shape|静态链确认；旧Forge实机未测|
|空气HUD|旧自定义Watcher向下夹原生air，QSCAir可重绘|NativeAir/SinkEngine单authority nativeSupply|现代兼容选择，须与旧事实分开|
|声音|旧核心已有Vanilla事件及精确门控/pitch|MaterialEffects换成泥步等统一fallback|素材合法不等于声音行为还原|
|泥浆几何|metadata/池宽/液体/侧边/装备|MudGeometry部分覆盖|保留已测现代功能；逐分支另核验|
|49/13数量|49是注册对象数、13原BlockFluid族|B2全量注册和现代流体框架|注册覆盖已做；原行为不能按数量宣称完成|

## 不进入编码的修复顺序

1. 先建立旧版客户端/服务端同场景轨迹和RNG/回调次序数据；模型容差待数据，不再凭体验反向制造一条统一递减曲线。
2. 运动先逐材料保留入口、坐标、分支、装备/实体/拓扑条件；将现代可保留的服务端权威、防异常落地、网络校正列为适配层，和旧公式分别验收。
3. 污渍恢复type/level/time三维数据；先准确私有映射20遮罩和UV，再考虑现代64×64/左右手/姿态/盔甲。旧打包错误用明确兼容决策修复。
4. 相机视觉shape、眼部遮挡和FOV分别测，不能通过加实体实心碰撞箱一并解决。
5. 声音按原事件及门控映射；若旧事件就是Vanilla则使用相应现代事件是有证据的迁移，不应换成无关声音后声称原版。

B1已验证的现代高速入池耗散、Y稳定、有条件着陆修复作为回归约束保留。没有在此报告中宣称这些现代回归测试是旧版测试，也没有新增一个候选JAR或继续Task004。
