# Phase5复现

基线main c8fa7214525dfecb6b66835a903edd25a19dfe9c，包含Phase1–4。用户仓库ZIP等同快照，无需另上传。实际Phase1目录名为research/original-mechanics-phase1；解压其中研究ZIP到PHASE1。原JAR从合法私有位置读取，不包含在公开工程。

依赖：Python3标准库、完整Java17 JDK。工具使用JDK内部ASM，需要add-exports（脚本自动传入）。无联网依赖、没有Gradle/游戏构建。

一条命令重建环境、校验原方法体指令、执行全部对照及旧阶段回归：

```bash
python -B research/original-phase5/evidence/tools/all_checks.py --phase1 "$PHASE1" --jar "$ORIGINAL" --java-home "$JDK17" --work /tmp/mfqm-phase5
```

所有派生class写/tmp，原JAR的SHA预期2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b。模拟BlockMorass/CustomPotionEvent仅含原选定方法体与受控构造外壳；BodyProof在日志前逐指令/操作数/目标序号比较，不改原算法以通过测试。其它原类从只读JAR加载，仅加日志。

预期摘要：62组native-vs-independent-VM完整事件/最终状态对照，44组额外声明式oracle；旧2条Morass父链正常返回（父链不宣称独立闭环）；stuck 8回调123事件；Phase2/3/4历史测试在隔离/tmp副本通过其原有验收（Phase4仍保留原预期2环境失败与1非法输入，不改历史成绿）。异常/不支持API/任一diff必须非零退出，不能吞掉或跳过fixture。

当前输入域与构造由run_all.py明列：PlantingThis的正常/拒绝/null花提供者，extent边界及seed、Root QS/Dry的正/负/拒写/组合，Tombs不同World seed/空Tile，WLD sparse正/拒绝/重叠群系。passed与World RNG分别记录；Tombs World seed等于case seed，其余World RNG固定9。坐标origin(-16,70,0)或Surface/WLD block origin(-16,0)，dimension0/height62为mock合同，不是MC跨版本分布统计。

独立VM是不同语言的栈/调用解释器，未知指令/API显式失败；没有复用JVM分派或读trace充当答案。另有不分派字节码的几何/事务/随机游走oracle。后者校验RNG与所有突变/最终状态，VM额外校验全部读取/分支/helper。两条证据都保留，不能把单个原方法自我重放称独立算法证明。

已保存native与oracle全日志为jsonl.gz（只含分析事件，没有原资源），trace-manifest的SHA针对解压内容。用Python gzip.open或gzip -dc查看。事件含原类/descriptor/offset；覆盖/最终.tsv也是完整数据。原Root Surface的return/switch日志定位在本轮修正；原算法不改。

重跑解释器对保存native输出的独立比较：

```bash
python -B research/original-phase5/evidence/tools/verify_saved.py --work /tmp/mfqm-phase5
python -B research/original-phase5/evidence/tools/finalize.py
python -B research/original-phase5/evidence/tools/validate.py --jar "$ORIGINAL"
```

固定seed重复性与负例检查见test_guards_and_replay.py；故意不支持的type/opcode必须失败。失败/修复记录在evidence/failures；protected缺Native定义、WLD群系重叠/门前次数抽样均保留回归，没有删除失败输入。全量数据域之外仍BLOCKED，不能把fixture限定省略。

--regress复制历史research/original-phase2/3/4到临时repo形状目录，.git标记仅用于重跑私有导入保护，避免覆盖仓库旧报告。不会启动MC客户端/专服，原版实机全部NOT_RUN。私有材质导入继续用Phase4工具，默认只输出路径/hash；本轮未提取或公开PNG/OGG，也不AI生成贴图。
