# Phase 9 完成报告

总体 **PARTIAL**。核心默认材质已恢复到私有构建并进入真实 Forge 开发客户端验证；并非全部原版素材、渲染器和 metadata 已移植。公开 JAR 有意保留 vanilla 占位，不宣称包含原版材质。

输入基线 `6a44d6f7f0403dfce67f597c8fc6b5edd5911317`（main，Phase8 补交已合并）。实现源码提交 `0229831`；后续提交扩展只读审计工具并补报告、日志和交付，运行时代码不变。环境 Linux / Java 17.0.21 / Gradle 8.1.1 / MC 1.20.1 / Forge 47.2.0。原始日志时间为 UTC；报告编写日期为 2026-11-19（北京时间）。

| 项目 | 状态 | 实际结果与证据 |
|---|---|---|
| 原版输入及只读保护 | PASS | 原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`；导入前后未变；路径由参数/环境变量提供 |
| 全资产清点 | PASS | 300 项：247 PNG、48 mcmeta、2 OGG、3 其他；完整大小写、哈希、尺寸、透明信息、动画元数据见 ORIGINAL_ASSET_INVENTORY.csv |
| 逐项映射 | PARTIAL | 167 行映射，38 CONFIRMED 纹理用途覆盖 25 注册 ID；13 流体辅助模型几何 PARTIAL，113 UNRESOLVED，3 vanilla 继承设计项仍部分待核；见 TEXTURE_MAPPING.csv |
| 私有导入工具 | PASS | 原始 PNG/mcmeta 不重编码；88 个生成文件、36 个独立 PNG；幂等、干运行、校验、受控清理、编辑保护、符号链接保护实测 |
| 核心实际显示 | PASS（限定范围） | quicksand、mud、soft_quicksand 世界及物品栏；acid、bog 世界流体。已肉眼查看私有截图，不只是解析 JSON |
| 其他材质显示 | PARTIAL | leaves_pile 的烘焙面/粒子绑定已验证，透明度未单独肉眼验收；其余已映射 ID 未逐个进场景；桶、旧变体、多面特殊渲染未完成 |
| 动画及重载 | PARTIAL | acid atlas still/flow 12/8 帧、bog 32/16 帧；12 次实际客户端捕获，程序调用 reloadResourcePacks（F3+T 等效）后正确；未逐帧核对原版时序 |
| 公开无素材构建 | PASS | clean test build runGameTestServer，最终 JAR 校验无 PNG/OGG/私有 marker，46 JUnit + 43 GameTests；公开客户端视觉检查 NOT_RUN |
| 私有构建 | PASS（本地） | clean test build 成功；最终 reobf JAR 的全部 88 个生成条目哈希已验证；真实客户端为开发类路径，不宣称已在正式启动器安装最终 JAR |
| 专服及回归 | PASS（现有覆盖） | 基线与候选实际运行 43/43 GameTests，候选干净构建 46/46 JUnit；基线 JUnit 沿用 UP-TO-DATE XML 46 项；私有专服实际连接客户端、正常 stop 保存；无客户端类链接崩溃 |
| 历史交付审计 | PASS（可取得证据） | 1062 行、16 份清单共 1950 条哈希全匹配，16 个可访问历史工作树未发现未跟踪项目文件；详见审计报告 |
| 公开/私有分发边界 | PASS | 原 JAR、原 PNG/音频、私有 JAR、截图均忽略且未提交；PRIVATE_ARTIFACT_NOT_DISTRIBUTED |
| Windows/整合包/其他资源包实机 | NOT_RUN | Linux 小写路径和引用自动检查通过；不以此声称 Windows 或整合包已测 |

25 个已建立纹理绑定的 ID：acid、bog、chocolate、corrupted_sand、dense_webbing、dry_quicksand、h_peat、honey、jungle_quicksand、leaves_pile、liquid_chocolate、liquid_mire、moor、mucus、mud、quicksand、sinking_slime、sinky_liquid、slurry、soft_quicksand、soft_snow、solid_honey、stable_liquid_mire、swallowing_flesh、tar（均为 `mfqm:`）。**绑定确认不等于全部视觉验收。**

普通流沙引用原 `quicksand.png`，泥浆引用 `mud.png`；松软流沙默认旧 metadata0 根据 getIcon 明确引用 `SoftQuicksand1.png`。现代 FILLED 只是同一材质的几何状态，不冒充旧 metadata1/2。外部模组维度泥浆纹理、特殊世界 SoftSnow 变体仍未覆盖。流体 world still/flow 原像素接入并取消私有模式的额外染色；桶图标仍为 vanilla 水桶，方块物品 cube 几何不宣称与原版一致。

源码差异检查见 evidence/source-regression.json：已有源码只改 LegacyFluids.initializeClient 的纹理取值与私有材质染色；新增两个仅客户端类。物理、注册、网络、世界生成、现有测试和公开模型资源与基线字节一致，未改现有玩法开关。Phase8 限定普通流沙非玩家自动碰撞仍为 PARTIAL；本阶段没有完成玩家自动接触、全部材料物理、完整垂直物理或自然生成。

最终产物及完整 SHA 见 ARTIFACTS.json、deliverables/phase9/BUILD_VERIFICATION.zh-CN.md。公开 ZIP 含公开 JAR 与本地私有构建入口。私有原素材授权不明确，未公开提交私有 JAR；最短操作见 USER_TEST_GUIDE.zh-CN.md。

日志保留了真实异常：离线鉴权连接失败、原版警告和基线的 config tracker 清理错误不隐藏；GameTests 仍全部通过、Gradle 正常退出。开发客户端捕获完成后人工终止/关闭 Xvfb，runClient 因此非零，不记作干净退出 PASS。早期 75 文件构建日志已被最终 88 文件构建取代，保留用于溯源。测试边界见 TEST_MATRIX.md。阶段至此停止。
