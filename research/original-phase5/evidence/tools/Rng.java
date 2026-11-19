package audit;
public class Rng extends java.util.Random {
 String id;long state;long ordinal;public Rng(long seed,String id){super(seed);this.id=id;state=(seed^0x5DEECE66DL)&((1L<<48)-1);}
 @Override protected int next(int bits){state=(state*0x5DEECE66DL+11)&((1L<<48)-1);return(int)(state>>>(48-bits));}
 @Override public int nextInt(int bound){long before=state;int n=super.nextInt(bound);Trace.emit("RNG_CALL","rng",id,"api","nextInt","bound",bound,"value",n,"before",before,"after",state,"ordinal",ordinal++);return n;}
 @Override public double nextDouble(){long before=state;double n=super.nextDouble();Trace.emit("RNG_CALL","rng",id,"api","nextDouble","value",n,"before",before,"after",state,"ordinal",ordinal++);return n;}
 @Override public float nextFloat(){long before=state;float n=super.nextFloat();Trace.emit("RNG_CALL","rng",id,"api","nextFloat","value",n,"before",before,"after",state,"ordinal",ordinal++);return n;}
}
