# 图标、模型与动画

**已定位的紫黑缺图。** 历史 docs/phase9/logs/private-client-final.log 中 SpriteLoader 明确拒绝宽 32、高 304 的 mucus_flowing。缺少帧尺寸时，加载器选择 32×32，304 不能被 32 整除；紧接着 ModelManager 同时报出 mfqm:mucus#inventory 和 level=8 的 missing textures。相同错误在资源重载后再次发生。历史通过结论需要以这份日志为准。

R1 的 private_models.py 为导入后的 .mcmeta 写入 width=32、height=16，保留原 frametime 和 PNG 字节。68296e6 的最终私有 JAR 经逐文件哈希和模型引用检查；Linux 单人及专服客户端的两次采样分别读取到同一个 mfqm:block/original/mucus_flowing，32×16、19 帧。截图保存在本地私人输出，仅发布无像素的模型导出及日志。未对动画速度、每帧形态、用户此前全部紫黑对象作目视对版。

**模型选择。** 花壁、花壁台阶和肉壁以 CFR 原纯函数为输入，对旧 damage 与六个面求值；catalog 中的六元组顺序为下、上、北、南、西、东。蜜巢使用阶段纹理，蜡木 0/4 的南面分别来自 WaxTree0/1，上下使用丛林木端面。泥沼顶面按旧数组（0、1 共用 Moor0），底面和侧面分开。薄板物品使用半高几何；全部世界方块朝向、特殊渲染、视觉一致性仍未通过逐件验收。

**范围。** 原版 300 资源均可在 R1_RESOURCE_PROVENANCE 中查 SHA 和相同载荷在私有包的路径；相同哈希不证明模型消费。R1 目录 110 行中 94 行有旧 PNG 绑定，16 行使用 Minecraft 羊毛。私有 JAR 含 119 PNG，原输入 247 PNG 中仍有 128 个找不到相同的导入载荷。新旧映射并表见 RESOURCE_USAGE。公开 JAR 共 210 个模型、0 PNG、0 OGG，使用原版引用。私有构建覆盖其中一部分模型。153 个栈都经过 GUI renderer，重载后私有模式有 120 个栈返回 mfqm 命名空间的 particle，33 个返回 minecraft；两组均无 missing model 或 missingno particle。particle 只能代表这一项引用，不足以证明每面都与旧版相同。

公开模式查询仅私有版提供的 mucus sprite 得到 minecraft:missingno，属于预期；公开版的实际在用模型与 particle 导出单独存放。Windows 资源包覆盖顺序和正式启动器安装待测。
