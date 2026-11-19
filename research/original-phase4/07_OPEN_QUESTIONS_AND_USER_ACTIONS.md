# 精确缺口与用户事项

|缺口|精确定位|本轮证据与下一步|
|---|---|---|
|Gardencia非GenMud全语义|gardencia-block-audit.csv各B起止|99块执行不是闭环；为各helper建独立oracle|
|Morass生态回调类型|CustomWorldGen#generateMorass(IIIILnet/minecraft/world/World;Ljava/util/Random;FI)V@801|两失败trace保留ClassCastException及前缀状态；修mock BlockMorass身份并执行PlantingThis，不能跳过|
|LiquidMire非法参数|generateLiquidMire(IIIILnet/minecraft/world/World;Ljava/util/Random;Lnet/minecraft/block/material/Material;I)V@325|isWL76令nextInt(75/76)=nextInt0，预期失败；不当自然默认参数|
|Surface25完整链|surface-25-audit.csv每条锚区间及callee descriptor/offset|0/25整支路闭环；先QS/SoftSand独立oracle，再Mire/Clay/环境兼容|
|Tombs15 helper|tombs-15-helper-audit.csv每次调用offset|全部NOT_RUN；NBT/loot/TE/World RNG合同|
|WLD结构|原generateWLD descriptor、Phase2 CFG全部466块|端到端结构未完成，不能拿Surface QS代替|
|10父链的Forge语义|ten-contact-inheritance.json|Vanilla noop已核对，补Forge patch/事件覆盖|
|物理/污染全变体与净轨迹|Phase3逐材料入口、metadata读点|不套统一profile，逐材料事件/装备/侧重与真实轨迹|

当前没有必须由用户补交资料或截图才能继续的静态研究阻塞，已有原JAR与仓库足够继续下批工具研究。**不重复索要已说明是仓库快照的ZIP，也不重复请求此前已同意的EULA。**

后续若要取得ORIGINAL_RUNTIME_TESTED，必须运行合法MC1.7.10+匹配Forge+原JAR/可选mod环境并记录版本/hash/配置/seed/逐tick或存档；本批没有这样的真实运行。USER_ACTION_REQUIRED仅在需要用户提供其私有原版环境日志或视觉观察时才成立：给出对应固定seed/配置/坐标的小场景，导出原始日志/截图，不让其阻塞无人工依赖的工作。现在不将此作为必须确认的请求。

研究交付点停止。下一最小研究建议：关闭Morass PlantingThis类型边界及一个Mire helper完整独立oracle；之后再验收Surface正/负/边界支路。任何新版玩法修改另待授权。
