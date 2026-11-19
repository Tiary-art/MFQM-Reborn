#!/usr/bin/env python3
import argparse,json,gzip,hashlib,shutil
from pathlib import Path
from oracle_vm import Oracle
import compare
p=argparse.ArgumentParser();p.add_argument('--work',type=Path,required=True);p.add_argument('--java-home',type=Path,required=True);p.add_argument('--jar',type=Path,required=True);a=p.parse_args();r=Path(__file__).resolve().parents[2];failures=[]
def expect(name,descriptor,ins,args,error):
 m={'class':'audit.Probe','name':'test','descriptor':descriptor,'declaration':'public static void test();','instructions':[dict(offset=i,opcode=op,args=text)for i,(op,text)in enumerate(ins)]}
 try:Oracle([m]).run('audit.Probe#test'+descriptor,args)
 except error:failures.append(name);return
 raise AssertionError('expected nonzero/exception '+name)
expect('unknown opcode rejected','()V',[('unknown_opcode','')],[],NotImplementedError)
expect('unknown allocation rejected','()V',[('new','#0 // class audit/Unknown')],[],NotImplementedError)
expect('wrong tile cast rejected','(Ljava/lang/Object;)V',[('aload_0',''),('checkcast','#0 // class net/minecraft/tileentity/TileEntityChest'),('return','')],[{'class':'TileEntityMobSpawner'}],AssertionError)
expect('negative Java array index rejected','([I)V',[('aload_0',''),('iconst_m1',''),('iaload',''),('return','')],[[42]],IndexError)
compare.configure(a.work,a.java_home,a.jar);rec=compare.case('repeat-dry-positive','generateSurface',38,4,'desert','GenSSand')
raw=r/'evidence/results/repeat-dry-positive.jsonl';canonical=r/'evidence/results/dry-positive.jsonl.gz'
with gzip.open(canonical,'rb')as f:expected=f.read()
assert raw.read_bytes()==expected,'fixed seed native trace replay mismatch'
replays=r/'evidence/replays';replays.mkdir(exist_ok=True)
for path in [raw,raw.with_suffix('.oracle.jsonl')]:
 with path.open('rb')as fin,(replays/(path.name+'.gz')).open('wb')as fout:
  with gzip.GzipFile(fileobj=fout,mode='wb',mtime=0)as z:shutil.copyfileobj(fin,z)
 path.unlink()
result=dict(status='MODEL_TESTED',negative_cases=failures,repeat_native_full_trace_sha256=hashlib.sha256(expected).hexdigest(),repeat_bytes_identical=True,repeat_case=rec,original_runtime='NOT_RUN');(r/'evidence/results/guards-and-replay.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='repeat_case'},indent=2))
