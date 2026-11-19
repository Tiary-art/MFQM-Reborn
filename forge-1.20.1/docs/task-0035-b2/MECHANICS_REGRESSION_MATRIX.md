# 实现与验证分开记录

环境：MC1.20.1、Forge47.2.0、Temurin17.0.21、软件渲染llvmpipe，游戏-Xmx1G/2CPU，Gradle-Xmx512m。原23项JUnit未修改；原20项GameTest断言未删除。最终构建/测试日志见 `evidence/logs/16-final-tests.log`。

|项目|实现|实际验证|状态/限制|
|---|---|---|---|
|49个旧Block|49注册+BlockItem+blockstate/model/lang/loot+创造栏策略|GameTest逐项注册、放置、NBT blockstate roundtrip；资源审计；单人创造栏可见项视觉检查|注册覆盖通过；44 PARTIAL、5 REGISTERED_ONLY，0项宣称完整复刻|
|13组Fluid/FluidType/桶|13source+13flowing+13FluidType+13BucketItem|GameTest逐组桶放置源/验证FluidType/回收；单人创造栏桶显示|基础注册/容器通过；长时流动、混合反应、所有材质视觉未逐一实测|
|慢速运动|motionV2独立调参/.012上限|原JUnit23/29GameTest全部通过；专服QS/SS实际位置CSV|平均速度不是每网络包都严格等于终端速度；重复/批量位置包保留|
|高落入池/底部摔伤/退出|保留B1预移动入口扫掠和有条件摔伤处理|旧MotionGameTests实际猪自由落体、位移、进出和外部摔伤回归通过|B2真实客户端高落三材料完整重跑未做，不借B1结论冒充B2实测|
|泥浆支撑|保留MudGeometry|原浅/深/边界GameTest，专服第二人Mud位置曲线|通过已覆盖样例；混合地形未覆盖|
|SS顶层/下层|.85/1轮廓和模型，空碰撞|GameTest叠层/拆层轮廓及碰撞通过|逐场景鼠标准星视觉检查未完成|
|条件下移|仅QS/SS随机刻单格迁移，水抑制/岩浆硬化|GameTest实际QS一格移动不复制，Mud不下落|SS随机路线、水/岩浆和卸载边界尚未逐例测试；旧调度时序缺口|
|内部放置射线|仅起点单元跳过，其后实体墙/原版reach保留|GameTest从内部clip到实墙通过|真实主手/副手、方块交互拒绝包未人工全测|
|FOV|排除自身UUID重算属性，保留其它modifier/事件比例|编译及客户端加载通过|速度/缓慢/冲刺/飞行/弓/望远镜/第三方组合未完成逐一视觉回归|
|空船/箱船×三材料|独立BoatMotion MODERN_COMPAT；不伪水|GameTest六组合80刻存活、吃水和速度稳定通过|载人箱船和cargo跨重载未测|
|载人船|本地驱动同一浮力，骑手不走旧纠正|真实Dev在SS中停留可见浮动，W划行/A转向后位置变化；服务器Pos日志|小11格试验池驶出后从高空落回平坦地面，不能把该Y下降算“池内沉船”；QS/Mud载人边界未测|
|原生空气/单结算|native airSupply共享下限，核心禁止vanilla同tick补/耗气；原16刻伤害时钟|GameTest共享水侧剩余7→6及重复调用不再耗；真实QS最终溺水；Mud原生气泡149/300可见|水↔流沙完整切换、Respiration与多模组叠加未实测|
|水肺|hasWaterBreathing抑制耗氧/伤害|真实专服Mud深埋水肺约10秒空气300，清除后299/294持续下降|水肺已测；其它免疫组合未逐一验证|
|相机遮挡|按实际相机位置/材料高度画原版纹理遮挡|真实第一人称QS/Mud内外观察；退出恢复|多第三人称相机模组未覆盖|
|脏污|持久残留+定期/追踪S2C同步；人物/标准盔甲/左右手层；水雨洗|真实手臂/人物/铁胸甲显示；原NBT/生命周期测试；新增exemptEntityStillWashesCosmeticResidue通过|最后清洗修正未重启双客户端视觉复测；自定义盔甲、主副手工具组合与脏污跨重登未完整覆盖|
|声效/泥泡|中央16刻节流、SoundEvent原版fallback、动作粒子|客户端资源加载无MFQM缺音错误，代码构建/GameTest服务器运行|ALSOFT_DRIVERS=null，无真实音频听验；动作/环境泥泡外观未人工验证|
|真实专服+2客户端|独立Server/Dev/Observer|双方成功登录，同期SS/Mud状态服务端日志；200/400行实际位置CSV|无人工延迟注入/B2 TPS负载测试；有环境Can't keep up警告，不宣称稳定20TPS|
|真实单人|集成服加载保存的试验世界、创造栏和桶模型|实际加载，复制的死亡角色复活，检查MFQM页/桶，保存返回标题|仅冒烟；不是全矩阵单人测试，也不是空白世界新建测试|

## 真实曲线摘要

详见 `evidence/trace-summary.csv`。QS站立199服务端刻下降1.249994格；SS站立独立双人场景199刻下降1.575478格；Mud399刻下降1.31格后受现有几何支撑。SS另一段已骑船，不能与站立曲线混用。CSV是服务端收到的位置采样：重复值/批量更新可导致相邻样本差异超出单次客户端控制速度，不能据平均数证明每个客户端tick均有界。

## 原始失败也保留

06/07：新流体注册RegistryObject泛型编译错误，已改显式类型；08后通过。11/12/13：shell直接启动无可用桌面授权/显示环境，GLFW失败；14/15从桌面终端重启后成功。日志内Yggdrasil密钥获取失败、userdev本地登录警告、Forge版本提示和环境卡顿均保留，不按模组功能失败或测试通过忽略。

真实GUI阶段运行 `53ad311`；其后仅补充 `SinkEngine.decayResidue` 创造/免疫清洗路径及其GameTest，再运行最终29项GameTest和构建。交付JAR包含这项修正；未声称对最后JAR重做完整GUI矩阵。
