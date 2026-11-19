"""Independent transaction planners from geometry/random-walk specifications.
No bytecode dispatch, ASM, JVM trace parsing, or copied trace replay.
Compare all ordered RNG+mutation outcomes in addition to independent-VM full events.
"""
import itertools,math
from oracle_vm import Random
class Spec:
 def __init__(self,seed,fixture):self.rng=Random(seed,'passed');self.fixture=fixture;self.cells={};self.meta={};self.events=[]
 def draw(self,api,*args):
  v,e=self.rng.draw(api,args);self.events.append(dict(event='RNG_CALL',**e));return v
 def query(self,p):
  if p in self.cells:return self.cells[p]
  x,y,z=p
  if self.fixture.startswith('plant-'):return 'MorassBlock'if y<=70 else'field_150350_a'
  if self.fixture=='empty':return 'field_150350_a'
  if self.fixture=='protected':return 'SoftQuicksandBlock'if y<=70 else'field_150350_a'
  if self.fixture=='desert':return 'field_150354_m'if y<=70 else'field_150350_a'
  return 'field_150348_b'if y<=70 else'field_150350_a'
 def write(self,p,b,flags=3,meta=0):
  x,y,z=p;applied=self.fixture!='deny'or y!=63
  if applied:self.cells[p]=b;self.meta[p]=meta
  self.events.append(dict(event='WORLD_WRITE',api='setBlock',x=x,y=y,z=z,block=b,metadata=meta,flags=flags,applied=applied))
 def noisy_mesh(self,rad,height):
  cof=max(rad/10.,1.);a=self.draw('nextDouble')+.5;b=1.-a+.5+.5;half=math.trunc(rad/2);cutoff=rad/2./(1.+abs(a-b)/3.)
  for ix,iy,iz in itertools.product(range(rad+1),range(height+1),range(rad+1)):
   p=(-16+ix-half,70-iy,iz-half);dx,dy,dz=-16-p[0],70-p[1],-p[2];distance=math.sqrt(dx*dx*a+dy*dy+dz*dz*b);threshold=cutoff+(self.draw('nextDouble')*cof-cof/2.)
   yield p,distance<threshold
 def mire(self,rad,target='JungleQuicksandBlock',replace_water=False):
  # Transaction grammar: each accepted voxel emits target; a later support pass repairs below targets.
  for p,inside in self.noisy_mesh(rad,math.trunc(rad/2)):
   if inside and self.query(p)!='SoftQuicksandBlock'and(not replace_water or self.query(p)in {'field_150355_j','field_150358_i'}):self.write(p,target)
  half=math.trunc(rad/2)
  for ix,iy,iz in itertools.product(range(rad+1),range(half+3),range(rad+1)):
   p=(-16+ix-half,70-iy,iz-half);above=(p[0],p[1]+1,p[2])
   if self.query(p)not in {target,'SoftQuicksandBlock','SlurryBlock'}and self.query(above)==target:self.write(p,'field_150348_b')
 def dry(self,rad):
  # Three-cell vertical stamp, preserving transaction order and overwrites.
  for p,inside in self.noisy_mesh(rad,rad):
   if inside:
    for delta,b in [(0,'SandBlock'),(-1,'SandBlock'),(-2,'field_150322_A')]:self.write((p[0],p[1]+delta,p[2]),b)
  if rad<=4:return
  hollow=rad<10 or self.draw('nextInt',2+rad//2)==0
  if not hollow:return
  half=rad//2;allowed={'field_150350_a','SandBlock'};neighbors=[(-1,0,0),(1,0,0),(0,0,1),(0,0,-1),(0,-1,0)]
  # Ordered erosion of unsupported shallow sand, not a simultaneous mask operation.
  for ix,iy,iz in itertools.product(range(rad+1),range(rad+2),range(rad+1)):
   p=(-16+ix-half,70-iy,iz-half)
   if iy<rad//3 and self.query(p)=='SandBlock'and all(self.query(tuple(a+b for a,b in zip(p,d)))in allowed for d in neighbors):self.write(p,'field_150350_a')
 def wld(self):
  self.draw('nextInt',5);assert self.draw('nextInt',10)!=0
  if self.fixture.startswith('wld-reject'):
   self.draw('nextInt',5) # Ashes fallback samples attempt count before testing isAshes
   if self.fixture.endswith('-overlap'):self.draw('nextInt',4)
   return
  dx=self.draw('nextInt',16)-8;dz=self.draw('nextInt',16)-8;assert (dx,dz)==(-5,1)
  worldrng=Random(9,'world');_,event=worldrng.draw('nextInt',[3]);self.events.append(dict(event='RNG_CALL',**event)) # open-air predicate rejects before puddle probability is sampled
  self.write((-64,63,-48),'TarBlock');self.write((-64,62,-48),'TarBlock')
  for axis in [(-1,0),(1,0),(0,-1),(0,1)]:
   for step in range(1,10):self.write((-64+axis[0]*step,62,-48+axis[1]*step),'field_150322_A')
  self.draw('nextInt',5) # rewriter leaves blockGen false; post-structure Ashes count draw remains
 def planting(self):
  for attempt in range(128):
   p=(-16,71,0);candidate=True
   for walk in range(attempt//16):
    dx=self.draw('nextInt',3)-1;dy=math.trunc((self.draw('nextInt',3)-1)*self.draw('nextInt',3)/2);dz=self.draw('nextInt',3)-1;p=(p[0]+dx,p[1]+dy,p[2]+dz)
    if self.query((p[0],p[1]-1,p[2]))not in {'field_150349_c','MorassBlock'}or self.query(p)not in {'field_150350_a','MorassBlock','fixture_flower'}:candidate=False;break
   if not candidate or self.query(p)!='field_150350_a':continue
   if self.draw('nextInt',8)!=0:continue
   self.events.append(dict(event='WORLD_READ',api='biome',x=p[0],z=p[2],id=1))
   self.events.append(dict(event='BIOME_FLOWER',x=p[0],y=p[1],z=p[2]));name='none'if self.fixture=='plant-null'else'fixture_flower';self.events.append(dict(event='FLOWER_LOOKUP',name=name))
   if name=='none':continue
   allowed=self.fixture!='plant-refuse';self.events.append(dict(event='PLANT_CHECK',x=p[0],y=p[1],z=p[2],allowed=allowed))
   if allowed:self.write(p,'fixture_flower',3,2)
def verify(events,model,name,rad,seed,fixture,config='0'):
 s=Spec(seed,fixture)
 if name=='generateMire':s.mire(rad,'MudBlock'if config=='MudBlock'else'JungleQuicksandBlock',config=='water-only')
 elif name=='generateSoftSand':s.dry(rad)
 elif name=='PlantingThis':s.planting()
 elif name=='generateWLD':s.wld()
 else:return None
 # Full BRANCH/helper/read equivalence is checked by the separate VM. This independently checks geometry/transaction semantics.
 kinds={'RNG_CALL','WORLD_WRITE'}|({'BIOME_FLOWER','FLOWER_LOOKUP','PLANT_CHECK'}if name=='PlantingThis'else set())
 actual=[{k:v for k,v in e.items()if k not in ['method','offset']}for e in events if e['event']in kinds];expected=[e for e in s.events if e['event']in kinds]
 assert actual==expected,(name,'independent declarative event diff',next((i for i,(a,b)in enumerate(zip(actual,expected))if a!=b),None),len(actual),len(expected))
 assert s.cells==model.blocks and s.meta==model.meta,(name,'declarative final state')
 return dict(status='MODEL_TESTED_DECLARATIVE_ORACLE',ordered_random_and_mutation_events=len(actual),final_cells=len(s.cells),scope='geometry/noise or random-walk transaction contract; full VM event equality checked separately')
