# B1 motion contract — candidate, pending user acceptance

Target: Minecraft 1.20.1, Forge 47.2.0, Java 17. No measured legacy trajectory is available. Task 001's bytecode supports different horizontal resistance and fast-fall damping (quicksand/soft sand divide by 2, mud by 10), but not numerical equivalence to this model. Vanilla web, gravity, random branches and integration order prevent equating one old assignment to a complete curve.

## Timing and authority

In Task 003, the real client integrates vanilla movement and sends accepted positions before server LevelTick END. END then computes a new vy, sends a velocity packet each tick and, on the next settlement, uses connection.teleport to enforce a small previous-step budget. Those three operations can compete. END clearing server fallDistance also cannot retroactively clear client landing history.

B1 adds local-player PlayerTick START kinematics and server LivingTick preparation for non-player LivingEntity. Both use the same ContactSampler and motion policy, before vanilla travel/move. Server player preparation protects its local landing history; its PlayerTick START callback is not a pre-hook for every C2S position packet, which may be accepted between callbacks. The conditional fall-event guard handles only confirmed material-controlled landing; raw timestamps document actual packet/tick ordering. client prediction controls its next actual move. Remote client replicas are not predicted. Server END still owns material state, modifiers, oxygen, drowning, settlement guard and snapshots. Client snapshots do not grant physiological authority. Protocol 2-b1 requires matching clients.

The per-entity transient phase is OUTSIDE → ENTERING (first three contact preparations) → SUBMERGED → EXITING → OUTSIDE; lifecycle reset goes straight to OUTSIDE. The same bounded policy applies during contact, with a separate swept entry limit while approaching from above. Phase is bookkeeping, not a permanent zero velocity lock.

## Candidate numbers

All speeds are blocks/game tick. Defaults are gameplay proposals, NOT approved original values:

| Parameter | Default | Config range |
|---|---:|---:|
| first-step penetration | 0.08 | 0.01–0.20 |
| terminal descent | 0.055 | 0.02–0.10 |
| depth gain | 0.020 | 0–0.05 |

Continuous descent magnitude = min(terminal, base + depthGain × min(1, depth/2) + moving?0.006 + struggle?0.015), bases quicksand 0.010, mud 0.007, soft sand 0.013. Depth and movement distinguish materials; old horizontal, stuck, soft-sand center and mud collision behavior remain in the server solver. Entry discards excess incoming velocity by limiting the first proposed feet position to surface − entryDepth. Air travel above the surface is preserved. No water buoyancy, fluid state, boat or collision shape changes.

Server-config file: world/serverconfig/mfqm-server.toml, section motionCandidate. Forge SERVER config is synchronized at login; reconnect after changing values. Do not hot-reload during comparison trials.

## Exceptional correction boundary

Ordinary accepted steps do not cause an unconditional motion packet or teleport. Connected players crossing a sampled surface are corrected only below surface − entryDepth. Already active players still in material are corrected only beyond terminal × clamp(server wall elapsed/50ms, 1, 4) + 0.08. This allowance is a bounded tolerance for packet/tick batching, not measured proof for all RTTs. Direct position changes over 16 blocks clear previous history; Forge teleport/lifecycle events reset it. Mounted players retain the old settlement fallback; the new predictor excludes passengers. Boats are not LivingEntity and have no new hook.

Reported terminal compliance must use actual Y differences, including correction steps, rather than END vy. A missing packet arrival tick is not a zero-movement proof. Network tests and current limitations are in TEST_RESULTS and KNOWN_GAPS.

## Rollback

Revert this B1 PR to main 79aac86 (or retain observation-only da60f10 for diagnosis). Remove the B1 JAR from client and server together and install Task 003 builds. Only residue is serialized; phase, velocity history and diagnostic sessions are not saved. Existing config keys can remain unused. Keep backups of disposable diagnostic worlds; fixture commands intentionally replace the documented test pool.
