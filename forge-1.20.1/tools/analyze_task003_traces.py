#!/usr/bin/env python3
"""Summarize real server CSV measurements; never synthesize unobserved trajectories."""
import argparse
import csv
import json
import math
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('directory', type=Path)
p.add_argument('--output', type=Path)
args = p.parse_args()
summaries = []
for path in sorted(args.directory.glob('*.csv')):
    with path.open() as f:
        rows = list(csv.DictReader(f))
    if not rows:
        continue
    vals = lambda name: [float(r[name]) for r in rows]
    ticks = vals('tick')
    settlements = vals('settlements')
    finite = all(math.isfinite(float(r[k])) for r in rows for k in ['x','y','z','vx','vy','vz','immersion','health'])
    once = len(set(ticks)) == len(ticks) and all(b-a == d-c for a,b,c,d in zip(settlements,settlements[1:],ticks,ticks[1:]))
    covered = [int(r['tick']) for r in rows if r['eye_covered'] == 'true']
    # A commanded exit can be measured, but does not prove unaided self-rescue.
    exits = [i for i in range(1,len(rows)) if rows[i-1]['material'] != 'none' and rows[i]['material'] == 'none']
    summaries.append(dict(file=path.name, rows=len(rows), first_tick=int(ticks[0]), last_tick=int(ticks[-1]),
        seconds=(ticks[-1]-ticks[0])/20, y_start=vals('y')[0], y_end=vals('y')[-1],
        y_min=min(vals('y')), y_max=max(vals('y')), vy_min=min(vals('vy')), vy_max=max(vals('vy')),
        horizontal_speed_max=max(math.hypot(float(r['vx']),float(r['vz'])) for r in rows),
        horizontal_displacement=math.hypot(vals('x')[-1]-vals('x')[0],vals('z')[-1]-vals('z')[0]),
        immersion_max=max(vals('immersion')), stuck_max=max(vals('stuck')), air_min=min(vals('air')),
        health_min=min(vals('health')), damage_requests=max(vals('damage_requests'))-min(vals('damage_requests')),
        eye_covered_first_tick=min(covered) if covered else None, jump_held_rows=sum(r['jump_held']=='true' for r in rows),
        finite=finite, once_per_tick=once, commanded_exit_ticks=[int(rows[i]['tick']) for i in exits]))
result = {'source': str(args.directory), 'measurements': summaries,
          'all_finite': all(s['finite'] for s in summaries), 'all_once_per_tick': all(s['once_per_tick'] for s in summaries),
          'note': 'Velocity is the post-solver server value; Y is accepted server position. These are not interchangeable for player packets. Unobserved exit time is unknown, not zero.'}
out = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
if args.output:
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(out)
else:
    print(out, end='')
