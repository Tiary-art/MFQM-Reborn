# Morass类型与PlantingThis

原`CustomWorldGen#generateMorass(IIIILnet/minecraft/world/World;Ljava/util/Random;FI)V@801`先cast MFQM.MorassBlock再调用PlantingThis。Phase4字段是普通Block，违反类型和this身份合同；不是原方法本身抛错。

本轮是**受控模拟类型外壳**：保留原全名/Block父类、MFQM单例与World中对象身份。构造器是mock，只初始化本方法实际查询的material151583_m；原PlantingThis(World,Random,III)V与func_149721_r()Z方法指令完整复制进外壳。后者原返回false，不能只消除cast却继承错误的solid判定。其它原BlockMorass方法/字段没有声称完整加载。

BodyProof在日志插桩前比较原与外壳方法的操作码、操作数、目标/跳转指令序号；body-identity.log提供SHA。原JAR不写入。后续仅加入日志；不改条件、RNG、返回或跳过128次尝试。

合同：坐标(-16,70,0)、below<=70为同一Morass单例，花材/func_149721_r谓词、Biome花名与canPlant均显式native API。plant-ok、plant-refuse、plant-null×seed0/1/-1共9例。null表示花查找返回null，不是假定World可为null。花提供者固定且不额外消费RNG；真实Vanilla/其他mod花提供者不在此闭环域。

独立Python栈机逐事件校验所有BRANCH/HELPER/RNG/读写；独立随机游走事务模型按attempt号生成可达候选，不读取JVM trace，校验RNG和花写入/最终状态。原this身份、每步4个nextInt3、整数除2、支撑/上方谓词、nextInt8、元数据2和写入flags3均保留。

父Gardencia seed10/2132两例已经执行实际回调并返回，完整日志见morass-parent-*。**没有对整个父链宣称独立闭环**；只对PlantingThis的指定API输入域标SEMANTICALLY_CLOSED。真实Biome映射与整个Morass物理仍BLOCKED。
