# Known gaps and integration gates

This phase's two pure cores PASS their declared offline domains. No permission is implied to integrate them into gameplay.

1. Obtain separate authorization before any Forge event/Feature/adapter work. No current game code calls the new package.
2. Validate Forge living-tick/collision ordering, global contact timing and last-contact ordering across all original materials. The test Contact sequence is injected, not measured original collisions. Keep material-specific Level producers distinct; no three-profile compression.
3. AttributePort has no external reentrant modification of the fixed UUID during a single Update. No concurrency/thread-safety guarantee; do not remove other UUIDs, change base speed or persist the lease. The LevelPort contract represents optional in-memory state, initialized to -1 by its future owner.
4. Map the future lease to MOVEMENT_SPEED / MULTIPLY_TOTAL / transient semantics, then test lifecycle, persistence, respawn, death, dimensions and other mods. No such Forge adapter exists here.
5. jumpMovementFactor is old air control; its modern mapping remains BLOCKED. It is not motionY. FOV/visual feedback, full net sinking and original runtime comparison remain separate gates.
6. Dry future block mappings: SandBlock→mfqm:dry_quicksand default; field_150322_A→minecraft:sandstone default; field_150350_a→AIR. cave_air/void_air→AIR is a future 1.20 compatibility choice, not original evidence. Test actual getBlock identity and metadata handling when an adapter is proposed.
7. Preserve legacy java.util.Random stream/seed, noise calls and every repeated read/write. Validate chunk boundaries/loading, neighbor updates, falling blocks, drops, rejected writes and flags3 in actual Level. Core only handles explicit immediate port transactions, no implicit live-world effects.
8. Full Surface coordinator, biome eligibility/distribution/configs/BoP and25 branches remain unclosed (0/25 full scope). The seed38 child slice does not execute a Java port of the parent.
9. Original1.7.10 clients/servers and1.20.1 gameplay/visual/audio/netY were NOT_RUN this phase. Existing B1 tests pass and sources stay unchanged; this is not a new runtime safety claim.
10. Full original material physics, worldgen, Tombs/WLD, modern NBT, assets/permissions remain outside this task. No original JAR modification or asset publication.

The local build still uses the repository's old candidate filename. It is only a build result containing unreferenced classes; it is not a validated gameplay release. No new JAR is distributed in this PR.
