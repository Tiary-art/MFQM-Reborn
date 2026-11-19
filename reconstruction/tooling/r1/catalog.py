"""Compile the reviewed R1 mappings. Input paths are relative to the pinned evidence tree."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
E = ROOT / "research/task-001/evidence"
RES = ROOT / "forge-1.20.1/src/main/resources"
DATA = RES / "data/mfqm"
ASSETS = RES / "assets/mfqm"
MF = (E / "MFQM.analysis.txt").read_text(encoding="utf-8").splitlines()
BLOCKS = json.loads((DATA / "legacy_block_catalog.json").read_text(encoding="utf-8"))
RESOURCES = {r["path"]: r["sha256"] for r in csv.DictReader((ROOT / "reconstruction/manifest/ORIGINAL_RESOURCES.csv").open(encoding="utf-8"))}
def load(name):
    return (E / (name + ".analysis.txt")).read_text(encoding="utf-8")
def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
def slug(s):
    return re.sub(r'(?<=[a-z0-9])(?=[A-Z])','_',s).replace(' ','_').lower()
def source(kind, icon):
    path=f"assets/morefunquicksandmod/textures/{kind}/{icon}.png"
    if path not in RESOURCES:
        raise ValueError(path)
    return path
def compile_catalog():
    entries=[]
    registrations=list(csv.DictReader((ROOT/'reconstruction/manifest/ORIGINAL_REGISTRY.csv').open(encoding='utf-8')))
    for reg in registrations:
        if reg['kind']!='ITEM' or not reg['registered_name']: continue
        line=int(reg['line'])
        name=reg['registered_name']
        assign=MF[line-2]
        cls=re.search(r'new (\w+)\(',assign)[1]
        code=load(cls) if (E/(cls+'.analysis.txt')).exists() else ''
        icons=re.findall(r'(?:func_111206_d|func_94245_a)\("morefunquicksandmod:([^"]+)"\)',assign) or re.findall(r'(?:func_111206_d|func_94245_a)\("morefunquicksandmod:([^"]+)"\)',code)
        names=re.findall(r'addName\(.*?"([^"]+)"',MF[line])
        special={'Bucket of Clay':[('brown_clay_bucket','Bucket of Brown Clay'),('mineral_clay_bucket','Bucket of Mineral Clay')],'Potion':[('bottle_of_mire','Bottle of Mire'),('sinking_potion','Sinking Potion'),('hot_chocolate','Hot Chocolate')],'SPotion':[('throwable_sinking_potion','Throwable Sinking Potion')]}
        existing={'BucketOfLiquidBog':'bog','BucketOfQuicksand':'jungle_quicksand','BucketOfMire':'stable_liquid_mire','BucketOfSlime':'sinking_slime','BucketOfMucus':'mucus','BucketOfTar':'tar','BucketOfAcid':'acid','BucketOfChocolate':'liquid_chocolate','BucketOfHoney':'honey','BucketOfSlurry':'slurry'}
        variants=special.get(name,[(existing[name]+'_bucket' if name in existing else slug(name),names[0] if names else '')])
        for d,(id,en) in enumerate(variants):
            if not en or d>=len(icons):continue
            image=source('items',icons[d])
            cap=re.search(r'func_77625_d\((\d+)\)',code)
            size=int(cap[1]) if cap else 1 if ('Bucket' in cls or 'Armor' in code or 'Boots' in cls) else 64
            food=re.search(r'new ItemFood\((\d+), ([\d.]+)f, (true|false)\)',assign)
            mode='bucket' if name in existing else 'food' if food and 'func_77844_a' not in assign else 'item' if cls=='Item' else 'sample'
            entries.append(dict(id=id,legacy=name,damage=d,en=en,mode=mode,stack=size,textures=[image],shape='flat',owner=cls,ref=f'MFQM.analysis.txt:{line}',food=[int(food[1]),float(food[2]),food[3]=='true'] if mode=='food' else None))
    variants=[('BrownClay',0,'brown_clay','Brown Clay','Brown_Clay0'),('BrownClay',4,'mineral_clay','Mineral Clay','Mineral_Clay0'),('SoftSnow',1,'soft_ash','Soft Ash','SoftSnow'),('Honeycomb',0,'honeycomb','Honeycomb','honeycomb0'),('Honeycomb',1,'honeycomb_empty','Honeycomb Empty','honeycomb1'),('Honeycomb',2,'honeycomb_filled','Honeycomb Filled','honeycomb2'),('SoftGravel',0,'soft_gravel','SoftGravel','SoftGravel0/SoftGravel1'),('SoftGravel',1,'soft_gravel_1','SoftGravel','SoftGravel2')]
    for key,d,id,en,images in variants:
        spec=next(b for b in BLOCKS if b['legacy_id']==key)
        entries.append(dict(id=id,legacy=key,damage=d,en=en,mode='block' if d==0 else 'sample',stack=64,textures=[source('blocks',v) for v in images.split('/')],shape='cube',owner=spec['legacy_class'],ref=spec['legacy_class']+'.analysis.txt',food=None))
    from face_vectors import selected_faces
    for cls in ['BlockBlossom','BlockBlossomSlab','BlockMeat']:
        spec=next(b for b in BLOCKS if b['legacy_class']==cls)
        code=load(cls)
        creative=code.split('void func_149666_a(',1)[1].split('    }',1)[0]
        damages=[int(x) for x in re.findall(r'new ItemStack\(block, 1, (\d+)\)',creative)]
        for d,icons in selected_faces(code,damages).items():
            en='Plant Wall' if cls!='BlockMeat' else 'Meat Wall '+['','Bottom','Conner','Conner','Conner','Conner','Side','Side','Side','Side','Anus'][d]
            entries.append(dict(id=spec['id']+('_'+str(d) if d else ''),legacy=spec['legacy_id'],damage=d,en=en.strip(),mode='sample' if d else 'block',stack=64,textures=[source('blocks',x) for x in icons],shape='slab' if cls=='BlockBlossomSlab' else 'faces',owner=cls,ref=cls+'.analysis.txt',food=None))
    # The original ItemMeta tab exposes only the two forward-facing wax logs.
    for damage, icon in [(0, "WaxTree0"), (4, "WaxTree1")]:
        entries.append(dict(id="wax_wood" if damage == 0 else "wax_wood_4",
            legacy="WaxWood", damage=damage, en="Wax Jungle Log", mode="block" if damage == 0 else "sample",
            stack=64, textures=[source("blocks", icon)], shape="wax_log", owner="BlockWaxWood",
            ref="BlockWaxWood.analysis.txt:74-100,122-126", food=None))
    # BlockColored supplies the vanilla wool palette. No private texture is needed.
    colors = "white orange magenta light_blue yellow lime pink gray light_gray cyan purple blue brown green red black".split()
    for damage, color in enumerate(colors):
        entries.append(dict(id="sinking_rug" if damage == 0 else "sinking_rug_" + color,
            legacy="SinkingRug", damage=damage, en="Sinking Rug", mode="block" if damage == 0 else "sample",
            stack=64, textures=[], vanilla="minecraft:block/" + color + "_wool", shape="wool",
            owner="BlockSinkingWool", ref="MFQM.analysis.txt:1115-1119; BlockSinkingWool.analysis.txt:35-50", food=None))
    # getSubBlocks(int,...) has a different descriptor from the Forge Item overload.
    # Preserve its eight outputs as samples without claiming Forge dispatched it.
    for damage in range(9):
        top = "Moor" + str(max(0, damage - 1))
        entries.append(dict(id="morass" if damage == 0 else "morass_" + str(damage),
            legacy="Morass", damage=damage, en="Morass", mode="block" if damage == 0 else "sample",
            stack=64, textures=[source("blocks", icon) for icon in ["Moor_side1", top] + ["Moor_side0"] * 4],
            shape="faces", owner="BlockMorass", ref="BlockMorass.analysis.txt:593-639", food=None))
    return entries
if __name__=='__main__':
    entries=compile_catalog()
    save(DATA/'r1_content.json',entries)
    print([(e['id'],e['mode']) for e in entries])
