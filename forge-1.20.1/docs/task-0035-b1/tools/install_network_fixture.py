#!/usr/bin/env python3
"""Install explicit disposable-world timed fixtures. Never loaded by the production mod.
Run: python install_network_fixture.py /path/to/test-server-world ; then console reload.
Invoke function mfqm_b1:net0/start (also net50/net150/net300).
Uses real Dev client physics; no fabricated movement or packet acknowledgements.
"""
from pathlib import Path
import json,sys
pack=Path(sys.argv[1])/'datapacks/mfqm_b1_network_fixture'
pack.mkdir(parents=True,exist_ok=True)
(pack/'pack.mcmeta').write_text(json.dumps({'pack':{'pack_format':15,'description':'Explicit MFQM B1 disposable test-world operator fixtures'}}))
root=pack/'data/mfqm_b1/functions';root.mkdir(parents=True,exist_ok=True)
(root/'park.mcfunction').write_text('tp Dev 8.5 65 -2.5\neffect clear Dev\nexecute as Dev at Dev run mfqm motion stop\n')
for profile in ['net0','net50','net150','net300']:
 folder=root/profile;folder.mkdir(exist_ok=True)
 for index,material in enumerate(['quicksand','mud','soft_quicksand']):
  next_fn=f'mfqm_b1:{profile}/'+['mud','soft_quicksand'][index] if index<2 else 'mfqm_b1:park'
  lines=['effect clear Dev',f'execute as Dev at Dev run mfqm motion trial {material} 3 10 player',
         f'execute as Dev at Dev run mfqm motion diag 260 {profile}_{material}',
         f'schedule function {next_fn} 280t replace']
  (folder/('start.mcfunction' if index==0 else material+'.mcfunction')).write_text('\n'.join(lines)+'\n')
print('Installed explicit network fixtures:',pack)

for material in ['quicksand','mud','soft_quicksand']:
 (root/('low_'+material+'.mcfunction')).write_text('effect clear Dev\nexecute as Dev at Dev run mfqm motion trial '+material+' 3 10 player\nexecute as Dev at Dev run mfqm motion diag 800 lowtps_'+material+'\nschedule function mfqm_b1:park 360t replace\n')
for material in ['quicksand','soft_quicksand']:
 (root/('low_deep_'+material+'.mcfunction')).write_text('effect clear Dev\nexecute as Dev at Dev run mfqm motion trial '+material+' 17 10 player\neffect give Dev minecraft:regeneration 60 255 true\nexecute as Dev at Dev run mfqm motion diag 1200 lowtps_deep_'+material+'\nschedule function mfqm_b1:park 900t replace\n')
