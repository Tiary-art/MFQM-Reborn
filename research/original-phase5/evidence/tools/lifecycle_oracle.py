#!/usr/bin/env python3
"""Independent per-callback state reducer: property renewal + fixed UUID commands."""
import json,math
from pathlib import Path
from oracle_vm import f32
r=Path(__file__).resolve().parents[2];root='MoreFunQuicksandMod.main.CustomPotionEvent#';key=root+'onLivingUpdateEvent(Lnet/minecraftforge/event/entity/living/LivingEvent$LivingUpdateEvent;)V';uuid='73a49882-85a3-4896-ad2d-8c591e24aa62';expected=[]
def e(kind,off,method=key,**data):expected.append(dict(event=kind,method=method,offset=off,**data))
def b(off,op,yes,target):e('BRANCH',off,opcode=op,taken=yes,target=target)
level=-1;active=False;callbacks=[[145],[],[],[145,128],[50],[255],[0],[]]
e('HELPER_ENTER',0,root+'<clinit>()V');e('HELPER_EXIT',9,root+'<clinit>()V')
jump=f32(.02)
for tick,contacts in enumerate(callbacks):
 e('TICK',-1,'',tick=tick)
 if tick!=7:
  for value in contacts:level=value;e('LEVEL_SET',-1,'',value=value)
  jump=f32(.02)
 e('HELPER_ENTER',0);e('ATTR_QUERY',15,present=active);b(22,198,not active,32)
 if active:e('ATTR_REMOVE',27,uuid=uuid);active=False
 attached=tick!=7;e('PROP_GET',36,present=attached);b(43,199,attached,47)
 if not attached:e('HELPER_EXIT',46);e('SNAPSHOT',-1,'',tick=tick,level='no-property',jump=jump,modifiers=0);continue
 b(52,158,level<=0,258)
 if level>0:
  collision=tick%2==0;b(75,154,collision,81);p=level-5;c=0 if collision else 1;b(87,156,p>=250,167)
  if p<250:jump=f32(jump/max((1+p*(1+c*2.5)/1000)**8,1));speed=max(1/(1+p*(1+c/2)/50)**2,.02);b(164,167,True,180)
  else:jump=0.;speed=.02
  b(192,156,jump>=.005,203)
  if jump<.005:jump=0.
  e('ATTR_QUERY',207,present=False);b(214,199,False,249);e('ATTR_ADD',244,uuid=uuid,operation=2,amount=speed-1,saved=False);active=True;level=0;e('LEVEL_SET',252,value=0);b(255,167,True,272)
 else:
  b(263,154,level!=0,272)
  if level==0:level=-1;e('LEVEL_SET',269,value=-1)
 e('HELPER_EXIT',272);e('SNAPSHOT',-1,'',tick=tick,level=level,jump=jump,modifiers=int(active))
actual=[json.loads(l)for l in (r/'evidence/results/stuck-lifecycle.jsonl').read_text().splitlines()];actual=[x for x in actual if x['event']!='HEADER'];assert len(actual)==len(expected)
for idx,(a,x)in enumerate(zip(actual,expected)):
 assert a.keys()==x.keys(),(idx,a,x)
 for k in a:
  if k=='jump':assert f32(a[k])==x[k],(idx,k,a[k],x[k])
  elif k=='amount':assert abs(a[k]-x[k])<=1e-14,(idx,k,a[k],x[k])
  else:assert a[k]==x[k],(idx,k,a[k],x[k])
(r/'evidence/results/stuck-lifecycle.oracle.jsonl').write_text(''.join(json.dumps(x)+'\n'for x in expected))
result={'status':'SEMANTICALLY_CLOSED_STATE_REDUCER_CONTRACT','events_matched':len(actual),'ticks':8,'tested':['renew then0->-1','remove fixed UUID before property check','last collision setter wins','saturation p>=250','null property','operation2 amount speed-1 and nonpersistent flag'],'not_tested':['original block collision execution','old/new Forge global event ordering','full net Y motion','other mods reentrancy'],'original_runtime':'NOT_RUN'};(r/'evidence/results/stuck-diff.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
