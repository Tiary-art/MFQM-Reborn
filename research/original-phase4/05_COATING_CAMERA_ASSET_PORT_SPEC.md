# 污渍、镜头与MFQM原资源规格核对

沿用Phase3的逐对象/变体证据；没有将无直接污染调用的材料改判成不沾污，也没有把干沙统一套Mud规则。33类型与20张64×32分级遮罩、Muddy Type/Level/Time和更新/清洗的精确offset依旧指向Phase1/2证据。逐材料完整污染路径尚未全部闭环，状态UNRESOLVED部分保留。

湿润且不在两类LiquidMire L检测中，time减5+time/100夹0，按worldTime门逐渐降高level；干燥有类型残留阈值与time<1000条件，不保证最终自动清白。等级选mask，不是触碰后全身alpha。旧Biped64×32/Alex现代左右独立UV/盔甲遮挡仍需独立映射和实测，不能把它写成完成。

原第一人称overlay来自玩家眼部位置-.2采样，原RGB .1、alpha1与原图不透明证据沿用；第三人称相机射线与玩家眼部触发分开。镜头在内玩家在外不能激活玩家浸没遮挡。空实体碰撞体不等于空视觉shape，不加实心碰撞修相机。旧音效/粒子随机消耗次序不能删除后声称物理RNG一致。

## 新增可复核资源映射与私有方案

`original-asset-path-map.csv`列247原资源路径/hash/尺寸/动画sidecar及**现代目标提案**，没有复制像素。`original-audio-path-map.csv`另列仅有的2份原JAR附带的bee OGG路径/hash/现代别名提案；没有给每种沙编造专有OGG，也没有音频听验。`mfqm:legacy/...`是建议的逻辑sprite/纹理标识，目标文件路径在另一列；现代渲染注册/UV还没实施。源指MFQM1.1.1自己的资源，不是minecraft:sand/mud；不生成AI图、不重绘、不缩放。

private_assets.py默认只写文本映射，验证整个原JARhash；只有显式--extract --out才提取到非Git工作树的私有目录。原PNG字节与sidecar保持不变，逐图hash核对；所有Git祖先路径拒绝。当前**pixels_extracted=false**，未运行实际提取或渲染。

原图有动画条、32像素宽纹理、64×32污渍mask等不同用途，不因16×16美术方向就擅自缩放所有图。原始贴图与声音授权未确认前不可公开分发，现代资源代码本轮不改。私有导入是计划/工具，不是素材授权或渲染验收通过。
