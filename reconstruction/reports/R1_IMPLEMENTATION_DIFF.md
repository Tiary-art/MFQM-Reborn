# 从 R0 到可安装 R1

|单位|R0|R1|
|---|---:|---:|
|mfqm 注册对象|153 静态|244，静态与 Forge 枚举吻合|
|物品注册 ID|63 静态|154 运行时|
|材料栏实际栈|旧版本未导出；源代码默认输出推算 60|153 运行时（含 Mud NBT）|
|独立英文、简中资源键|各 64|各 156，分别修改 59 和 19 个既存键|

R1 保留 153 个既有注册身份，新增 91 个 Item ID。每个新增 ID 由 RestoredItems 对 data/mfqm/r1_content.json 内的稳定键进行一次 DeferredRegister。80 个是有待复原使用或放置功能的收藏样本，5 个是普通物品，6 个带 FoodProperties（五种甜甜圈和 Filled Honeycomb）。另外复用 10 个已有桶和 9 个已有默认方块。旧版有字面键的 43 个独立物品候选在目录中对应 46 份表示，包含多 damage 桶和饮品。目录和 CONTENT_PARITY_MATRIX 有逐对象详情。使用类、特效、护甲、钩索、消耗交互与原版仍有差距。

Forge 的分类为 Block 50、Item 154、Fluid 26、FluidType 13、创造栏 1。创造栏内计量为 BlockItem 48 栈、PlaceOnWaterBlockItem 1、BucketItem 13、DisplaySample 80、普通 Item 11。原版内部和工具方块不以目录数充当玩家可见物品。藏起 dev_test_block 后其注册 ID 仍在。生成器和陷落相关行为沿用 R0。

MODERN_REGISTRY、ORIGINAL_TO_MODERN、RESTORATION_MATRIX 与资源图均已重新生成。旧矩阵 3510 个身份全数保留，2321 个仍无现代对象链接。清理台账将展示样本列作有限实现，保留稳定性与其他 R0 人工结论。
