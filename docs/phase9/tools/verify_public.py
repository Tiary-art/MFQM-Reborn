#!/usr/bin/env python3
"""Verify the actual public Phase9 JAR without requiring private input."""
from pathlib import Path
import argparse,hashlib,json,zipfile
R=Path(__file__).resolve().parents[3]
p=argparse.ArgumentParser();p.add_argument('jar',type=Path);a=p.parse_args()
with zipfile.ZipFile(a.jar)as z:
 names=z.namelist();forbidden=[n for n in names if n.lower().endswith(('.png','.ogg'))or n=='assets/mfqm/original_texture_bindings.json'or'/original/'in n]
 assert not forbidden,forbidden
 required=['art/tiary/mfqm/client/OriginalTextureBindings.class','art/tiary/mfqm/client/Phase9RenderProbe.class','art/tiary/mfqm/integration/OriginalContactBridge.class','art/tiary/mfqm/legacy/DryQuicksandCore.class','art/tiary/mfqm/legacy/StuckLease.class']
 for n in required:assert n in names,n
 assert '0.0.9-phase9-resources'in z.read('META-INF/mods.toml').decode()
 models={id:json.loads(z.read('assets/mfqm/models/block/'+id+'.json'))for id in['quicksand','mud','soft_quicksand']}
 print(json.dumps({'mode':'PUBLIC_SOURCE_BUILD','jar':str(a.jar),'bytes':a.jar.stat().st_size,'sha256':hashlib.sha256(a.jar.read_bytes()).hexdigest(),'zip_entries':len(names),'mfqm_resource_entries':sum(n.startswith('assets/mfqm/')and not n.endswith('/')for n in names),'private_png_ogg_marker_entries':forbidden,'required_classes':required,'models':models,'status':'PASS'},indent=2))
