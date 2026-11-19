# MoreFunQuicksandMod/main/CustomVarPlayer

ID `class:1545a9697cbb0cefc823afb2`；class SHA `cf7f48b5a7b46c61627cf920f7ad4a91dc8331757845a207b633aca225120332`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `java/lang/Object`；interfaces `net/minecraftforge/common/IExtendedEntityProperties`；access `33`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/CustomVarPlayer`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__CustomVarPlayer.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

- `field:e3871833f20dddafef970526` `EXT_PROP_NAME:Ljava/lang/String;` access 25
- `field:daef559d3d8657f7efae367d` `MUDDYLEVEL_WATCHER:I` access 25
- `field:979f0dd6e7f2f6a474c89b9b` `player:Lnet/minecraft/entity/player/EntityPlayer;` access 18

## 方法目录

- `method:df6cbf342370daedf4057327` `<init>(Lnet/minecraft/entity/player/EntityPlayer;)V` access 1，71 code bytes；语义 NOT_ANALYZED
- `method:07da611047d628dffc07f038` `register(Lnet/minecraft/entity/player/EntityPlayer;)V` access 25，16 code bytes；语义 NOT_ANALYZED
- `method:eb087cf4fa670fcdc20be721` `get(Lnet/minecraft/entity/player/EntityPlayer;)LMoreFunQuicksandMod/main/CustomVarPlayer;` access 25，10 code bytes；语义 NOT_ANALYZED
- `method:b4976e841bf076b06f536852` `saveNBTData(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，35 code bytes；语义 NOT_ANALYZED
- `method:b86172b2148066b6c55cf6f6` `loadNBTData(Lnet/minecraft/nbt/NBTTagCompound;)V` access 1，33 code bytes；语义 NOT_ANALYZED
- `method:59962e6e823d9d1116313c03` `init(Lnet/minecraft/entity/Entity;Lnet/minecraft/world/World;)V` access 1，1 code bytes；语义 NOT_ANALYZED
- `method:bfea52ca126d7565280990bf` `getData()I` access 1，14 code bytes；语义 NOT_ANALYZED
- `method:ff6476ac190f8048025d152e` `getMuddyLevel()I` access 1，13 code bytes；语义 NOT_ANALYZED
- `method:6a6b0c1ae0de6d1397264a34` `getMuddyTime()I` access 1，8 code bytes；语义 NOT_ANALYZED
- `method:c80fa6629e678c25a2d1c7ef` `getMuddyType()I` access 1，9 code bytes；语义 NOT_ANALYZED
- `method:8177916c697c58999993d152` `setMuddyLevel(I)V` access 1，41 code bytes；语义 NOT_ANALYZED
- `method:c4da8d7899e3cd4f5d7dc6de` `setMuddyTime(I)V` access 1，29 code bytes；语义 NOT_ANALYZED
- `method:6a3091e10fe2b03162c198fa` `setMuddyType(I)V` access 1，31 code bytes；语义 NOT_ANALYZED
- `method:53fb38c4159a70488de9f00a` `addMuddyTime(I)V` access 1，36 code bytes；语义 NOT_ANALYZED
- `method:607712415772de29eccd9470` `<clinit>()V` access 8，7 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
