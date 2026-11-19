# Original Contact evidence and admitted scope

Baseline b1461ba (merged Phase7/PR13). Read Phase7 integration audit, gaps, adapter spec, matrix and user guide; Phase5 PORT_READY_COMPONENTS/material-level-callbacks; Phase6 pure implementations and test vectors. Existing indexes are reused, not regenerated. `original-callsite-evidence.json` is a small extraction of relevant existing Phase1 instructions.

## Confirmed original facts

Original `BlockQuicksand#func_149670_a(World,III,Entity)V` is in `research/original-phase3/evidence/source/BlockQuicksand.cfr.txt`, original setter offsets1970/2163/2416/2486. For non-player living entities, snapshot `EposY=entity.posY`; `kof=-((double)y-EposY-.5)` and `km=max(kof,0)`. `mtdkof=10f` and `mr=min(5+floor(max(0,(double)(mtdkof*10f)*(1.5-km))),145)`.

Contact-only control flow, after excluding the original SandBlob early-return branch:

| Above identities | Effective kof / condition | Ordered requests |
|---|---|---|
| above!=this | kof>=1.2 | none |
| above!=this | .9<=kof<1.2 | mr (unguarded helper) |
| above!=this | .45<=kof<.9 | mr if isTrulySink |
| above!=this | kof<.45 | mr then145 if isTrulySink; duplicates retained |
| above==this, twoAbove!=this | kof<.5 |145 if isTrulySink; otherwise none |
| above==this, twoAbove==this | set kof=.001 AFTER calculating km/mr | mr then145 for non-player; km/mr are not recomputed |

`MFQM#isTrulySink(Entity,D)Z` is not a depth test: original instructions0..16 return client-side flag for EntityPlayer, true for every non-player. `tools/HelperProbe.java` copies the unchanged nine-instruction original method into an isolated mock type shell, verifies the Phase5 BodyProof fingerprint and executes all four player/side cases. Results in logs/helper-probe-1.stdout: players false on server/true on client; non-players true on both. This is selected native-method evidence, NOT original1.7.10 gameplay or a full native collision callback test.

Player coordinate mapping is distinct: original client EntityPlayer constructor assigns old yOffset1.62f (private Vanilla decompile `external-decompiled/yz.java`, joined.srg Entity.field_70129_M); pose/server variants and old side ownership need their own mapping. Current bridge does not substitute modern feet/eyes or force isTrulySink=true for players. **Player automation BLOCKED**.

## What is actually automated

`legacy/QuicksandContacts.java` implements only the above output projection, with no new motion, effects or RNG calls. `integration/OriginalContactBridge` is called by the real SinkingBlock.entityInside; server-only, exact registered ordinary Quicksand identity, non-player living entities, bounded finite body dimensions, not riding/exempt. Original SandBlob/WLD special entity/dimension are absent from this runtime. Mixed contact with any unsupported SinkingMedium rejects/cancels only the automatic lease, retaining the old path; it does not invent a second material Level. Diagnostic injections remain separately labeled.

Full callback consumes many RNG calls before/between physics and effects. Those predicates do not change the admitted Contact output: the relevant k/km snapshots precede those operations, the only later k assignment is the two-above .001 override, and non-player isTrulySink is unconditional. `original-callsite-evidence.json` retains RNG and Contact callsites. This is a dataflow projection of the Contact outputs, **not a port of the complete callback random stream**. We do not fabricate RNG draws for unported effects or claim random-seed/full-physics parity. Full callback RNG/motion/particles/sound remain PARTIAL.

`tools/contact_vectors.py` deterministically derives72 branch-boundary/static-decision vectors from the cited source, verifies source tokens/hash, and tests full ordered output lists (including duplicated145). They are STATIC_VERIFIED/model projections, not72 native callback executions. The separate real Forge test `actualQuicksandCollisionEmitsWithoutInjection` has no contact/hold/manual entityInside call; a naturally moving pig receives the UUID and emits85→88 requests. Metadata is not read by this Quicksand Contact subgraph.

## Dry and Mud research boundaries

Dry is original `MoreFunQuicksandMod.main.liquids.BlockSand`, **not SoftQuicksand**. It reads metadata and uses Java int `mtd/3` in the vertical offset, retains separate non-player -.5/player+1 coordinates, and chooses mtdkof **1f normally,2f in the specified ABC dimensions**; the multiplier is20f, not a constant mtdkof20f. Formula `min(5+floor(max(0,pow((mtdkof*20f)*(1.5-km),1.5))),128)`. The above-column structure is similar, but flow/density, metadata, special entities/ABC and other branches are not mapped to a modern production adapter. Dry automatic Contact remains PARTIAL/BLOCKED, despite default-state worldgen mapping.

Mud `BlockMud` uses default mtdkof2f and factor2f, a1.5 power and cap145. Metadata0 has an early-return movement branch before normal Contact; other special return branches, metadata geometry, isTrulySink and RNG gates must remain distinct. Source lines289..375 and setter sites in extracted evidence apply; no profile fallback. Mire special255 and Honey deep50 from Phase5 remain separate static research, not activated.

`MATERIAL_CONTACT_MATRIX.csv` preserves49 registered IDs. CONFIRMED means the explicitly limited QS non-player Contact projection only; it never means a complete material physics port.
