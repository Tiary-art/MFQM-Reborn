#!/usr/bin/env python3
from pathlib import Path
import csv,json,statistics,hashlib
D=Path(__file__).resolve().parents[1];R=D/'evidence'
rows=list(csv.DictReader((R/'paired-mob-motion.csv').open()));out={}
for mode in ['old','injected']:
 a=[r for r in rows if r['mode']==mode];dy=[float(r['dy'])for r in a]
 out[mode]={'samples':len(a),'first_y':float(a[0]['y']),'last_y':float(a[-1]['y']),'min_dy':min(dy),'max_dy':max(dy),'mean_dy':statistics.mean(dy),'stdev_dy':statistics.pstdev(dy),'old_modifier_frames':sum(r['old_modifier']=='true'for r in a),'legacy_modifier_frames':sum(r['legacy_modifier']=='true'for r in a),'both_modifiers_frames':sum(r['old_modifier']=='true'and r['legacy_modifier']=='true'for r in a)}
lines=[l.split('\t')for l in(R/'dry-real-world.tsv').read_text().splitlines()];coords=[tuple(map(int,l[1:4]))for l in lines if l[0]in['Q','W']]
out['dry']={'events':len(lines),'chunks_touched':sorted({(x//16,z//16)for x,y,z in coords}),'scope':'seed0 extent5 synchronous API trace, not a full side-effect observer'}
out['trace_hashes']={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in R.glob('*.csv')};out['trace_hashes']['dry-real-world.tsv']=hashlib.sha256((R/'dry-real-world.tsv').read_bytes()).hexdigest()
(R/'statistics.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
