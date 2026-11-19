# 在游戏中核验 R1

1. 关闭 Minecraft，备份实例的 saves 文件夹。选 Minecraft 1.20.1、Forge 47.2.0、Java 17。在测试实例的 mods 文件夹只留一个版本的 MFQM Reborn。
2. 使用公开版时，将同目录的 mfqm-reborn-r1-public.jar 放入 mods。Windows PowerShell 执行 `Get-FileHash .\mfqm-reborn-r1-public.jar -Algorithm SHA256`，与 SHA256SUMS 对照。在模组列表确认版本 0.1.0-r1-content，在 logs/latest.log 核对装载文件。公开版用 Minecraft 材质。要看旧 MFQM 图标，按 README.zh-CN.md 生成私有版，并替换 mods 中的公开版。
3. 进入测试世界的创造模式，打开 MFQM 栏。按 F3+H 查看物品 ID。按 logs/r1-runtime.json 的 creative 顺序可查每个栈的 ID 和 NBT，也可在仓库 reconstruction/manifest/MODERN_CREATIVE_RUNTIME.csv 按编号查阅。输入 `/give @s mfqm:soft_ash`、`/give @s mfqm:mineral_clay`、`/give @s mfqm:grappling_hook` 可直接取样。带“收藏物品”提示的条目用于查看，应分别记录其名称、图标和能否使用。
4. 在语言设置中分别选 English (US) 和简体中文。测试湿泥的四个栈、下陷地毯颜色、蜡丛林原木、黏土桶和下沉药水。打开背包，将有同名的两个样本并列比较 ID。用 `/setblock ~ ~ ~2 mfqm:mucus[level=8]` 检查流面，再看同方块的物品栏图标；旋转视角比较顶面、底面和侧面。
5. 暂时关闭其他资源包，按 F3+T，等加载完成，再检查一次；恢复原来的资源包组合并复查。发现异常时，记录物品 ID、方块状态、语言、已启用包顺序、公开/私有版、JAR SHA、截图和 latest.log 相邻行。回报“紫黑”时，注明是在物品栏、已放置方块还是流动表面看到。
6. 回退时关闭游戏，换回旧 JAR，恢复测试前的世界副本。请保留原备份和旧模组文件，以便复查历史物品。
