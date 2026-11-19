# 原版注册入口与对象身份

原 JAR 的 SHA-256 为 `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。类、方法描述符和指令来自 R0 的 bytecode 清单。下文行号来自 CFR 0.152 的编号文本。静态分支的执行情况均没有原版游戏运行记录。

|入口|证据与解释|
|---|---|
|MFQM.preInit|MFQM.analysis.txt 第 593 行进入，第 602–604 行注册消息，第 606 行以 getNextID 创建 tabMFQM。第 954–966 行把 13 个已经构造的 Fluid 实例交给 FluidRegistry。静态初始化第 2711–2723 行以及对应构造函数提供 Fluid 名称。两份 Mire 共用类、构造字符串不同。|
|方块及物品|同一 preInit 内依次构造并保存静态字段，将实例和大小写敏感的文本键交给 GameRegistry。第 968 行 Mud 的 ItemBlock 类是 ItemMud，989 行 Morass 使用 ItemMeta。第 1183–1187 行棕黏土桶和流沙桶各有独立物品对象。桶内携带的 Block 引用没有产生另一次 Block 注册。|
|MFQM.load / postInit|1485、1489 行的事件描述符见方法清单。postInit 扫描可选模组的实例和 ID。1835–1855 行 BoP 存在时尝试附加冶炼，缺席时显式注册 Emptycomb 和 HoneycombItem。1856–1861 行 BootsID 等于 1 才创建 wadingBoots，随后把该变量改写成实际物品数字 ID。|
|CustomRegister.registerItem|35–87 行。id 不以 modId 加冒号开头时调用 GameRegistry；另一路从 RegistryNamespaced 查旧对象和数字 ID，通过反射获得名称表与身份表，以同一 ID 放入新实例，并把旧实例挂到 removed 名称下、移出创造栏。随后替换 Items 的静态引用及已有统计对象中的引用。查找及反射可失败，异常会被打印。|
|CustomRegister.registerBlock|89 行起有相同的前缀判断，目标改为方块全局表和静态引用。两个 helper 的形参调用点没有常量注册名。没有外部调用输入，不能据此生成额外的现代 Item 或 Block。|
|CreativeTabsMFQM|构造器第 16–18 行委托父类。func_78016_d 第 20–22 行返回 GrapplingHookItem。物品的创造栏成员资格由各构造/注册处设置，部分使用原版食品栏。R1 将可收集样本集中在 mfqm:materials；其图标和排列仍有差异。|
|实体、方块实体与药效|16 个 Entity、4 个 TileEntity 相关调用分别保留。没有将注册实体直接换算成刷怪蛋。PotionStuck.analysis.txt 第 35 行经 registerExtendedProperties 给实体挂状态；这个名字本身没有提供独立药水注册证据。|

**计数。** 原表 210 行含 79 条显式栈用途、131 个注册相关调用点。由调用点得到的 131 个候选身份中包含 50 个 Block、44 个 Item、13 个 Fluid、16 个 Entity、4 个 TileEntity、3 个消息、1 个 worldgen 候选。去掉上述两个参数化 helper 后，有字面注册键的 Block 为 49，Item 为 43。另有 1 个直接构造的创造栏对象，故对象表合计 132 行。流体名从字段与构造器连接，保留 R0 原 ID。未取得 Forge 1.7.10 的动态 dump，条件分支可能影响实际安装所得数量。

按 original_object_id 查询 ORIGINAL_REGISTRY_OBJECTS，再按 r0_call_ids 跳回 ORIGINAL_REGISTRY。按 owner、method 和 descriptor 查询 R1_METHOD_EVIDENCE，可同时定位 CFR 区间、字节码文件和原有类档案。
