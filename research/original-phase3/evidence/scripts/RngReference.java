import java.util.Random;
public class RngReference {
 public static void main(String[] args) {
  long[] seeds={0,1,-1,10,384,987654321};
  int[] bounds={1,2,3,7,16,100,1073741825};
  for(long seed:seeds){Random r=new Random(seed);for(int repeat=0;repeat<20;repeat++)for(int bound:bounds)System.out.println(seed+","+repeat+","+bound+","+r.nextInt(bound));}
 }
}
