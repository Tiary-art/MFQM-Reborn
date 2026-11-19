# MoreFunQuicksandMod/main/Fields

ID `class:1c838d5ab1e7cf537b8113ad`；class SHA `bd3eb7cfe75d53cff2cf986b0ec8a296fc193c20d1bf97840a3c09c029c99591`；原 JAR SHA `2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b`。

状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `java/lang/Object`；interfaces ``；access `49`；annotations/attributes `SourceFile`。内部类宿主 `MoreFunQuicksandMod/main/Fields`；客户端/服务端语义 UNKNOWN，不能按包名断言。

原始字节码证据位于仓库 `research/task-001/evidence/MoreFunQuicksandMod__main__Fields.bytecode.txt`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `UNKNOWN / modern bridge review`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。

## 字段目录

无声明字段。

## 方法目录

- `method:8fe8029211b709f90f319645` `<init>()V` access 2，5 code bytes；语义 NOT_ANALYZED
- `method:baa8549cbbc0e658f745e16d` `findFieldAndGet(Ljava/lang/Class;Ljava/lang/Class;Ljava/lang/Object;I)Ljava/lang/Object;` access 9，75 code bytes；语义 NOT_ANALYZED
- `method:e95bfca0eb7eb4bd907b0962` `findFieldsAndGet(Ljava/lang/Class;Ljava/lang/Class;Ljava/lang/Object;)[Ljava/lang/Object;` access 9，94 code bytes；语义 NOT_ANALYZED
- `method:52826d52a69a47b55212b632` `findField(Ljava/lang/Class;Ljava/lang/Class;I)Ljava/lang/reflect/Field;` access 9，61 code bytes；语义 NOT_ANALYZED
- `method:001e50c78f2c0378ffe2d287` `findFields(Ljava/lang/Class;Ljava/lang/Class;)[Ljava/lang/reflect/Field;` access 9，7 code bytes；语义 NOT_ANALYZED
- `method:bbb4cff3e04e8b85928ff892` `findFields(Ljava/lang/Class;Ljava/lang/Class;I)[Ljava/lang/reflect/Field;` access 9，113 code bytes；语义 NOT_ANALYZED
- `method:b0855fa7a336a0f87a009382` `removeFinal(Ljava/lang/Class;Ljava/lang/Object;[Ljava/lang/String;)Ljava/lang/reflect/Field;` access 137，53 code bytes；语义 NOT_ANALYZED

## 证据与待证问题

字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。

## 验证计划

用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。
