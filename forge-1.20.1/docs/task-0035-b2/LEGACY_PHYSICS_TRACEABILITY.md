# 物理证据与现代适配

基线 `c399b3b`，Task 001 静态源码/字节码证据均在仓库 `research/task-001/evidence/`。未运行 1.7.10 参考实例，没有原版逐 tick 曲线或原版完整 registry dump。

|行为|原证据|B2实现/性质|限制|
|---|---|---|---|
|49个 Block / 13个 Fluid|`MFQM.analysis.txt` 约968–1178；`reports/03_registration_and_network.md` 每行引用|保留所有可证实旧Block映射，独立13组流体|可证实调用数，不虚构旧运行时dump|
|高速进入耗散|`BlockQuicksand.analysis.txt` / `BlockSoftQuicksand.analysis.txt` 的 Y /2；`BlockMud.analysis.txt` 的 Y /10|保留B1预移动扫掠；首步穿入 .08；新增3刻阻尼 .08^age|现代有界适配，非旧公式逐行移植|
|持续缓慢下沉|三核心类实体接触分支、按深度/运动/跳跃分支|新 `motionV2`：上限 .012，QS .0055/Mud .0048/SS .0065，深度 .004，移动 .001，挣扎 .002|全部数值是保守提案；B1 .055上限降低78.2%；其它材料倍率亦为提案|
|软流沙顶/内层高度|`BlockSoftQuicksand.analysis.txt`，上层存在时完整单元，顶层 .85|同一高度函数驱动轮廓/眼部/相机接触；filled模型内层1、顶层.85；碰撞空|邻块更新恢复模型；人为破坏state或异常导入未覆盖|
|QS/SS条件下移|`BlockQuicksand.analysis.txt`350ff及Soft同名updateTick；QS随机1/5、Soft1/2，下方可替换且不阻运动|仅两种CoreSinkingBlock随机刻单格搬移；水邻接抑制，岩浆硬化；非FallingBlock|现代不用旧全局LiqFixer；旧scheduleUpdate时序未等价恢复；Mud不下移|
|泥浆地形支撑|`BlockMud.analysis.txt`及B1 MudGeometry审计|保留有效深度/边界浅层支撑，不套用沙子重力|旧地形递归完整等价仍未证明|
|船只|旧三核心只处理LivingEntity，没有可证实船浮力路径；1.20.1 Boat.getStatus/floatBoat只认可流体/地面检测|用户批准 MODERN_COMPAT；船体预移动补偿原版 -.04f 重力，阻尼弹簧目标吃水 .65*船高，保留原版.9水平阻力/划桨/转向|普通/箱船共用；仅三核心，真实原版水仍用原版路径；不是伪水FluidState|
|船沉底根因|SinkingBlock空碰撞+空FluidState，LivingEntity采样不包含Boat|过去Boat处IN_AIR持续受重力，骑手还可能被旧位移纠正；B2独立船体与骑手路径|载人边界/高速过池人工测试需另列|
|内部放置|旧源码射线/可替换行为相关，现代合法交互适配|仅射线起点所在流沙单元轮廓跳过，其余目标/实墙仍走原版clip及reach|不提高reach、不绕过服务端；真实主/副手操作待检查|
|FOV|现代兼容要求|重算MOVEMENT_SPEED，单独排除MFQM UUID，保留其余操作/属性clamp及事件FOV比例；望远镜不改|多模组同时改FOV的组合未实测|
|空气|旧独立300预算、16刻伤害节奏|共享native airSupply与原cap下限，核心接触时LivingBreatheEvent禁止同刻原版消耗/补气；服务端唯一结算；原生泡泡条|保留旧16刻伤害节奏；水切换和效果需专项实测，不能只凭界面宣称全兼容|
|13种黏稠物|对应13个BlockFluidClassic类与MFQM.registerFluid|独立FluidType/源/流动/桶；非water tag，不把所有流沙伪装成水；共享SinkingMedium+材料倍率|统一现代流动tick20/坡距2/衰减2、无无限源；密度1500/黏度6000为占位，旧参数待逐项复原|
|砂岩陷阱|`BlockSandstoneTrap.analysis.txt`34–55，红石触发横向递归转QS|有界队列横向最多64个visited位置转换|安全界限与旧无界递归不同，大群不保证一次全转换|
|脏污/声效|旧相关类接触/渲染/音效引用；现代适配|服务端残留量持久化、定期/追踪同步；独立人物/标准盔甲/手臂层，vanilla纹理；水雨清洗；中央预算声音/泥泡|旧特殊分区UV/自定义盔甲/雨洗速率/环境泡泡非完整复刻|

相关实现：`physics/MotionMath`, `MotionRuntime`, `SinkEngine`, `CoreSinkingBlock`, `BoatMotion`, `NativeAir`, `content/LegacyFluids`, `client/ClientCompatibility`。没有永久Y锁定，也没有任何全局fallDamage豁免。旧材质/音频均未加入公开资产。
