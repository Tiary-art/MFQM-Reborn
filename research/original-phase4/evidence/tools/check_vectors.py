#!/usr/bin/env python3
import csv,json,math,struct
from pathlib import Path
r=Path(__file__).resolve().parents[2];rows=list(csv.DictReader((r/'evidence/results/physics-vectors.csv').open()))
def f32(v):return struct.unpack('>f',struct.pack('>f',v))[0]
for x in rows:
 level=int(x['level']);p=level-5;c=0 if x['horizontalCollision']=='true'else 1;j=f32(float(x['jumpInput']))
 if p<250:j=f32(j/max(math.pow(1+p*(1+c*2.5)/1000,8),1));s=max(1/math.pow(1+p*(1+c/2)/50,2),.02)
 else:j=0;s=.02
 if j<.005:j=0
 assert abs(j-float(x['jumpOutput']))<1e-7,(x,j)
 assert abs(s-float(x['speed']))<1e-12,(x,s)
 assert x['operation']=='2'and x['nextLevel']=='0'
print(json.dumps({'status':'MODEL_TESTED_NUMERIC_EXPRESSION','vectors':len(rows),'speed_abs_tolerance':1e-12,'float_text_abs_tolerance':1e-7,'boundary':'not an execution of original LivingUpdateEvent or net sinking physics','source':'CustomPotionEvent#onLivingUpdateEvent(Lnet/minecraftforge/event/entity/living/LivingEvent$LivingUpdateEvent;)V@55..203; modifier@217..252','original_runtime':'NOT_RUN'},indent=2))
