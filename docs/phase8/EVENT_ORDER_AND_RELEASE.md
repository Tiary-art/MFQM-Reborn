# Event order, release and shutdown safety

## Two independent findings, not a three-tick workaround

1. **Visibility gap reproduced on baseline.** Phase7 END iterates `level.getAllEntities()`. A valid server living entity can have a pending lease before it is in that lookup. `Phase8VisibilityBaseline.java` creates such an entity without addFreshEntity, proves invisibility, sets a real attribute lease, then observes it still present two world ticks later. Baseline log: worldTick280, updated278, level0. It is a deterministic failing baseline input, retained verbatim. This explains a concrete lost-update path; historical Phase7 logs did not record visibility for every intermittent case, so we do not assert every historical failure had this sole cause.
2. **Fixture config race observed separately.** Later runs captured `PHASE8_ROLLBACK_SETUP enabled=false alive=true exempt=false removed=false` immediately after the test's ConfigValue.set(true) calls. Forge's file-backed auto-save/watch reload can race rapid test-side value changes. It also produced a missing modifier in a Phase7 fixture. `Phase8TestIsolation` removes only this mod's config file watcher in the disposable GameTest harness before defaultBatch, with explicit log marker; production file watching is unchanged. It does not replace attributes/events with mocks. Original failure logs and before/after enabled states remain.

## Defined modern contract

Vanilla calls `SinkingBlock.entityInside` on the server entity movement thread. The bridge preserves callback arrival order and each ordered output from the original Contact projection. It never uses ContactSampler overlap priority, max(Level), a Set or sorting. Distinct repeated145 writes remain distinct. Mixed unsupported SinkingMedium volumes are rejected rather than assigned guessed Levels. Cross-version global callback order is not claimed identical; arrival order of the actual modern callbacks is authoritative in this limited domain.

Normal SinkEngine settlement remains Level END NORMAL. Lease update is END LOWEST, once per entity/world gameTime. The adapter now owns and iterates a snapshot of its tracked state keys, not an intersection with the world's currently visible entity list. A no-contact Level0 is removed and becomes-1 at the next END, even across the registration gap. Removed entities clear instead. No NBT persistence or clone transfer.

Tests no longer equate an ambiguously phased intermediate GameTest callback with END. `LeaseFrame` test observers capture actual post-Update world tick, Level, hold remaining and UUID presence. The two-fixture-tick test checks that the **recorded frame at start+1** released the lease; it is not a three-tick allowance. The input hold2 likewise checks active atN/remaining1, active atN+1/remaining0, released atN+2. Original inputs retained. No production snapshot observer is installed by default.

## Rollback and mode/lifecycle

`/mfqm_phase7 disable` (op2) sets a one-way runtime stop latch, disables automatic Contact, lease and destructive test entry flags, clears only owned leases immediately and saves the config. A stale watcher reload cannot re-enable it. Re-enabling requires config edits plus a server/world restart; server-start resets the latch. The rollback GameTest uses the real Brigadier command, foreign UUID and simulated stale flag re-enable; a test-only AfterBatch resets the private latch between independent test cases. It is not a production re-enable command.

Existing death/respawn/dimension/login/logout/teleport/leave/capability invalidation/exemption/rider cleanup remains. Runtime client observations include real survival→creative active-lease cleanup, death/automatic respawn, active teleport and active logout followed by rejoin. No small arbitrary direct-setPos guarantee beyond existing event/fallback behavior is invented.

## Shape shutdown fix

Phase7 dump showed a lighting worker entering CoreSinkingBlock.surfaceHeight→Level.getBlockState→chunk load while the server saved worlds. Core surfaceHeight now reads the maintained FILLED BlockState property; updateShape uses its supplied UP neighbor instead of querying the world again. Placement/neighbor updates maintain that property. No world lookup remains on this light/shape path. The worker test supplies a BlockGetter that throws on every world read; filled and top heights plus outline shape complete off-thread. Existing shape/stack tests remain. Shutdown and world-lock release are independently checked.

## Four different outcomes

The result verifier requires: Gradle success; expected GameTest assertion count/pass; explicit normal GameTest shutdown; independently acquirable session.lock after process completion. The retained Phase7 lock failure demonstrates why Gradle success alone is insufficient. Real dedicated-server startup, stop and all-dimension save have separate log assertions.
