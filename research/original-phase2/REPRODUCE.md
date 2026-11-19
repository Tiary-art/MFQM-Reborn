# 复现与证据边界

研究记录日期：2026-11-19（Asia/Shanghai）。本包为阶段性研究，详细未完成项见00，不是已通过全部Phase2验收的工程实现。

输入：仓库main `88b9ad1a53dd34a2322b7bb78ce0f5dc52d0a69c` 的Phase1研究ZIP（解压到PHASE1）；合法私有原JAR；CFR0.152先前的私有反编译目录CFR；OpenJDK17.0.21+9；Python3标准库；Vineflower1.11.2。原JAR与反编译输入不包含于本包。原JAR预期SHA-256见manifest。

以下是参数化复现命令，PHASE1/CFR/WORK/OUT/ORIGINAL按自己的路径赋值（不是系统环境变量重定义）。实际本机命令/退出码见evidence/logs/commands.log。javap与Vineflower派生输入已作为纯文本结果保留；需要重新生成时：

```bash
mkdir -p "$WORK/vineflower-targeted" "$WORK/selected-classes"
javap -c -p -v -s -classpath "$ORIGINAL" MoreFunQuicksandMod.main.CustomWorldGen MoreFunQuicksandMod.main.CustomWorldGenLakes MoreFunQuicksandMod.main.CustomGenerationEvent MoreFunQuicksandMod.main.GenerateDesertTombs MoreFunQuicksandMod.main.GenerateMucusBlossom > "$WORK/worldgen-javap-v.txt"
# 用zipfile只提取CustomWorldGen.class到private selected-classes；不修改JAR。
java -Xmx1536m -jar vineflower-1.11.2.jar --folder --thread-count=1 --bytecode-source-mapping=true "$WORK/selected-classes/CustomWorldGen.class" "$WORK/vineflower-targeted" > "$WORK/vineflower-targeted-02.log" 2>&1
python evidence/scripts/build_phase2.py --phase1 "$PHASE1" --cfr "$CFR" --work "$WORK" --out "$OUT"
python evidence/scripts/finalize_phase2.py --phase1 "$PHASE1" --cfr "$CFR" --work "$WORK" --out "$OUT" --original-jar "$ORIGINAL"
python evidence/scripts/validate_phase2.py "$OUT"
```

必须按build→finalize次序：build生成原始参数表达式矩阵，finalize将其移至evidence/indexes并建立主生成器/辅助方法矩阵。finalize复用Phase1报告数据，不宣称重新完成其全部语义研究。单独重复finalize会把当前主矩阵误当原始矩阵；请始终从build开始。

第一轮整JAR反编译在墓室方法OOM，不用于“成功还原”的计数；单类第一次运行输出目录不存在而保存失败，第二次成功。失败日志也保留。private反编译器目录内可能包含自动复制的资源，**不能整体拷入公开仓库**；这里只选择纯文本。

验证范围：213个CFG节点/边目标存在、10个要求的交付文件存在、49材料/161类缺口索引数量、禁用二进制资源扫描、原JARhash对照。它们是静态工件自检，不是算法语义等价证明，不是Minecraft实机测试。没有Gradle构建，因为本轮不修改玩法、不生成候选JAR；原版运行统一NOT_RUN。

标记：VERIFIED_CALLSITE/STATIC_LITERAL只证明指令/常量存在，不证明已理解整段算法。PARTIAL为局部规格/未闭环；UNKNOWN为未确定；NOT_RUN专用于未执行运行验证。本批未用猜测填补缺口。
