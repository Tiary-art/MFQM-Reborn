# Phase4复现：实际原方法体＋声明的mock世界

基线：`37d18a17a1d6cdc679c4b8182c8621df97024c57`（已合并Phase3）。Phase1包在仓库实际目录`research/original-mechanics-phase1/`，任务书所称Phase1证据即其研究ZIP；解压到PHASE1。原JAR只读且不分发。

需要Python3标准库、Java17完整JDK。ASM使用JDK自带内部库，编译/运行均显式add-exports；不联网下载、不构建游戏模组。所有派生class和环境合同源码写到/tmp，仓库只提交研究工具、文本与gzip分析日志。

## 一键复跑全部本轮检查

```bash
python -B research/original-phase4/evidence/tools/all_checks.py --phase1 "$PHASE1" --jar "$ORIGINAL" --java-home "$JDK17" --phase1-work "$PHASE1_WORK"
```

最后的phase1-work参数只用于重新核对Vanilla/SRG父链，可省略；省略时日志明确标记未在本次复跑此项，保留的静态结果不冒充新测试。其他模型/回归/差分/hash检查均执行。已知2条环境失败仍保留在cases/ERROR中，不能把“一键检查完成”解释成65条算法全通过。

## 一键核心模型和完整事件差分

在仓库根目录，以自己的输入路径替换参数：

```bash
python -B research/original-phase4/evidence/tools/run_all.py --phase1 "$PHASE1" --jar "$ORIGINAL" --java-home "$JDK17" --work /tmp/mfqm-phase4 --extended
```

这一个命令编译mock API、从原JAR读取CustomWorldGen/依赖class、内存插入原offset日志，执行65组case及14组独立完整事件/最终状态比较。**62正常结束、1预期invalid bound、2未解Morass环境错误**；命令结束不表示每case通过。cases.json记录每次非零退出和完整error，不能删除后算绿。

工具遇不满足的API链接/类型或插桩指令序号不一致就失败；原JVM执行实际int/long、返回/异常，而不是Python忽略未知opcode。插桩只保留源JAR读取，原JARhash前后校验。仅环境合同可控，不是Minecraft实机。

默认fixture/seed/半径在run_all.py；passed RNG来自seed参数，World RNG单独固定seed9，origin为(-16,0)，辅助方法Y70。直调MireO/OD与LiquidMire使用Material.field_151568_F哨兵，MireO/OD目标为JungleQuicksandBlock；Morass固定ty=1、lush=0，MireOD模式0。最后arg字段只对根方法配置或LiquidMire isWL有作用，不能把它当Morass ty。原方法签名/原offset来自Phase1索引，通过ASM逐指令数量校验。Surface只在调用/字段/分支处记offset以避免64KiB方法限制，其coverage不能与Gardencia逐指令覆盖直接混算。所有内部helper按实际调用闭包插桩，未执行的回调不伪造输出。

## 全部后续检查

```bash
cp /tmp/mfqm-phase4/methods-selected.json research/original-phase4/evidence/results/methods-selected.json
python -B research/original-phase4/evidence/tools/prove_b694.py
python -B research/original-phase4/evidence/tools/private_assets.py --jar "$ORIGINAL"
javac -d /tmp/mfqm-phase4/classes research/original-phase4/evidence/tools/PhysicsVectors.java
java -cp /tmp/mfqm-phase4/classes audit.PhysicsVectors > research/original-phase4/evidence/results/physics-vectors.csv
python -B research/original-phase4/evidence/tools/check_vectors.py
python -B research/original-phase3/evidence/scripts/test_trace.py research/original-phase3
python -B research/original-phase4/evidence/tools/summarize.py
python -B research/original-phase4/evidence/tools/write_reports.py
python -B research/original-phase4/evidence/tools/validate.py --jar "$ORIGINAL"
```

如需重新核对10个Vanilla父链，另指向Phase1私有工作目录（含官方minecraft-1.7.10-client.jar和joined.srg）：

```bash
python -B research/original-phase4/evidence/tools/check_inheritance.py --phase1-work "$PHASE1_WORK" --java-home "$JDK17"
```

原client/SRG未分发；本包附原hash、选择的文本javap和父链结果。缺这两项可复用已交付静态证据，不宣称本地重新执行了该检查。

官方840个JavaRandom对照重新生成：编译Phase3的RngReference.java到/tmp后运行，与Phase3 reference.csv比较；本轮已重新执行且一致。数值向量112项只是共享受困公式，不是完整原LivingUpdateEvent执行。

## 完整日志与错误重放

大JQS/LiquidMire/Moor/Blossom轨迹压成*.jsonl.gz，**只包含分析事件，没有旧JAR/PNG/OGG**。run_all保存raw SHA，validate流式解压核对全部事件数与SHA。可用`gzip -dc`或Python gzip查看完整有序事件，不是仅前缀样本。

原始未压缩trace还会留在/tmp/mfqm-phase4/private-traces。其错误样本同样完整压缩。两条Moor链在generateMorass@801因mock MorassBlock普通Block不能cast到原BlockMorass失败，不能称原版bug，也不能改成跳过PlantingThis。isWL76的LiquidMire样本在@325 nextInt0失败属预期非法输入。

初期缺IInventory环境类型时曾ClassNotFound失败，已补合同接口；当前未解失败仍如实保留。所有旧游戏实机、视觉/净下沉/生成统计为NOT_RUN；没有ORIGINAL_RUNTIME_TESTED。

## 私有原始资源导入（本轮未执行）

```bash
python -B research/original-phase4/evidence/tools/private_assets.py --jar "$ORIGINAL" --extract --out /tmp/mfqm-private-assets
```

默认不带--extract只输出247路径/hash映射；显式提取拒绝任何Git工作树目标。保留原像素/sidecar、不缩放、不AI重绘。资源提取和现代渲染/UV验收是不同事项，工具存在不等于素材授权或游戏渲染已通过。
