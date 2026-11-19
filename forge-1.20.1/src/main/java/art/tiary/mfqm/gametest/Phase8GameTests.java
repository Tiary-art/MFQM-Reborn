package art.tiary.mfqm.gametest;

import art.tiary.mfqm.MfqmReborn;
import art.tiary.mfqm.integration.StuckAdapter;
import art.tiary.mfqm.legacy.StuckLease;
import art.tiary.mfqm.physics.*;
import art.tiary.mfqm.registry.ModBlocks;
import net.minecraft.core.BlockPos;
import net.minecraft.gametest.framework.*;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.phys.Vec3;
import net.minecraftforge.gametest.*;

@GameTestHolder(MfqmReborn.MOD_ID)
@PrefixGameTestTemplate(false)
public final class Phase8GameTests {
    @GameTest(template="pool_test", timeoutTicks=100, batch="phase8_visibility")
    public static void trackedLeaseNotLostBeforeEntityVisibility(GameTestHelper h) {
        SinkConfig.EXPERIMENTAL_STUCK.set(true);
        var pig=EntityType.PIG.create(h.getLevel()); // deliberately NOT addFreshEntity
        h.assertTrue(h.getLevel().getEntity(pig.getUUID())==null,"registration gap is real");
        var frames=StuckAdapter.observeForTest(pig);
        StuckAdapter.contact(pig,145); StuckAdapter.update(pig);
        h.assertTrue(pig.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(StuckLease.UUID_KEY)!=null,"initial lease");
        long start=h.getLevel().getGameTime();
        h.runAfterDelay(2,()-> {
            // GameTest runs after a full server-world settlement. One next END is the contract.
            h.assertTrue(h.getLevel().getGameTime()==start+2,"exact one world tick, not three fixture ticks");
            h.assertTrue(frames.stream().anyMatch(f->f.tick()==start+1 && f.level()==-1 && !f.modifierPresent()),"actual next END released at exact world tick");
            h.assertTrue(pig.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(StuckLease.UUID_KEY)==null,
                    "unregistered tracked entity releases at next world END: "+StuckAdapter.diagnosticState(pig));
            MfqmReborn.LOGGER.info("PHASE8_RELEASE start={} end={} visible=false modifier=false",start,h.getLevel().getGameTime());
            StuckAdapter.clear(pig); SinkConfig.EXPERIMENTAL_STUCK.set(false); pig.discard(); h.succeed();
        });
    }

    @GameTest(template="pool_test", timeoutTicks=100, batch="phase8_auto")
    public static void actualQuicksandCollisionEmitsWithoutInjection(GameTestHelper h) {
        SinkConfig.EXPERIMENTAL_STUCK.set(true); SinkConfig.ORIGINAL_CONTACTS.set(true); SinkConfig.PHASE7_DIAGNOSTICS.set(true);
        CoreMaterialGameTests.pool(h,MaterialProfile.QUICKSAND);
        for(int x=4;x<=12;x++)for(int z=4;z<=12;z++) {
            h.setBlock(x,3,z,Blocks.STONE);h.setBlock(x,2,z,Blocks.STONE);
            h.setBlock(x,4,z,ModBlocks.QUICKSAND.get());h.setBlock(x,5,z,Blocks.AIR);
        }
        var pig=h.spawnWithNoFreeWill(EntityType.PIG,new Vec3(8.5,4.2,8.5));
        // No StuckAdapter.contact/hold, bridge.inside or block.entityInside calls in this test.
        h.runAfterDelay(5,()-> {
            var speed=pig.getAttribute(Attributes.MOVEMENT_SPEED);
            h.assertTrue(speed.getModifier(StuckLease.UUID_KEY)!=null,"real vanilla entity collision drove automatic lease");
            h.assertTrue(speed.getModifier(SinkEngine.SLOWNESS_ID)==null,"automatic mode has no old modifier stacking");
            MfqmReborn.LOGGER.info("PHASE8_AUTO_PROOF entity={} tick={} amount={}",pig.getUUID(),h.getLevel().getGameTime(),speed.getModifier(StuckLease.UUID_KEY).getAmount());
            pig.setPos(h.absoluteVec(new Vec3(14,7,14))); // leave pool
        });
        h.runAfterDelay(7,()-> {
            h.assertTrue(pig.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(StuckLease.UUID_KEY)==null,"automatic lease releases outside material");
            StuckAdapter.clear(pig); SinkConfig.ORIGINAL_CONTACTS.set(false); SinkConfig.EXPERIMENTAL_STUCK.set(false); SinkConfig.PHASE7_DIAGNOSTICS.set(false);
            pig.discard(); h.succeed();
        });
    }

    @GameTest(template="pool_test")
    public static void softShapeHasNoWorldReadsOnWorker(GameTestHelper h) {
        net.minecraft.world.level.BlockGetter forbidden=new net.minecraft.world.level.BlockGetter(){
            public net.minecraft.world.level.block.entity.BlockEntity getBlockEntity(BlockPos p){throw new AssertionError("world read");}
            public net.minecraft.world.level.block.state.BlockState getBlockState(BlockPos p){throw new AssertionError("cross-thread chunk read");}
            public net.minecraft.world.level.material.FluidState getFluidState(BlockPos p){throw new AssertionError("fluid read");}
            public int getHeight(){return 384;}public int getMinBuildHeight(){return -64;}
        };
        var block=(CoreSinkingBlock)ModBlocks.SOFT_QUICKSAND.get();
        try {
            var task=java.util.concurrent.CompletableFuture.supplyAsync(()-> {
                double lower=block.surfaceHeight(block.defaultBlockState().setValue(CoreSinkingBlock.FILLED,true),forbidden,BlockPos.ZERO);
                double upper=block.surfaceHeight(block.defaultBlockState(),forbidden,BlockPos.ZERO);
                h.assertTrue(lower==1 && Math.abs(upper-.85)<1e-12,"state-only geometry matches filled/top");
                block.getShape(block.defaultBlockState(),forbidden,BlockPos.ZERO,net.minecraft.world.phys.shapes.CollisionContext.empty());
                return true;
            });
            h.assertTrue(task.get(2,java.util.concurrent.TimeUnit.SECONDS),"worker finished without Level access");h.succeed();
        }catch(Exception ex){throw new RuntimeException(ex);}
    }

    @GameTest(template="pool_test",timeoutTicks=100,batch="phase8_mixed")
    public static void unsupportedMixedMaterialRetainsOldPath(GameTestHelper h) {
        SinkConfig.EXPERIMENTAL_STUCK.set(true);SinkConfig.ORIGINAL_CONTACTS.set(true);
        CoreMaterialGameTests.pool(h,MaterialProfile.QUICKSAND);
        for(int y=2;y<=4;y++)h.setBlock(9,y,8,ModBlocks.MUD.get().defaultBlockState().setValue(MudBlock.DEPTH,3));
        var pig=h.spawnWithNoFreeWill(EntityType.PIG,new Vec3(8.95,3.8,8.5));
        h.runAfterDelay(5,()->{
            h.assertTrue(pig.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(StuckLease.UUID_KEY)==null,"unclosed mixed material cannot create guessed automatic lease");
            h.assertTrue(pig.getAttribute(Attributes.MOVEMENT_SPEED).getModifier(SinkEngine.SLOWNESS_ID)!=null,"old path retained for mixed unclosed contact");
            StuckAdapter.clear(pig);SinkConfig.ORIGINAL_CONTACTS.set(false);SinkConfig.EXPERIMENTAL_STUCK.set(false);pig.discard();h.succeed();
        });
    }

    @GameTest(template="pool_test",timeoutTicks=100,batch="phase8_neighbors")
    public static void flagsThreeActuallySchedulesFallingSand(GameTestHelper h) {
        var level=h.getLevel();var base=h.absolutePos(new BlockPos(8,25,8));
        level.setBlock(base.below(),Blocks.AIR.defaultBlockState(),3);
        level.setBlock(base,Blocks.STONE.defaultBlockState(),3);
        level.setBlock(base.above(),Blocks.SAND.defaultBlockState(),3);
        var trace=new java.util.ArrayList<String>();
        new art.tiary.mfqm.integration.DryWorldAdapter(level,trace::add).write(base.getX(),base.getY(),base.getZ(),art.tiary.mfqm.legacy.LegacyBlock.AIR,0,3);
        h.assertTrue(trace.size()==1 && trace.get(0).endsWith("true"),"API trace records one accepted AIR flags3 write");
        h.runAfterDelay(4,()->{
            h.assertTrue(!level.getBlockState(base.above()).is(Blocks.SAND),"neighbor update caused real scheduled sand tick");
            int count=level.getEntitiesOfClass(net.minecraft.world.entity.item.FallingBlockEntity.class,new net.minecraft.world.phys.AABB(base).inflate(3,8,3)).size();
            h.assertTrue(count>0,"falling entity is a separately observed modern side effect");
            MfqmReborn.LOGGER.info("PHASE8_NEIGHBOR api_writes=1 falling_entities={} pure_events_exclude_falling=true",count);h.succeed();
        });
    }

    @GameTest(template="pool_test")
    public static void dryCrossesLoadedChunkBoundary(GameTestHelper h) {
        var seedPos=h.absolutePos(new BlockPos(8,25,8));
        var origin=new BlockPos((seedPos.getX()>>4)*16+15,seedPos.getY(),(seedPos.getZ()>>4)*16+15);
        for(int x=-4;x<=5;x++)for(int y=-8;y<=2;y++)for(int z=-4;z<=5;z++)h.getLevel().setBlock(origin.offset(x,y,z),Blocks.AIR.defaultBlockState(),3);
        var actual=new java.util.ArrayList<String>();var expected=new java.util.ArrayList<String>();
        art.tiary.mfqm.integration.DryWorldAdapter.generate(h.getLevel(),origin,5,0,actual::add);
        var cells=new java.util.HashMap<BlockPos,art.tiary.mfqm.legacy.LegacyBlock>();
        art.tiary.mfqm.legacy.VoxelPort grid=new art.tiary.mfqm.legacy.VoxelPort(){
            public art.tiary.mfqm.legacy.LegacyBlock blockAt(int x,int y,int z){var b=cells.getOrDefault(new BlockPos(x,y,z),art.tiary.mfqm.legacy.LegacyBlock.AIR);expected.add("Q\t"+x+"\t"+y+"\t"+z+"\t"+b);return b;}
            public boolean write(int x,int y,int z,art.tiary.mfqm.legacy.LegacyBlock b,int m,int f){cells.put(new BlockPos(x,y,z),b);expected.add("W\t"+x+"\t"+y+"\t"+z+"\t"+b+"\t"+m+"\t"+f+"\ttrue");return true;}
        };
        art.tiary.mfqm.legacy.DryQuicksandCore.generateDry(origin.getX(),origin.getY(),origin.getZ(),5,grid,art.tiary.mfqm.integration.DryWorldAdapter.random(0,expected::add));
        h.assertTrue(actual.size()==expected.size(),"cross-chunk complete API count");
        var prior=new java.util.HashMap<String,String>();var chunks=new java.util.HashSet<String>();int duplicates=0;
        for(int i=0;i<actual.size();i++){
            var a=actual.get(i).split("\t");var e=expected.get(i).split("\t");
            if(a[0].equals("W")){
                String key=a[1]+","+a[2]+","+a[3];chunks.add((Integer.parseInt(a[1])>>4)+","+(Integer.parseInt(a[3])>>4));
                if(!a[7].equals(e[7])){h.assertTrue(a[7].equals("false")&&a[4].equals(prior.get(key)),"only same-state false difference");duplicates++;e[7]=a[7];}prior.put(key,a[4]);
            }
            h.assertTrue(java.util.Arrays.equals(a,e),"cross-chunk ordered event "+i);
        }
        var port=new art.tiary.mfqm.integration.DryWorldAdapter(h.getLevel(),ignored->{});
        for(var e:cells.entrySet()){var p=e.getKey();h.assertTrue(port.blockAt(p.getX(),p.getY(),p.getZ())==e.getValue(),"cross-chunk final cell");}
        h.assertTrue(chunks.size()>1,"actual writes cross loaded chunks");
        MfqmReborn.LOGGER.info("PHASE8_DRY_CHUNK chunks={} events={} same_state_false={} oracle=Phase6_pure_core_not_full_native_callback",chunks.size(),actual.size(),duplicates);h.succeed();
    }
    @GameTest(template="pool_test",batch="phase8_rollback")
    public static void operatorDisableIsImmediateAndPreservesForeignUUID(GameTestHelper h) {
        SinkConfig.EXPERIMENTAL_STUCK.set(true);SinkConfig.ORIGINAL_CONTACTS.set(true);SinkConfig.PHASE7_TEST_WORLD.set(true);
        var pig=EntityType.PIG.create(h.getLevel());var speed=pig.getAttribute(Attributes.MOVEMENT_SPEED);
        var foreign=java.util.UUID.fromString("00000000-0000-0000-0000-000000000777");
        speed.addTransientModifier(new net.minecraft.world.entity.ai.attributes.AttributeModifier(foreign,"foreign",.2,net.minecraft.world.entity.ai.attributes.AttributeModifier.Operation.MULTIPLY_TOTAL));
        MfqmReborn.LOGGER.info("PHASE8_ROLLBACK_SETUP enabled={} alive={} exempt={} removed={}",StuckAdapter.enabled(),pig.isAlive(),SinkEngine.exempt(pig),pig.isRemoved());
        StuckAdapter.contact(pig,145);StuckAdapter.update(pig);
        h.assertTrue(speed.getModifier(StuckLease.UUID_KEY)!=null,"active before rollback: " + StuckAdapter.diagnosticState(pig) + " alive=" + pig.isAlive() + " exempt=" + SinkEngine.exempt(pig));
        h.getLevel().getServer().getCommands().performPrefixedCommand(h.getLevel().getServer().createCommandSourceStack(),"mfqm_phase7 disable");
        h.assertTrue(!SinkConfig.EXPERIMENTAL_STUCK.get()&&!SinkConfig.ORIGINAL_CONTACTS.get()&&!SinkConfig.PHASE7_TEST_WORLD.get(),"all entry gates disabled");
        h.assertTrue(speed.getModifier(StuckLease.UUID_KEY)==null&&speed.getModifier(foreign)!=null,"immediate own-only cleanup");
        SinkConfig.EXPERIMENTAL_STUCK.set(true);
        h.assertTrue(!StuckAdapter.enabled(),"operator stop latch survives asynchronous/stale config re-enable until server restart");
        SinkConfig.EXPERIMENTAL_STUCK.set(false);
        pig.discard();h.succeed();
    }
}
