# MoreFunQuicksandMod/main/client/CustomRenderOverlayEvent

ID `class:ab31357f84145b5857791696`；class SHA `944cffaf54ce81e24c1dbd1a7fc5399c36ed0d1d2fb2ab35bda73c91dec78b0d`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `java/lang/Object`；interfaces ``；access `33`；annotations/attributes `InnerClasses;SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/client/CustomRenderOverlayEvent`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__client__CustomRenderOverlayEvent.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:2cf3eafc78cbc74f0dba6773` `quicksandIDS:[Lnet/minecraft/block/Block;` access 10

## 方法目录

- `method:5d08f391cf99043342f133d3` `<init>()V` access 1，5 code bytes；语义 NOT_ANALYZED
- `method:800b9408fca653e059df4292` `renderAirGUI(Lnet/minecraftforge/client/event/RenderGameOverlayEvent$Pre;)V` access 1，357 code bytes；语义 NOT_ANALYZED
- `method:b54e228a8acdd75baba7512c` `RenderOverlay(Lnet/minecraftforge/client/event/RenderWorldLastEvent;)V` access 1，132 code bytes；语义 NOT_ANALYZED
- `method:0c963e400d5913c6d469961e` `renderInsideOfBlockR(FLnet/minecraft/util/IIcon;)V` access 1，252 code bytes；语义 NOT_ANALYZED
- `method:77ee36d123962cbc3699dba4` `<clinit>()V` access 8，213 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
