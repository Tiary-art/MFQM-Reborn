# 复核方法

本包不含原JAR、CFR工具二进制或原PNG/OGG。请使用用户持有的原1.1.1 JAR。原文件SHA见manifest.json。Python3需Pillow，JDK17含javap；本轮CFR0.152的工具SHA-256是f686e8f3ded377d7bc87d216a90e9e9512df4156e75b06c655a16648ae8765b2。

结构与资源清点可重做：

```bash
python3 tools/build_evidence.py \
  --jar '/private/original.jar' \
  --task001 '/path/to/MFQM/research/task-001' \
  --b2 '/path/to/B2-repo' \
  --out '/private/research-output' \
  --javap '/path/to/jdk17/bin/javap'
python3 tools/curate_core.py --root '/private/research-output'
javac -d '/private/probe-classes' tools/ArithmeticProbe.java
java -cp '/private/probe-classes' ArithmeticProbe
```

build_evidence.py可加`--fresh evidence/fresh-javap-all.txt`复用本包的字节码文本，而非重新执行javap；复核原始输入时应省略这个选项。生成的branches.csv为机器跳转索引；人工分支释义在curate_core.py里，对这个确定的JAR哈希有效，不是自动证明任意改版算法。

独立CFR比对：对原JAR使用CFR0.152重新输出Java，把Task001相应analysis.txt开头的`数字: `去除后，比较13个优先类文本；本轮相同，哈希见independent-cfr-comparison.csv。CFR报告的5个世界生成方法未完整结构化问题见logs/cfr-summary.txt。没有把反编译成功等同语义或实机验证。

外部UV/相机参考的官方客户端URL/SHA-1和MCP SRG URL/SHA-256在evidence/external/provenance.json；本包只附必要文本摘录、SRG对应行，未附官方游戏二进制。它们只用于静态参考，不是旧Forge补丁/完整运行环境。

`tools/finalize_evidence.py`是此次工作区的整理脚本，包含本次工作路径；其每步检查逻辑可供审阅，不宣称无需调整路径即可在其它机器一键运行。verify_delivery.py可校验本交付文件及原JAR哈希：

```bash
python3 tools/verify_delivery.py --root '/path/to/this/package' --jar '/private/original.jar'
```

原版游戏场景均NOT_RUN，不能从重跑这些静态脚本得到原版逐tick轨迹。采样方案见reports/07_original_runtime_measurement_plan.md。
