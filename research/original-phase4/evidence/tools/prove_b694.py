#!/usr/bin/env python3
"""Bounded loop proof for Gardencia B694; validate controlling bytecode facts first."""
import json,re
from pathlib import Path
r=Path(__file__).resolve().parents[2];repo=r.parents[1];cfg=json.loads((repo/'research/original-phase2/evidence/cfg/CustomWorldGen__generateAOADimGardencia.json').read_text());ins={i['offset']:i for b in cfg['blocks']for i in b['instructions']}
# Print full controlling span for independent review; no synthetic execution of B694.
span=[ins[k]for k in sorted(ins)if 579<=k<=709]
(r/'evidence/results/b694-control-instructions.json').write_text(json.dumps(span,indent=2)+'\n')
assert ins[0]['opcode']=='iconst_0' and ins[1]['opcode']=='istore' and ins[1]['args']=='5'
assert [i['offset'] for i in ins.values() if i['offset']<777 and i['opcode']=='istore' and i['args']=='5']==[1]
assert not cfg['exception_handlers']
assert {e['from']for e in cfg['edges']if e['to']==694}=={687}
# Required facts: y local7 starts70, countBlock local17 starts0, scan lower bound60,
# only increments +1 for count, only decrements -1 for Y in this loop.
text='\n'.join(f"{i['offset']} {i['opcode']} {i['args']}"for i in span)
assert any(i['opcode']=='bipush'and i['args']=='70'for i in span)
assert any(i['opcode']=='bipush'and i['args']=='60'for i in span)
assert ins[601]['opcode']=='bipush' and ins[601]['args']=='70'
assert ins[606]['opcode']=='istore' and ins[606]['args']=='7'
assert ins[619]['opcode']=='iconst_0' and ins[620]['opcode']=='istore' and ins[620]['args']=='17'
assert ins[627]['opcode']=='bipush' and ins[627]['args']=='60' and ins[632]['opcode']=='if_icmple'
assert ins[697]['opcode']=='iinc' and ins[697]['args']=='7, -1'
assert ins[700]['opcode']=='goto' and ins[700]['args']=='625'
assert ins[689]['opcode']=='bipush' and ins[689]['args']=='10' and ins[691]['opcode']=='if_icmple'
assert [i['offset'] for i in span if i['opcode']=='iinc' and i['args'].startswith('17,')]==[684]
assert [i['offset'] for i in span if i['opcode']=='iinc' and i['args'].startswith('7,')]==[697]
assert ins[684]['opcode']=='iinc'and ins[684]['args']=='17, 1'
assert ins[694]['opcode']=='goto'and ins[694]['args']=='703'
# Evidence review is explicit; exhaustive bound covers the 0..10 domain, independent of world predicates.
proof={'status':'SEMANTICALLY_CLOSED_UNREACHABLE_BLOCK','method':cfg['class']+'#'+cfg['method']+cfg['descriptor'],'block':'B694','premises':['Y initialized70, loop runs only while Y>60','Y decreases exactly1 on each continued iteration','countBlock initialized0 each attempt; at most one increment by1 per iteration','subcalls cannot modify caller JVM locals; early break/exception cannot add iterations'],'invariant':'after n completed/current increments: 0 <= countBlock <= n <= 10','guard_to_B694':'countBlock > 10','counterexample_domain':[{'max_iterations':n,'max_count':n,'guard_gt10':n>10}for n in range(11)],'conclusion':'B694 cannot be reached under original normal control flow; exceptions do not make it reachable','evidence':'evidence/results/b694-control-instructions.json; ../original-phase2/evidence/cfg/CustomWorldGen__generateAOADimGardencia.json','original_runtime':'NOT_RUN'}
(r/'evidence/results/b694-unreachable-proof.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':proof['status'],'block':'B694','guard':'countBlock>10','bound':10}))
