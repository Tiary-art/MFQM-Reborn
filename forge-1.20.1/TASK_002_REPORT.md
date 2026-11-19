# MFQM Reborn 任务 002 完成报告

日期：**2026-11-18（Asia/Shanghai）**。日志由宿主按UTC记时（2026-11-17 16:46起，对应上海次日00:46起）。

## 结果与范围

已创建并实际构建 Minecraft 1.20.1 Forge 最小工程。模组入口、共同侧注册、客户端独立生命周期、开发方块及对应BlockItem、创造栏入口、blockstate/model/item model、英文/中文语言、掉落表和GameTest均已接通。

本任务不是流沙系统移植完成。physics/state/network/worldgen/rescue只保留包边界，不注册流体、旧药水、生物、救援工具、生成器或自定义消息，不复制反编译源码。任务001研究目录保持原样。

默认开发方块 `mfqm:dev_test_block` 是普通固体Block，外观引用Minecraft沙纹理（16×16），没有重力沙或陷落行为。名称明确标为开发测试，不误称原版Quicksand。没有生成AI贴图、重绘、缩放旧PNG，也没有修改原JAR。

## 精确版本

| 项目 | 本次版本 |
| --- | --- |
| Minecraft / mappings | 1.20.1 / official 1.20.1 |
| Forge / MDK | 47.2.0 / 1.20.1-47.2.0 |
| ForgeGradle | **6.0.24**（精确锁定） |
| Gradle wrapper | **8.1.1**，含distributionSha256Sum |
| Java | **Eclipse Temurin 17.0.21+9**，toolchain与release=17 |
| modid / namespace | `mfqm` |
| 模组工作名称 / 开发版本 | More Fun Quicksand Reborn / `0.0.2-dev` |
| 基线提交 | `35c9e38`，任务001 PR #1已合并后的main |

MDK及JDK下载来源和SHA-256见 [docs/toolchain_provenance.json](docs/toolchain_provenance.json)。没有发现现有mfqm注册冲突；不声称已检查所有外部Mod组合。

## 已执行的验收

| 检查 | 实际结果 | 证据 |
| --- | --- | --- |
| Java17 Wrapper版本 | PASS，Gradle8.1.1 / JVM17.0.21 | logs/task-002/05-toolchain.log |
| 初次完整build | PASS，exit0，含reobfJar | 02-build-proxy.log |
| 最终clean build | PASS，exit0，生成测试JAR | 14-final-clean-build.log；最终复核见19-final-build.log |
| 真实Forge GameTest | **1/1 required测试通过**；BlockItem关联、世界内放置、掉落表确实执行 | 09-gametest-fixed.log，`All 1 required tests passed` |
| 客户端启动 | PASS，主菜单/Mods显示mfqm、0.0.2-dev；正常退出exit0 | 10-run-client.log；截图01 |
| 单人进入世界 | PASS，创造、超平坦、seed4242002，世界名MFQM Task 002 Smoke Test | 10-run-client.log；截图02 |
| 单人获取与手动放置 | PASS，`/give @s mfqm:dev_test_block 4`，右键实际放置；F3目标为mfqm:dev_test_block | 10-run-client.log；截图02 |
| 默认贴图显示 | PASS，方块及物品均显示Minecraft沙纹理，无紫黑缺失贴图 | 截图02/03，JSON引用检查 |
| 专服启动 | PASS，真实forgeserveruserdev，输出Done；无client类在专服加载崩溃 | 12-run-server-eula-accepted.log、18-run-server-stdin-fixed.log |
| 专服控制台正常停止 | PASS，转发stdin后输入stop，世界保存完成、Gradle exit0 | 18-run-server-stdin-fixed.log |
| 专服客户端连接 | **PASS，仅回环地址的离线开发联机**；Dev在服务端登录，客户端记录Connected to a modded server | 12-run-server-eula-accepted.log、10-run-client.log、截图03 |
| 专服创造栏物品 | PASS，联机世界搜索mfqm显示开发测试方块 | 截图03 |
| 静态资源/产物检查 | PASS，资源引用、语言/掉落、162行映射、48份元数据、无资源路径重名、class版本61 | 16-final-artifact-validation.log |
| 私有资源包生成工具 | PASS，对默认quicksand和异常Mucus_Flowing分别生成到git忽略目录，逐字节保留PNG/mcmeta，未进游戏启用 | 04-private-pack-tool.log、13-private-anomalous-texture.log |
| 原始JAR与PNG完整性 | PASS，SHA256不变、CRC通过、247张原PNG与任务001哈希全部一致 | 17-integrity-audit.json |
| 任务001资料未改动 | PASS，原SHA256SUMS全部通过、git无研究目录修改 | 17-integrity-audit.json |

**限制**：build中的常规`:test`为NO-SOURCE，不算JUnit测试通过；实际游戏测试是独立执行的GameTest。运行与图形检查基于Gradle开发环境，未把测试JAR装入独立正式启动器再测；Windows/macOS、正版账户在线认证、跨设备/公网、双客户端、多Mod兼容和长时性能均未实测。没有开启旧贴图资源包在游戏内测试；Mucus异常动画的现代兼容性未验证。未提供旧版与新版流沙曲线比较，因为本任务没有流沙物理。

## 真实失败、修复与环境信息

- `00-gradle-version.log` / `01-build.log`：Java首次直连Gradle下载站被拒绝。云环境要求代理，但Java不会自动使用http_proxy。配置**私有**Gradle用户代理与系统信任库后下载/构建成功，未关闭TLS验证，未把代理凭据或环境路径写入工程构建配置。命令见docs/ENVIRONMENT.md。
- `06-gametest.log`：首个测试注解使用带冒号的模板串，被Forge加上mfqm命名空间后得到非法路径`mfqm:forge:empty3x3`，导致测试服务器崩溃。改为本工程独立创建的`data/mfqm/structures/empty3x3.nbt`和template=`empty3x3`后，09日志证实1/1通过。这个NBT是新建的空测试结构，不是旧Mod素材。
- `08-gametest-fixed.log`：一次脚本在错误工作目录调用`./gradlew`，exit127；09从正确项目目录重新执行。保留这份短失败日志，不将其伪装为游戏失败或通过。
- `11-run-server.log`：首次专服停在EULA，虽然Gradleexit0，**当时服务端并未完成启动**。用户在会话中明确阅读并同意后，才在被忽略的本地run目录设置eula=true，继续实际验证；工程不携带EULA接受文件。
- 12中的`No key layers in MapLike[{}]`来自本次超平坦测试server.properties缺少generator-settings层定义，服务器使用回退配置后完成启动。现已提供完整层JSON的本地测试配置样例，后续18启动无此错误。这不是MFQM资源缺失。
- 12/15的进程最终退出143：测试结束时通过SIGTERM触发Minecraft保存世界的shutdown hook，Gradle据此报告FAILED/exit1，**不是启动或联机失败，也不是exit0正常停服**。复核发现JavaExec默认未转发控制台stdin，现已在build.gradle显式转发runServer标准输入，18已再次实测`stop`命令，服务器保存全部维度并正常退出，Gradle BUILD SUCCESSFUL / EXIT_CODE=0。
- 日志中的Yggdrasil公钥请求失败/聊天签名不可验证来自此云环境未具备真实登录会话及认证服务连接；本次专服仅绑定127.0.0.1，online-mode=false，用于开发握手验证，不能据此宣称正版认证已通过。样例配置明确限定本地开发用途；不要直接当公开服务器配置。
- OpenAL/ALSA提示无可用音频设备，客户端自动关闭声音。画面和交互已实测，**声音未验证**。shader Sampler2提示与Forge union资源schema、加载器内部JAR缺mods.toml提示均发生在框架/原生资源路径；MFQM模型/贴图未出现缺失日志，已通过实际画面与资源图验证。Forge首次自动补全默认配置的警告已保留。
- Forge版本检查提示较新47.x存在；本任务锁定的是实际验证的47.2.0，未声称验证其他47.x。Gradle9弃用提示不影响已锁定的8.1.1，未升级到9。
- 桌面控制曾有一次300秒超时，恢复后通过实际窗口及双端日志确认联机成功；未用超时前的点击当成完成证据。

## 资源与授权处理

[docs/texture_mapping_draft.csv](docs/texture_mapping_draft.csv)准确记录162张旧方块PNG的原路径/原文件名大小写、原尺寸、mcmeta存在性/路径/内容、预定现代小写路径与接入状态。全部`integrated=false`，不存在小写转换重名；48份动画设置保留。`Mucus_Flowing.png`保持32×304，未裁剪或改帧。

公开src资源没有PNG/OGG；测试JAR同样不含旧图片/音频。仅引用游戏自带的沙纹理，占位不涉及旧作者素材再分发。docs/screenshots是运行证据，不是纹理资源。私有工具只在操作者本机读取校验后的原JAR，把**单张选定**图片与元数据原样复制到private-resources；不会一次塞入162张，也不写入src，gitignore和交付排除项已检查。工具生成成功不代表贴图加载或动画兼容已通过。完整用法见README。

原JAR分析前后SHA-256：

`2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`

最终测试JAR SHA-256：`8f0920eccaad748d002d28e455599c68a5ff6ca95c38c27cdcec3c821b0ac0fc`。最终两次clean build在此环境所得JAR哈希一致；不据此推断其他平台逐字节一致。

## 修改文件清单

完整逐文件路径/大小/哈希见 [docs/task002_file_manifest.csv](docs/task002_file_manifest.csv)。主要分组：

- 工程：build.gradle、settings.gradle、gradle.properties、gradlew/gradlew.bat、Wrapper JAR/properties、.gitignore、MDK_LICENSE/CREDITS。
- Java：MfqmReborn、registry/ModBlocks/ModItems、client/ClientLifecycle、各模块package-info、gametest/FoundationGameTests。
- 资源：mods.toml、pack.mcmeta、blockstates/dev_test_block、block/item models、en_us/zh_cn、loot table、empty3x3测试结构。
- 工具与文档：tools/verify_project.py、tools/private_legacy_pack.py、README、TASK_002_REPORT、docs/ENVIRONMENT、版本来源JSON、映射草案、本地服务器配置样例、三张截图、构建测试日志。
- 仓库首页新增任务002导航；.gitattributes对原样日志/CSV及上游MDK通知/Wrapper脚本保留空白，新写Java与构建代码仍接受空白检查。
- 测试产物位于仓库deliverables/task-002/，是开发测试JAR，不是完整移植发行包。

## 复现与任务003前置条件

从工程目录使用JDK17运行 `./gradlew --no-daemon --console=plain clean build`、`runClient`、`runServer`、`runGameTestServer`；静态检查执行`python3 tools/verify_project.py build/libs/mfqm-reborn-0.0.2-dev.jar`。详细单人、专服、EULA、命令获取、私有贴图加载步骤在README；云环境代理细节在docs/ENVIRONMENT.md。

任务003需另行授权。开始前应确定三核心材料的坐标/表面定义、服务端权威与每实体每tick聚合规则、状态Capability/NBT版本与重生清理、氧气与伤害时序，补旧版1.7.10实测轨迹基线和对照矩阵。旧状态打包溢出、String引用比较和非有限网络值等不作为新版必须复制的行为。素材使用权、手绘风格/分辨率及最终映射仍待单独确认；当前基础工程不承诺自动兼容旧存档。
