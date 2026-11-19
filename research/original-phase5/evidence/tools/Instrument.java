package audit;
import java.nio.file.*;import java.util.*;import java.io.*;import jdk.internal.org.objectweb.asm.*;
public class Instrument extends ClassLoader {
 Map<String,List<Integer>> offsets=new HashMap<>();Map<String,Map<Integer,Integer>> targets=new HashMap<>();java.util.jar.JarFile jar;
 public Instrument(String j,String map)throws Exception{super(Instrument.class.getClassLoader());jar=new java.util.jar.JarFile(j);for(String s:Files.readAllLines(Path.of(map))){String[]p=s.split("\t");offsets.computeIfAbsent(p[0],k->new ArrayList<>()).add(Integer.valueOf(p[1]));if(p.length>2)targets.computeIfAbsent(p[0],k->new HashMap<>()).put(Integer.valueOf(p[1]),Integer.valueOf(p[2]));}}
 @Override protected Class<?> findClass(String name)throws ClassNotFoundException {try{var en=jar.getJarEntry(name.replace('.','/')+".class");if(en==null)throw new ClassNotFoundException(name);byte[]raw=jar.getInputStream(en).readAllBytes();byte[]derived=transform(raw,name);return defineClass(name,derived,0,derived.length);
 }catch(Exception e){throw new ClassNotFoundException(name,e);}}
 public byte[] transform(byte[]raw,String name){ClassReader cr=new ClassReader(raw);ClassWriter cw=new ClassWriter(ClassWriter.COMPUTE_MAXS);cr.accept(new ClassVisitor(Opcodes.ASM8,cw){
 public MethodVisitor visitMethod(int access,String n,String d,String sig,String[]exc){MethodVisitor base=super.visitMethod(access,n,d,sig,exc);String key=name+"#"+n+d;if(!offsets.containsKey(key))return base;
 return new MethodVisitor(Opcodes.ASM8,base){int index=0,off;
 void push(int x){mv.visitLdcInsn(x);}void call(String n,String d){mv.visitMethodInsn(Opcodes.INVOKESTATIC,"audit/Trace",n,d,false);}
 void pre(){List<Integer>list=offsets.get(key);if(index>=list.size())throw new IllegalStateException("instruction count mismatch "+key);off=list.get(index++);if(!n.equals("generateSurface")){push(off);call("at","(I)V");}}
 void mark(){if(n.equals("generateSurface")){push(off);call("at","(I)V");}}
 public void visitCode(){super.visitCode();mv.visitLdcInsn(key);call("enter","(Ljava/lang/String;)V");}
 public void visitInsn(int op){pre();if(op>=172&&op<=177){mark();call("exit","()V");}super.visitInsn(op);}
 public void visitIntInsn(int op,int v){pre();super.visitIntInsn(op,v);}public void visitVarInsn(int op,int v){pre();if(((n.equals("generateAOADimGardencia")&&v==11)||(n.equals("generateSurface")&&v==13))&&op==Opcodes.ISTORE){mark();mv.visitInsn(Opcodes.DUP);call("blockGen","(I)V");}super.visitVarInsn(op,v);}
 public void visitTypeInsn(int op,String v){pre();super.visitTypeInsn(op,v);}
 public void visitFieldInsn(int op,String o,String n,String d){pre();mark();super.visitFieldInsn(op,o,n,d);if(op==Opcodes.GETSTATIC&&o.equals("MoreFunQuicksandMod/main/MFQM")&&n.startsWith("Gen")&&d.equals("Z")){mv.visitInsn(Opcodes.DUP);mv.visitLdcInsn(n);mv.visitInsn(Opcodes.SWAP);call("config","(Ljava/lang/String;Z)V");}}
 public void visitMethodInsn(int op,String o,String n,String d,boolean itf){pre();mark();super.visitMethodInsn(op,o,n,d,itf);}
 public void visitJumpInsn(int op,Label label){pre();mark();int target=targets.getOrDefault(key,Map.of()).getOrDefault(off,-1);if(op>=153&&op<=158){mv.visitInsn(Opcodes.DUP);push(op);push(target);call("one","(III)V");}else if(op>=159&&op<=164){mv.visitInsn(Opcodes.DUP2);push(op);push(target);call("pair","(IIII)V");}else if(op==165||op==166){mv.visitInsn(Opcodes.DUP2);push(op);push(target);call("obj","(Ljava/lang/Object;Ljava/lang/Object;II)V");}else if(op==198||op==199){mv.visitInsn(Opcodes.DUP);push(op);push(target);call("nul","(Ljava/lang/Object;II)V");}else if(op==167){push(target);call("jump","(I)V");}else throw new UnsupportedOperationException("jump "+op);super.visitJumpInsn(op,label);}
 public void visitLdcInsn(Object v){pre();super.visitLdcInsn(v);}public void visitIincInsn(int v,int i){pre();super.visitIincInsn(v,i);}
 public void visitTableSwitchInsn(int min,int max,Label def,Label...labs){pre();mark();mv.visitInsn(Opcodes.DUP);call("sw","(I)V");super.visitTableSwitchInsn(min,max,def,labs);}
 public void visitLookupSwitchInsn(Label def,int[]keys,Label[]labs){pre();mark();mv.visitInsn(Opcodes.DUP);call("sw","(I)V");super.visitLookupSwitchInsn(def,keys,labs);}
 public void visitMultiANewArrayInsn(String d,int dims){pre();super.visitMultiANewArrayInsn(d,dims);}
 public void visitEnd(){if(index!=offsets.get(key).size())throw new IllegalStateException("instruction list mismatch "+key+" "+index+"/"+offsets.get(key).size());super.visitEnd();}
 };}},0);return cw.toByteArray();}
}
