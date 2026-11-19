from pathlib import Path
import json

def add(src,ms,selected,lines):
 def w(cls,body):
  p=src/(cls.replace('.','/')+'.java');p.parent.mkdir(parents=True,exist_ok=True);p.write_text('package '+cls.rsplit('.',1)[0]+';\n'+body+'\n')
 w('net.minecraft.entity.ai.attributes.IAttribute','public interface IAttribute {}')
 w('net.minecraft.entity.ai.attributes.AttributeModifier','''public class AttributeModifier {public java.util.UUID uuid;public double amount;public int operation;public boolean saved=true;public AttributeModifier(java.util.UUID id,String n,double a,int op){uuid=id;amount=a;operation=op;}public AttributeModifier func_111168_a(boolean b){saved=b;return this;}}''')
 w('net.minecraft.entity.ai.attributes.IAttributeInstance','''public interface IAttributeInstance {AttributeModifier func_111127_a(java.util.UUID id);void func_111124_b(AttributeModifier m);void func_111121_a(AttributeModifier m);}''')
 w('audit.AttributeState','''public class AttributeState implements net.minecraft.entity.ai.attributes.IAttributeInstance {public java.util.Map<java.util.UUID,net.minecraft.entity.ai.attributes.AttributeModifier> map=new java.util.HashMap<>();public net.minecraft.entity.ai.attributes.AttributeModifier func_111127_a(java.util.UUID id){audit.Trace.emit("ATTR_QUERY","present",map.containsKey(id));return map.get(id);}public void func_111124_b(net.minecraft.entity.ai.attributes.AttributeModifier m){map.remove(m.uuid);audit.Trace.emit("ATTR_REMOVE","uuid",m.uuid);}public void func_111121_a(net.minecraft.entity.ai.attributes.AttributeModifier m){map.put(m.uuid,m);audit.Trace.emit("ATTR_ADD","uuid",m.uuid,"operation",m.operation,"amount",m.amount,"saved",m.saved);}}''')
 w('net.minecraft.entity.EntityLivingBase','''public class EntityLivingBase {public float field_70747_aH=.02f;public boolean field_70124_G=false;public audit.AttributeState attrs=new audit.AttributeState();public MoreFunQuicksandMod.main.PotionStuck props=new MoreFunQuicksandMod.main.PotionStuck();public net.minecraft.entity.ai.attributes.IAttributeInstance func_110148_a(net.minecraft.entity.ai.attributes.IAttribute a){return attrs;}}''')
 w('net.minecraft.entity.SharedMonsterAttributes','public class SharedMonsterAttributes {public static net.minecraft.entity.ai.attributes.IAttribute field_111263_d=new net.minecraft.entity.ai.attributes.IAttribute(){};}')
 w('MoreFunQuicksandMod.main.PotionStuck','''public class PotionStuck {public int Level=-1;public static PotionStuck get(net.minecraft.entity.EntityLivingBase e){audit.Trace.emit("PROP_GET","present",e.props!=null);return e.props;}public int getLevel(){return Level;}public void setStuckLevel(int value){Level=value;audit.Trace.emit("LEVEL_SET","value",value);}}''')
 w('net.minecraftforge.event.entity.living.LivingEvent','public class LivingEvent {public static class LivingUpdateEvent {public net.minecraft.entity.EntityLivingBase entityLiving;public LivingUpdateEvent(net.minecraft.entity.EntityLivingBase e){entityLiving=e;}}}')
 w('net.minecraft.nbt.NBTTagCompound','''public class NBTTagCompound {public java.util.Map<String,Object>data=new java.util.TreeMap<>();public void func_74777_a(String k,short v){data.put(k,(int)v);audit.Trace.emit("NBT_SET","key",k,"value",(int)v);}public void func_74778_a(String k,String v){data.put(k,v);audit.Trace.emit("NBT_SET","key",k,"value",v);}}''')
 w('net.minecraft.tileentity.TileEntity','public class TileEntity {}')
 w('net.minecraft.tileentity.TileEntityMobSpawner','''public class TileEntityMobSpawner extends TileEntity {public net.minecraft.nbt.NBTTagCompound saved;public void func_145841_b(net.minecraft.nbt.NBTTagCompound tag){audit.Trace.emit("NBT_EXPORT");}public void func_145839_a(net.minecraft.nbt.NBTTagCompound tag){saved=tag;audit.Trace.emit("NBT_IMPORT","data",tag.data);}}''')
 w('net.minecraft.tileentity.TileEntityChest','public class TileEntityChest extends TileEntity implements net.minecraft.inventory.IInventory {}')
 # Verification-only declarations for a genuine chest attempt; missing API fails explicitly, not skipped.
 w('net.minecraft.item.Item','public class Item {public String id;public Item(String n){id=n;}}')
 w('net.minecraft.init.Items','public class Items {}')
 for m in ms:
  choose=(m['class'].endswith('.CustomPotionEvent')and m['name']in ['onLivingUpdateEvent','<clinit>'])or(m['class'].endswith('.GenerateDesertTombs')and m['name']in ['generateSpawner','generateChest','generateChest2','setBlock'])or(m['class'].endswith('.CustomWorldGen')and m['name']=='generateWLD')
  if not choose:continue
  selected.append(m)
  for i in m['instructions']:
   t=i['args'].split()[0]if i['opcode'].startswith('if')or i['opcode']in ['goto','goto_w']else'';lines.append(m['class']+'#'+m['name']+m['descriptor']+'\t'+str(i['offset'])+('\t'+t if t else''))
 # Item field descriptors must match original bytecode for class verification/linkage.
 fields={}
 for m in ms:
  if not m['class'].endswith('.GenerateDesertTombs'):continue
  for i in m['instructions']:
   if 'Field net/minecraft/init/Items.'in i['args']:
    field,d=i['args'].split('Items.',1)[1].split(':');fields[field]=d[1:-1].replace('/','.')
 for cls in set(fields.values())-{'net.minecraft.item.Item'}:w(cls,'public class '+cls.split('.')[-1]+' extends Item {public '+cls.split('.')[-1]+'(String id){super(id);}}')
 w('net.minecraft.init.Items','public class Items {'+'\n'.join('public static '+t+' '+n+'=new '+t+'("'+n+'");'for n,t in fields.items())+'}')
 w('net.minecraft.tileentity.TileEntityChest','''public class TileEntityChest extends TileEntity implements net.minecraft.inventory.IInventory {public java.util.Map<Integer,String>slots=new java.util.TreeMap<>();public void set(int slot,String id,int meta,int count){slots.put(slot,id+":"+meta+"x"+count);audit.Trace.emit("INVENTORY_SET","slot",slot,"item",id,"metadata",meta,"count",count);}}''')
 w('net.minecraft.util.WeightedRandomChestContent','''public class WeightedRandomChestContent {public net.minecraft.item.Item item;public int meta,min,max,weight;public WeightedRandomChestContent(net.minecraft.item.Item i,int m,int a,int b,int c){item=i;meta=m;min=a;max=b;weight=c;}public static void func_76293_a(java.util.Random r,WeightedRandomChestContent[] table,net.minecraft.inventory.IInventory inv,int rolls){int total=0;for(var e:table)total+=e.weight;for(int t=0;t<rolls;t++){int v=r.nextInt(total);WeightedRandomChestContent chosen=null;for(var e:table){v-=e.weight;if(v<0){chosen=e;break;}}int count=chosen.min+r.nextInt(chosen.max-chosen.min+1);int slot=r.nextInt(27);((net.minecraft.tileentity.TileEntityChest)inv).set(slot,chosen.item.id,chosen.meta,count);}}}''')
 w('net.minecraftforge.common.ChestGenHooks','''public class ChestGenHooks {public static net.minecraft.util.WeightedRandomChestContent[]getItems(String name,java.util.Random r){audit.Trace.emit("LOOT_TABLE","name",name,"entries",1);return new net.minecraft.util.WeightedRandomChestContent[]{new net.minecraft.util.WeightedRandomChestContent(new net.minecraft.item.Item("fixture_token"),0,1,1,2)};}}''')
 # Original Tombs class verification also resolves specialized vanilla Block field types.
 blockfields={}
 for m in ms:
  if not m['class'].endswith('.GenerateDesertTombs'):continue
  for i in m['instructions']:
   if 'Field net/minecraft/init/Blocks.'in i['args']:
    field,d=i['args'].split('Blocks.',1)[1].split(':');blockfields[field]=d[1:-1].replace('/','.')
 bp=src/'net/minecraft/init/Blocks.java';body=bp.read_text();decl=[]
 for name,t in blockfields.items():
  if name in body:continue
  decl.append('public static '+t+' '+name+'=new '+t+'("'+name+'");')
  if t!='net.minecraft.block.Block'and not(src/(t.replace('.','/')+'.java')).exists():w(t,'public class '+t.split('.')[-1]+' extends Block {public '+t.split('.')[-1]+'(String id){super(id);}}')
 bp.write_text(body.rsplit('}',1)[0]+'\n'+'\n'.join(decl)+'\n}')
