#!/usr/bin/env python3
"""Summarize actual JSONL. Never treats solver vy as measured displacement."""
import csv,json,sys
from pathlib import Path
rows=[]
for folder in sys.argv[1:]:
 for f in sorted(Path(folder).glob('*_server.jsonl')):
  records=[json.loads(x) for x in f.read_text().splitlines() if x.strip()]
  ends=[x for x in records if x.get('point')=='settle_end']
  contacts=[x for x in ends if x.get('material') not in (None,'none')]
  if not ends: continue
  first=contacts[0] if contacts else None
  continuous=[x for x in contacts if first and x['tick']>=first['tick']+3]
  # Position correction is included in measured deltas, deliberately not hidden.
  dy=[x['dy'] for x in continuous]
  sounds=[]
  client_ends=[]
  client=f.with_name(f.name.replace('_server.jsonl','_client.jsonl'))
  if client.exists():
   client_records=list(map(json.loads,client.read_text().splitlines()))
   sounds=[x for x in client_records if x.get('point')=='sound_requested']
   client_ends=[x for x in client_records if x.get('point')=='client_tick_end' and x.get('local_player')
                and first and x.get('tick',0)>=first['tick']+5 and x.get('y',1000)<=first.get('surface',0)+0.05]
  rows.append(dict(case=f.stem.rsplit('_',2)[0],trace_file=f.name,samples=len(ends),contact_tick=first['tick'] if first else '',
    post_contact_ticks=ends[-1]['tick']-first['tick'] if first else '',
    entry_depth=first.get('depth',0) if first else '',
    min_continuous_dy=min(dy) if dy else '',max_continuous_dy=max(dy) if dy else '',
    corrections=ends[-1]['corrections']-ends[0]['corrections'],
    first_y=ends[0]['y'],last_y=ends[-1]['y'],first_hp=ends[0]['health'],last_hp=ends[-1]['health'],
    min_hp=min(x['health'] for x in ends),
    min_local_client_dy=min((x['dy'] for x in client_ends),default=''),
    fall_events=sum(x.get('point')=='fall_event' for x in records),sound_requests=len(sounds),
    source_revision=records[0].get('detail','')))
if rows:
 writer=csv.DictWriter(sys.stdout,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
