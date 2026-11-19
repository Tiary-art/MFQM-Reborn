# 可见栈、状态与名称

清单记录 174 个旧栈候选。67 个含显式 append，其中 49 个位于 Item 参数方法；另 18 个在 Morass、MoorGrass、Tent 的 getSubBlocks(int, CreativeTabs, List) 中。后者与接收 Item 的方法描述符不同，旧 Forge 分派情况待测。一个 SandstoneTrap 空覆盖单列。其余可见性保留 UNKNOWN，包括依赖父类的普通物品。

|对象|旧证据|R1 的表达|
|---|---|---|
|Mud|ItemMeta 第 21 行将 damage 拼到名称键；ItemMud 第 25–35 行只给 1、2、3 增加各自提示|同一 mfqm:mud 的默认栈和三份带 BlockStateTag.depth 的栈；运行时逐栈验证 NBT 往返。|
|BrownClay / WaxWood|前者第 92–95 行、后者第 74–77 行均只输出 0 和 4。语言循环还为其余六个值命名。|各展示两个旧状态；方位/深度在证据表中保留，避免增加六个无原创造栏依据的副本。|
|ItemClayBucket / ItemMyPotion|前者第 64–82 行、后者第 108–136 行按 damage 选 icon 和后缀；创造列表分别追加两栈、三栈。越界的 Error 名称不列为正常可获得物品。|两种黏土桶以及泥潭液瓶、下沉药水、热巧克力分别有稳定 ID 和私有图标。效果及放置尚待移植。|
|BlockSinkingWool|MFQM 第 1115–1119 行为 0..15 命名，方块构造第 35–50 行继承 BlockColored 并使用 wool_colored。ItemMetaColor 第 21–23 行拼接 damage。|16 种颜色对应现代原版羊毛模型。0 使用原有方块，其余为收藏物品。|
|SoftSnow|0 和 1 均进入标准创造栏路径（78–81 行），第 288 行依据 WLD_MIC 决定外部材质路径。|默认场景记录 Soft Snow / Soft Ash。未安装外部依赖，未验该分支。|

原版只有 en_US、ru_RU 语言文件。中文是项目本地化。同一键的两种英文证据可能冲突，例如 Morass 的 addName 与英语资源 Moor，以及 SoftGravel 的 SoftGravel 与 Silt Sludge。ORIGINAL_NAME_BINDINGS 并列记载旧语言键、行号、旧英语资源、现代名称和冲突状态。未取得旧运行时名称优先级，不能关闭 U-02。真正在现代客户端显示的名称见 client-atlas-100.json。
