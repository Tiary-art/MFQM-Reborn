# 材质、模型、名称

RESOURCE_USAGE复用Phase9 167行，不把历史38 CONFIRMED纹理用途当作完整恢复；25个ID的映射也不是全游戏视觉PASS。RESOURCE_REFERENCE_GRAPH扫描当前全部MFQM JSON的parent/model/texture，vanilla外部路径、存在但未渲染验收、需私有导入、缺失/动态未解分别保留。动态Java资源另在MODERN_RESOURCE_REFERENCES。

紫黑案例U-01仍OPEN：用户Windows私有包实际hash/具体ID/截图/log本轮未知，不能伪造根因。普通/松软流沙、泥浆与流体历史Linux样本不覆盖所有metadata、多面、物品和外部资源包。bucket还是water_bucket；mud/soft特殊变体、原实体/污渍图集等未完整接入。所有原始PNG/mcmeta只作私人输入，未提交。

名称需同时检验旧LanguageRegistry运行时名称、lang键、ItemBlock damage和现代en_us/zh_cn，不做名字相似自动parity。UNKNOWN不能按“没有贴图文件”直接判原私有导入失效，也不能按私有文件存在判显示PASS。
