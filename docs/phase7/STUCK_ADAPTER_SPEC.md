# Stuck Forge adapter specification

`integration/StuckAdapter.java` retains Phase6 StuckLease unchanged. Attribute: MOVEMENT_SPEED; UUID73a49882-85a3-4896-ad2d-8c591e24aa62; MULTIPLY_TOTAL; addTransientModifier. Cleanup only this UUID, except mutual exclusion separately removes our preexisting035c UUID. Never modifies base value or foreign UUID. Vanilla tracks/synchronizes attributes; no custom synchronization packet added.

Weak entity-keyed in-memory state implements optional LevelPort with default-1, no NBT and no clone transfer. No entity reference stored in value. Contact overwrites. Each Level END LOWEST Update follows normal SinkEngine settlement; same gameTime update guard. No contact next tick consumes0→-1 and drops state. Missing movement attribute clears the owned state/UUID instead of throwing. Fixed-UUID no-reentrancy/server-thread assumption retained.

`phase7.stuckLease=false` by default. Level START HIGHEST cleans disabled/exempt/riding entities before old settlement resumes. Death, leave/unload, teleport event, login/logout, respawn, dimension-change, clone and capability invalidation clear state/UUID. Creative/spectator/invulnerable follow existing SinkEngine.exempt, not a new original claim. Player lifecycle fixture tests exercise handlers with real server-side attributes but mock Player instances; they are NOT real disconnect/respawn travel tests.

Automatic material contact producers: **BLOCKED for all catalog rows**, see MATERIAL_CONTACT_MATRIX.csv. Existing SinkingBlock has no original entityInside callback, and ContactSampler's max-overlap priority is not last contact order. No cap or modern profile substituted for original branches. QS/Dry/Mud/Mire/Honey static expressions remain separate. Only op-only test-world commands inject explicit Level inputs. `contact L` queues one value; `hold L N` is a bounded diagnostic script (1..200 ticks) that emits Contact immediately before Update, so this injected contact is deliberately last. It is not a material collision producer. `release` clears immediately without needing guards (safe rollback).

Modern policy limitations:

- Existing vertical engine, jump safety and fall events retained. Old jumpMovementFactor is air control; no mapping to VY/no new disable-jump rule. Faithful air control remains BLOCKED.
- While managed, server drops old XY solver result/old UUID; client bypasses old XY only after vanilla sync of legacy UUID. Network transition latency may cause a short mixed prediction window. No client-side attribute write. Live connected-client correction/FOV measurement NOT_RUN.
- Existing FOV handler removes only the old UUID from its counterfactual; it does not hide the new lease. Vanilla potion/equipment FOV untouched; experimental FOV change is visible/unverified.
- Event-based teleports clear; arbitrary small direct setPos calls that emit no event are not fully handled. Dimension/unload release is event-based and needs real-player acceptance before broad rollout.

Conclusion: controlled ground-attribute integration **PARTIAL**, not full Stuck/original physics PASS. Flag remains off; no automatic material gameplay change.
