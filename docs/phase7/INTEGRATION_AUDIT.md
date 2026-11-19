# Integration audit (before controlled implementation)

Baseline: main9eda883, merged Phase6 PR12. Read Phase6 IMPLEMENTATION_REPORT, EVIDENCE_MAPPING, KNOWN_GAPS, both unchanged pure components and Phase5 PORT_READY_COMPONENTS, material-level-callbacks, original BlockQuicksand branches. Audit found layered slowdown; adapter is experimental/default-off and only accepts explicit ordered test contacts. No inferred automatic material producer.

## Actual call order

```mermaid
sequenceDiagram
 participant C as Local client
 participant S as Server entity tick
 participant L as Server Level END
 C->>C: PlayerTick START → ClientMotionPrediction → MotionRuntime.prepare
 Note over C: Y safety; old XY solver unless synced legacy UUID present
 S->>S: PlayerTick START / mob LivingTick → MotionRuntime.prepare
 S->>S: vanilla travel/move → block entityInside (may repeat per cell)
 Note over S: SinkingBlock has shapes, no original Stuck callback; legacy specialized callbacks do damage/web
 S->>L: SinkEngine NORMAL → contact sampler → old settle
 Note over L: sampler uses overlap/priority, NOT original last-contact sequence
 L->>L: StuckAdapter LOWEST → pure Update → transient speed attribute
 L-->>C: vanilla tracked attribute synchronization (client latency not measured)
 C->>C: ComputeFovModifier → existing old-UUID-only FOV compensation
```

Level START HIGHEST clears legacy state/UUID if switch disabled, exempt, riding. At END normal SinkEngine executes once via lastTick/dimension guard, then adapter executes once via per-state gameTime guard. Multiple explicit contact calls overwrite in arrival order, never max. No assumption that Forge callback order across blocks equals old1.7.10; automatic producers are BLOCKED. Test command may arrive before/after entity movement; this modern END settlement is a documented test scheduling policy, not proved original global timing.

## Slowdown inventory and decisions

| Existing operation | Flag off / no lease | Managed experimental lease |
|---|---|---|
| SinkEngine.setModifier old035c UUID | unchanged | mutually exclusive, remove old UUID |
| SinkMath horizontal retention, shallow mud0.1, Soft centering | unchanged | bypass result.x/z, retain incoming x/z; no duplicated profile slowdown |
| client MotionRuntime XY result | unchanged | bypass only while server-owned73a UUID has synchronized |
| MotionRuntime/SinkEngine VY, entry sweep, terminal correction, fallDistance | unchanged | retain B1/B2 safety; no air-control→Y mapping |
| mounted legacy step budget | unchanged | riders excluded from new adapter |
| MaterialEffects, web/honey/trap callbacks | unchanged | not globally removed; no natural Level producers activated |
| vanilla potions/equipment/foreign attributes | unchanged | retain all other UUIDs/base; normal composition |
| old FOV compensation | unchanged | only existing old UUID logic; new UUID uses vanilla FOV; no global potion FOV suppression |

Client receives vanilla attribute asynchronously; transition frames may still have the old client XY prediction before the UUID arrives. No new protocol is invented to hide this gap. Client-server motion correction/FOV must be measured before opening broader integration.

## Evidence and risks

MATERIAL_CONTACT_MATRIX.csv retains all49 registered material rows. Quicksand/Dry/Mud/Mire/Honey relationships are distinct static evidence; their eligibility includes branch, metadata, isTrulySink, coordinate offsets and RNG. Merely knowing a cap145/128 is insufficient to implement callbacks. Other materials are unresolved, not assigned one of three profiles. The existing catalog's approximation is not promoted to original truth.

QS original `mtdkof=10f`, `mr_kof=min(5+floor(max(0,(mtdkof*10f)*(1.5-kof1m))),145)`; later deep branch forces145. Stuck is only a locomotion attribute; support/drag/suction/randomness and Y are separate. Full collision callback execution remains unverified. Modern jump uses jumpFromGround/setDeltaMovement and travel/getFlyingSpeed; inherited MotionRuntime already controls jump for safety. This phase does not claim faithful old air control, and does not change that path.

Baseline run: all29 required existing Forge GameTests passed (logs/baseline-gametest.log), plus prior45 JUnit. Candidate comparison and missing client measurements are reported separately, not inferred from unchanged code. New features default false. Rollback disables switches, clears UUID on next START, restores old slowdown path; no migration or new persisted lease data.
