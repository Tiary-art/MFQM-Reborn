"""Independent Python stack machine, never calls the JVM/ASM implementation.
Used alongside declarative geometry/action oracles, not as sole semantic proof.
Fail closed on unsupported opcode/API; supports declared fixture contracts only.
"""
import math,struct,re

def f32(x):return struct.unpack('>f',struct.pack('>f',x))[0]
def i32(x):return (int(x)+(1<<31))%(1<<32)-(1<<31)
def params(desc):
 x=desc[1:desc.index(')')];out=[]
 while x:
  m=re.match(r'(?:\[)*(?:L[^;]+;|[ZBCSIJFD])',x);assert m,desc;out.append(m[0]);x=x[len(m[0]):]
 return out
class Random:
 def __init__(self,seed,name):self.state=(seed^0x5DEECE66D)&((1<<48)-1);self.ordinal=0;self.name=name
 def bits(self,n):self.state=(self.state*0x5DEECE66D+11)&((1<<48)-1);return self.state>>(48-n)
 def draw(self,api,args):
  before=self.state
  if api=='nextInt':
   b=args[0]
   if b<=0:raise ValueError('bound must be positive')
   if b&-b==b:v=(b*self.bits(31))>>31
   else:
    while True:
     n=self.bits(31);v=n%b
     if n-v+b-1<1<<31:break
  elif api=='nextDouble':v=((self.bits(26)<<27)+self.bits(27))/(1<<53)
  elif api=='nextFloat':v=f32(self.bits(24)/(1<<24))
  else:raise NotImplementedError(api)
  e=dict(rng=self.name,api=api,value=v,before=before,after=self.state,ordinal=self.ordinal);self.ordinal+=1
  if api=='nextInt':e['bound']=args[0]
  return v,e
class Oracle:
 def __init__(self,methods,seed=0,fixture='stone',config='NONE',dim=0):
  self.methods={m['class']+'#'+m['name']+m['descriptor']:m for m in methods};self.fixture=fixture;self.config=config;self.dim=dim;self.events=[];self.blocks={};self.meta={};self.cur='';self.offset=-1;self.passed=Random(seed,'passed');self.worldrng=Random(9,'world');self.this={'T_BoP':False};self.steps=0
 def emit(self,event,**data):self.events.append(dict(event=event,method=self.cur,offset=self.offset,**data))
 def peek(self,x,y,z):
  if(x,y,z)in self.blocks:return self.blocks[x,y,z]
  if self.fixture=='wld-positive':
   return 'fixture_lava'if(x,y,z)==(-64,63,-48)else'field_150354_m'if(x,y,z)==(-69,63,-47)else'field_150348_b'if(x,y,z)==(-64,61,-48)else'field_150350_a'
  if self.fixture.startswith('wld-reject'):return 'field_150350_a'
  if self.fixture.startswith('plant-'):return 'MorassBlock'if y<=70 else'field_150350_a'
  if self.fixture=='empty':return 'field_150350_a'
  if self.fixture=='pond':return 'field_150350_a'if y>66 else'field_150355_j'if y==66 and x%4==0 else'field_150354_m'
  if self.fixture=='water':return 'field_150355_j'if y<=70 else'field_150350_a'
  if self.fixture in ['desert','desert-refuse']:return 'field_150354_m'if y<=70 else'field_150350_a'
  if self.fixture=='protected':return 'SoftQuicksandBlock'if y<=70 else'field_150350_a'
  return 'field_150348_b'if y<=70 else'field_150350_a'
 def material(self,b):return 'field_151583_m'if b=='MorassBlock'else'field_151585_k'if b=='fixture_flower'else'field_151587_i'if b=='fixture_lava'else'field_151579_a'if b=='field_150350_a'else'field_151586_h'if b in ['field_150355_j','field_150358_i']else'field_151595_p'if b=='field_150354_m'else'field_151576_e'
 def solid(self,b):return self.material(b)not in ['field_151579_a','field_151586_h','field_151587_i']
 def get(self,x,y,z):
  b=self.peek(x,y,z);self.emit('WORLD_READ',api='getBlock',x=x,y=y,z=z,block=b);return b
 def write(self,x,y,z,b,m=0,f=3):
  applied=self.fixture!='desert-refuse'and(self.fixture!='deny'or y!=63)
  if applied:self.blocks[x,y,z]=b;self.meta[x,y,z]=m
  self.emit('WORLD_WRITE',api='setBlock',x=x,y=y,z=z,block=b,metadata=m,flags=f,applied=applied);return applied
 def invoke(self,name,desc,args,obj,currentclass,static):
  n=name.rsplit('.',1)[-1];owner=name.rsplit('.',1)[0].replace('/','.')if'.'in name else currentclass
  key=owner+'#'+n+desc
  if key in self.methods:
   values=args if static else[obj]+args;return self.run(key,values)
  if n=='<init>':
   if obj.get('class')=='java/util/ArrayList':obj['items']=list(args[0])
   elif obj.get('class')=='net/minecraft/util/WeightedRandomChestContent':obj.update(dict(zip(['item','meta','min','max','weight'],args)))
   return None
  if n=='func_72899_e':
   x,y,z=args;self.emit('WORLD_READ',api='chunkExists',x=x,y=y,z=z)
   if self.fixture.startswith('wld-reject'):return False
   if self.fixture=='wld-positive':return x==-56 and z==-40
   raise NotImplementedError('chunk storage contract missing')
  if n=='func_147438_o':
   if self.fixture=='null-tile':self.emit('TILE_GET',kind='null');self.tile=None;return None
   kind='TileEntityMobSpawner'if self.peek(*args)=='field_150474_ac'else'TileEntityChest';self.tile={'class':kind,'data':{},'slots':{}};self.emit('TILE_GET',kind=kind);return self.tile
  if n=='func_145841_b':self.emit('NBT_EXPORT');return None
  if n in ['func_74777_a','func_74778_a']:obj['data'][args[0]]=args[1];self.emit('NBT_SET',key=args[0],value=args[1]);return None
  if n=='func_145839_a':obj['data']=dict(args[0]['data']);self.emit('NBT_IMPORT',data=self.java_map(obj['data']));return None
  if n=='println':self.stderr=args[0];return None
  if owner=='net.minecraftforge.common.ChestGenHooks' and n=='getItems':self.emit('LOOT_TABLE',name=args[0],entries=1);return [dict(item='fixture_token',meta=0,min=1,max=1,weight=2)]
  if owner=='java.util.Arrays'and n=='asList':return list(args[0])
  if n=='add':obj['items'].append(args[0]);return True
  if n=='size':return len(obj['items'])
  if n=='toArray':return list(obj['items'])
  if n=='func_76293_a':
   import bisect,itertools
   rng,table,tile,rolls=args;cdf=list(itertools.accumulate(e['weight']for e in table))
   def draw(bound):
    value,event=rng.draw('nextInt',[bound]);self.emit('RNG_CALL',**event);return value
   for roll in range(rolls):
    chosen=table[bisect.bisect_right(cdf,draw(cdf[-1]))];count=chosen['min']+draw(chosen['max']-chosen['min']+1);slot=draw(27);tile['slots'][slot]=chosen['item']+':'+str(chosen['meta'])+'x'+str(count);self.emit('INVENTORY_SET',slot=slot,item=chosen['item'],metadata=chosen['meta'],count=count)
   return None
  if isinstance(obj,Random):
   v,e=obj.draw(n,args);self.emit('RNG_CALL',**e);return v
  if owner=='java.lang.Math':return {'pow':math.pow,'sqrt':math.sqrt,'max':max,'min':min,'abs':abs,'floor':math.floor,'round':lambda x:math.floor(x+.5),'sin':math.sin,'cos':math.cos,'toRadians':math.radians}[n](*args)
  if n=='func_147439_a':return self.get(*args)
  if n=='func_147465_d':return self.write(*args)
  if n=='func_147449_b':return self.write(*args,0,3)
  if n=='func_147468_f':return self.write(*args,'field_150350_a',0,3)
  if n=='func_72805_g':
   x,y,z=args;v=self.meta.get(tuple(args),0);self.emit('WORLD_READ',api='metadata',x=x,y=y,z=z,value=v);return v
  if n=='func_72807_a':
   x,z=args;self.emit('WORLD_READ',api='biome',x=x,z=z,id=0 if self.fixture.startswith('wld-')else 1);return {'class':'BiomeGenDesert','field_76756_M':0 if self.fixture.startswith('wld-')else 1,'field_76752_A':'field_150349_c','field_76753_B':'field_150346_d'}
  if n=='func_149688_o':return 'material:'+self.material(obj)
  if n in ['func_76220_a','func_76218_k']:return obj not in ['material:field_151579_a','material:field_151586_h','material:field_151587_i']
  if n=='func_76224_d':return obj in ['material:field_151586_h','material:field_151587_i']
  if n=='func_149721_r':return False if obj in ['MorassBlock','fixture_flower']else self.solid(obj)
  if n=='func_149662_c':return self.solid(obj)
  if n=='func_149716_u':return False
  if n=='func_147437_c':return self.get(*args)=='field_150350_a'
  if n=='func_150572_a':
   rng,x,y,z=args;self.emit('BIOME_FLOWER',x=x,y=y,z=z);return 'none'if self.fixture=='plant-null'else'fixture_flower'
  if n=='func_149857_e':self.emit('FLOWER_LOOKUP',name=args[0]);return None if args[0]=='none'else'fixture_flower'
  if n=='func_149856_f':return 2
  if n=='func_149718_j':
   w,x,y,z=args;ok=self.fixture!='plant-refuse';self.emit('PLANT_CHECK',x=x,y=y,z=z,allowed=ok);return ok
  raise NotImplementedError((self.cur,self.offset,name,desc))
 def java_map(self,d):return '{'+', '.join(str(k)+'='+str(d[k])for k in sorted(d))+'}'
 def run(self,key,args):
  m=self.methods[key];ins=m['instructions'];pos={v['offset']:i for i,v in enumerate(ins)};st=[];loc={};types=params(m['descriptor']);isstatic='static'in m['declaration'];slot=0;values=list(args)
  if not isstatic:loc[0]=values.pop(0);slot=1
  for typ,v in zip(types,values):loc[slot]=v;slot+=2 if typ in ['J','D']else 1
  saved=self.cur,self.offset;self.cur=key;self.offset=0;self.emit('HELPER_ENTER');pc=0;cls=m['class']
  while pc<len(ins):
   self.steps+=1
   if self.steps>50000000:raise RuntimeError('oracle instruction budget')
   i=ins[pc];pc+=1;op=i['opcode'];text=i['args'];self.offset=i['offset']
   if op.startswith(('aload','iload','fload','dload','lload')):st.append(loc[int(op.split('_')[1])if'_'in op else int(text)])
   elif op.startswith(('astore','istore','fstore','dstore','lstore')):
    idx=int(op.split('_')[1])if'_'in op else int(text);loc[idx]=st.pop()
    if m['name']=='generateSurface'and idx==13 or m['name']=='generateAOADimGardencia'and idx==11:self.emit('BLOCKGEN',value=loc[idx])
   elif op=='new':
    target=text.split('// class ',1)[1]
    if target not in ['net/minecraft/nbt/NBTTagCompound','java/util/ArrayList','net/minecraft/util/WeightedRandomChestContent']:raise NotImplementedError(('new',target))
    st.append({'class':target,'data':{},'items':[]})
   elif op=='anewarray':n=st.pop();st.append([None]*n)
   elif op=='aconst_null':st.append(None)
   elif op.startswith('iconst_'):st.append(-1 if op.endswith('m1')else int(op[-1]))
   elif op.startswith(('dconst_','fconst_','lconst_')):st.append(float(op[-1]))
   elif op in ['bipush','sipush']:st.append(int(text))
   elif op.startswith('ldc'):
    typ,v=text.split('// ',1)[1].split(' ',1);st.append(v if typ=='String'else float(v.rstrip('dDfF'))if typ in ['double','float']else int(v.rstrip('lL')))
   elif op=='iinc':v,delta=map(int,text.split(','));loc[v]=i32(loc[v]+delta)
   elif op in ['iadd','isub','imul','idiv','irem','dadd','dsub','dmul','ddiv','fadd','fsub','fmul','fdiv','ladd']:
    b=st.pop();a=st.pop();kind=op[1:];v={'add':lambda:a+b,'sub':lambda:a-b,'mul':lambda:a*b,'div':lambda:math.trunc(a/b)if op[0]in'il'else a/b,'rem':lambda:a-math.trunc(a/b)*b}[kind]();st.append(i32(v)if op[0]=='i'else f32(v)if op[0]=='f'else v)
   elif op in ['i2d','f2d','d2f','i2f','d2i','l2i','i2l']:
    v=st.pop();st.append(f32(v)if op in ['d2f','i2f']else float(v)if op in ['i2d','f2d']else i32(v)if op in ['d2i','l2i']else int(v))
   elif op in ['dcmpg','dcmpl','fcmpg','fcmpl']:
    b=st.pop();a=st.pop();st.append((1 if op.endswith('g')else -1)if math.isnan(a)or math.isnan(b)else(1 if a>b else -1 if a<b else 0))
   elif op=='getstatic':
    field,desc=text.split('// Field ',1)[1].split(':',1);n=field.split('.')[-1]
    if 'MFQM.'in field:
     value=n in self.config.split(',') if desc=='Z'else[0]*256 if desc=='[I'else 0 if desc=='I'else n
     if n=='WLDBiomes'and self.fixture.startswith('wld-')and not self.fixture.endswith('-overlap'):value=[0 if j==1 else-999 for j in range(256)]
     if desc=='Z'and n.startswith('Gen'):self.emit('CONFIG_GATE',name=n,value=value)
    else:value='material:'+n if'/Material.'in field else n
    st.append(value)
   elif op=='getfield':
    field=text.split('// Field ',1)[1].split(':')[0].split('.')[-1];obj=st.pop()
    if obj=='WORLD':v=self.worldrng if field=='field_73012_v'else{'field_76574_g':self.dim}if field=='field_73011_w'else None
    else:v=obj[field]
    st.append(v)
   elif op=='putfield':v=st.pop();obj=st.pop();n=text.split('// Field ',1)[1].split(':')[0].split('.')[-1];obj[n]=v
   elif op=='arraylength':st.append(len(st.pop()))
   elif op=='iaload':
    idx=st.pop();arr=st.pop()
    if idx<0 or idx>=len(arr):raise IndexError('Java array index')
    st.append(arr[idx])
   elif op=='instanceof':obj=st.pop();name=text.split('// class ',1)[1].split('/')[-1];st.append(isinstance(obj,dict)and obj.get('class')==name)
   elif op=='checkcast':
    target=text.split('// class ',1)[1].strip(chr(34));obj=st[-1]
    if obj is not None:
     if target.startswith('[Lnet/minecraft/util/WeightedRandomChestContent;'):assert isinstance(obj,list)and all(isinstance(v,dict)and 'weight'in v for v in obj),'array cast contract'
     elif target in ['net/minecraft/tileentity/TileEntityMobSpawner','net/minecraft/tileentity/TileEntityChest']:assert isinstance(obj,dict)and obj.get('class')==target.split('/')[-1],'tile cast contract'
     else:raise NotImplementedError(('checkcast',target))
   elif op=='dup':st.append(st[-1])
   elif op=='pop':st.pop()
   elif op.startswith('invoke'):
    target=text.split('// ',1)[1].split(' ',1)[1];n,d=target.split(':',1);n=n.replace('"','');nargs=len(params(d));aa=[st.pop()for _ in range(nargs)][::-1];obj=None if op=='invokestatic'else st.pop();v=self.invoke(n,d,aa,obj,cls,op=='invokestatic')
    if d.split(')')[1]!='V':st.append(v)
   elif op in ['tableswitch','lookupswitch']:
    v=st.pop();self.emit('SWITCH',value=v);pc=pos[int(m['switches'][str(i['offset'])].get(str(v),m['switches'][str(i['offset'])]['default']))]
   elif op in ['goto','goto_w']:self.emit('BRANCH',opcode=167,taken=True,target=int(text));pc=pos[int(text)]
   elif op.startswith('if'):
    names={'eq':(153,lambda a,b:a==b),'ne':(154,lambda a,b:a!=b),'lt':(155,lambda a,b:a<b),'ge':(156,lambda a,b:a>=b),'gt':(157,lambda a,b:a>b),'le':(158,lambda a,b:a<=b)}
    if op in ['ifnull','ifnonnull']:a=st.pop();yes=(a is None)if op=='ifnull'else a is not None;opcode=198 if op=='ifnull'else 199
    else:
     pair=op.startswith(('if_icmp','if_acmp'));b=st.pop()if pair else 0;a=st.pop();code=op.split('cmp')[1]if pair else op[2:];opcode,fn=names[code];opcode+=6 if op.startswith('if_icmp')else 12 if op.startswith('if_acmp')else 0;yes=fn(a,b)
    self.emit('BRANCH',opcode=opcode,taken=yes,target=int(text))
    if yes:pc=pos[int(text)]
   elif op in ['return','ireturn','areturn','freturn','dreturn']:
    value=None if op=='return'else st.pop();self.emit('HELPER_EXIT');self.cur,self.offset=saved;return value
   else:raise NotImplementedError((key,self.offset,op,text))
  raise AssertionError('fell off method')
