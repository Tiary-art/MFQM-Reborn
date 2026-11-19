#!/usr/bin/env python3
"""Run unchanged original method through Phase5's declared mock JVM, then project.
Requires Phase5 harness prepared using its REPRODUCE.md; does not change that evidence.
"""
import argparse,subprocess,gzip,hashlib,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent));import convert_vectors as cv
p=argparse.ArgumentParser();p.add_argument('--java',required=True);p.add_argument('--jar',required=True);p.add_argument('--harness',default='/tmp/mfqm-phase5');a=p.parse_args()
out=cv.ROOT/'docs/phase6/evidence'; records=[]
for fixture in ['desert-refuse','deny','protected']:
 tag='supplement-'+fixture;raw=Path('/tmp')/(tag+'.jsonl')
 cmd=[a.java,'--add-exports','java.base/jdk.internal.org.objectweb.asm=ALL-UNNAMED','-cp',a.harness+'/classes','audit.Run',a.jar,a.harness+'/offsets.tsv',str(raw),'generateSoftSand','0','5',fixture,'0']
 r=subprocess.run(cmd,capture_output=True,text=True);assert r.returncode==0,r.stderr
 data=raw.read_bytes();dest=out/(tag+'.jsonl.gz')
 with gzip.GzipFile(filename=str(dest),mode='wb',mtime=0)as f:f.write(data)
 lines=[v for e in map(json.loads,data.splitlines()) if(v:=cv.project(e))is not None]
 (cv.OUT/(tag+'.tsv')).write_text('\n'.join(lines)+'\n')

 records.append(dict(tag=tag,command=cmd,exit=r.returncode,stderr=r.stderr,sha256=hashlib.sha256(data).hexdigest(),scope='Phase5 mock APIs, NOT original Minecraft runtime'))
(out/'native-cases.json').write_text(json.dumps(records,indent=2)+'\n')

subprocess.run([sys.executable,str(Path(__file__).with_name("convert_vectors.py"))],check=True)
