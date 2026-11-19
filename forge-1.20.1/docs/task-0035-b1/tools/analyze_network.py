#!/usr/bin/env python3
"""Read actual paired JSONL and explicit load-END markers; produce no simulated results."""
import csv,json,re,statistics,sys,math
from pathlib import Path
server,client,log,out=map(Path,sys.argv[1:]);out.mkdir(parents=True,exist_ok=True)
rows=[];low=[]
for f in sorted(server.glob('*_server.jsonl')):
 if not f.name.startswith(('net0_','net50_','net150_','net300_','lowtps_','dimension_')):continue
 records=[json.loads(x) for x in f.read_text().splitlines() if x.strip()]
 ends=[x for x in records if x.get('point')=='settle_end']
 contacts=[x for x in ends if x['material']!='none']
 if not ends:continue
 peer=client/f.name.replace('_server','_client')
 cr=[json.loads(x) for x in peer.read_text().splitlines()] if peer.exists() else []
 first=contacts[0] if contacts else None
 local=[x for x in cr if x.get('point')=='client_tick_end' and x.get('local_player') and first
        and x.get('tick',0)>=first['tick']+5 and x['y']<=first['surface']+0.05]
 falls=[x for x in cr if x.get('point')=='sound_requested' and 'fall' in x['sound']]
 corrections=[b['tick'] for a,b in zip(ends,ends[1:]) if b['corrections']>a['corrections']]
 run=best=0;previous=None
 for tick in corrections:
  run=run+1 if previous is not None and tick==previous+1 else 1;previous=tick;best=max(best,run)
 row=dict(trace=f.name,samples=len(ends),post_contact_ticks=ends[-1]['tick']-first['tick'] if first else '',
          first_depth=first['depth'] if first else '',first_y=ends[0]['y'],last_y=ends[-1]['y'],min_y=min(x['y'] for x in ends),
          min_hp=min(x['health'] for x in ends),corrections=ends[-1]['corrections']-ends[0]['corrections'],
          max_consecutive_corrections=best,
          min_local_dy=min((x['dy'] for x in local),default=''),fall_sound_requests=len(falls),
          fall_hurt_requests=sum(x.get('point')=='hurt_event' and x.get('detail','').startswith('fall;') for x in records),
          unique_settlement_ticks=len({x['tick'] for x in ends})==len(ends),
          finite_y_vy=all(math.isfinite(x['y']) and math.isfinite(x['vy']) for x in ends),
          max_settlements_per_tick=max((b['settlements']-a['settlements'] for a,b in zip(ends,ends[1:])),default=0))
 rows.append(row)
 if f.name.startswith('lowtps_'):low.append((records[0]['nano'],ends,row))
if rows:
 with (out/'network-cases.csv').open('w') as dest:
  w=csv.DictWriter(dest,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
ends_ns=[int(x) for x in re.findall(r'MFQM_LOAD_END nano=(\d+)',log.read_text())]
measures=[]
for (_,samples,row),end in zip(sorted(low),ends_ns):
 after=next((i for i,x in enumerate(samples) if x['nano']>=end),None)
 if after is None or after<200:continue
 ms=[(samples[i]['nano']-samples[i-1]['nano'])/1e6 for i in range(after-199,after+1)]
 measures.append(dict(trace=row['trace'],intervals=len(ms),median_tick_ms=statistics.median(ms),mean_tick_ms=statistics.mean(ms),
                      median_tps=1000/statistics.median(ms),effective_mean_tps=1000/statistics.mean(ms)))
(out/'low-tps-timing.json').write_text(json.dumps(measures,indent=2)+'\n')
print(json.dumps({'paired_cases':len(rows),'load_windows':measures},indent=2))
