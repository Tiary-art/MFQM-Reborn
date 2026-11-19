package audit;
import java.nio.file.*;
import java.util.jar.*;
import jdk.internal.org.objectweb.asm.*;
/** Copy exactly the original isTrulySink body into an isolated class shell, never patch the input JAR. */
public class HelperProbe {
    public static void main(String[] args) throws Exception {
        String owner="MoreFunQuicksandMod/main/MFQM";
        byte[] raw;
        try(var jar=new JarFile(args[0])){raw=jar.getInputStream(jar.getJarEntry(owner+".class")).readAllBytes();}
        ClassWriter shell=new ClassWriter(0);shell.visit(Opcodes.V1_8,Opcodes.ACC_PUBLIC,owner,null,"java/lang/Object",null);
        new ClassReader(raw).accept(new ClassVisitor(Opcodes.ASM8){
            public MethodVisitor visitMethod(int flags,String name,String desc,String sig,String[] ex){
                return name.equals("isTrulySink")?shell.visitMethod(flags,name,desc,sig,ex):null;
            }
        },0);shell.visitEnd();byte[] copied=shell.toByteArray();BodyProof.check(raw,copied,"isTrulySink");
        Path dest=Path.of(args[1],owner+".class");Files.createDirectories(dest.getParent());Files.write(dest,copied);
        var method=Class.forName(owner.replace('/','.')).getMethod("isTrulySink",net.minecraft.entity.Entity.class,double.class);
        for(boolean player:new boolean[]{false,true})for(boolean client:new boolean[]{false,true}){
            var entity=player?new net.minecraft.entity.player.EntityPlayer():new net.minecraft.entity.Entity();
            entity.field_70170_p=new net.minecraft.world.World();entity.field_70170_p.field_72995_K=client;
            boolean result=(Boolean)method.invoke(null,entity,.2);
            if(result!=(player?client:true))throw new AssertionError("native gate differs");
            System.out.println("NATIVE_GATE player="+player+" client="+client+" result="+result);
        }
    }
}
