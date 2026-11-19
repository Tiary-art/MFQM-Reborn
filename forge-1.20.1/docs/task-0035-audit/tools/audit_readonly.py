#!/usr/bin/env python3
"""003.5-A: read immutable inputs; write audit metadata only. Never launch Minecraft."""
import argparse
from collections import Counter
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import zipfile

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
EVIDENCE = ROOT / 'research/task-001/evidence'
STATUSES = ['已实现且有证据', '部分实现', '未实现', '实现但行为疑似错误', '待验证', '原版规则不明', '不适用（有证据）']
JAR_HASH = '2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b'
sha = lambda b: hashlib.sha256(b).hexdigest()

def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def write_csv(path, records, fields):
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator='\n'); w.writeheader(); w.writerows(records)

def class_metadata(data):
    """Parse constant-pool UTF8 and declared Code hashes, without decompiling/exporting code."""
    f = io.BytesIO(data)
    def u(n):
        b = f.read(n)
        if len(b) != n: raise ValueError('truncated class')
        return int.from_bytes(b, 'big')
    assert u(4) == 0xcafebabe
    minor, major = u(2), u(2)
    cp = [None] * u(2)
    i = 1
    while i < len(cp):
        tag = u(1)
        if tag == 1: cp[i] = f.read(u(2)).decode('utf-8', errors='replace')
        elif tag in (3, 4): f.read(4)
        elif tag in (5, 6): f.read(8); i += 1
        elif tag in (7, 8, 16, 19, 20): cp[i] = u(2)
        elif tag in (9, 10, 11, 12, 17, 18): f.read(4)
        elif tag == 15: f.read(3)
        else: raise ValueError(f'unknown constant pool tag {tag}')
        i += 1
    u(2); this, parent = u(2), u(2)
    f.read(u(2) * 2)
    def attributes():
        result = []
        for _ in range(u(2)):
            name, length = cp[u(2)], u(4)
            result.append((name, f.read(length)))
        return result
    for _ in range(u(2)):
        f.read(6); attributes()
    methods = []
    for _ in range(u(2)):
        u(2); name, desc = cp[u(2)], cp[u(2)]
        attrs = attributes()
        code = next((v for k,v in attrs if k == 'Code'), None)
        body = code[8:8+int.from_bytes(code[4:8], 'big')] if code else None
        methods.append(dict(name=name, descriptor=desc, code_bytes=len(body) if body is not None else 0,
                            code_sha256=sha(body) if body is not None else None))
    return dict(name=cp[cp[this]], superclass=cp[cp[parent]] if parent else '', major=major,
                utf8=[x for x in cp if isinstance(x,str)], methods=methods)

def route(name):
    short = name.rsplit('/',1)[-1].removesuffix('.class').split('$')[0]
    special = {'BlockQuicksand':'C04/C05/C12', 'BlockMud':'C08/C09', 'BlockSoftQuicksand':'C06/C07/C10/C12',
        'AirEvent':'C22/C23', 'CustomVarPlayer':'C24/C25', 'MuddyEvent':'C24/C25/C26',
        'PotionStuck':'C21', 'CustomPotionEvent':'C21/C31', 'CustomRenderOverlayEvent':'C23/C32',
        'CustomRenderPlayerEvent':'C24', 'MudModelRenderer':'C24', 'EntityBubble':'C33', 'RenderBubble':'C33',
        'CustomRegister':'G09', 'MFQM':'C18/C19/C22/G08', 'CustomBucketEvent':'G02',
        'CustomFuelHandler':'G04', 'CustomWorldGen':'G07/G11', 'CustomWorldGenLakes':'G07',
        'CustomGenerationEvent':'G07', 'GenerateDesertTombs':'G07', 'GenerateMucusBlossom':'G07',
        'HandEvent':'G03', 'Fields':'G08', 'ItemMud':'C01/C13', 'ItemMeta':'G12', 'ItemMetaColor':'G12',
        'BlockBlossom':'G06', 'BlockBlossomSlab':'G06', 'BlockLarvae':'G01/G06', 'BlockLure':'G06',
        'BlockMeat':'G01/G06', 'BlockMeatHole':'G01/G06', 'BlockVoreHole':'G01/G06',
        'BlockSwallowingFlesh':'G01/G06', 'BlockSandstoneTrap':'G06', 'BlockCustomLilyPad':'G06',
        'BlockLeaves':'G06', 'BlockMoorGrass':'G01/G06'}
    if short in special: return special[short]
    if any(x in short for x in ('Rope','Hook','Rescue','LongStick','Fish2','Fish3')): return 'G03'
    if any(x in short for x in ('WadingBoots','LifeJacket','GasMask')): return 'C18/G04'
    if short in ('ModelBee','RenderBee','ModelVoreSlime','RenderMuddyBlob','RenderSandBlob','RenderSlimeHole',
                 'RenderTarSlime','RenderTarTreads','RenderTentacles','RenderVoreSlime'): return 'G05/G12'
    if '/Tileentity/' in name: return 'G06'
    if '/liquids/' in name or 'Bucket' in short or short.startswith('CustomMaterial'): return 'G02'
    if '/blocks/' in name: return 'G01'
    if '/items/' in name: return 'G04'
    if '/entity/' in name: return 'G05'
    return 'G12'

def legacy_air_map():
    def array(class_file, expected):
        text=(EVIDENCE/class_file).read_text().split('METHOD <clinit> ()V',1)[1]
        pattern=(r'\d+:\s+(?:iconst_([0-5])|bipush\s+(\d+))\s*\n'
                 r'\d+:\s+getstatic\s+#\d+\s+MoreFunQuicksandMod/main/MFQM\.(\w+):[^\n]+\n'
                 r'\d+:\s+aastore')
        result={int(a or b):name for a,b,name in re.findall(pattern,text)}
        assert set(result)==set(range(expected)),class_file
        return result
    rope=array('MoreFunQuicksandMod__main__entity__EntityRope.bytecode.txt',33)
    overlay=array('MoreFunQuicksandMod__main__client__CustomRenderOverlayEvent.bytecode.txt',30)
    air=(EVIDENCE/'MoreFunQuicksandMod__main__AirEvent.bytecode.txt').read_text()
    body=air.split('METHOD onLivingUpdateEvent ',1)[1].split('\nMETHOD ',1)[0]
    assert 'MoreFunQuicksandMod/main/entity/EntityRope.quicksandIDS:' in body
    skipped=sorted({int(x) for x in re.findall(r'\d+:\s+iload_3\s*\n\d+:\s+bipush (\d+)\s*\n\d+:\s+if_icmpeq',body)})
    assert skipped==[6,7,13,15,21]
    core={name:next(i for i,n in rope.items() if n==name) for name in ['QuicksandBlock','SoftQuicksandBlock','MudBlock']}
    assert core==dict(QuicksandBlock=4,SoftQuicksandBlock=17,MudBlock=29)
    assert not set(core.values()).intersection(skipped)
    return dict(air_field_owner='MoreFunQuicksandMod/main/entity/EntityRope',
        air_array=rope,skipped_indices=skipped,skipped_blocks={i:rope[i] for i in skipped},core_indices=core,
        render_array_owner='MoreFunQuicksandMod/main/client/CustomRenderOverlayEvent',render_array=overlay,
        note='Parsed from existing raw bytecode initialization instructions and AirEvent actual field owner; same field name does not imply same index ordering.')

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--baseline', required=True)
    p.add_argument('--original-jar', type=Path)
    p.add_argument('--vanilla-jar', type=Path)
    a = p.parse_args()
    baseline = subprocess.check_output(['git','rev-parse',a.baseline],cwd=ROOT,text=True).strip()
    out = HERE/'evidence'; out.mkdir(exist_ok=True)
    (out/'legacy-air-map.json').write_text(json.dumps(legacy_air_map(),ensure_ascii=False,indent=2)+'\n')
    units = rows(HERE/'audit-index.csv')
    assert len({r['id'] for r in units}) == len(units)
    assert all(r['status'] in STATUSES for r in units)
    classes, methods, entries = (rows(EVIDENCE/x) for x in ['classes.csv','methods.csv','archive_entries.csv'])
    assert len(classes) == 161 and len(methods) == 1955
    records = []
    for r in classes:
        name = r['class_path']; short = name.rsplit('/',1)[-1].removesuffix('.class')
        analysis = short.split('$')[0] + '.analysis.txt'
        bytecode = name.removesuffix('.class').replace('/','__')+'.bytecode.txt'
        assert (EVIDENCE/bytecode).is_file()
        assert (EVIDENCE/analysis).is_file()
        own = [m for m in methods if m['class_path'] == name]
        records.append(dict(class_path=name,superclass=r['superclass'],method_count=len(own),
            audit_units=route(name),analysis=analysis,bytecode=bytecode,sha256=r['sha256']))
    write_csv(out/'class-coverage.csv',records,list(records[0]))
    resources=[]
    for r in entries:
        name=r['path']
        if name.endswith(('/', '.class')): continue
        if name.endswith(('.png','.mcmeta')): group='图像/动画'; target='C35/G12'
        elif name.endswith('.ogg') or name.endswith('sounds.json'): group='声音';target='C34/G05'
        elif '/lang/' in name: group='语言';target='G12'
        else: group='元数据/归档';target='G12'
        resources.append(dict(path=name,category=group,audit_units=target,sha256=r['sha256']))
    write_csv(out/'resource-coverage.csv',resources,list(resources[0]))
    # Metadata appendix: no new decompiled source or asset content.
    lines=['# 全部原始类归属附录','', '由只读脚本从任务001清单生成。161类全部列出；类枚举覆盖不等于1955个方法均已逐指令完成语义审计。详见主目录的类别结论和未结构化生成缺口。','',
        '| 类 / 父类 | 自有方法数 | 机制归属 | 原证据 |','| --- | --- | --- | --- |']
    for r in records:
        lines.append(f"| {r['class_path']} / `{r['superclass']}` | {r['method_count']} | {r['audit_units']} | [analysis](../../../research/task-001/evidence/{r['analysis']}) · [bytecode](../../../research/task-001/evidence/{r['bytecode']}) |")
    (HERE/'CLASS_COVERAGE.md').write_text('\n'.join(lines)+'\n')
    registration=(ROOT/'research/task-001/reports/03_registration_and_network.md').read_text().splitlines()
    reglines=['# 全量静态注册归属附录','', '原始字符串、条件和定位来自任务001注册表；本次通过原JAR文件hash复核其输入，没有旧实例registry dump。这里仅复制注册元数据，不复制源码。49 Block + 43显式Item，不包含附带ItemBlock；16实体和13流体，条件调用不保证运行成功。','',
        '| 类型 | 原字段/类 | 原注册字符串 | 当前/后续归属 | 旧证据 |','| --- | --- | --- | --- | --- |']
    regcounts=Counter()
    for line in registration:
        parts=[x.strip() for x in line.strip('|').split('|')]
        if not line.startswith('| '): continue
        if len(parts)==6 and parts[0] in ('Block','Item'):
            kind,field,key,ctor,condition,source=parts
            target=route('MoreFunQuicksandMod/main/'+('blocks/' if kind=='Block' else 'items/')+ctor+'.class')
            if field in ('MudBlock','QuicksandBlock','SoftQuicksandBlock'): target='C01；已有独立注册，行为见三材料矩阵'
            reglines.append(f'| {kind} | {field} / {ctor} | {key} | {target}；{condition} | [MFQM {source}](../../../research/task-001/evidence/MFQM.analysis.txt) |');regcounts[kind]+=1
        elif len(parts)==8 and re.fullmatch('Entity[A-Za-z0-9]+',parts[0]):
            reglines.append(f'| Entity | {parts[0]} | {parts[1]} | {route("MoreFunQuicksandMod/main/entity/"+parts[0]+".class")}；{parts[6]} | [MFQM L{parts[7]}](../../../research/task-001/evidence/MFQM.analysis.txt#L{parts[7]}) |');regcounts['Entity']+=1
        elif len(parts)==3 and re.fullmatch('[A-Za-z]+Fluid',parts[0]):
            reglines.append(f'| Fluid | {parts[0]} | {parts[1]} | G02；{parts[2]} | [MFQM注册](../../../research/task-001/evidence/MFQM.analysis.txt#L954) |');regcounts['Fluid']+=1
    assert dict(regcounts)==dict(Block=49,Item=43,Entity=16,Fluid=13),regcounts
    (HERE/'REGISTRATION_COVERAGE.md').write_text('\n'.join(reglines)+'\n')
    original = {'available':False,'reason':'未提供--original-jar；不把任务001哈希当本次原件复核'}
    if a.original_jar:
        before=sha(a.original_jar.read_bytes());assert before==JAR_HASH
        with zipfile.ZipFile(a.original_jar) as z:
            checked=0;boat_refs=[];declared=0
            for r in entries:
                if r['path'].endswith('/'):continue
                data=z.read(r['path']);assert sha(data)==r['sha256'];checked+=1
                if r['path'].endswith('.class'):
                    m=class_metadata(data);declared+=len(m['methods'])
                    for word in m['utf8']:
                        if re.search(r'boat',word,re.I):boat_refs.append({'class':r['path'],'utf8':word})
            assert declared==1955
        assert sha(a.original_jar.read_bytes())==before
        original=dict(available=True,sha256=before,verified_files=checked,classes=161,declared_methods=declared,
                      png_verified=247,boat_utf8_references=boat_refs,jar_unchanged=True,
                      caution='零Boat字符串仅说明未找到显式引用；不能排除继承/间接/外部运行时机制。核心非Living分支另有人工控制流核对。')
    vanilla={'available':False}
    if a.vanilla_jar:
        selected={'net/minecraft/world/entity/vehicle/Boat.class':['getStatus','checkInWater','isUnderwater','floatBoat','tick','getGroundFriction','positionRider'],
            'net/minecraft/world/entity/LivingEntity.class':['travel','causeFallDamage','playBlockFallSound'],
            'net/minecraft/client/player/AbstractClientPlayer.class':['getFieldOfViewModifier'],
            'net/minecraft/client/renderer/ScreenEffectRenderer.class':['getOverlayBlock'],
            'net/minecraft/client/gui/Gui.class':['renderPlayerHealth'],
            'net/minecraft/world/level/block/state/BlockBehaviour.class':['getFluidState']}
        result=[]
        with zipfile.ZipFile(a.vanilla_jar) as z:
            for name,wanted in selected.items():
                data=z.read(name);meta=class_metadata(data)
                result.append(dict(class_path=name,class_sha256=sha(data),superclass=meta['superclass'],
                    methods=[m for m in meta['methods'] if m['name'] in wanted]))
        vanilla=dict(available=True,jar_sha256=sha(a.vanilla_jar.read_bytes()),classes=result,
                     note='Forge47.2.0映射构建；方法哈希定位所读字节码，不是实机结果。无反编译源码复制。')
    (out/'vanilla-methods.json').write_text(json.dumps(vanilla,ensure_ascii=False,indent=2)+'\n')
    protected=subprocess.check_output(['git','ls-tree','-r','--name-only',baseline],cwd=ROOT,text=True).splitlines()
    changed=[]
    for name in protected:
        # Respect the existing .gitattributes checkout form (gradlew.bat uses CRLF).
        data=subprocess.check_output(['git','cat-file','--filters',f'--path={name}',f'{baseline}:{name}'],cwd=ROOT)
        path=ROOT/name
        if not path.is_file() or path.read_bytes()!=data:changed.append(name)
    delta=subprocess.check_output(['git','diff',baseline,'--name-only'],cwd=ROOT,text=True).splitlines()
    untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT,text=True).splitlines()
    allowed='forge-1.20.1/docs/task-0035-audit/'
    outside=[n for n in delta+untracked if not n.startswith(allowed)]
    assert not changed and not outside,(changed,outside)
    summaries=[]
    for path in sorted((ROOT/'forge-1.20.1/docs/task-003/traces/phase2').glob('*.csv')):
        r=rows(path)
        if not r:continue
        drops=[float(b['y'])-float(c['y']) for b,c in zip(r,r[1:]) if int(c['tick'])-int(b['tick'])==1]
        summaries.append(dict(file=path.name,rows=len(r),first_tick=int(r[0]['tick']),
            max_accepted_downward_step=max(drops,default=0),fallDistance_recorded='fallDistance' in r[0],
            correction_count_recorded='correction_count' in r[0],sound_event_recorded='sound' in r[0]))
    (out/'historical-trace-audit.json').write_text(json.dumps(summaries,ensure_ascii=False,indent=2)+'\n')
    output=dict(baseline=baseline,status='PASS',audit_units=len(units),
        status_counts={s:sum(r['status']==s for r in units) for s in STATUSES},
        enumerated_classes=len(records),class_group_counts=dict(Counter(r['class_path'].split('/')[-2] for r in records)),
        enumerated_resources=len(resources),original=original,
        baseline_files_compared=len(protected),baseline_comparison='bytes after existing Git checkout filters',
        changed_baseline_files=changed,changes_outside_audit=outside,
        new_builds_run=0,new_game_sessions_run=0,
        limit='元数据/引用/范围核查通过，不代表行为验收通过；新人工验收结果保持空白。')
    (out/'audit-check.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(output,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
