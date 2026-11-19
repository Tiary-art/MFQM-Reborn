"""Add class-specific method locators, recovered branch inputs and linked stack outcomes."""
import collections
import re
from content_database import MAN,MAP,ROOT,E,load,read,write

def run():
    parity=read(MAP/'CONTENT_PARITY_MATRIX.csv')
    groups=collections.defaultdict(list)
    for s in parity:groups[s['original_owner']].append(s)
    rows=[]
    specials={'MFQM':{'<init>','preInit','load','postInit'},'CustomRegister':{'registerItem','registerBlock'},
              'CreativeTabsMFQM':{'<init>','func_78016_d'},'ItemMud':{'func_77624_a'}}
    relevant={'func_149666_a','getSubBlocks','func_150895_a','func_77667_c','func_149691_a','func_149651_a',
              'func_77617_a','func_94581_a','func_77647_b','func_77653_i','getIcon','getSubItems'}
    for m in read(MAN/'ORIGINAL_METHODS.csv'):
        owner=m['owner'];simple=owner.split('/')[-1];name=m['name']
        if name not in relevant|specials.get(simple,set()) and not (name=='<init>' and '/items/' in owner):continue
        path=E/(simple+'.analysis.txt')
        if not path.is_file():continue
        lines=path.read_text(encoding='utf-8').splitlines()
        decl=re.escape(simple if name=='<init>' else name)
        loc=[i for i,x in enumerate(lines) if re.search(r':     (?:public|private|protected) .*(?<!\w)'+decl+r'\(',x)]
        if len(loc)!=1:continue
        start=loc[0];end=next((i for i in range(start+1,len(lines)) if lines[i].endswith(':     }')),start)
        sub=lines[start:end+1];v=[]
        for line in sub:
            marker=line.split(':',1)[0]
            for value in re.findall(r'"((?:morefunquicksandmod:)[^"]+)"',line):v.append(marker+' '+value)
            if 'add(new ItemStack' in line:v.append(marker+' damage='+line.rsplit(',',1)[-1].split(')')[0].strip())
        rows.append(dict(method_id=m['member_id'],owner=owner,method=name,descriptor=m['descriptor'],
            cfr_start=start+1,cfr_end=end+1,branch_evidence=' | '.join(v),evidence_ref=str(path.relative_to(ROOT)),
            bytecode_ref=m['evidence_ref'],status='BYTECODE_SIGNATURE; DECOMPILED_INTERPRETATION'))
    write(MAN/'R1_METHOD_EVIDENCE.csv',rows)
    by=collections.defaultdict(list)
    for r in rows:by[r['owner']].append(r)
    for owner,methods in by.items():
        path=ROOT/'docs/reconstruction/original/classes'/(owner+'.md')
        text=path.read_text(encoding='utf-8').split('\n## R1 注册与显示证据')[0]
        text+='\n## R1 注册与显示证据\n\n'
        for r in methods:
            text+=f"- `{r['method']}{r['descriptor']}` · CFR {r['cfr_start']}–{r['cfr_end']}"
            if r['branch_evidence']:text+=' · '+r['branch_evidence']
            text+='\n'
        group=groups[owner.split('/')[-1]]
        if group:
            text+='\n|旧对象|damage|旧名称候选|现代物品|\n|---|---:|---|---|\n'
            for s in group:text+=f"|{s['legacy_registry_name']}|{s['old_damage']}|{s['original_display_name']}|`{s['modern_registry_id'] or '未映射'}`|\n"
        text+='\n上述行号指向 research/task-001/evidence 中同类的分析文本。模型、名称冲突、行为与存档验证按 original_stack_id 查询 CONTENT_PARITY_MATRIX。\n'
        path.write_text(text,encoding='utf-8')
if __name__=='__main__':run()
