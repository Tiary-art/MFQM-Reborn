"""Validate R1 identities and references in both complete distributable archives."""
import argparse
import hashlib
import json
import sys
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree
from content_database import MAN, MAP, ROOT, DATA, O, read, dump, declared_creative, bindings

D=ROOT/'deliverables/r1'
def digest(data):return hashlib.sha256(data).hexdigest()
def unique(values):
    values=list(values)
    if len(values)!=len(set(values)):raise ValueError('duplicate identity')
def assert_models(z):
    files=set(z.namelist())
    parents={}
    for path in sorted(files):
        if not path.startswith(('assets/mfqm/models/','assets/mfqm/blockstates/')) or not path.endswith('.json'):continue
        doc=json.loads(z.read(path))
        def visit(obj):
            if isinstance(obj,list):
                for value in obj:visit(value)
            if not isinstance(obj,dict):return
            for key,value in obj.items():
                if key in ('model','parent') and isinstance(value,str) and value.startswith('mfqm:'):
                    target='assets/mfqm/models/'+value[5:]+'.json'
                    if target not in files:raise ValueError('missing model '+target)
                    if key=='parent':parents[path]=target
                if key=='textures':
                    for tex in value.values():
                        if tex.startswith('mfqm:') and 'assets/mfqm/textures/'+tex[5:]+'.png' not in files:
                            raise ValueError('missing texture '+tex)
                visit(value)
        visit(doc)
    for path in parents:
        seen=set()
        while path in parents:
            if path in seen:raise ValueError('parent cycle '+path)
            seen.add(path);path=parents[path]
    return sum(p.startswith('assets/mfqm/models/') for p in files)

def audit(public,private,original):
    catalog=json.loads((DATA/'r1_content.json').read_text())
    stacks=read(MAN/'ORIGINAL_ITEMSTACK_VARIANTS.csv');objects=read(MAN/'ORIGINAL_REGISTRY_OBJECTS.csv')
    matrix=read(MAP/'CONTENT_PARITY_MATRIX.csv')
    unique(s['original_stack_id'] for s in stacks)
    unique((s['original_object_id'],s['old_damage']) for s in stacks)
    unique(e['id'] for e in catalog);unique((e['legacy'],e['damage']) for e in catalog)
    object_ids={r['original_object_id'] for r in objects}
    assert all(s['original_object_id'] in object_ids for s in stacks)
    assert {s['original_stack_id'] for s in stacks}=={r['original_stack_id'] for r in matrix}
    runtime={(r['kind'],r['registry_id']) for r in read(MAN/'MODERN_REGISTRY_RUNTIME.csv')}
    assert runtime=={(r['kind'],r['registry_id']) for r in read(MAN/'MODERN_REGISTRY.csv')}
    baseline=json.loads((O/'checks/R1_BASELINE.json').read_text())
    frozen={(kind,k) for kind,items in baseline['r0_registry'].items() for k in items}
    new={('ITEM','mfqm:'+r['id']) for r in catalog if r['mode'] not in ('block','bucket')}
    assert frozen<=runtime and new==runtime-frozen
    assert set(declared_creative('BlockBrownClay'))=={0,4} and set(declared_creative('BlockMorass'))==set(range(1,9))
    assert bindings()['SoftSnowBlock',1][0]=='Soft Ash'
    result={}
    for mode,path in [('public',public),('private',private)]:
        if path is None:
            result[mode]={'status':'NOT_RUN'};continue
        with zipfile.ZipFile(path) as z:
            assert z.testzip() is None
            names=set(z.namelist());model_count=assert_models(z)
            assert 'art/tiary/mfqm/registry/RestoredItems.class' in names
            assert '0.1.0-r1-content' in z.read('META-INF/mods.toml').decode()
            assert json.loads(z.read('data/mfqm/r1_content.json'))==catalog
            langs=[json.loads(z.read(f'assets/mfqm/lang/{locale}.json')) for locale in ['en_us','zh_cn']]
            for row in catalog:
                key=('block' if row['mode']=='block' else 'item')+'.mfqm.'+row['id']
                assert all(lang.get(key) for lang in langs),key
                assert 'assets/mfqm/models/item/'+row['id']+'.json' in names
            if mode=='public':
                assert not any(n.endswith(('.png','.ogg')) for n in names)
                assert 'assets/mfqm/original_texture_bindings.json' not in names
            else:
                expected=json.loads((D/'logs/private-entry-hashes.json').read_text())
                assert all(digest(z.read(name))==h for name,h in expected.items())
                assert json.loads(z.read('assets/mfqm/textures/block/original/mucus_flowing.png.mcmeta'))['animation']['height']==16
            result[mode]=dict(status='PASS',sha256=digest(path.read_bytes()),models=model_count,entries=len(names),
                               png=sum(n.endswith('.png') for n in names),ogg=sum(n.endswith('.ogg') for n in names))
    if original is not None:
        assert digest(original.read_bytes())==baseline['original_jar_sha256']
    result['original_input']='PINNED_SHA_VERIFIED' if original else 'NOT_RUN'
    dump(O/'checks/R1_JAR_ASSET_AUDIT.json',result)
    gaps=[s for s in matrix if not s['modern_registry_id']]
    assert gaps and all(s['runtime_registered']=='False' for s in gaps)
    dump(O/'checks/R1_VALIDATION.json',dict(status='PASS_WITHIN_CHECKED_SCOPE',registries=len(runtime),
        retained_base_ids=len(frozen),new_ids=len(new),indexed_legacy_stacks=len(stacks),unmapped_stacks=len(gaps),
        simulated_brown_clay=[0,4],simulated_morass_int_overload=list(range(1,9)),original_input=result['original_input'],
        private_package=result['private']['status'],universe_closed=False))
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--private',type=Path);parser.add_argument('--original',type=Path)
    a=parser.parse_args();audit(D/'mfqm-reborn-r1-public.jar',a.private,a.original)
