# Phase 3复现

基线：main `1f320442e0196319af24e40073cce6631cd7ec48`。用户已说明MFQM-main (6).zip就是仓库快照，因此直接从该合并提交复现，不要求另一份ZIP。研究日期2026-11-19（Asia/Shanghai）。需要Python3标准库；官方RNG对照需要Java17 javac/java（输出只写/tmp，不生成游戏JAR）。

所有变更限research/original-phase3。本包包含纯文本选择字节码和Phase2引用，不重新反编译全JAR。原JAR只在最后校验hash，不参与修改；原PNG/OGG不包含。

## 已交付工件的最小复现

在仓库根目录执行：

```bash
python -B research/original-phase3/evidence/scripts/test_trace.py research/original-phase3
python -B research/original-phase3/evidence/scripts/write_reports.py research/original-phase3
```

test_trace读取保留的官方Java参考数据，重新执行RNG/fixture/差分与负例，并重建8489条墓室直接蓝图。重新生成官方数据：

```bash
mkdir -p /tmp/mfqm-phase3-java
javac -d /tmp/mfqm-phase3-java research/original-phase3/evidence/scripts/RngReference.java
java -cp /tmp/mfqm-phase3-java RngReference > research/original-phase3/evidence/tests/java-rng-reference.csv
```

## 重新生成全部六个模型轨迹

```bash
python -B research/original-phase3/evidence/scripts/trace_vm.py --methods research/original-phase3/evidence/indexes/trace-methods.json --out research/original-phase3/evidence/traces/gardencia-mud.jsonl --scenario mud --seed 0
python -B research/original-phase3/evidence/scripts/trace_vm.py --methods research/original-phase3/evidence/indexes/trace-methods.json --out research/original-phase3/evidence/traces/gardencia-jqs.jsonl --scenario jqs --seed 10
python -B research/original-phase3/evidence/scripts/trace_vm.py --methods research/original-phase3/evidence/indexes/trace-methods.json --out research/original-phase3/evidence/traces/gardencia-blossom.jsonl --scenario blossom --seed 384
python -B research/original-phase3/evidence/scripts/trace_vm.py --methods research/original-phase3/evidence/indexes/trace-methods.json --out research/original-phase3/evidence/traces/gardencia-moor.jsonl --scenario moor --seed 10
python -B research/original-phase3/evidence/scripts/trace_vm.py --methods research/original-phase3/evidence/indexes/trace-methods.json --out research/original-phase3/evidence/traces/gardencia-liqmire.jsonl --scenario liqmire --seed 1
python -B research/original-phase3/evidence/scripts/trace_vm.py --methods research/original-phase3/evidence/indexes/trace-methods.json --out research/original-phase3/evidence/traces/tombs.jsonl --scenario tombs --seed 0
```

默认x=-16,z=0；墓室Y40，其余方法没有Y参数。所有输出为MODEL_TRACE。不能删除fixture说明、HELPER_NOT_EXECUTED事件后称完整原版轨迹。

## 从Phase1重建材料和Surface索引

解压仓库Phase1研究ZIP到PHASE1；CFR指向合法私有的先前CFR0.152结果目录（含blocks/、liquids/），无需重复反编译161类。这些私有输入路径不可替代为原贴图包。

```bash
python -B research/original-phase3/evidence/scripts/build_inventory.py --phase1 "$PHASE1" --repo "$PWD" --cfr "$CFR"
python -B research/original-phase3/evidence/scripts/summarize_evidence.py "$PWD" --phase1 "$PHASE1"
python -B research/original-phase3/evidence/scripts/write_reports.py research/original-phase3
python -B research/original-phase3/evidence/scripts/check_provenance.py research/original-phase3 --phase1 "$PHASE1"
python -B research/original-phase3/evidence/scripts/validate_delivery.py research/original-phase3 --original-jar "$ORIGINAL"
```

先build再summarize：build建立49块基础表，summarize附加有具体offset的meta记录和12 Fluid定义。metadata-domain-coverage的784行仅是存储域审计格，不是可达变体声明。

trace-methods.json由Phase1 methods-with-instructions.json筛选：CustomWorldGen#generateAOADimGardencia和GenerateDesertTombs#func_76484_a/generate2..6，保留完整descriptor/instructions。没有改原JAR。索引脚本生成的源码片段是反编译推断，不宣称原始源码或算法等价。

## 结果与失败边界

正式日志在evidence/tests；first-test-failure记录首次工具测试发现的None上下文及(Block)cast解析遗漏，修复后重跑通过。未知opcode/未知helper/非法bound仍必须失败，不能被吞掉。该解释器不是通用JVM，不支持任意Java溢出/异常/对象和任意世界；仅声明的fixture样本MODEL_TESTED。

没有启动1.7.10客户端/专服，没有Gradle构建或候选JAR。没有ORIGINAL_RUNTIME_TESTED条目，原版实机全部NOT_RUN。
