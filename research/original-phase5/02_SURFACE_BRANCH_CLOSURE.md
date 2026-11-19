# QS、DryQuicksand与共享Mire：限定域关闭

原`CustomWorldGen#generateSurface(World,Random,III)V@0..14261`，完整25行状态在surface-25-status.csv。源条件/参数/callee offset沿用Phase4同名审查表。主世界dim0、height62（dHeight0）、origin(-16,0)，BoP等可选模组关闭，原BiomeGenDesert、dT0；没有用原CF自我重放作为唯一oracle。

## 原条件与顺序

GenSSand先于GenQS。dT0时SSand次数1+nextInt2、门1/20、extent4+nextInt15；QS次数1+nextInt2、门1/15、extent5+nextInt10。均从96扫到>60，沙材/free space和平坦条件先通过才调用helper。isAboveFreeSpace消费单独World RNG。源rad是旧循环extent，数学半径约rad/2，不能将其误当球半径翻倍。

GenSSand调用generateSoftSand，写SandBlock（注册DryQuicksand）与砂岩；QS调用generateMire(F哨兵,QuicksandBlock)。SSand成功后blockGen使后续QS跳过；QS尝试循环与SSand停止规则不同。组合seed10/38回归及refused-writes保留共享blockGen、前置RNG、void helper返回后仍置状态等副作用；不拆成独立PlacedFeature。

## 验证域

QS和SSand分别有desert正例、empty地面拒绝、seed0概率拒绝、desert-refuse全部写返回false、组合配置；helper extent -1/0/1/4/5/10/18×seed0/1、空背景、SoftQuicksand保护、water替换拒绝、MudBlock目标等。全部有原native与独立栈机完整事件/最终状态；关键helper另有独立事务oracle。

Mire oracle以噪声体素筛选+目标写入+下方支撑事务定义；Dry oracle以三格竖印和**有序**浅层侵蚀定义，不共享字节码分派。genMire普通/目标Mud/保护/替换域已验证，但植物、雪、Nether及任意动态方块API未全闭环。旧helper即便extent<0仍消费初始nextDouble，不能优化掉。

每个点的噪声先消费，所有重复写入和metadata/flags保留；不能只对最终去重体素比对。独立栈机覆盖分支和读取，事务模型额外检查数学/写入语义。原helper写入可能拒绝，后续查询反映实际应用状态；refused-write用例不被删除。

**SEMANTICALLY_CLOSED仅用于cases.json中明确的有限环境/输入域**。全原支路的所有群系、配置和更新回调仍0/25闭环。只有Dry体素核心形成PORT_READY接口规格；整个Surface/天然生成注册仍BLOCKED。
