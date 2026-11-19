package art.tiary.mfqm.legacy;
/** Writes apply immediately if accepted, including duplicate/same-state writes. */
public interface VoxelPort {
    LegacyBlock blockAt(int x, int y, int z);
    boolean write(int x, int y, int z, LegacyBlock block, int metadata, int flags);
}
