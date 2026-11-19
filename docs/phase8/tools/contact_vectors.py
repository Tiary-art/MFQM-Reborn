#!/usr/bin/env python3
"""Deterministic independent decision table from cited original branch text.
This is a static contact-output projection, NOT a claim of executing the full original callback.
"""
from pathlib import Path
import csv,math,hashlib,json
R=Path(__file__).resolve().parents[3];source=R/'research/original-phase3/evidence/source/BlockQuicksand.cfr.txt'
s=source.read_text()
for token in ['float mtdkof = 10.0f','if (kof1 >= 1.2)','if (kof1 >= 0.9)','if (kof1 < 0.45','if (kof1 < 0.5','kof1 = 0.001','MFQM.setStuckEffect((EntityLivingBase)entity, 145)']:
 assert token in s,token
out=R/'forge-1.20.1/src/test/resources/phase8';out.mkdir(parents=True,exist_ok=True);rows=[]
for k in [-1.,0.,.449999999,.45,.499999999,.5,.899999999,.9,1.199999999,1.2,1.5,2.]:
 for a,b in [(False,False),(True,False),(True,True)]:
  for truly in [False,True]:
   y=k-.5;km=max(k,0.);mr=min(5+math.floor(max(0.,100.*(1.5-km))),145);levels=[]
   if a and not b:
    if k<.5 and truly:levels=[145]
   else:
    kk=.001 if a and b else k
    if kk<1.2:
     if kk>=.9:levels=[mr]
     elif truly:
      levels=[mr]
      if kk<.45:levels.append(145)
   # k is reconstructed by the original arithmetic; near boundaries preserve its exact floating value.
   actual_k=-((0.-y)-.5)
   if actual_k!=k:
    # Recompute table at the actual representable input, not by rounding an expected result.
    km=max(actual_k,0.);mr=min(5+math.floor(max(0.,100.*(1.5-km))),145);kk=.001 if a and b else actual_k
    levels=([145]if kk<.5 and truly else[])if a and not b else([]if kk>=1.2 else[mr]if kk>=.9 else([mr]+([145]if kk<.45 else[])if truly else[]))
   rows.append([format(y,'.17g'),str(a).lower(),str(b).lower(),str(truly).lower(),';'.join(map(str,levels))or'-'])
with(out/'quicksand-contact.tsv').open('w',newline='')as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerows(rows)
(R/'docs/phase8/contact-vector-provenance.json').write_text(json.dumps({'source':str(source.relative_to(R)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'rows':len(rows),'kind':'STATIC_VERIFIED original branch decision projection, not full native callback runtime','metadata':'not read by QS Contact path','rng':'output is invariant to full-callback random outcomes; no full-callback RNG port claimed'},indent=2)+'\n')
print('generated',len(rows),'static-evidence Contact vectors')
