"""Fold the reviewed stack evidence into the original R0 identities."""
from collections import defaultdict
from pathlib import Path
import json
from common import read, write

def run(root,out):
    manifest, mapping = out/'manifest', out/'mapping'
    def rows(name): return read(mapping/(name+'.csv'))
    def save(name, values): write(mapping/(name+'.csv'),values)
    stacks = rows('CONTENT_PARITY_MATRIX')
    objects = {r['original_object_id']:r for r in read(manifest/'ORIGINAL_REGISTRY_OBJECTS.csv')}
    regs = {(r['kind'],r['registry_id']):r for r in read(manifest/'MODERN_REGISTRY.csv')}
    resources = read(manifest/'ORIGINAL_RESOURCES.csv')
    sources = {r['path']:r for r in resources}
    hashes = json.loads((root/'deliverables/r1/logs/private-entry-hashes.json').read_text())
    links = [r for r in rows('ORIGINAL_TO_MODERN') if r['mapping_kind']!='R1_STACK_IDENTITY']
    usage = [r for r in rows('RESOURCE_USAGE') if r['usage']!='R1 private inventory']
    covered = defaultdict(set)
    by_call = defaultdict(list)
    used = set()
    evidence = 'reconstruction/mapping/CONTENT_PARITY_MATRIX.csv'
    for s in stacks:
        item = s['modern_registry_id']
        if not item: continue
        reg = regs['ITEM',item]
        for call in objects[s['original_object_id']]['r0_call_ids'].split(';'):
            by_call[call].append(s)
            if (call,item) in used: continue
            used.add((call,item))
            links.append(dict(original_id=call,modern_id=reg['modern_id'],modern_path=reg['source'],
                              mapping_kind='R1_STACK_IDENTITY',status='PARTIAL',evidence_ref=evidence))
        for path in dict.fromkeys(s['original_resource_path'].split(';')):
            if not path: continue
            kind = 'item' if '/items/' in path else 'block'
            target = 'assets/mfqm/textures/'+kind+'/original/'+Path(path).name.lower()
            if hashes.get(target)!=sources[path]['sha256']:raise ValueError((path,target))
            covered[path].add(item)
            usage.append(dict(original_path=path,original_sha256=sources[path]['sha256'],new_registry_id=item,
                target_resource_path=target,usage='R1 private inventory',mapping_evidence=s['original_icon_evidence'],
                status='SOURCE_AND_PACKAGE_HASH',blocker='geometry / individual visual parity unverified',
                r0_status='R1',visual_status='GUI_MODEL_PROBE'))
    matrix=rows('RESTORATION_MATRIX')
    for row in matrix:
        group=by_call.get(row['original_id'],[])
        if not group: continue
        old=set(filter(None,row['modern_ids'].split(';')))
        row.update(modern_ids=';'.join(sorted(old|{s['modern_registry_id'] for s in group})),
            semantic_mapping='PARTIAL',registration_status='FORGE_REGISTRY_ENUMERATED',
            asset_status='SEE_STACK_ROWS',name_status='SEE_STACK_ROWS',owner='R1',
            evidence_ref=evidence,blocker='Original runtime, per-stack mechanics and visual parity open')
    save('ORIGINAL_TO_MODERN',links);save('RESOURCE_USAGE',usage);save('RESTORATION_MATRIX',matrix)
    digests=defaultdict(list)
    for target,h in hashes.items():digests[h].append(target)
    inventory=[]
    for r in resources:
        path=r['path'];targets=digests[r['sha256']]
        if path.lower().endswith('mucus_flowing.png.mcmeta'):status='R1_REFRAMED_METADATA'
        elif targets:status='BYTE_MATCH_IN_PRIVATE_PACKAGE'
        else:status='NO_IDENTICAL_PAYLOAD_IN_OVERLAY'
        inventory.append(dict(original_file_id=r['original_file_id'],path=path,sha256=r['sha256'],
            matching_packed_paths=';'.join(sorted(targets)),r1_stack_users=';'.join(sorted(covered[path])),
            status=status,usage_scope='hash equality alone does not identify a consumer'))
    write(mapping/'R1_RESOURCE_PROVENANCE.csv',inventory)
    gaps=rows('USER_OBSERVED_GAPS')
    for row in gaps[:3]:
        row.update(status='PARTIAL',observed={'U-01':'Phase9 mucus flowing invalid frames; R1 private Linux atlas before/after reload',
            'U-02':'English names compared by legacy stack; Chinese project translations',
            'U-03':'See Forge registry and creative runtime dumps; old runtime total unknown'}[row['gap_id']],
            evidence_ref=evidence,next_action='Confirm the reported Windows object ID, locale, JAR SHA and active packs')
    save('USER_OBSERVED_GAPS',gaps)
