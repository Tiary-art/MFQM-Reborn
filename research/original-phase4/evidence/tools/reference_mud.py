"""Independent hand-derived control flow for GenMud, no trace_vm/ASM interpreter.
Every branch/API/helper/PRNG event has an original offset from javap. Domain:
only GenMud enabled, API predicates pure, declared World fixture contract.
"""
import json
ROOT='MoreFunQuicksandMod.main.CustomWorldGen#'
MAIN=ROOT+'generateAOADimGardencia(Lnet/minecraft/world/World;Ljava/util/Random;II)V'
class Reference:
 def __init__(self,seed,fixture,enabled=True):self.events=[];self.method=MAIN;self.state=(seed^0x5DEECE66D)&((1<<48)-1);self.ordinal=0;self.fixture=fixture;self.enabled=enabled;self.blocks={};self.meta={}
 def emit(self,event,offset,**kw):self.events.append(dict(event=event,method=self.method,offset=offset,**kw))
 def branch(self,offset,op,taken,target):self.emit('BRANCH',offset,opcode=op,taken=taken,target=target)
 def rnd16(self,offset):
  before=self.state;self.state=(self.state*0x5DEECE66D+11)&((1<<48)-1);v=(16*(self.state>>17))>>31
  self.emit('RNG_CALL',offset,rng='passed',api='nextInt',bound=16,value=v,before=before,after=self.state,ordinal=self.ordinal);self.ordinal+=1;return v
 def peek(self,x,y,z):
  if(x,y,z)in self.blocks:return self.blocks[x,y,z]
  if self.fixture=='all-layouts':
   code=(x+16)*16+z
   if y==66:return 'field_150355_j'if code&64 else'field_150350_a'
   if y==65:return 'field_150348_b'if code&32 else'field_150350_a'
   if 60<=y<=64:return 'field_150348_b'if code&(1<<(y-60))else'field_150350_a'
   return 'field_150350_a'
  if self.fixture=='empty':return 'field_150350_a'
  if self.fixture=='mixed':
   # Java remainder sign does not affect equality to zero.
   if y==66:return 'field_150348_b'if(x+z)%3==0 else'field_150355_j'
   if(y==65 and(x+z)%2==0)or y==62:return 'field_150348_b'
   return 'field_150350_a'
  return 'field_150355_j'if y==66 else'field_150350_a'
 def pred(self,kind,x,y,z):
  prev=self.method;self.method=ROOT+kind+'(IIILnet/minecraft/world/World;)Z';self.emit('HELPER_ENTER',0);b=self.peek(x,y,z);self.emit('WORLD_READ',5,api='getBlock',x=x,y=y,z=z,block=b)
  result=b=='field_150355_j'if kind=='validWaterMaterial'else b not in ['field_150350_a','field_150355_j']
  self.branch(14,166 if kind=='validWaterMaterial'else 153,not result,19);self.emit('HELPER_EXIT',18 if result else 20);self.method=prev;return result
 def write(self,offset,x,y,z,b,m):
  applied=(self.fixture!='deny'or y!=63)and(self.fixture!='all-layouts'or not(((x+16)*16+z)&128))
  if applied:self.blocks[x,y,z]=b;self.meta[x,y,z]=m
  self.emit('WORLD_WRITE',offset,api='setBlock',x=x,y=y,z=z,block=b,metadata=m,flags=2,applied=applied)
 def run(self):
  self.emit('HELPER_ENTER',0);x=-16+self.rnd16(7);z=self.rnd16(25);self.emit('WORLD_READ',36,api='biome',x=x,z=z,id=1);self.emit('BLOCKGEN',49,value=0);self.emit('CONFIG_GATE',51,name='GenMud',value=self.enabled);self.branch(54,153,not self.enabled,193)
  if self.enabled:
   h=0
   while True:
    self.branch(64,162,h>=16,193)
    if h>=16:break
    v=0
    while True:
     self.branch(74,162,v>=16,187)
     if v>=16:break
     x=-16+h;z=v;water=self.pred('validWaterMaterial',x,66,z);self.branch(105,153,not water,181)
     if water:
      solid=self.pred('validSolidMaterial',x,65,z);self.branch(119,154,solid,138)
      if not solid:self.write(134,x,65,z,'field_150355_j',0)
      y=60
      while True:
       self.branch(142,163,y>64,181)
       if y>64:break
       solid=self.pred('validSolidMaterial',x,y,z);self.branch(156,154,solid,175)
       if not solid:self.write(171,x,y,z,'MudBlock',3)
       y+=1;self.branch(178,167,True,138)
     v+=1;self.branch(184,167,True,70)
    h+=1;self.branch(190,167,True,60)
  for off,branch,target,name in [(193,196,530,'GenJQS'),(530,533,777,'GenMucBl'),(780,783,1067,'GenMoor'),(1070,1073,1322,'GenLiqMire')]:self.emit('CONFIG_GATE',off,name=name,value=False);self.branch(branch,153,True,target)
  self.emit('HELPER_EXIT',1322);return self.events

def compare(path,seed,fixture,enabled=True):
 actual=[json.loads(l)for l in path.read_text().splitlines()];actual=[e for e in actual if e['event']not in ['HEADER','RESULT']];ref=Reference(seed,fixture,enabled);expected=ref.run()
 assert len(actual)==len(expected),(path,len(actual),len(expected))
 for i,(a,b)in enumerate(zip(actual,expected)):
  assert a==b,(path,i,a,b)
 final={}
 for line in path.with_name(path.name+'.final.tsv').read_text().splitlines():
  xyz,b,m=line.split('\t');final[tuple(map(int,xyz.split(',')))]=(b,int(m))
 assert final=={k:(v,ref.meta[k])for k,v in ref.blocks.items()}
 return {'case':path.name,'seed':seed,'fixture':fixture,'events_identical':len(actual),'final_cells_identical':len(final),'comparison':'all ordered events including BRANCH/HELPER/CONFIG/RNG/READ/WRITE and final state','verdict':'SEMANTICALLY_CLOSED_CONTRACT_BOUND_GenMud'}
