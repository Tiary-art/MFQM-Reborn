#!/usr/bin/env python3
"""Conservative joins: unknowns retained; no name-only semantic parity claims."""
import argparse,re,json,collections
from pathlib import Path
from common import *
def run(root,out):
 files=read(out/'manifest/ORIGINAL_JAR_FILES.csv');classes=read(out/'manifest/ORIGINAL_CLASSES.csv');methods=read(out/'manifest/ORIGINAL_METHODS.csv');fields=read(out/'manifest/ORIGINAL_FIELDS.csv');modern=read(out/'manifest/NEW_PROJECT_INVENTORY.csv');regs=[];maps=[];matrix=[]
 catalog=json.loads((root/'forge-1.20.1/src/main/resources/data/mfqm/legacy_block_catalog.json').read_text(encoding='utf-8'))
 bysimple={s['legacy_class']:s for s in catalog}
 for p in sorted((root/'research/task-001/evidence').glob('*.analysis.txt')):
  for line in p.read_text(encoding='utf-8').splitlines():
   number,_,body=line.partition(':');number=number.strip()
   if not number.isdigit():continue
   for call in re.finditer(r'\.(registerBlock|registerItem|registerFluid|registerModEntity|registerTileEntity|registerMessage|registerWorldGenerator)\((.*)',body):
    kind={'registerBlock':'BLOCK','registerItem':'ITEM','registerFluid':'FLUID','registerModEntity':'ENTITY','registerTileEntity':'TILEENTITY','registerMessage':'NETWORK','registerWorldGenerator':'WORLDGEN'}[call[1]]
    values=re.findall(r'"([^"]+)"',call[2]);rid=ident('original-registration',str(p.relative_to(root))+':'+number+call[1]);regs.append(dict(original_id=rid,kind=kind,registered_name=values[-1]if values else'',expression=body.strip(),evidence_ref=str(p.relative_to(root)),line=number,evidence_type='DECOMPILED_INTERPRETATION',metadata='UNKNOWN_SEE_VARIANTS',visibility='UNKNOWN_CONDITIONAL_PATH_NOT_EXECUTED',status='STATIC_CALLSITE_NOT_RUNTIME_REGISTRY'))
   # Explicit metadata constants only; loops/arrays remain unknown rather than invented variants.
   for m in re.finditer(r'new ItemStack\((\w+),\s*1,\s*(\d+)\)',body):
    regs.append(dict(original_id=ident('variant',str(p.relative_to(root))+':'+number+m[0]),kind='ITEMBLOCK_VARIANT',registered_name=m[1],expression=body.strip(),evidence_ref=str(p.relative_to(root)),line=number,evidence_type='DECOMPILED_INTERPRETATION',metadata=m[2],visibility='NAME_CALLSITE_ONLY_NOT_CREATIVE_PROOF',status='PARTIAL_VARIANT_CENSUS'))
 write(out/'manifest/ORIGINAL_REGISTRY.csv',regs)
 mids=read(out/'manifest/MODERN_REGISTRY.csv');md={r['registry_id']:r['source']for r in mids if r['kind']=='BLOCK'}
 # Every original file/class/member/callsite gets a row, not just selected materials.
 for kind,rows,key,path,symbol,desc in [('FILE',files,'original_file_id','path','path',None),('CLASS',classes,'class_id','archive_path','class_name',None),('METHOD',methods,'member_id',None,'name','descriptor'),('FIELD',fields,'member_id',None,'name','descriptor'),('REGISTRATION',regs,'original_id',None,'registered_name',None)]:
  for x in rows:
   owner=x.get('owner',x.get('class_name',''));simple=owner.split('/')[-1];s=bysimple.get(simple);paths=[];ids=[]
   if kind=='REGISTRATION'and x['kind']=='BLOCK':s=next((v for v in catalog if v['legacy_id']==x['registered_name']),None)
   if s:
    ids=['mfqm:'+s['id']];paths=[md[ids[0]],'forge-1.20.1/src/main/java/art/tiary/mfqm/content/LegacyBlocks.java'];maps.append(dict(original_id=x[key],modern_id=ident('registry','BLOCK:'+ids[0]),modern_path=paths[0],mapping_kind='CATALOG_IDENTITY_ONLY',status='PARTIAL',evidence_ref='forge-1.20.1/src/main/resources/data/mfqm/legacy_block_catalog.json'))
   row=dict(original_id=x[key],original_kind=kind,original_path=x.get(path,'')if path else x.get('evidence_ref',''),original_symbol=x.get(symbol,''),original_descriptor=x.get(desc,'')if desc else'',original_sha256=x.get('sha256',''),evidence_ref=x.get('evidence_ref','reconstruction/manifest/ORIGINAL_JAR_FILES.csv'),evidence_type='DECOMPILED_INTERPRETATION'if kind=='REGISTRATION'else'BYTECODE_CONFIRMED'if kind in['METHOD','FIELD','CLASS']else'BYTE_INPUT_CONFIRMED',evidence_confidence='IDENTITY_ONLY_SEMANTICS_UNKNOWN',behavior_summary='签名/来源已登记；语义深度状态见类档案，不能视为行为等价',modern_ids=';'.join(ids),modern_paths=';'.join(paths),semantic_mapping='PARTIAL'if ids else'UNKNOWN',registration_status='SOURCE_MAPPED'if ids else'UNKNOWN',asset_status='UNKNOWN',name_status='UNKNOWN',behavior_status='APPROXIMATION'if ids else'UNKNOWN',compat_status='NOT_RUN',oracle_status='RESEARCH_ONLY',visual_test_status='NOT_RUN_R0',last_verified='2026-11-19',blocker='Member-level semantics / dynamic equivalence not established',owner='reconstruction',next_action='R1 registration/variant closure'if kind=='REGISTRATION'else'Review class dossier and work package')
   matrix.append(row)
 write(out/'mapping/RESTORATION_MATRIX.csv',matrix);write(out/'mapping/ORIGINAL_TO_MODERN.csv',maps)
 # Every modern source/resource/config gets a review record, including necessary bridges.
 audit=[]
 for m in modern:
  p=root/m['path'];txt=p.read_text(encoding='utf-8')if p.suffix not in['.png','.ogg']else'';suspects=[word for word in ['motionScale','MaterialProfile','setDeltaMovement','entityInside','setStuck','register','minecraft:block/','water_bucket','worldgen','muddy','FOV']if word.lower()in txt.lower()]
  decision='KEEP_EXACT_OR_NECESSARY'if m['role']in['MODERN_BRIDGE','DEV_ONLY']else'KEEP_TEMPORARILY'if suspects else'BLOCKED_EVIDENCE'
  audit.append(dict(candidate_id=ident('audit',m['path']),new_path=m['path'],new_symbol=p.stem,modern_role=m['role'],original_refs=';'.join(s['legacy_class']for s in catalog if s['legacy_class']in txt)or m['original_refs'],why_suspected_approximation=';'.join(suspects)or'No automatic parity proof; manual review required',difference_evidence=m['path'],decision=decision,replacement_plan='Do not delete; close original branches and paired tests in module PR',dependencies='reconstruction/mapping/MODERN_DEPENDENCIES.csv',side_effects='Review motion/tick/render/state writes before replacement',save_network_risks='COMPATIBILITY_FREEZE.csv must remain unchanged',paired_test_refs='reconstruction/mapping/BEHAVIOR_CASES.csv',rollback_commit='BASELINE_IMPORT',implementation_status='AUDIT_ONLY_NO_RUNTIME_CHANGE',proof_status='STATIC_TRIAGE_NOT_FULL_SEMANTIC_REVIEW'))
 write(out/'mapping/AI_APPROXIMATION_AUDIT.csv',audit);write(out/'mapping/CODE_CLEANUP_DECISIONS.csv',audit)
 deps=[]
 for m in modern:
  if m['kind']!='JAVA':continue
  for target in re.findall(r'import\s+(art\.tiary\.mfqm\.[\w.*]+);',(root/m['path']).read_text(encoding='utf-8')):deps.append(dict(source=m['modern_id'],target=target,kind='JAVA_IMPORT_ONLY',status='PARTIAL_NOT_COMPLETE_CALL_GRAPH'))
 write(out/'mapping/MODERN_DEPENDENCIES.csv',deps)
 usage=read(root/'docs/phase9/TEXTURE_MAPPING.csv')
 for row in usage:row['r0_status']='HISTORICAL_BINDING_ONLY_WINDOWS_USER_GAP_OPEN';row['visual_status']='NOT_RUN_R0'
 write(out/'mapping/RESOURCE_USAGE.csv',usage)
 # Class-specific directories, exact signatures and edge summaries; no generic empty class files.
 mm=collections.defaultdict(list);ff=collections.defaultdict(list)
 for x in methods:mm[x['class_id']].append(x)
 for x in fields:ff[x['class_id']].append(x)
 for c in classes:
  p=root/'docs/reconstruction/original/classes'/(c['class_name']+'.md');p.parent.mkdir(parents=True,exist_ok=True)
  s=bysimple.get(c['class_name'].split('/')[-1]);mapped=s['id']if s else'UNKNOWN / modern bridge review'
  text=f"# {c['class_name']}\n\nID `{c['class_id']}`；class SHA `{c['sha256']}`；原 JAR SHA `{files[0]['input_sha256']}`。\n\n状态 **INDEXED / NOT_ANALYZED**（除重点模块报告给出的分支外）。super `{c['super']}`；interfaces `{c['interfaces']}`；access `{c['access']}`；annotations/attributes `{c['attributes']}`。内部类宿主 `{c['class_name'].split('$')[0]}`；客户端/服务端语义 UNKNOWN，不能按包名断言。\n\n原始字节码证据位于仓库 `{c['evidence_ref']}`，METHOD name+descriptor 节及十进制 offset；本轮从私人 JAR 直接读取，未提交 class 字节。工具 jawa2.2.0。反编译不是原作者源代码。现代身份候选 `{mapped}`，只映射身份，不代表机制一致。调用边以 member_id 查询 CALL_GRAPH.csv；重要注解值尚未解码。\n\n## 字段目录\n\n"
  text+='\n'.join('- `'+x['member_id']+'` `'+x['name']+':'+x['descriptor']+'` access '+x['access']for x in ff[c['class_id']])or'无声明字段。'
  text+='\n\n## 方法目录\n\n'+'\n'.join('- `'+x['member_id']+'` `'+x['name']+x['descriptor']+'` access '+x['access']+'，'+x['code_bytes']+' code bytes；语义 NOT_ANALYZED'for x in mm[c['class_id']])
  text+='\n\n## 证据与待证问题\n\n字段/方法签名 BYTECODE_CONFIRMED；副作用/随机顺序/客户端权威/外部继承语义尚未逐方法闭合。不得视为无调用的死代码。重点模块分析见 reconstruction/reports/DEEP_FIRST_BATCH.md；完整方法和字段外键见 ORIGINAL_METHODS/FIELDS.csv。\n\n## 验证计划\n\n用 CALL_GRAPH 按类和 JVM descriptor 取调用/字段写入，逐条比对历史 bytecode，再做同输入 oracle 与现代 tick/状态轨迹。原1.7.10游戏本轮 NOT_RUN，现代正式安装 NOT_RUN；签名与反编译定位不是行为 PASS。\n'
  topics={'MFQM':'注册和Stuck委派：MFQM.analysis.txt:602、954、968、1380、1480、2641；重点报告§1/§3。','CustomRegister':'反射注册分派：CustomRegister.analysis.txt:35起；动态参数尚未闭合；重点报告§1。','BlockQuicksand':'接触坐标/强制Stuck：BlockQuicksand.analysis.txt:88–140、288–332；重点报告§2。','BlockMud':'metadata深度和safe覆盖：BlockMud.analysis.txt:199–247、483–545、618起；重点报告§2/§4。','BlockSoftQuicksand':'独立幂指数/175/metadata图标：BlockSoftQuicksand.analysis.txt:104、265、350；重点报告§2/§4。','CustomPotionEvent':'UUID更新/level续租/jumpMovementFactor：历史reports/03_stuck_and_tick_order.md；重点报告§3。','PotionStuck':'状态setter与非持久属性；MFQM.analysis.txt:2641委派；重点报告§3。','MuddyEvent':'湿润/干燥分支与残留阈值：original-phase3/08_COATING_CAMERA_TEXTURE_SPEC.md；重点报告§5。','CustomRenderPlayerEvent':'遮罩与旧UV：原版逐层遮罩不等同现代全身方块纹理；重点报告§5。','CustomWorldGen':'generateSurface先SSand再QS共享blockGen；original-phase5/02_SURFACE_BRANCH_CLOSURE.md；重点报告§6。'}
  topic=topics.get(c['class_name'].split('/')[-1])
  if topic:
   text=text.replace('**INDEXED / NOT_ANALYZED**','**INDEXED / FIRST_BATCH_PARTIAL**')
   import os
   link=os.path.relpath(root/'reconstruction/reports/DEEP_FIRST_BATCH.md',p.parent)
   text+='\n## 首批深度档案入口\n\n'+topic+'\n\n[深度证据、规范与对照]('+link+')\n\n1. 身份/字节哈希/工具：本页顶部，原始来源非原作者源码。\n2. 原文证据与解释：按上述位置与重点报告分栏读取。\n3. 职责和触发：重点报告对应模块列出输入、调用次序、提前返回。\n4. 功能与资源：对应 ORIGINAL_REGISTRY、RESOURCE_USAGE 和本类调用边，不将名字映射当语义。\n5. 行为规范：重点报告的分支和边界；未列分支 UNKNOWN。\n6. 现代差异：重点报告逐模块对照现代真实路径及存档风险。\n7. 测试设计：原版对照本轮 NOT_RUN，现有现代回归见 R0_TEST_RESULTS.json。\n8. 结论：PARTIAL，仅已列静态链；下一步按 NEXT_WORK_PACKAGES.md 闭合。\n'
  p.write_text(text,encoding='utf-8')

 write(root/'docs/reconstruction/original/CLASS_DOSSIER_INDEX.csv',[dict(class_id=c['class_id'],class_name=c['class_name'],path='docs/reconstruction/original/classes/'+c['class_name']+'.md',status='INDEXED_SEMANTICS_PARTIAL')for c in classes])
 if (out/'mapping/CONTENT_PARITY_MATRIX.csv').exists():
  from r1.reconcile import run as reconcile
  reconcile(root,out)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo-root',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();run(a.repo_root.resolve(),a.out_dir)
