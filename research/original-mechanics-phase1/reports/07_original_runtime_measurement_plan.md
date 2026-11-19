# 原版实机测量：状态NOT_RUN与可执行记录规范

本轮是静态文件研究。**没有原版逐tick数据、截图、录像或声音听验，以下全部是待测计划。**没有用B2曲线、独立Java算术或伪造空CSV充当原版结果。已下载官方客户端仅为静态UV/相机参考；未启动1.7.10 Forge、未搭好记录器，也未验证原模组加载。

## 基本矩阵

original-runtime-cases.csv有90个NOT_RUN基础案例：3材料×5场景（静止、水平输入、连续跳跃、高处入沙、深层脱困）×2池深（1、3格）×3种子标签（0、1、2）。这些种子是计划输入，不是已取得的运行种子。泥浆需再扩展窄池/宽池、meta0–3、侧边空气/实体、上覆水/液体，以及无靴/普通靴/WadingBoots；它们当前也未执行，不用90案例掩盖额外缺口。

先记录原模组与Forge/Java版本、所有配置、Jar SHA、维度、原MC/Forge客户端和服务端、实体实际类、玩家皮肤/模型、装备/36格库存、池坐标与metadata、初始worldTime和seed。固定输入与几何、同步RNG初始条件，每场景至少重复三次；仅固定worldSeed并不能证明World RNG消费序列相同。

## 每tick至少记录

- tick ID、worldTime、单调时钟、侧别、玩家UUID/实体类/维度、碰撞回调计数和本tick回调次序。
- posX/Y/Z、prevPosX/Y/Z、AABB.minY脚部位置、AABB.maxY、eyeHeight与eyeWorldY、该回调block坐标/metadata及上邻块。
- k、km、previous k、mtd/getMudDepth/getMudSafe、World RNG调用序号（可安全取得时），而非只记“浸没百分比”。
- motionX/Y/Z在实体更新前、方块回调前后、引擎移动/重力/web后的值；实际ΔX/Y/Z另列，不混为“速度”。
- mr局部、PotionStuck.Level在碰撞和LivingUpdate前后、移动属性modifier UUID/amount/operation、jumpMovementFactor；onGround、isInWeb、collidedHorizontally、fallDistance。
- movement/jump/splash/rotation判定、本地按键、boots/装备/负重配置；自定义air/nativeAir、健康、伤害请求和实际伤害。
- 污渍type/level/time/raw packed值、湿润、遮罩族/等级、overlay触发、第一/第三人称与视角切换、相机最终位置、播放音效/音高/音量和实际泡泡生成。

插桩应采用外部测试Mod/调试代理并保留原JAR哈希，明确记录注入位置；不修改原始上传JAR。不在随机分支内额外消费RNG，不因日志读取改变模拟时钟或运动输入；记录性能与异常，不声称插桩天然无扰动。

## 数据处理与判定

以真实脚部位置和当前材料表面分别定义深度；旧k仍单独保留。按0.25格深度区间输出静止/移动/跳跃各自净下降ΔfootY/Δtick的样本数、分位数/范围，分开客户端和服务端采样、web/ground/装备/元数据与回调次数。停在底部的0速度不能混入悬浮净速度估计；网络批量位移不能当单客户端tick速度。

同时保存视频/关键帧，对照深陷横移/跳跃因子、逐级污染身体部位、干燥残留/湿洗、头埋与仅相机入沙、音效门控。原版事实和现代适配容差等测完再决策，不预先写“越深严格越慢”或给现代速度系数。

运行状态文件original-runtime-status.json明确标为NOT_RUN，所有数据文件列表为空。类/方法和语义未闭合的区域，继续保留UNKNOWN/PARTIAL，不把空数据当通过。
