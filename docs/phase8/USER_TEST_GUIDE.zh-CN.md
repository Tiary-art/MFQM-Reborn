# 10分钟内的人工验收

仅在备份的一次性世界测试。本轮自动链路只支持**普通流沙内的非玩家生物**；玩家、Dry和泥浆等不会被假装自动恢复。当前画面引用Minecraft贴图，不能称为MFQM原始材质。

1. 用Java17、Minecraft1.20.1、Forge47.2.0与本PR构建的模组，新建开启作弊的世界 `MFQM_PHASE8_TEST`。先退出，复制整个世界目录作备份。
2. 编辑该世界 `serverconfig/mfqm-server.toml` 的 `[phase7]`：设 `stuckLease=true`、`originalQuicksandContacts=true`。要运行诊断/受控Dry命令，再设 `testWorld=true`；要记录详细日志，设 `diagnostics=true`。重新进入。所有开关默认false，不要用于正式存档。
3. 用创造模式摆一层普通流沙并在下面铺石头，放一只猪。猪自然碰撞后应在日志出现 `PHASE8_AUTO ... material=quicksand ... level=...`；不要用hold/contact命令替代这项测试。移走猪或移除流沙后，租约应在下一次服务端结算释放。
4. 在流沙边缘混放泥浆让生物同时接触：该未闭环组合应保持旧路径，不产生猜测的新自动租约。这不是多材料全物理已经恢复。
5. 要看真实玩家的属性/FOV同步，在安全石台上切生存，执行 `/mfqm_phase7 hold 145 100`，然后 `/mfqm_phase7 release`。这是约5秒的**诊断输入**，不是玩家材料自动接入。可在有速度药水时对比，药水效果不应被全局清掉。创造/旁观/无敌/骑乘会清理或拒绝新租约。
6. 可在测试服中做一次死亡重生、跨维度或退出重进，检查没有残留租约。原版空气控制/完整Y下沉与音效仍不能按本轮判定已恢复；若出现视角不适直接回退。
7. 如需Dry：只在已备份的空区域，用 `/mfqm_phase7 dry 0 80 0 5 0`（坐标/旧循环范围extent/seed）。它会改方块；范围-1..18，未加载区块/高度越界拒绝。不会开启自然生成。
8. **一键回退**：执行 `/mfqm_phase7 disable`，关闭自动接触/租约/测试生成入口并立即清理本模组租约。旧运动路径恢复；重新启用需编辑开关并重启世界/服务器。此命令不撤销已写入Dry地形，撤销地形请恢复备份。

日志位置：实例 `logs/latest.log`，查PHASE8_AUTO/PHASE7_CONTACT/PHASE7_STUCK/PHASE7_CLEAR；使用 `/mfqm motion diag 200 manual_check` 可在实例 `mfqm-motion/` 收集有限时长服务端/客户端运动记录（需要同版模组）。请附种子、模式、开关、命令和异常现象；不需要分析Java。
