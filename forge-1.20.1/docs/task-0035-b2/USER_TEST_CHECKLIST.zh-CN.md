# 25–30分钟候选复测清单

请使用全新/已备份测试世界，Forge 47.2.0、MC 1.20.1、Java17，客户端和专服都装同一候选JAR。开作弊/OP。开发测试命令会重建坐标原点附近11×11池子，请不要在正式建筑旁运行。新配置是世界serverconfig/mfqm-server.toml的motionV2，旧motionCandidate不再控制运动。

|时间|步骤/命令|预期|记录|
|---|---|---|---|
|0–3分|创造栏MFQM Materials检查分类；`/give @s mfqm:quicksand`、`/give @s mfqm:soft_quicksand`、`/give @s mfqm:mud`、`/give @s mfqm:bog_bucket`、`/give @s mfqm:acid_bucket`；矩阵附49个ID|均有名称/物品图，无紫黑；桶图暂为原版水桶，区别看名称|截图及缺失ID|
|3–6分|`/mfqm trial quicksand still`，20秒站立；然后`/mfqm trial soft_quicksand still`和`/mfqm trial mud still`|缓慢下沉，不锁Y；三者速度/泥边支撑有区别；motionV2上限.012方块/刻|`/mfqm status`，CSV|
|6–9分|各材料`/mfqm trial quicksand fast_fall`（替换材料ID）；移动、连续按跳跃、脱离池后自然跌落|入池穿入被耗散、无高频上下纠正；挣扎更快下沉；离开后仍有原版摔伤|不要仅靠服务端速度值判断，观察位移|
|9–11分|`/gamemode creative`；叠放2层soft_quicksand再拆顶层；给quick/soft下方留一格空洞并等待随机tick；泥浆同样设置|SS下层1格、顶层.85，准星吻合、可以陷入；两沙偶发下移，Mud不因该规则下落|模型、轮廓、碰撞分别记录|
|11–14分|三池分别`/summon minecraft:boat 0.5 65.1 0.5`及`/summon minecraft:chest_boat 2.5 65.1 0.5`；右键上船，前进/转弯/靠岸/下船；箱船放物品再重进|船浮在表面、可划行；玩家下船仍能陷落；物品保存|特别记录载人靠岸/边界抖动|
|14–17分|`/mfqm trial quicksand deep_oxygen`；看原生气泡条，用`/effect give @s minecraft:water_breathing 20 0 true`；再去水池|气泡减少、退出恢复；水肺期间不消耗/伤害；水↔流沙不能额外获得第二份300空气或双伤害|最后一泡、伤害间隔和水切换|
|17–19分|头埋入并切F5，走出/水洗；`/give @s minecraft:iron_chestplate`穿戴，切换左右主手|相机在材料内才遮挡；玩家/标准盔甲/空手有独立污渍；水雨洗掉；不更换全局皮肤|手持工具/自定义盔甲若不显示列未兼容|
|19–21分|流沙中主手及副手持方块，尝试往邻接合法面放置；隔墙目标、超距目标也尝试|起点不被自身单元拦截，实墙与原版reach仍限制放置|主/副手成功与失败都记录|
|21–23分|普通FOV、冲刺、速度/缓慢药水、飞行、弓、望远镜，进出池对比|仅抵消MFQM减速产生的镜头缩窄；其它正常FOV变化保留|第三方FOV模组另测|
|23–25分|桶放置/回收Bog/Honey/Tar/Acid等；红石激活sandstone_trap；主手/移动/挣扎声效；泥浆泡泡|真实流动源和回收；流体可有保守统一速度；陷阱转QS；动作声有预算不连爆|不能把桶存在当完整流体恢复|
|25–30分|专服两人同时进不同材料，旁观污渍，重连/跨维度/死亡；保存退出再重开49方块测试区|注册/状态持久；服务端权威空气与脏污；无崩溃/残留减速|提交两端latest.log、mfqm-traces和复现步骤|

人工观察不通过请保留原始日志；未运行的格子写“未验证”，不要据此填“通过”。Larvae/Lure/Blossom/Meat/Gas等REGISTERED_ONLY缺口已知，不应按完整功能验收。
