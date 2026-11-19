# MoreFunQuicksandMod/main/client/CustomRenderPlayerEvent

ID `class:d302e5c3a0815cb2f43b89a6`；class SHA `6f8fe7e1cfbe24044a73f7d8057cc024c1fa48034c26c0954fd6ffc66d9469b3`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / FIRST_BATCH_PARTIAL**（除重点模块报告给出的分支外）。super `java/lang/Object`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/client/CustomRenderPlayerEvent`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__CustomRenderPlayerEvent.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

无声明字段。

## 方法目录

- `method:ca193300d7872c700c2dee61` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:87dc46f7ce2e7f32e7be5331` `preRenderPlayer(Lnet/minecraftforge/client/event/RenderPlayerEvent$Pre;)V` access 1，67 code bytes；语义 NOT_ANALYZED
- `method:415ef8a1e228fabb666e5e61` `handRenderPlayer(Lnet/minecraftforge/client/event/RenderHandEvent;)V` access 1，55 code bytes；语义 NOT_ANALYZED
- `method:a54f0ba5d8214846ca540bb8` `turnOnRenderMuddyModel(Lnet/minecraft/client/renderer/entity/RenderPlayer;Lnet/minecraft/entity/player/EntityPlayer;)Z` access 1，106 code bytes；语义 NOT_ANALYZED
- `method:d0981fb8e6a97ee22d3d97ce` `turnOnRenderMuddyModelFirstPerson(Lnet/minecraft/client/renderer/entity/RenderPlayer;Lnet/minecraft/entity/player/EntityPlayer;)Z` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:846dc78918e8fda46ac60927` `registerPlayerMuddyModel(Lnet/minecraft/client/renderer/entity/RenderPlayer;Lnet/minecraft/entity/player/EntityPlayer;)Z` access 1，139 code bytes；语义 NOT_ANALYZED
- `method:13f588594d88cca771f120f0` `checkPlayerMuddyModel(Lnet/minecraft/client/renderer/entity/RenderPlayer;Lnet/minecraft/entity/player/EntityPlayer;)Z` access 1，233 code bytes；语义 NOT_ANALYZED
- `method:127134d4785be7630cdbfa52` `checkPlayerMuddyModelChild(Lnet/minecraft/client/model/ModelRenderer;Lnet/minecraft/entity/player/EntityPlayer;)I` access 1，142 code bytes；语义 NOT_ANALYZED
- `method:f211ed7a4acaa6771631fde1` `scanChilds(Lnet/minecraft/client/model/ModelRenderer;Lnet/minecraft/entity/player/EntityPlayer;)V` access 1，311 code bytes；语义 NOT_ANALYZED
- `method:d7f576351b4d9981775d5d26` `deleteChilds(Lnet/minecraft/client/model/ModelRenderer;Lnet/minecraft/entity/player/EntityPlayer;)V` access 1，119 code bytes；语义 NOT_ANALYZED
- `method:68c22bdd29109f5a04e965f6` `turnOnChilds(Lnet/minecraft/client/model/ModelRenderer;Lnet/minecraft/entity/player/EntityPlayer;)V` access 1，97 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。

## 首批深度档案入口

遮罩与旧UV：原版逐层遮罩不等同现代全身方块纹理；重点报告§5。

[深度证据、规范与对照](../../../../../../../reconstruction/reports/DEEP_FIRST_BATCH.md)

1. 身份/字节哈希/工具：本页顶部，原始来源非原作者源码。
2. 原文证据与解释：按上述位置与重点报告分栏读取。
3. 职责和触发：重点报告对应模块列出输入、调用次序、提前返回。
4. 功能与资源：对应 ORIGINAL_REGISTRY、RESOURCE_USAGE 和本类调用边，不将名字映射当语义。
5. 行为规范：重点报告的分支和边界；未列分支 UNKNOWN。
6. 现代差异：重点报告逐模块对照现代真实路径及存档风险。
7. 测试设计：原版对照本轮 NOT_RUN，现有现代回归见 R0_TEST_RESULTS.json。
8. 结论：PARTIAL，仅已列静态链；下一步按 NEXT_WORK_PACKAGES.md 闭合。
