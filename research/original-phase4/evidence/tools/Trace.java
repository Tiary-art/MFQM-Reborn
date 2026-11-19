package audit;
import java.io.*;import java.util.*;
public final class Trace {
 public static PrintWriter out; public static String method="",site="";public static int offset=-1;
 static Deque<String[]> frames=new ArrayDeque<>(); public static Map<String,Set<Integer>> coverage=new TreeMap<>();
 static String q(Object x){if(x==null)return "null";String s=String.valueOf(x);return "\""+s.replace("\\","\\\\").replace("\"","\\\"").replace("\n","\\n")+"\"";}
 public static void emit(String event,Object... args){StringBuilder b=new StringBuilder("{\"event\":").append(q(event)).append(",\"method\":").append(q(method)).append(",\"offset\":").append(offset);for(int i=0;i<args.length;i+=2)b.append(',').append(q(args[i])).append(':').append(args[i+1] instanceof Number||args[i+1] instanceof Boolean?args[i+1]:q(args[i+1]));out.println(b.append('}'));}
 public static void enter(String name){frames.push(new String[]{method,site,String.valueOf(offset)});method=name;offset=0;emit("HELPER_ENTER");}
 public static void exit(){emit("HELPER_EXIT");String[]s=frames.pop();method=s[0];site=s[1];offset=Integer.parseInt(s[2]);}
 public static void at(int i){offset=i;coverage.computeIfAbsent(method,k->new TreeSet<>()).add(i);}
 public static void blockGen(int v){emit("BLOCKGEN", "value",v);}
 public static void config(String name,boolean value){emit("CONFIG_GATE","name",name,"value",value);}
 public static void one(int a,int opcode,int target){boolean t=switch(opcode){case 153->a==0;case 154->a!=0;case 155->a<0;case 156->a>=0;case 157->a>0;case 158->a<=0;default->throw new IllegalArgumentException();};emit("BRANCH","opcode",opcode,"taken",t,"target",target);}
 public static void pair(int a,int b,int opcode,int target){boolean t=switch(opcode){case 159->a==b;case 160->a!=b;case 161->a<b;case 162->a>=b;case 163->a>b;case 164->a<=b;default->throw new IllegalArgumentException();};emit("BRANCH","opcode",opcode,"taken",t,"target",target);}
 public static void obj(Object a,Object b,int opcode,int target){boolean t=(opcode==165)?a==b:a!=b;emit("BRANCH","opcode",opcode,"taken",t,"target",target);}
 public static void nul(Object a,int opcode,int target){emit("BRANCH","opcode",opcode,"taken",opcode==198?a==null:a!=null,"target",target);}
 public static void sw(int value){emit("SWITCH","value",value);}
 public static void jump(int target){emit("BRANCH","opcode",167,"taken",true,"target",target);}
 public static void unresolved(String s){emit("UNRESOLVED","dependency",s);throw new UnsupportedOperationException(s);}
}
