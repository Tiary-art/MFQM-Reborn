#!/usr/bin/env python3
"""Check audit deliverables/links/empty acceptance columns, not game behavior."""
import csv
import json
from pathlib import Path
import re
from urllib.parse import unquote

HERE = Path(__file__).resolve().parents[1]
required = ['README.md','ORIGINAL_MECHANICS_INVENTORY.md','THREE_MATERIAL_GAP_MATRIX.md',
    'USER_OBSERVATIONS.md','PHYSICS_AND_INTERACTION_AUDIT.md','STATE_AUDIO_VISUAL_AUDIT.md',
    'IMPLEMENTATION_ROADMAP.md','MANUAL_ACCEPTANCE_MATRIX.md','AUDIT_REPORT.md']
for name in required + ['BOAT_COMPATIBILITY_AUDIT.md','CLASS_COVERAGE.md','REGISTRATION_COVERAGE.md']:
    assert (HERE/name).is_file(), name
with (HERE/'audit-index.csv').open() as f:
    units=list(csv.DictReader(f))
assert len(units)==51 and len({u['id'] for u in units})==51
manual=(HERE/'MANUAL_ACCEPTANCE_MATRIX.md').read_text()
cases={}
observations=[]
for line in manual.splitlines():
    if not line.startswith('| '):continue
    cells=[c.strip() for c in line.strip().strip('|').split('|')]
    if re.fullmatch(r'M-(?:C\d\d|G\d\d|BOAT)',cells[0]):
        assert cells[0] not in cases, cells[0]
        assert len(cells)==6 and cells[-2:]==['',''],line
        cases[cells[0]]=cells
    elif re.fullmatch(r'OBS-\d\d',cells[0]):
        assert len(cells)==4 and cells[-2:]==['',''],line
        observations.append(cells[0])
assert set(cases)=={u['acceptance_id'] for u in units}
assert set(observations)=={f'OBS-{i:02}' for i in range(1,15)}
user=(HERE/'USER_OBSERVATIONS.md').read_text()
for i in range(1,15):assert f'OBS-{i:02}' in user
boat=(HERE/'BOAT_COMPATIBILITY_AUDIT.md').read_text()
assert all(x in boat for x in ['MFQM-003.5-BOAT-01','Quicksand','SoftQuicksand','Mud','canBoatInFluid'])
checked_links=0
for path in HERE.rglob('*.md'):
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',path.read_text()):
        if target.startswith(('https://','http://')):continue
        name,_,anchor=unquote(target).partition('#')
        dest=(path.parent/name).resolve() if name else path
        assert dest.exists(),f'{path.name}: missing {target}'
        if re.fullmatch(r'L\d+',anchor):
            assert int(anchor[1:])<=len(dest.read_text().splitlines()),f'{path.name}: invalid line {target}'
        checked_links+=1
for name,expected in [('class-coverage.csv',161),('resource-coverage.csv',302)]:
    with (HERE/'evidence'/name).open() as f:assert len(list(csv.DictReader(f)))==expected
stats=json.loads((HERE/'evidence/audit-check.json').read_text())
assert sum(stats['status_counts'].values())==51
assert stats['changed_baseline_files']==[] and stats['changes_outside_audit']==[]
assert stats['new_builds_run']==0 and stats['new_game_sessions_run']==0
air=json.loads((HERE/'evidence/legacy-air-map.json').read_text())
assert air['core_indices']==dict(QuicksandBlock=4,SoftQuicksandBlock=17,MudBlock=29)
assert not set(air['core_indices'].values()).intersection(air['skipped_indices'])
result=dict(status='PASS',required_documents=9,boat_supplement=True,unique_audit_units=51,
            manual_mechanism_cases=len(cases),observation_cases=len(observations),
            blank_result_columns=True,relative_links_checked=checked_links,
            meaning='Only document/reference/coverage consistency; no game behavior tested.')
(HERE/'evidence/validation-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
