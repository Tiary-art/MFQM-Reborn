"""Join the historical evidence, preserved content decisions and actual Forge exports."""
import collections
import json
import re
import sys
from pathlib import Path
from catalog import ROOT, MF, E, BLOCKS, DATA, RESOURCES, ASSETS, load

sys.path.insert(0, str(ROOT/'reconstruction/tooling'))
from common import read, write, ident, dump

O=ROOT/'reconstruction'
MAN=O/'manifest'
MAP=O/'mapping'
EVIDENCE='research/task-001/evidence/MFQM.analysis.txt'

def bindings():
    names={}
    arrays={}
    for i,line in enumerate(MF):
        arr=re.search(r'String\[\] (\w+) = new String\[\]\{(.*?)\}',line)
        if arr: arrays[arr[1]]=re.findall(r'"([^"]*)"',arr[2])
        direct=re.search(r'addName\(\(Object\)(?:new ItemStack\((\w+), 1, (\d+)\)|(\w+)), \(String\)"([^"]+)"',line)
        if direct:names[direct[1] or direct[3],int(direct[2] or 0)]=(direct[4],i+1)
        loop=re.search(r'new ItemStack\((\w+), 1, (ix\d*)\)',line)
        if loop and i+1<len(MF) and 'addName' in MF[i+1]:
            count=re.search(r'< (\d+);',MF[i-1])
            if not count:continue
            expression=MF[i+1].split('(String)',1)[1]
            array=re.search(r'(\w+)\[ix\d*\]',expression)
            literal=re.search(r'"([^"]*)"',expression)
            for d in range(int(count[1])):
                en=(literal[1] if literal else '')+(arrays[array[1]][d] if array else '')
                names[loop[1],d]=(en.strip(),i+2)
    return names

def declared_creative(owner):
    path=E/(owner+'.analysis.txt')
    if not path.exists():return {}
    code=path.read_text(encoding='utf-8')
    match=re.search(r'void (?:func_(?:149666|150895)_a|getSubBlocks)\([^\n]+\{(.*?)\n\d+:     }',code,re.S)
    if not match:return {}
    return {int(d):int(line) for line,d in re.findall(r'(\d+):\s*\w+\.add\(new ItemStack\((?:\(Block\))?\w+, 1, (\d+)\)',match[1])}

def run():
    curated=json.loads((DATA/'r1_content.json').read_text(encoding='utf-8'))
    impl={(e['legacy'],e['damage']):e for e in curated}
    runtime=json.loads((ROOT/'deliverables/r1/logs/r1-runtime.json').read_text(encoding='utf-8'))
    rr=runtime['registries']
    shown=collections.defaultdict(list)
    for stack in runtime['creative']:shown[stack['id']].append(stack)
    write(MAN/'MODERN_REGISTRY_RUNTIME.csv',[dict(kind=k,registry_id=id,scenario='public Forge GameTest; default features, operator') for k,ids in rr.items() for id in ids])
    write(MAN/'MODERN_CREATIVE_RUNTIME.csv',[dict(order=i,tab='mfqm:materials',locale='en_us',**row) for i,row in enumerate(runtime['creative'])])
    atlas_path=ROOT/'deliverables/r1/logs/client-atlas-100.json'
    atlas={x['id']:x for x in json.loads(atlas_path.read_text(encoding='utf-8'))} if atlas_path.exists() else {}
    names=bindings()
    language={}
    for index,text in enumerate((E/'assets__morefunquicksandmod__lang__en_US.lang').read_text(encoding='utf-8').splitlines(),1):
        key,sep,value=text.partition('=')
        if sep:language[key]=(value,index)
    old=read(MAN/'ORIGINAL_REGISTRY.csv')
    objects={};variants=[];parity=[];creatives=[];name_rows=[];conditions=[]
    blocks={b['legacy_id']:b for b in BLOCKS}
    english=json.loads((ASSETS/'lang/en_us.json').read_text(encoding='utf-8'))
    private_manifest=ROOT/'deliverables/r1/logs/private-entry-hashes.json'
    packed=json.loads(private_manifest.read_text(encoding='utf-8')) if private_manifest.exists() else {}
    for row in old:
        if row['kind']=='ITEMBLOCK_VARIANT':continue
        kind=row['kind'];key=row['registered_name']
        expr=row['expression'];line=int(row['line']);field=''
        match=re.search(r'\((?:Block|Item|Fluid)\)(\w+)',expr)
        if match:field=match[1]
        identity=key or field or expr
        oid=ident('object',kind+':'+identity)
        spec=blocks.get(key,{})
        owner=spec.get('legacy_class','')
        if not owner and kind=='ITEM' and key:
            match=re.search(r'new (\w+)\(',MF[line-2]);owner=match[1] if match else 'UNKNOWN'
        condition='UNKNOWN enclosing branch' if kind not in ['ITEM','BLOCK'] or not key else '!BoP' if line in (1848,1852) else 'BootsID == 1' if line==1858 else 'static lifecycle call'
        obj=objects.setdefault(oid,dict(original_object_id=oid,kind=kind,legacy_registry_name=key or 'UNKNOWN',field=field,owner=owner or 'UNKNOWN',phase=('postInit' if line>=1489 else 'preInit') if row['evidence_ref'].endswith('/MFQM.analysis.txt') else 'helper',condition=condition,r0_call_ids=[],line=line,evidence_ref=row['evidence_ref']))
        if kind in ('ENTITY','TILEENTITY','NETWORK','WORLDGEN'):
            classes=re.findall(r'(\w+)\.class',expr)
            created=re.search(r'new (\w+)\(',expr)
            if classes:obj['owner']=classes[1] if kind=='NETWORK' else classes[0]
            elif created:obj['owner']=created[1]
            obj['registration_expression']=expr
        if kind=='FLUID':
            declaration=next((x for x in MF if re.search(r'\b'+field+r' = new \w+Fluid\(',x)),None)
            if declaration:
                make=re.search(r'= new (\w+)\(([^)]*)',declaration)
                if make:
                    cls,arg=make.groups()
                    literal=re.search(r'"([^"]+)"',arg)
                    ctor=load(cls)
                    fallback=re.search(r'super\("([^"]+)"',ctor)
                    obj.update(owner=cls,resolved_registry_literal=(literal or fallback)[1] if literal or fallback else 'UNKNOWN',
                        constructor_ref=declaration.split(':',1)[0]+'; '+cls+'.analysis.txt')
        obj['r0_call_ids'].append(row['original_id'])
        conditions.append(dict(original_object_id=oid,condition=condition,call_id=row['original_id'],proof='STATIC; runtime NOT_RUN',evidence_ref=row['evidence_ref'],line=line))
        if not key or kind not in ('BLOCK','ITEM'):continue
        declared=declared_creative(owner);dnames={d:v for (f,d),v in names.items() if field==f}
        body=load(owner) if (E/(owner+'.analysis.txt')).is_file() else ''
        source=MF[line-2]+'\n'+body
        basename=re.search(r'(?:func_149663_c|func_77655_b)\("([^"]+)"',source)
        base=('tile.' if kind=='BLOCK' else 'item.')+(basename[1] if basename else key)
        lang_keys={}
        for lang_key in language:
            match=re.fullmatch(re.escape(base)+r'(\d*)\.name',lang_key)
            if match:lang_keys[int(match[1] or 0)]=lang_key
        suffixes=re.search(r'String\[\] items = new String\[\]\{([^}]+)',body)
        if suffixes:
            for d,suffix in enumerate(re.findall(r'"([^"]+)"',suffixes[1])):
                if 'error' in suffix.lower():continue
                token=base+'.'+suffix+'.name'
                if token in language:lang_keys[d]=token
        damages=sorted({0,*declared,*dnames,*lang_keys,*[d for k,d in impl if k==key]})
        for damage in damages:
            curated_row=impl.get((key,damage),{})
            name,ln=dnames.get(damage,('',line))
            lang_key=lang_keys.get(damage,'')
            lang_name,lang_line=language.get(lang_key,('',0))
            conflict=bool(name and lang_name and name!=lang_name)
            if not name:name=lang_name or curated_row.get('en','')
            id=curated_row.get('id',spec.get('id','') if damage==0 or key=='Mud' else '')
            modern='mfqm:'+id if id else ''
            sid=ident('stack',oid+'#'+str(damage))
            vis='INT_OVERLOAD_DISPATCH_UNKNOWN' if owner in ('BlockMorass','BlockTent','BlockMoorGrass') and damage in declared else 'EXPLICIT' if damage in declared else 'EMPTY_OVERRIDE' if owner=='BlockSandstoneTrap' else 'UNKNOWN'
            model=f'forge-1.20.1/src/main/resources/assets/mfqm/models/item/{id}.json' if id else ''
            textures=curated_row.get('textures',[])
            refs=[('assets/mfqm/textures/'+('item' if '/items/' in t else 'block')+'/original/'+Path(t).stem.lower()+'.png') for t in textures]
            stack=dict(original_object_id=oid,original_stack_id=sid,original_owner=owner,legacy_registry_name=key,old_damage=damage,condition=condition,creative_visibility=vis,original_display_name=name or 'UNKNOWN',original_name_evidence=f'MFQM.analysis.txt:{ln}' if (damage in dnames) else curated_row.get('ref','UNKNOWN'),original_icon_evidence=curated_row.get('ref','UNKNOWN'),modern_registry_id=modern,modern_variant_encoding=f'BlockStateTag.depth={damage}' if key=='Mud' and damage else ('separate Item ID' if damage and id else 'default' if id else 'UNMAPPED'),modern_creative_tab='mfqm:materials' if modern in shown else '',modern_english_name=english.get('item.mfqm.'+id,english.get('block.mfqm.'+id,'')),modern_chinese_name_status='project localization' if id else 'UNKNOWN',model_path=model,original_resource_path=';'.join(textures),imported_resource_sha256=';'.join(packed.get(t,'') for t in refs),runtime_registered=modern in rr['ITEM'],runtime_visible=modern in shown and (key!='Mud' or damage==0 or any(str(damage) in s['nbt'] for s in shown[modern])),name_parity='MATCH' if name and name==english.get('item.mfqm.'+id,english.get('block.mfqm.'+id,'')) else 'UNKNOWN',asset_bind='PACKAGED' if refs and all(t in packed for t in refs) else 'VANILLA_WOOL' if curated_row.get('shape')=='wool' else 'UNKNOWN',actual_visual='NOT_INDIVIDUALLY_ASSESSED',behavior_parity='DISPLAY_SAMPLE' if curated_row.get('mode')=='sample' else 'UNKNOWN',dedicated_server='REGISTRY_GAMETEST' if modern in rr['ITEM'] else 'NOT_RUN',save_compat='STACK_NBT_ROUNDTRIP' if modern in shown else 'NOT_RUN',evidence_type='DECOMPILED_INTERPRETATION',evidence_ref=row['evidence_ref'],blocker='' if id else 'named damage; state/placement/creative output not established',next_action='compare legacy creative dump and packaged client',last_verified='2026-11-19')
            stack.update(legacy_unlocalized_key=lang_key or 'UNKNOWN',old_english_lang=lang_name,
                language_file_line=lang_line or '',name_source_conflict=conflict)
            if conflict:stack['name_parity']='CONFLICT_OLD_RESOLUTION_NOT_RUN'
            if lang_name and damage not in dnames:
                stack['original_name_evidence']=f'assets__morefunquicksandmod__lang__en_US.lang:{lang_line}'
            tabcall=re.search(r'(?:func_149647_a|func_77637_a)\(([^)]+)\)',source)
            stack.update(legacy_tab_expression=tabcall[1] if tabcall else 'UNKNOWN / inherited',
                         original_stack_quantity=1,nbt_predicate='no explicit extra NBT in enumerated exemplar')
            if key=='SoftSnow' and damage==1:
                stack['blocker']='Icon depends on WLD_MIC; tested default branch only'
            if id and key=='Morass' and damage>0 and lang_name and lang_name!=stack['modern_english_name']:
                stack['name_parity']='CONFLICT_OLD_RESOLUTION_NOT_RUN' if damage in dnames else 'LANG_DIFF'
            if not id:
                stack['blocker']={
                    'BrownClay':'world depth; standard creative override appends only damage 0 and 4',
                    'WaxWood':'orientation state; standard creative override appends only damage 0 and 4',
                    'MoorGrass':'int overload dispatch unconfirmed; foliage tint and shear/drop variants',
                    'Tendrils':'int overload dispatch unconfirmed; crossed plant geometry and placement',
                    'Morass':'language-table damage beyond explicit append range 1..8'
                }.get(key,stack['blocker'])
            if modern in atlas and stack['runtime_visible']:
                model=atlas[modern]
                stack['gui_model_after_reload']='MISSING' if model['missing_model'] or model['particle']=='minecraft:missingno' else 'RENDERED_MODEL_RESOLVED'
            else:stack['gui_model_after_reload']='NOT_RUN'
            parity.append(stack)
            variants.append({k:stack[k] for k in ['original_stack_id','original_object_id','old_damage','original_owner','legacy_registry_name','original_display_name','creative_visibility','condition','evidence_ref','legacy_tab_expression','original_stack_quantity','nbt_predicate']})
            name_rows.append({k:stack[k] for k in ['original_stack_id','original_display_name','original_name_evidence','modern_english_name','modern_chinese_name_status','name_parity','legacy_unlocalized_key','old_english_lang','language_file_line','name_source_conflict']})
            if damage in declared:creatives.append(dict(original_stack_id=sid,owner=owner,damage=damage,method='getSubBlocks(int,CreativeTabs,List)' if owner in ('BlockMorass','BlockTent','BlockMoorGrass') else 'func_149666_a' if kind=='BLOCK' else 'func_150895_a',line=declared[damage],evidence_ref=f'research/task-001/evidence/{owner}.analysis.txt',status='static append; tab membership conditional'))
    for index,text in enumerate(MF,1):
        tab=re.search(r'(\w+) = new CreativeTabsMFQM\(CreativeTabs.getNextID\(\), "([^"]+)"',text)
        if tab:
            oid=ident('object','CREATIVE_TAB:'+tab[2])
            objects[oid]=dict(original_object_id=oid,kind='CREATIVE_TAB',legacy_registry_name=tab[2],
                field=tab[1],owner='CreativeTabsMFQM',phase='preInit',condition='static lifecycle construction',
                r0_call_ids=[],line=index,evidence_ref=EVIDENCE)
    for obj in objects.values():obj['r0_call_ids']=';'.join(obj['r0_call_ids'])
    for file,rows in [('ORIGINAL_REGISTRY_OBJECTS',list(objects.values())),('ORIGINAL_ITEMSTACK_VARIANTS',variants),('ORIGINAL_CREATIVE_OUTPUT',creatives),('ORIGINAL_NAME_BINDINGS',name_rows),('ORIGINAL_DEPENDENCY_CONDITIONS',conditions)]:write(MAN/(file+'.csv'),rows)
    write(MAP/'CONTENT_PARITY_MATRIX.csv',parity)
    dump(O/'checks/REGISTRY_COUNT_RECONCILIATION.json',dict(r0_call_or_usage_rows=len(old),registration_callsites=len(conditions),candidate_objects=len(objects),identified_stacks=len(variants),static_explicit_creative_appends=len(creatives),legacy_actual_creative_total=None,legacy_runtime='NOT_RUN',modern_registry={k:len(v) for k,v in rr.items()},modern_items_by_creative_class=dict(collections.Counter(s['type'] for s in runtime['creative'])),modern_creative_stacks=len(runtime['creative']),unmapped_identified_stacks=sum(not x['modern_registry_id'] for x in parity),content_catalog=len(curated),new_ids=sum(e['mode'] not in ['bucket','block'] for e in curated)))
if __name__=='__main__':run()
