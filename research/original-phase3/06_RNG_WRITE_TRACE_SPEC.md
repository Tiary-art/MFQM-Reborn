# 离线字节码驱动模型与轨迹规范

工具`evidence/scripts/trace_vm.py`依赖Python标准库与选择后的原指令JSON，不加载/改写原JAR，不启动Minecraft。输入JSON含675条Gardencia指令及墓室六段指令，原方法descriptor/offset都保留。其执行是**MODEL_TRACE**：真实原控制流在声明的世界/方法stub上求值，不是ORIGINAL_RUNTIME_TRACE。

## 有效范围

支持当前选定方法实际出现的受限opcode；未知opcode、未声明helper直接报错，绝不跳过假装成功。Java Random 48bit LCG和nextInt拒绝采样已与JDK官方840个结果核对，含负seed、nextInt1、非2幂和拒绝路径。浮点f32显式舍入。它不是通用JVM：对象/异常/完整Java整型溢出/任意大坐标和全部字节码未实现，当前测试仅声明的有界fixture输入；不能在任意旧类上执行后宣称等价。

mock判定及生成helper与原算法分开。所有FIXTURE_PREDICATE给出方法/offset/输入/输出；HELPER_NOT_EXECUTED列出缺失函数，不能用其false返回理解为原版真实失败。RNG只统计当前执行体，省略helper内部RNG会改变后续真轨迹，报告不得做全链随机一致性承诺。

## 轨迹列

每行seq/method/offset/event；RNG含bound/result/state_before/state_after/draws；WRITE含XYZ/metadata/flags/区块及cross_chunk；CONFIG_READ含开关；BLOCKGEN_STORE含slot11；BRANCH含目标/是否跳转。墓室BLUEPRINT_WRITE表示setBlock直写，不能代表宝箱TE的最终数据。

固定样本：Gardencia mud(seed0)、jqs(10)、blossom(384)、moor(10)、liqmire(1)，origin(-16,0)；墓室seed0、origin(-16,40,0)。完整命令在REPRODUCE。输出jsonl与summary均保留。五组只单独开启各开关，不代表全开原版配置的联合分布。

## 对照与失败案例

`test-trace.json`记录：840 RNG值精确匹配、nextInt1删除后下个值改变、Mud1536写入坐标/meta、负区块、全事件确定性重放、Blossom false返回仍blockGen true，以及8489墓室写入与独立CFR解码器比较。输入非法bound/未知opcode/未知helper均是预期失败测试。首次工具None上下文bug和漏解析(Block)cast导致77项差异，失败记录与修复说明保留，不当原版游戏故障。

静态方法选择/指令复制仅STATIC_VERIFIED来源；模型执行/差分为MODEL_TESTED；原版游戏运行状态均NOT_RUN，没有任何ORIGINAL_RUNTIME_TESTED条目。
