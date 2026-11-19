#!/usr/bin/env python3
"""Restricted bytecode-driven MODEL_TRACE, not an original Minecraft runtime.
Fail closed on unsupported opcodes/methods. Terrain predicates and generator helpers
are declared fixture stubs. Never silently execute omitted helper writes or RNG.
"""
import argparse,json,math,re,struct
from pathlib import Path

def f32(x):return struct.unpack('>f',struct.pack('>f',x))[0]
class JavaRandom:
 def __init__(self,seed,emit=lambda **k:None):self.state=(seed^0x5DEECE66D)&((1<<48)-1);self.emit=emit
 def bits(self,n):self.state=(self.state*0x5DEECE66D+11)&((1<<48)-1);return self.state>>(48-n)
 def nextInt(self,bound):
  if bound<=0 or bound>2147483647:raise ValueError('bound must be positive signed int')
  before=self.state;draws=0
  if bound&-bound==bound:draws=1;value=(bound*self.bits(31))>>31
  else:
   while True:
    bits=self.bits(31);draws+=1;value=bits%bound
    if bits-value+(bound-1)<(1<<31):break
  self.emit(event='RNG',api='java.util.Random.nextInt',bound=bound,result=value,state_before=before,state_after=self.state,draws=draws)
  return value

def arity(desc):
 args=desc.split(')',1)[0][1:];n=0;i=0
 while i<len(args):
  while args[i]=='[':i+=1
  if args[i]=='L':i=args.index(';',i)+1
  else:i+=1
  n+=1
 return n

def target(s):
 spec=s.split('// ',1)[1].split(' ',1)[1];name,desc=spec.split(':',1);name=name.replace('"','')
 return name,desc
class VM:
 def __init__(self,methods,seed=0,origin=(0,0),scenario='mud'):
  self.methods=methods;self.events=[];self.coverage={};self.pc=None;self.current=None;self.steps=0;self.stub_count=0
  self.rng=JavaRandom(seed,self.emit);self.origin=origin;self.scenario=scenario
  self.config={n:False for n in ['GenMud','GenJQS','GenMucBl','GenMoor','GenLiqMire']}
  self.config[{'mud':'GenMud','jqs':'GenJQS','blossom':'GenMucBl','moor':'GenMoor','liqmire':'GenLiqMire'}[scenario]]=True
 def emit(self,**e):self.events.append(dict(seq=len(self.events),method=self.current,offset=self.pc,**e))
 def invoke(self,name,desc,args,receiver):
  n=name.split('.')[-1]
  if n=='nextInt':return self.rng.nextInt(args[0])
  if name.startswith('java/lang/Math.'):
   op=n
   return {'round':lambda x:math.floor(x+.5),'pow':math.pow,'sqrt':math.sqrt,'max':max,'min':min}[op](*args)
  if n=='func_72807_a':return {'biome':1}
  if n=='func_147439_a':return 'net/minecraft/init/Blocks.field_150355_j' if args[1]==70 else 'fixture:stone'
  if n=='func_147465_d':
   x,y,z,block,meta,flags=args
   self.emit(event='WRITE',x=x,y=y,z=z,block=block,metadata=meta,flags=flags,chunk_x=x//16,chunk_z=z//16,cross_chunk=(x//16,z//16)!=(self.origin[0]//16,self.origin[1]//16));return True
  if n=='<init>':return None
  if (self.current or '').startswith('GenerateDesertTombs'):
   if n in ['func_76484_a','generate2','generate3','generate4','generate5','generate6']:
    return self.run(n,[receiver]+args,'GenerateDesertTombs')
   if n=='setBlock':
    world,x,y,z,block,meta=args;self.emit(event='BLUEPRINT_WRITE',x=x,y=y,z=z,block=block,metadata=meta,flags=2,chunk_x=x//16,chunk_z=z//16);return None
   if n in ['generateSpawner','generateChest','generateChest2']:
    self.stub_count+=1;self.emit(event='HELPER_NOT_EXECUTED',helper=n,args=args,reason='TileEntity/loot helpers excluded; RNG and final overwrite semantics NOT reproduced');return None
   raise NotImplementedError((name,desc))
  predicates={'validWaterMaterial':lambda *a:a[1]==66,'validSolidMaterial':lambda *a:a[1]==70,'validGroundMaterial':lambda *a:a[1]==65,'validLiqMaterial':lambda *a:False,'isAboveFreeSpace':lambda *a:True,'genIsFlatSolid':lambda *a:True,'genIsFlat':lambda *a:True,'isGroundQS':lambda *a:True,'isGroundNear':lambda *a:True}
  if n in predicates:
   result=predicates[n](*args);self.emit(event='FIXTURE_PREDICATE',helper=n,args=[x for x in args if x!='WORLD'],result=result);return result
  if n.startswith('generate') or n=='func_76484_a':
   self.stub_count+=1;self.emit(event='HELPER_NOT_EXECUTED',helper=n,args=[x for x in args if x not in ['WORLD','RNG']],reason='record call only; helper body RNG/writes absent from MODEL_TRACE');return False if desc.endswith('Z') else None
  raise NotImplementedError((name,desc))
 def run(self,name,args,cls='CustomWorldGen'):
  key=cls+'#'+name;m=self.methods[key];ins=m['instructions'];positions={x['offset']:i for i,x in enumerate(ins)};stack=[];loc=dict(enumerate(args));j=0
  saved=(self.current,self.pc);self.current=key
  while j<len(ins):
   self.steps+=1
   if self.steps>2000000:raise RuntimeError('instruction budget exceeded')
   i=ins[j];self.pc=i['offset'];op=i['opcode'];s=i['args'];self.coverage.setdefault(key,set()).add(self.pc);j+=1
   if op.startswith(('aload','iload','dload','fload','lload')):stack.append(loc[int(op.split('_')[1])if '_'in op else int(s)])
   elif op.startswith(('astore','istore','dstore','fstore','lstore')):
    slot=int(op.split('_')[1])if '_'in op else int(s);v=stack.pop();loc[slot]=v
    # Gardencia LocalVariableTable says blockGen is slot11; guarded by class/method.
    if key=='CustomWorldGen#generateAOADimGardencia' and slot==11:self.emit(event='BLOCKGEN_STORE',value=v,local_slot=slot)
   elif op.startswith('iconst_'):stack.append(-1 if op=='iconst_m1' else int(op[-1]))
   elif op.startswith(('fconst_','dconst_','lconst_')):stack.append(float(op[-1]))
   elif op in ['bipush','sipush']:stack.append(int(s))
   elif op.startswith('ldc'):
    raw=s.split('//',1)[1].strip();typ,val=raw.split(' ',1);stack.append(float(val.rstrip('dDfF')) if typ in ['double','float'] else int(val.rstrip('lL')))
   elif op=='getstatic':
    field=s.split('// Field ',1)[1].split(':',1)[0]
    if field.startswith('MoreFunQuicksandMod/main/MFQM.Gen'):
     v=self.config[field.split('.')[-1]];self.emit(event='CONFIG_READ',field=field,result=v);stack.append(v)
    else:stack.append(field)
   elif op=='getfield':
    receiver=stack.pop();field=s.split('// Field ',1)[1].split(':',1)[0]
    if field.endswith('field_76756_M'):stack.append(receiver['biome'])
    else:raise NotImplementedError(field)
   elif op=='iinc':slot,delta=[int(x.strip()) for x in s.split(',')];loc[slot]+=delta
   elif op in ['iadd','isub','imul','dadd','dsub','dmul','fdiv']:
    b=stack.pop();a=stack.pop();v={'iadd':lambda:a+b,'isub':lambda:a-b,'imul':lambda:a*b,'dadd':lambda:a+b,'dsub':lambda:a-b,'dmul':lambda:a*b,'fdiv':lambda:f32(a/b)}[op]();stack.append(v)
   elif op in ['i2d','i2f','d2f','l2i','d2i']:
    v=stack.pop();stack.append(f32(v) if op in ['d2f','i2f'] else float(v) if op=='i2d' else int(v))
   elif op=='dup':stack.append(stack[-1])
   elif op=='pop':stack.pop()
   elif op=='new':stack.append('NEW:'+s.split('// class ',1)[1])
   elif op.startswith('invoke'):
    n,d=target(s);count=arity(d);aa=[stack.pop()for _ in range(count)][::-1];recv=None if op=='invokestatic' else stack.pop();v=self.invoke(n,d,aa,recv)
    if d.split(')',1)[1]!='V':stack.append(v)
   elif op=='goto':j=positions[int(s)]
   elif op.startswith('if'):
    if op.startswith(('if_icmp','if_acmp')):b=stack.pop();a=stack.pop();cond=op.split('cmp',1)[1]
    else:a=stack.pop();b=0;cond=op[2:]
    yes={'eq':lambda:a==b,'ne':lambda:a!=b,'lt':lambda:a<b,'le':lambda:a<=b,'gt':lambda:a>b,'ge':lambda:a>=b}[cond]()
    self.emit(event='BRANCH',opcode=op,taken=yes,target=int(s))
    if yes:j=positions[int(s)]
   elif op in ['return','ireturn']:
    v=None if op=='return' else stack.pop();self.current,self.pc=saved;return v
   else:raise NotImplementedError((key,self.pc,op,s))
  raise RuntimeError('fell off bytecode')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--methods',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--seed',type=int,default=0);ap.add_argument('--x',type=int,default=-16);ap.add_argument('--z',type=int,default=0);ap.add_argument('--scenario',choices=['mud','jqs','blossom','moor','liqmire','tombs'],default='mud');a=ap.parse_args()
 methods=json.loads(a.methods.read_text());v=VM(methods,a.seed,(a.x,a.z),a.scenario if a.scenario!='tombs' else 'mud')
 v.emit(event='HEADER',trace_kind='MODEL_TRACE',seed=a.seed,origin=[a.x,a.z],scenario=a.scenario,warning='Original bytecode control flow under declared fixtures; no original game/helper execution; not ORIGINAL_RUNTIME_TRACE')
 if a.scenario=='tombs':v.run('func_76484_a',['THIS','WORLD','RNG',a.x,40,a.z],'GenerateDesertTombs')
 else:v.run('generateAOADimGardencia',['THIS','WORLD','RNG',a.x,a.z])
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n'for e in v.events))
 summary={'trace_kind':'MODEL_TRACE','scenario':a.scenario,'seed':a.seed,'instructions_executed':v.steps,'events':len(v.events),'helper_bodies_not_executed':v.stub_count,'counts':{k:sum(e['event']==k for e in v.events)for k in ['RNG','WRITE','BLUEPRINT_WRITE','CONFIG_READ','BLOCKGEN_STORE','HELPER_NOT_EXECUTED']},'instruction_offsets_exercised':{k:sorted(x)for k,x in v.coverage.items()},'original_runtime':'NOT_RUN'}
 a.out.with_suffix('.summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:x for k,x in summary.items()if k!='instruction_offsets_exercised'}))
if __name__=='__main__':main()
