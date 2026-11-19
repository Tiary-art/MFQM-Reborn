# B1 landing contract

The fix addresses history before collision rather than canceling sound events. MotionRuntime.prepare limits a swept entry move and clears the replaced free-fall history before vanilla move. During actual contact it clears fallDistance only after setting a finite downward velocity within the configured bound. It excludes passengers, creative/spectator/invulnerable entities and locations with no core-material contact or swept entry.

A HIGH-priority LivingFallEvent safeguard sets only this event's distance to zero when current material contact, a controlled-motion flag and bounded finite vertical movement all agree. It does not cancel all falls, intercept a sound or edit global damage rules. Leaving contact clears controlled history. Stone, ordinary water, and falls after exit follow vanilla movement/history. A fast uncontrolled fall must fail the controlled-landing predicate.

Source timing: Entity.move performs collision and fall checks during movement. LivingEntity.causeFallDamage invokes Forge's fall hook, then computes damage and plays the generic fall and block landing sounds only when appropriate. Server END alone occurs too late for the local client's already performed move. Therefore the client and server pre-move hooks are both required. PlaySoundEvent observation records requested IDs, not proof of audible playback or a callback from the physical audio device.

Expected comparisons:

| Scenario | Rule |
|---|---|
| 0/3/10-block entry, then slow sink to floor | incoming momentum replaced; slow controlled landing does not inherit original fall distance |
| ordinary stone drop | vanilla fall history, damage and sound |
| ordinary water drop | vanilla water behavior; no MFQM interception |
| exit then fall onto stone | fresh outside fall history, normal damage/sound |
| shallow mud jump | preserve existing solid mud support and upward vanilla jump |
| deep mud / quicksand / soft sand held jump | material struggle, no unbounded vanilla jump impulse |

Unobserved backend audio and unperformed scenarios must remain unverified in TEST_RESULTS. Existing mud layers may provide an internal collision surface; B1 does not claim that landing there proves reaching the bottom bedrock of a 17-layer pit.
