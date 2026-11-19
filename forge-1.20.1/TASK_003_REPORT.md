# MFQM Reborn 任务003交付报告

日期：2026-11-18（北京时间）。基线为已合并任务002的最新 `main f9a6fc7`，开发分支 `codex/mfqm-task-003`。目标 Minecraft1.20.1 / Forge47.2.0 / Java17 / modid `mfqm`；Gradle8.1.1、ForgeGradle6.0.24未改变。测试JDK为Temurin17.0.21+9。开发版本 `0.0.3-dev`。

**交付结论：三核心材料的近似机制、服务端状态/耗氧/伤害链路、自动化回归、单人和一次真实专服连接已实现并测试。没有取得1.7.10实机轨迹，不能称原版数值完全恢复。动画、旧覆盖视觉及下文忠实性缺项仍未完成/未验证，不能以本报告冒充全部旧版功能完成。任务004未开始。**

## 交付导航

- [源码及构建说明](README.md)、[本任务重现步骤](docs/task-003/REPRODUCE.md)、[设计与公式](docs/task-003/DESIGN.md)。
- [原证据→实现→差异→测试追踪表](docs/task-003/EVIDENCE_TRACEABILITY.md)。先核对任务001的物理、移植计划、三材料analysis/bytecode、CustomVarPlayer、AirEvent、PotionStuck、CustomPotionEvent和MFQM；没有复制CFR反编译源码。
- [24项单人场景矩阵](docs/task-003/SINGLEPLAYER_MATRIX.md)、[阶段2统计](docs/task-003/phase2-summary.json)、[最终单人统计](docs/task-003/final-singleplayer-summary.json)、[最终专服统计](docs/task-003/final-dedicated-summary.json)、[逐tick原始CSV](docs/task-003/traces)。
- [完整日志目录](logs/task-003)、[默认纹理实机截图](docs/task-003/screenshots)、[开发测试JAR](../deliverables/task-003/mfqm-reborn-0.0.3-dev.jar)。完整仓库源码可由本分支下载ZIP；私有原始JAR、旧PNG/OGG、游戏运行目录及私有纹理截图均不在源码包内。

## 已实现与实际验证范围

| 项目 | 已实现 | 自动化 | 实际游戏 / 边界 |
| --- | --- | --- | --- |
| 三独立方块/BlockItem、稳定ID、创造栏、独立模型/名称/掉落 | 是，quicksand / mud / soft_quicksand | live GameTest放置、取物、掉落通过 | 三默认模型实际显示；私有原始静态纹理另测 |
| 普通流沙 | 横向清零、深度浮力、运动惩罚、挣扎吸力 | 纯函数与真实Pig逐tick通过 | 静止/行走/跳/连跳/快速落入/中心/边缘/单层/多层均有CSV |
| 松软流沙 | 0.71阻尼、独立浮力、深区中心环带牵引、0.85表面 | 参数/环带/真实Pig牵引通过 | 上述8场景实测；玩家准确中心起步时牵引为0，不能仅凭该样本证明偏心牵引 |
| 泥浆 | 八邻、±2/±3、液体、安全边缘、深度0..3和0.7/0.5/0.25/空碰撞 | 几何分支JUnit和世界shape/中心边缘GameTest通过 | 中心与安全边缘支撑不同；深处眼部覆盖另有耗氧/退出记录 |
| 每实体每tick一次结算 | 服务端LevelTick END + 维度/tick守卫；按体积确定主材料 | 同种多格/混合材料、多次主动调用、伤害时钟均通过 | CSV tick唯一，settlements增量等于tick增量；未见非有限值 |
| Capability/NBT/属性清理 | 短期状态不保存；版本化残留字段；单一自有TransientModifier | 真实体NBT保存/重载、死亡/移除、外来modifier保留、免疫模式、句柄失效/重建通过 | 实际死亡/点击重生、换维度再陷落、活跃保存退出/重进、离池后状态清理通过 |
| 氧气/伤害 | 眼部独立；默认300、覆盖−1、离开+5；耗尽后16tick一次伤害请求 | 默认配置链路及重复调用守卫通过 | 实际耗氧、伤害/溺亡、三材料指令退出恢复通过；非默认开关/倍率未实测 |
| 网络/显示 | S2C只读快照、C2S仅boolean挣扎、HUD | dedicated可加载，无强制client类加载崩溃 | 真实回环socket连接；280条已发快照全部配对，比较字段零差异；非多人观众/高延迟验收 |
| 任务002回归 | dev_test_block及原测试保留 | 原FoundationGameTests仍通过 | 历史报告/日志/JAR、wrapper和任务001研究未改 |

18项JUnit（SinkMath14 + MudGeometry4）、15项必需GameTest（原foundation1 + 本任务14）最终全部通过，无跳过。GameTest的玩家模式/Clone/维度事件使用无socket玩家fixture，**这些fixture不等同真实客户端测试**；实际单人/专服分别补测并保留日志。

## 实机记录与问题修复

测试世界为独立超平坦、命令开启；trial建立显式测试池而非自然世界生成。walk实际按W约2.5秒；jump按Space约0.12秒；hold_jump按住约3秒，CSV分别观察到2–3行和约59–60行held。每材料8个场景、各200ticks（24项4800行）。Y、水平/垂直速度、immersion、stuck、眼覆盖、air、health、伤害请求、结算次数都在原始CSV，见矩阵。速度是求解器输出，Y是接受的玩家位置，不能混用。

开发阶段分开保存，避免拿旧构建的结果冒充最终复测：

1. **阶段1**：`04-first-client.log`及pre-correction CSV暴露“只发送速度包仍可被玩家位置批处理快速下沉”。没有将该结果算作成功。增加服务端有界位移校正，使用原生传送纠偏包；没有在客户端计算物理或氧气。
2. **阶段2**：`10-corrected-client.log`完成24场景及三材料退出恢复。发现换维度后状态命令无输出；线程转储显示服务器在正常tick等待，并非死锁。根因是Forge复用ServerPlayer并revive外层dispatcher时，内部LazyOptional已永久失效。新增句柄重建及独立GameTest，旧失效句柄保持无效。`14-dimension-thread-dump.txt`只记录jcmd被沙箱拒绝；实际SIGQUIT转储在10日志中，不能将失败jcmd说成成功诊断。
3. **最终构建**：`15-final-clean-build-gametest.log` clean build + 18 JUnit + 15 GameTest成功（2m39s）。`16-final-client.log`重新启动最终字节码，完成活跃换维度→下界状态none/air300/stuck0→返回再陷落；活跃保存退出时air122，重进首个生理tick重新从299扣减，未延续旧气息/stuck存档。最终物理求解器与阶段2矩阵相同，最终仅修复Capability句柄；没有虚称最终构建重新做过全部24项。
4. **真实专服**：`17-final-dedicated.log`启动成功，客户端日志03:34:57 UTC连接127.0.0.1:25565，03:35:00记录真实socket登录；测试普通流沙中心、Mud边缘、Soft深区与按键、Soft指令退出、活跃状态/kill及点击重生。03:37:26客户端status为none/depth0/air300/stuck0/eyefalse/contacts0。03:37:42正常断开，服务器收到stop后保存退出。仅回环offline开发联机，未验证正版认证、公网连接或高延迟；沿用任务002用户已接受的Minecraft EULA。

快照统计见[20-final-dedicated-sync.json](logs/task-003/20-final-dedicated-sync.json)：服务端280、客户端282（额外2条login/respawn的syncTo没有服务端trace记录），280条公共UUID/tick键全部相等。比较material、wire float immersion、air、stuck、settlements；没有把眼标志/维度字段的线缆值、丢包/观众跟踪或恶意客户端测试也算成通过。

三材料的指令辅助退出发生在：Quicksand tick19517首air127→19552满300（35ticks）；Soft tick19993首168→20020满300（27ticks）；Mud tick20454首138→20487满300（33ticks）。首个无接触记录stuck均0，之后每tick+5（末步封顶）。这是 `/tp` 退出后的恢复延时，**未测得自主逃脱时间，不能填0或声称可自行逃脱**。最终专服也观测到clear状态回满300。

## 资源与完整性

公开src和JAR中PNG/OGG均为0；只引用Minecraft sand/mud/red_sand，保留16×16美术风格，没有AI生成、重绘、放大或重新编码旧图片。

原始JAR只读且SHA256仍为：

```
2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b
```

247张原PNG逐项与任务001archive_entries.csv SHA256一致。发行测试JAR没有任何条目与原JAR文件hash相同，见[21-final-integrity.json](logs/task-003/21-final-integrity.json)。原研究、任务002报告/原测试/wrapper的git diff为空。没有提交未授权旧素材或修改原JAR。

扩展私有工具`--core`：quicksand.png、mud.png、SoftQuicksand1.png，均16×16，PNG字节逐字不变，原hash见[07日志](logs/task-003/07-private-core-pack.log)。这三个文件本来没有mcmeta，不伪造动画。2026-11-18日志03:32:33 UTC实际重载`file/core-legacy-test-pack.zip`，三块摆放后人工观察均显示对应静态原始纹理；私有截图留在仓库外，不公开。03:33:44已切回vanilla/mod_resources，公开截图15为默认占位。其他带mcmeta条目的复制能力保留，但**动画播放、48条动画、异常32×304均未在本任务验证**。

最终开发JAR：82,974字节；SHA256：

```
0836fca8463a0a7534e113b82728c76ac3371d4fbb56864d610218947cfb27bc
```

## 未完成、未验证与明确差异

- 这是静态逆向证据指导的近似实现。现代深度归一化、净浮力公式、位移预算及混合材料同分优先级是明确的新策略；不复制旧玩家Y偏移、onGround/web伪装、全局64槽、Watcher25或有符号打包溢出。玩家与生物净轨迹可不同；没有旧版轨迹对照。
- 装备/负重/涉水靴、旧随机吸力/声音/气泡、旧特定生物免疫、完整污泥覆盖/洗净视觉、Soft旧metadata多纹理切换没有恢复。残留字段仅持久化最小类型/计时，不冒称有覆盖渲染。
- 氧气玩家/生物开关和伤害倍率配置已实现，但改变开关/倍率的实际游戏组合未验证；当前通过结果为默认值。关闭储气槽仍按眼覆盖16tick请求伤害，是防多次结算的现代退化规则。
- 位移纠偏可能可见；未测高延迟/多客户端/第三方传送与移动模组。Forge传送事件清历史，未知直接位移超过16格不拉回；第三方不发事件的小幅直接传送可能被纠正。保留其他modifier的测试不等于模组生态兼容验收。
- 对超大实体、超过采样边界/16格连续材料列未实测；渲染0.85表面与内部软沙连续列的视觉接缝未完整恢复。生物只用真实Pig代表，未逐个测试所有LivingEntity。
- 已观察到死亡画面可能暂留上一条HUD快照，重生后清除；服务器死亡状态已清理，无永久stuck。此显示细节未作为完整客户端效果恢复。
- 测试环境无可用OpenAL播放设备，日志有音频初始化错误；未验收声音。Forge“缺mods.toml”、版本过时提示、Gradle9弃用提示未当作本任务构建失败，项目版本按要求未升级。
- 没有加入绳索/抓钩、其他材料/生物、世界生成、旧存档转换或任务004内容。

## 构建与失败日志保留

01编译成功；02首次clean build/JUnit17成功；03首次GameTest4失败；05修正后2失败（测试用网络玩家不具备真实Netty管线），随后改用无socket fixture，并保留实际网络测试；06全部14通过；09位移预算后18JUnit/14GameTest通过；15最终18/15全部通过。初次伤害fixture时钟和Mud观察窗口问题也在03/05原日志保留，没有删除失败记录或将其当产品通过。

08/11是较早构建的专服启动，不能作为最终客户端联机证据；最终联机只认16/17/20。18/19为最终默认/核心资源链审计，21为原JAR/PNG/发行JAR完整性。原始日志均可重查，未实际执行的项目没有标为通过。
