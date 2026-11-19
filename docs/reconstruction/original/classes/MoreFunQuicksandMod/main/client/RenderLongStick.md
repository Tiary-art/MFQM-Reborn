# MoreFunQuicksandMod/main/client/RenderLongStick

ID `class:93e4c60168db7154e7d1ab09`；class SHA `8ae22e64be68275dadc85115eedede0c913145140e8978195b630225c25ef421`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `java/lang/Object`；interfaces `net/minecraftforge/client/IItemRenderer`；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/client/RenderLongStick`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__RenderLongStick.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

无声明字段。

## 方法目录

- `method:5265f03dd43ce5c768bb3b88` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:bcd00fba7ca8fcd94b94107c` `handleRenderType(Lnet/minecraft/item/ItemStack;Lnet/minecraftforge/client/IItemRenderer$ItemRenderType;)Z` access 1，20 code bytes；语义 NOT_ANALYZED
- `method:855132e88555ac76783ea95b` `shouldUseRenderHelper(Lnet/minecraftforge/client/IItemRenderer$ItemRenderType;Lnet/minecraft/item/ItemStack;Lnet/minecraftforge/client/IItemRenderer$ItemRendererHelper;)Z` access 1，2 code bytes；语义 NOT_ANALYZED
- `method:f6fa78b4879859348a47d7c8` `renderItem(Lnet/minecraftforge/client/IItemRenderer$ItemRenderType;Lnet/minecraft/item/ItemStack;[Ljava/lang/Object;)V` access 129，326 code bytes；语义 NOT_ANALYZED
- `method:d4c851b32fe7eb93334e42f2` `renderStick(Lnet/minecraftforge/client/IItemRenderer$ItemRenderType;Lnet/minecraft/item/ItemStack;FFF)V` access 1，180 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
