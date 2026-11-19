# Controlled Dry world adapter

`integration/DryWorldAdapter.java` wraps actual ServerLevel, synchronous and ordered. Original SandBlock→registered mfqm:dry_quicksand default state, sandstone→minecraft:sandstone default, AIR→minecraft:air. `air/cave_air/void_air` read as the same Legacy AIR is an explicit modern compatibility decision. Other registered blocks are not given physical profile aliases; identities needed by original AIR/Dry comparisons are retained. Metadata0/flags3 only; other writes rejected by exception.

Calls every getBlock/setBlock requested by the unchanged Phase6 core, including repeated neighbor reads and same-state writes. java.util.Random(seed) stays one stream within each explicit test transaction; no RandomSource or reseeding inside the core. Command starts a declared test seed, not a Surface shared stream.

Command safety: op2 + per-world `phase7.testWorld=true` + actual level name prefix `MFQM_PHASE7_`; all defaults false. User must back up a disposable world before enabling. No automatic on-load writes, migration, Feature, PlacedFeature or BiomeModifier. Public Java entry is used by GameTest; it does not bypass a command-side automatic trigger because none exists.

Extent limited -1..18. Preflight read/write XZ bounds (including erosion neighbor margin) must all be loaded; no force-load or partial generation/RNG before preflight failure. Build height checks include two support cells. Direct port writes to unloaded/out-of-height return false and log W; direct unloaded reads fail closed. Safety restrictions are modern test policy, not original generation behavior.

Real `setBlock` flags3 performs neighbor/client notification; same-state vanilla setBlock returns false while old mock accepted it. Do not rewrite its return value. Real-world test compares all ordered RNG/Q/W coordinates/identities/meta/flags, allows a return-value difference **only** when the write repeats a previous accepted same state, counts it separately, and checks final real grid against native cells. Initial validated slice: extent5 seed0 desert fixture;401 API events,12 same-state false differences,56 final cells (attempt1). This is a scoped compatibility result, not exact equality of all boolean outputs and not broad Forge worldgen PASS.

Neighbor updates, lighting, scheduled falling entities/drops/chunk side effects are outside the pure trace. Guard/alias tests and subsequent side-effect observations are listed in TEST_MATRIX; not measured items stay NOT_RUN. One earlier GameTest shutdown encountered existing dynamic-shape lighting code loading a chunk while saving; thread dump retained. No unrelated surface-height fix was silently added.

Full Surface parent eligibility/coordinator/shared blockGen/biomes remains0/25 full-scope. Controlled Dry helper is not natural generation.
