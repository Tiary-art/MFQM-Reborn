#!/usr/bin/env python3
"""Match actual owner snapshots by UUID/tick and compare wire-format fields."""
import argparse
import json
import re
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('server', type=Path)
p.add_argument('client', type=Path)
p.add_argument('--client-after', help='Only use client lines following this exact connection marker')
args = p.parse_args()
pattern = re.compile(r'MFQM_SYNC_(SERVER|CLIENT) ([0-9a-f-]+) (\d+) (\S+) ([\d.Ee+-]+) (-?\d+) (\d+) (\d+)')
def read(path, side):
    result = {}
    content = path.read_text(errors='replace')
    if side == 'CLIENT' and args.client_after:
        if args.client_after not in content:
            raise SystemExit('Connection marker not found')
        content = content.split(args.client_after, 1)[1]
    for m in pattern.finditer(content):
        if m[1] == side:
            result[(m[2], int(m[3]))] = (m[4], float(m[5]), int(m[6]), int(m[7]), int(m[8]))
    return result
s = read(args.server, 'SERVER')
c = read(args.client, 'CLIENT')
shared = sorted(s.keys() & c.keys())
bad = [dict(uuid=k[0],tick=k[1],server=s[k],client=c[k]) for k in shared if s[k] != c[k]]
print(json.dumps(dict(server_snapshots=len(s),client_snapshots=len(c),matched=len(shared),mismatches=bad,
                     materials=sorted({s[k][0] for k in shared}),
                     note='Only common UUID/tick keys compared; login syncTo packets are not server-trace logged. Delivery/tracking drops remain separate from value equality.'),indent=2))
if not shared or bad:
    raise SystemExit(1)
