# 注册与内容差异

ORIGINAL_REGISTRY实际210行，是带点注册调用与显式metadata用途候选：包含49个BLOCK调用、45个ITEM调用、13 FLUID、16 ENTITY、4 TILEENTITY、3 NETWORK、1 WORLDGEN，以及79个显式ITEMBLOCK_VARIANT用途。条件分支与动态参数可能重复/替换，非运行时独立注册总数。

现代源解析153项：50 BLOCK（49目录+dev）、63 ITEM（50 BlockItem+13 bucket）、26 FLUID（source+flow）、13 FLUID_TYPE、1 CREATIVE_TAB。数字单位不同，不能作“153>原版因此完整”的结论；现代目录不能当旧注册完整集合。独立工具/装备、实体、TileEntity、原物品metadata与隐藏/条件条目仍需逐项绑定。动态CustomRegister/反射和ItemMeta/ItemMetaColor的getSubItems逻辑不能靠字符串名字猜测。

R1-REG先执行旧registry/creative栈枚举、LanguageRegistry+ItemStack名称解析，再补原版→现代缺口。旧字段名/原注册大小写/现代小写ID分别保存。已保存mfqm ID、blockstate、网络、NBT等冻结记录见 COMPATIBILITY_FREEZE；不按本清点直接重命名。完整运行时注册/正确creative显示/名称 parity本轮NOT_RUN。
