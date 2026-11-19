# Gardencia、WLD与五大方法状态

精确原签名、B块起止、对应CFG文件在five-method-block-status.csv；复用Phase2原始CFG。下表闭环与模型覆盖分列：

|方法|语义闭环/总块|MODEL exercised/总块|其余状态|
|---|---:|---:|---|
|generateSurface|0/1054|0/1054|UNRESOLVED|
|generateAOADimGardencia|0/100|90/100|UNRESOLVED|
|generateWLD|0/466|0/466|UNRESOLVED|
|generateNether|0/131|0/131|UNRESOLVED|
|generateABC2|0/135|0/135|UNRESOLVED|

## Gardencia本批推进

受限解释器读取原方法675条指令，执行其分支、循环、locals、RNG及直接World写入。LocalVariableTable明确blockGen位于slot11（Phase2 worldgen-javap-v.txt中本方法LocalVariableTable），故BLOCKGEN_STORE事件不凭变量名猜测。

固定origin(-16,0)：Mud seed0只开GenMud，mock validWater在Y66、validSolid只在Y70，故65与60..64均可写，得到16×16×6=1536条写入（水65 meta0、泥60..64 meta3）。入口只消费两个nextInt16。这是fixture结果，不是自然世界平均分布。

JQS seed10、Blossom seed384、Moor seed10、LiquidMire seed1分别进入其门；合并覆盖90/100块。validGround/solid/liquid/free/flat/groundNear的返回由工具明确给定，并记录FIXTURE_PREDICATE。生成helper只记录调用和返回fixture，不执行其内部读写或RNG；因此后续父方法随机序列不代表真实生成后的World RNG。

Blossom stub返回false，原调用者仍写blockGen=1，离线测试专门断言此副作用。JQS成功后循环未因blockGen停止也能从轨迹观察；这些都是指定fixture下的原控制流执行，不能上升为全方法/全输入证明。

未覆盖10块及已覆盖但语义仍未证明的90块均列offset，没有删去。需要增加Tar/地面拒绝/Flat/scan中止/锚点坐标0等反例并实际执行helper才能关闭。

## WLD保留缺口

原方法466块，本批没有执行。Phase2已定位沙漠QS及±3区块金字塔查找、底部采样、k20向0的截面和刷怪笼多级随机替换。父区块存在检查不等于所有实际半径写入都在区块内；跨区块加载、读不存在邻区、边界metadata和已写后失败均待复核。完整旧片段与CFG引用不丢失，仍PARTIAL，不虚报本批完成。

Nether131块/ABC2 135块也全部保留原证据和未解表。本批未替换其旧成果或宣称获得完整闭环。01字段→生成引用可导航这些额外维度中实际材料。
