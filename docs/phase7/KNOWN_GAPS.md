# Known gaps

- Automatic material→Contact(Level) producers BLOCKED;49 catalog rows retained. Static QS/Dry/Mud/Mire/Honey formulas alone do not close metadata/eligibility/RNG/isTrulySink and old callback order. No three-profile fallback.
- Stuck only controlled ground movement attribute. Old jumpMovementFactor/air-control, original full Y, random suction/struggle/buoyancy remain unported. Existing B1/B2 Y safety is a retained modern approximation.
- Real connected-player death/respawn/dimension/logout/relogin and attribute packet timing NOT_RUN. Server handler fixtures are not real player lifecycle. Direct small setPos without teleport events is not universally cleaned.
- Client FOV, prediction transition, correction packet counts, landing sound playback and live creative/survival switching NOT_RUN. No global potion FOV suppression or new network protocol.
- Dry exact flags3 calls preserved, but modern same-state return false differs from mock. Only declared fixed-seed real-world slice compared, no broad parity. General neighbor side effects, falling entities/drops and unloaded/height/chunk cases need separate measurement, see test matrix; not silently counted as pure algorithm events.
- Existing CoreSinkingBlock dynamic shape can query Level chunks on a lighting worker during shutdown; first candidate GameTest assertions passed but save hung. Thread dump retained; no unrelated physics rewrite. A separate run initially failed to acquire the still-held test-world lock even though Gradle reported BUILD SUCCESSFUL. Result parser must check actual tests, not Gradle alone.
- Full Surface coordinator/biomes/shared blockGen all25 branches still0/25 full scope; no natural generation registration.
- Full materials, Tombs/WLD structures/modernNBT, stains, camera/FOV, sound, original assets/authorization still outstanding. No old JAR or original textures redistributed/modified.
- Original1.7.10 game runtime not run. The old method/body trace evidence remains modeled JVM API evidence.

Default-off gates stay in place. This phase is overall PARTIAL until broader runtime acceptance; completion does not authorize next-phase worldgen or materials.

- A2-fixture-tick release assertion failed once;3-tick bounded observation passes. Strict one-world-tick release timing remains unresolved, not concealed by treating the longer check as equivalent. Retained failure and next measurement in TEST_MATRIX.
