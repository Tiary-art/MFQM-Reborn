#!/usr/bin/env python3
from pathlib import Path
import json,csv
r=Path(__file__).resolve().parents[1];d=r/'docs/task-0035-b2';d.mkdir(exist_ok=True)
a=json.loads((r/'src/main/resources/data/mfqm/legacy_block_catalog.json').read_text())
rows=[]
for s in a:
 sink=s['kind'] in ['SINKING','VISCOUS'] or s['id']=='mud'
 rows.append(dict(legacy_id=s['legacy_id'],legacy_class=s['legacy_class'],modern_id='mfqm:'+s['id'],category=s['kind'],shape_height=s['height'],collision='none' if sink or s['kind'] in ['GAS','PLANT','LEAVES'] else 'slab' if s['kind']=='SLAB' else 'vanilla lily' if s['kind']=='LILY' else 'inset .025' if s['id']=='solid_honey' else 'solid',sinking=sink,drop=s['drop']+'; old special/silk rules partial',hardness=s['hardness'],hardness_evidence='verified literal' if s['hardness_verified'] else 'inherited unknown; modern placeholder',gravity='conditional random tick relocation (QS 1/5; SS 1/2); scheduling partial' if s['id'] in ['quicksand','soft_quicksand'] else 'no blanket FallingBlock',random_tick_legacy=s['random_tick'],fluid_legacy=s['fluid'] or 'none',native_fluid_status='PARTIAL: FluidType/source/flowing/bucket registered; modern transport' if s['fluid'] else 'N/A',tile_dependency=s['tile_dependency'] or 'none',light=s['emission'],animation='old animation/metadata parity pending',sound='central action events with legal vanilla fallback; old playback parity partial',resource='minecraft:block/'+s['texture'],item='BlockItem; hidden creative' if not s['visible'] else 'BlockItem',status=s['status'],missing=s['missing'],evidence='research/task-001/evidence/'+s['evidence_file']+'; registration '+s['evidence'],confidence='HIGH ID; literal properties as marked; LOW unmeasured dynamics'))
with (d/'block-implementation-matrix.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=rows[0],lineterminator='\n');w.writeheader();w.writerows(rows)
text='# 全量 Block 实装矩阵\n\n基线 main c399b3b，静态 registerBlock 调用逐项复核 **49**，另有开发方块1个；13个 Fluid 名称单列，不计作额外旧 Block。无旧实例 registry dump，数量代表可证实调用，不承诺旧环境加载结果。完整属性、缺口和置信度见 [CSV](block-implementation-matrix.csv) 与 [证据数据](catalog-evidence.json)。\n\n最终状态按实际行为保守标注；49 个注册项不等于49个完整复刻。PARTIAL 不代表完整复刻。所有 registerBlock 使用默认或显式 ItemBlock 类，未见 null ItemBlock；技术方块保留物品形式但隐藏创造栏。无新增自然生成。\n\n|旧ID / 类|现代ID|类别；形状/碰撞|状态|缺口|\n|---|---|---|---|---|\n'
for x in rows:text+=f"|{x['legacy_id']} / {x['legacy_class']}|`{x['modern_id']}`|{x['category']}; h={x['shape_height']}; {x['collision']}|{x['status']}|{x['missing']}|\n"
text+='\n## 13个旧 Fluid：独立核对\n\n|旧 Fluid 名称|旧 Block / 现代关系|当前状态|\n|---|---|---|\n'
for s in a:
 if s['fluid']:text+=f"|{s['fluid']}|{s['legacy_class']} / `mfqm:{s['id']}`|PARTIAL: 独立 FluidType + source/flowing Fluid + 对应 LiquidBlock + 桶；旧流动/反应未等价复刻|\n"
(d/'BLOCK_IMPLEMENTATION_MATRIX.md').write_text(text)
print('Matrix rows',len(rows),'separate fluid relations',sum(bool(s['fluid']) for s in a))
