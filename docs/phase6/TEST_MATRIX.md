# Phase6 test matrix

All PASS entries below refer to offline Java/JVM/mocked API or artifact tests, **not original Minecraft runtime**.

## Dry: full ordered interface events

Each row is a JUnit DynamicTest under originalDryTraces. Sources: Phase5 native `.jsonl.gz`, except supplement-* captured this phase with unchanged original method and the Phase5 JVM harness. parent38 is a child slice of Phase5 dry-positive seed38, with every preceding passed-stream RNG call replayed and checked first. This is not a Java implementation of the Surface parent.

| Test ID | Seed | Extent | Fixture | RNG | Reads | Writes | Rejected writes | Repeated write positions | Result |
|---|---:|---:|---|---:|---:|---:|---:|---:|---|
| generateSoftSand-r-1-s0 | 0 | -1 | desert | 1 | 0 | 0 | 0 | 0 | PASS |
| generateSoftSand-r-1-s1 | 1 | -1 | desert | 1 | 0 | 0 | 0 | 0 | PASS |
| generateSoftSand-r0-s0 | 0 | 0 | desert | 2 | 0 | 0 | 0 | 0 | PASS |
| generateSoftSand-r0-s1 | 1 | 0 | desert | 2 | 0 | 0 | 0 | 0 | PASS |
| generateSoftSand-r1-s0 | 0 | 1 | desert | 9 | 0 | 3 | 0 | 0 | PASS |
| generateSoftSand-r1-s1 | 1 | 1 | desert | 9 | 0 | 3 | 0 | 0 | PASS |
| generateSoftSand-r4-s0 | 0 | 4 | desert | 126 | 0 | 57 | 0 | 14 | PASS |
| generateSoftSand-r4-s1 | 1 | 4 | desert | 126 | 0 | 48 | 0 | 12 | PASS |
| generateSoftSand-r5-s0 | 0 | 5 | desert | 217 | 100 | 84 | 0 | 28 | PASS |
| generateSoftSand-r5-s1 | 1 | 5 | desert | 217 | 106 | 94 | 0 | 28 | PASS |
| generateSoftSand-r10-s0 | 0 | 10 | desert | 1333 | 0 | 630 | 0 | 293 | PASS |
| generateSoftSand-r10-s1 | 1 | 10 | desert | 1333 | 0 | 606 | 0 | 276 | PASS |
| generateSoftSand-r18-s0 | 0 | 18 | desert | 6861 | 0 | 3393 | 0 | 1810 | PASS |
| generateSoftSand-r18-s1 | 1 | 18 | desert | 6861 | 0 | 3435 | 0 | 1816 | PASS |
| dry-helper-air-boundary | 0 | 10 | empty | 1333 | 0 | 630 | 0 | 293 | PASS |
| supplement-deny | 0 | 5 | deny | 217 | 132 | 94 | 0 | 38 | PASS |
| supplement-desert-refuse | 0 | 5 | desert-refuse | 217 | 36 | 81 | 81 | 25 | PASS |
| supplement-protected | 0 | 5 | protected | 217 | 100 | 84 | 0 | 28 | PASS |
| parent38 | 38 | 5 | desert | 217 | 145 | 121 | 0 | 39 | PASS |

Writes are not deduplicated; rejected writes do not change test-grid state. Subsequent Q events compare real grid values. Identity comparison ignores metadata. Protected fixture means SoftQuicksand identities in the input: Dry still overwrites them where the original does; it does not inherit Mire's protection.

## Stuck and existing tests

| Test / check | Evidence | Result / boundary |
|---|---|---|
| originalEightCallbacks | Phase5 native and oracle123 events revalidated; all48 projected Tick/Level/attribute/property events compared in Java | PASS, 8 updates:145, no renewal, idle,145→128,50,255,0, absent property; collision alternates |
| all112MathVectors | Phase4 physics-vectors.csv | PASS112 rows, amount tolerance1e-12, op2 andLevel0; jump output outside scope |
| cleanupIsolationAndNegativeLevels | Explicit port contract negative/identity tests | PASS old UUID removed before absent-property check; other UUID preserved; negative Level unchanged; lease lasts until next Update |
| MudGeometryTest | Existing JUnit | PASS4 |
| SinkMathTest | Existing JUnit | PASS14 |
| MotionMathTest | Existing JUnit | PASS5 |
| clean test build | logs/gradle-clean-test-build.log | PASS45 JUnit, zero failure/error/skip,11 executed Gradle tasks |
| Phase2 static / Phase3 trace / Phase4 math | logs/historical-regressions.json; isolated copy | PASS; no historical evidence overwritten |
| Phase5 saved native vs independent VM | logs/phase5-saved-native.stdout | PASS62 full streams, historical declared domains |
| Supplemental original vs independent VM | logs/supplemental-oracle.json | PASS2050/2268/2204 full events; deny fixture explicitly matched to original mock World |
| Resource auditors (Task002/003/B2) | logs/project-resource-audit.json, task003-resources.json, b2-resource-audit.log | PASS; no original textures/audio imported |
| Call isolation / pure compile | logs/isolation.json | PASS547 old files unchanged,52 outside Java files scanned; javac empty dependency classpath |
| 1.7.10 client/server;1.20.1 gameplay/client connection/visual/netY | No live game launched | NOT_RUN |
| Original air-control/global Forge scheduling/collision callbacks/natural distribution | Excluded integration gates | NOT_RUN |

## Failures retained during development

Initial Java event mismatch (missing repeated neighbor read); equivalent RNG scientific-number text formatting; deny grid fixture mismatch and missing deny fixture in the independent VM; checkout CRLF normalization in the artifact guard. Corrected implementation/declared test environments and comparison representation, not expected numeric values. All input cases retained. Earlier Gradle failure logs and supplemental-oracle-initial.log are historical failed attempts, not the final result. A pre-test-source build log only tests the old suite; the authoritative final run is clean-test-build and its XML.
