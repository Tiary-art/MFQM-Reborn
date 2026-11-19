# 范围、来源和证据等级

本轮任务为原始文件研究，不继续修改1.20.1的运动、贴图或玩法，不推进Task004，不更新/合并B2 PR。时间2026-11-18（北京时间）。附件自身是一份带有既有结论的研究任务书；本轮把这些结论当作待核对命题，重新查原始JAR，而非当作原作者源码。

## 输入

|输入|本轮实际使用情况|
|---|---|
|原始MFQM 1.1.1 / 1.7.10 JAR|用户此前上传件，1,644,655字节；SHA-256 `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`，前后相同|
|Task001研究|使用B2仓库research/task-001中的文本；另对原JAR重新javap全部类，重新CFR解包；13个优先类的CFR文本与Task001逐文本一致|
|B2实现|本地分支task/0035-b2-consolidated，提交03a6a20354bb98174a970754293411b3a7197970；未假定它就是附件提到的ZIP|
|MFQM-main (5).zip|本轮未提供/未找到，不能宣称逐字节核对该ZIP；B2对比只针对上述提交|
|MFQM_Original_Texture_Catalog.zip|本轮未提供/未找到；直接清点原JAR资源，不等待素材包，也不以Minecraft原版图冒充原图|
|1.7.10官方客户端及MCP SRG|为核对旧Biped UV和相机射线链，读取官方客户端并校验官方SHA-1，配Forge Maven的MCP1.7.10 SRG；仅静态外部参考，不是启动旧游戏；URL/hash见evidence/external/provenance.json|

原JAR实际为484个条目、463个文件、161个class、247张PNG，其中162张位于textures/blocks；48份mcmeta、2份OGG。**162是方块PNG数，不是全部纹理数**。

## 已完成的证据工作与边界

- 161/161类、1955个声明方法结构索引（包括构造器/静态初始化器）、29276个invoke调用位置、14169个跳转位置。结构来自本轮javap原字节码；异常表保留在原始文本。
- 49个可证实旧Block注册对象的逐项行为存在性索引；实际算法仅优先深入三核心。`source_has_*`只表示本类源码有该调用，不等于继承后的完整行为或游戏实测。
- 三核心39条人工核对的主要运动阶段/深度分支；全部嵌套条件、兼容实体分支尚非逐条解释完成。80个相关World RNG消费调用点保留偏移/上下文，供后续精确重放。
- 20张污渍遮罩的尺寸、alpha统计、UV区覆盖与逐级像素差；33个污渍类型的颜色/默认参数/遮罩族表；13个重点类二次CFR比对。
- 10项独立Java算术检查通过，验证NaN转int及打包操作等；这不是执行原模组、不是原版GameTest，更不是净轨迹数据。

## 状态定义

`VERIFIED`只用于归档/指令/像素/算术直接支持的窄结论；`PARTIAL`为路径已读但外部依赖、全部分支或运行效果未闭合；`UNKNOWN`没有充分解释；`NOT_PORTED`用于已识别但未恢复的旧实体/TileEntity链。结构验证、语义验证、运行验证和移植状态是不同列。调用图只保存字节码声明目标，未解析所有虚调用、继承目标、反射和Forge事件调度。

不能把“161类已反汇编”写成“161类1955方法都已语义还原”。CFR输出158份Java（内部类可并入外类），CustomWorldGen的5个方法报告Unable to fully structure code；完整错误摘要保留。

本轮**未启动1.7.10 Forge客户端/专服**，没有原版逐tick曲线或录像。本轮取得的官方客户端JAR仅供静态读取，仍缺旧Forge运行/测量环境及插桩链。原版净速度单调性、RNG跨tick路径和旧事件顺序均不能据此标成已测。

文件导航：classes.csv / methods.csv / calls.csv / branches.csv / methods-with-instructions.json可机器查询；evidence/bytecode保存逐类原字节码，evidence/source为重点CFR分析文本。附录保留SRG字段，不把反编译局部变量名当原作者命名。

本文worldTime统一指原代码的world.func_82737_E()时钟；测量时应同时保留该原始总tick值与日夜时间，勿用现代时钟名称自行替换。

注册计数另核对：全JAR有50个GameRegistry.registerBlock调用点，49个位于MFQM.preInit，另1个位于通用CustomRegister.registerBlock包装方法；本JAR内未见对该包装方法的声明调用。CustomRegister对象本身有构造调用，但构造不等于执行registerBlock。因此49材料索引是已识别注册条目，不把包装器当第50种材料，也不把静态清单称为运行时registry dump。见registrations-from-bytecode.csv。
