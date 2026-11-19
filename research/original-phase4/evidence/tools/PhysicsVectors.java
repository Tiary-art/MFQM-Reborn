package audit;
public class PhysicsVectors {
 public static void main(String[]args){
 int[] levels={1,4,5,6,50,100,145,175,249,250,254,255,256,400};float[] inputs={0.004999f,0.005f,0.02f,1.0f};
 System.out.println("level,horizontalCollision,jumpInput,jumpOutput,speed,operation,amount,nextLevel");
 for(int level:levels)for(boolean coll:new boolean[]{false,true})for(float input:inputs){double p=level-5,c=coll?0:1;float jump=input;double speed;
 if(p<250){jump=(float)((double)jump/Math.max(Math.pow(1+p*(1+c*2.5)/1000,8),1));speed=Math.max(1/Math.pow(1+p*(1+c/2)/50,2),.02);}else{jump=0;speed=.02;}
 if((double)jump<.005)jump=0;
 System.out.println(level+","+coll+","+Float.toString(input)+","+Float.toString(jump)+","+speed+",2,"+(speed-1)+",0");
 }
 }
}
