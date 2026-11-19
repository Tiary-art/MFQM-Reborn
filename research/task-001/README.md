# MFQM Reborn — 任务001交付

六份报告在 reports/，审计证据在 evidence/。本次仅只读逆向研究与移植设计：没有新版工程、构建、发布或贴图重绘。

## 阅读顺序

1. 01_jar_inventory.md：原JAR、依赖、资源及完整路径清单。
2. 02_physics_and_player_state.md：物理、污泥、氧气、死亡/清理与证据。
3. 03_registration_and_network.md：92处方块/物品注册调用、16处mod实体注册、13种流体与三种消息。
4. 04_texture_inventory.csv：162张方块PNG，原尺寸、48份动画元数据、图标/渲染引用和可确认映射。
5. 05_porting_plan_1.20.1_forge.md：架构与阶段验收，未启动任务002。
6. 06_rights_and_provenance.md：权利与来源待核查项。

## 校验结果

原JAR 1,644,655字节，484个ZIP条目。分析前后SHA-256完全一致：

`2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`

全部ZIP文件CRC校验通过，161个class均已输出字节码。evidence/audit.json记录核验结果。

## 证据说明与限制

bytecode.txt给出原class的SHA-256、方法描述符、十进制指令偏移、常量引用。analysis.txt为CFR反编译分析文本；不声称是原始Java源码，也不是新版实现。报告中的事实与推测/待验证项分别标注。

原Mod未执行，未搭建旧版游戏或专服，因此运行时注册成功、净下沉轨迹、兼容依赖启动、资源加载和多人行为尚未实测。CustomWorldGen的五个方法存在CFR结构恢复告警，见decompiler_summary.txt。

CSV使用UTF-8 BOM，便于表格工具打开；保留大小写/空格和原始mcmeta JSON。`square_frame_capacity`只是按默认方帧整除所得容量，不是显式frames顺序长度或已验证的实际播放帧数。Mucus_Flowing.png的32×304必须进一步测试，不能改当静图。

04的未解决项：部分文件仅有资源证据，状态/用途未确认；部分实体直接使用blocks目录中的图；missing_icon_resources.csv列出精确图标调用路径缺失候选，不能据此断言游戏已崩溃。下一步先收集旧加载日志和atlas，保留所有原文件。

完整研究包包含反编译分析与语言/元数据，不附原始JAR、PNG、OGG或分析工具二进制。仅供项目内部核查，未经许可不据此对外再发布。
