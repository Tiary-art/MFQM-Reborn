"""Offline check usable from a downloaded project ZIP."""
import hashlib
import json
from pathlib import Path
import sys
import zipfile

root=Path(sys.argv[1])
folder=root/'deliverables/r1'
record=json.loads((folder/'ARTIFACTS.json').read_text(encoding='utf-8'))
jar=folder/record['filename']
digest=hashlib.sha256(jar.read_bytes()).hexdigest()
assert digest==record['jar_sha256']
assert (folder/'SHA256SUMS').read_text().split()==[digest,jar.name]
with zipfile.ZipFile(jar) as z:
    assert z.testzip() is None
    assert 'art/tiary/mfqm/registry/RestoredItems.class' in z.namelist()
    assert not any(p.endswith(('.png','.ogg')) for p in z.namelist())
    assert 'assets/mfqm/original_texture_bindings.json' not in z.namelist()
print(digest,jar.name)
