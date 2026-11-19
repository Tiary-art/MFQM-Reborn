#!/usr/bin/env python3
"""Summarize actual captured client/server rows; no fake-player substitutes or missing frames synthesized."""
from pathlib import Path
import json,gzip,collections
R=Path(__file__).resolve().parents[1];out={'clients':{},'network':{}}
def read(p):
 with (gzip.open(p,'rt')if p.suffix=='.gz'else p.open())as f:return [json.loads(l)for l in f if l.strip()]
paths=sorted((R/'evidence').glob('client-session*/*.jsonl*'))
for p in paths:
 es=read(p);ticks=[e for e in es if e.get('event')=='client_tick'];fov=[e for e in es if e.get('event')=='fov_observed'];trans=[];last=None
 for e in ticks:
  state=(e['lease'],e['creative'],e['dimension'])
  if state!=last:trans.append({k:e[k]for k in ['millis','tick','lease','creative','dimension','speed','y']});last=state
 key=str(p.relative_to(R/'evidence'))
 out['clients'][key]={'ticks_captured':len(ticks),'fov_events':len(fov),'lease_frames':sum(e['lease']for e in ticks),'dimensions':sorted({e['dimension']for e in ticks}),'modes':sorted({e['creative']for e in ticks}),'speed_min':min(e['speed']for e in ticks),'speed_max':max(e['speed']for e in ticks),'fov_min':min((e['new_modifier']for e in fov),default=None),'fov_max':max((e['new_modifier']for e in fov),default=None),'transitions':trans,'bounded_capture':'max3600 client ticks; frames beyond budget NOT_OBSERVED'}
for p in sorted((R/'evidence/network').glob('*.jsonl*')):
 es=read(p);cor=[e['corrections']for e in es if 'corrections'in e]
 out['network'][p.name]={'rows':len(es),'points':dict(collections.Counter(e.get('point')for e in es)),'corrections_min':min(cor,default=None),'corrections_max':max(cor,default=None),'scope':'recorded trial only; explicit teleports and no human movement input must not be generalized'}
out['interpretation']={'automatic_player_contact':'BLOCKED; all observed player leases are diagnostic commands','actual_clients':'Minecraft client JVMs connected to localhost offline-mode Forge server, not GameTest mock players','human_input_and_visual_comfort':'NOT_RUN','potion_foreign_combination':'server/client recorded speed .15400000295043 before/after lease; .005695266381302885 while active; after potion expiry .110000001639128 with foreign UUID; not a universal performance benchmark'}
(R/'observations.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:{'ticks':v['ticks_captured'],'lease_frames':v['lease_frames']}for k,v in out['clients'].items()},indent=2))
