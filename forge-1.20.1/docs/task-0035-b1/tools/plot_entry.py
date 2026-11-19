#!/usr/bin/env python3
"""Measured server positions, no simulated curves. Run against extracted trace folders."""
import json,sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
base,candidate,out=map(Path,sys.argv[1:])
fig,axes=plt.subplots(1,3,figsize=(12,3.6),sharey=True)
for ax,material in zip(axes,['quicksand','mud','soft_quicksand']):
 for folder,prefix,label,color in [(base,'baseline','Baseline','#b54738'),(candidate,'candidate','Candidate','#176a98')]:
  file=next(folder.glob(f'{prefix}_player_{material}_L3_H10_*server.jsonl'))
  rows=[json.loads(s) for s in file.read_text().splitlines()]
  rows=[r for r in rows if r.get('point')=='settle_end']
  first=next(r for r in rows if r['material']!='none')
  rows=[r for r in rows if first['tick']-3<=r['tick']<=first['tick']+200]
  ax.plot([r['tick']-first['tick'] for r in rows],[first['surface']-r['y'] for r in rows],color=color,label=label,lw=1.6)
 ax.axhline(.08,color='#888888',ls=':',lw=.8)
 ax.set(title=material.replace('_',' '),xlabel='Server ticks from first contact',ylim=(-.3,3.3),xlim=(-3,200))
 ax.grid(alpha=.2)
axes[0].set_ylabel('Feet depth below material surface (blocks)')
axes[0].legend(frameon=False)
fig.suptitle('Real survival player: 3 layers, 10-block drop — accepted server positions')
fig.tight_layout()
fig.savefig(out,metadata={'Date':None,'Description':'Measured JSONL; correction steps included. Candidate values await gameplay acceptance.'})
