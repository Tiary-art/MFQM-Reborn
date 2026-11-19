# Phase7 test matrix

All tests are Forge1.20.1/47.2.0/Java17 unless explicitly noted. Original1.7.10 gameplay NOT_RUN. Overall PARTIAL, including unresolved automatic Level producers and real connected-player acceptance.

| Check | Source / command | Result and precise scope |
|---|---|---|
| Baseline existing Forge tests | baseline-gametest.log; Phase6 checkout runGameTestServer --offline | PASS29 required tests, normal shutdown |
| Pure cores/112 vectors/B1 mathematical tests | clean test build; final JUnit XML | PASS45;19 Dry native vectors and8 Stuck callbacks included; no pure-core source change |
| Initial candidate suite | candidate-gametest-attempt1.log |31 assertions passed, **shutdown FAILED/HUNG**; worker lighting loaded chunk via old CoreSinkingBlock surfaceHeight; thread dump saved; disposable process killed after capture |
| Attempt while old test world locked | candidate-gametest-final.log | FAILED_TO_START; DirectoryLock; Gradle misleadingly returned success; not counted as a test pass |
| Isolated candidate expanded suite | candidate-isolated-gametest.log | PASS34 required tests, normal shutdown; handler fixtures/paired motion/guard tests |
| 35-test successful run | final-verified.log | See RESULTS.json and actual pass marker; parser rejects missing tests/lock failure even if Gradle succeeds |
| Last145→128 contact; foreign UUID; temporary persistence; no-renewal; config disable; death/unload | leaseLifecycleAndMutualExclusion | Live server attributes, normal END release plus direct death/leave handler fixture; failed short-delay release attempt retained in failed-release-timing.log; final check observes release at3 fixture ticks, NOT proof of a strict one-server-tick deadline |
| Login/logout/respawn/clone/dimension/creative | playerLifecycleHandlerFixtures | Server Player fixture invokes adapter handlers; NOT real player reconnect/dimension travel |
| Bounded explicit injection expiry | boundedInjectedContactScript | Automated hold then release; not a material Level producer |
| Motion old path vs injected | measuredMotionWithAndWithoutInjectedLease |40 tick paired pigs, evidence/paired-mob-motion.csv and statistics.json; not client/network motion |
| Dry exact seed0 extent5 native slice | dryRealWorldOrderedNativeSlice |401 ordered API events;12 same-state false return differences;56 final written cells; retained Q/R/W and final-grid assertions |
| AIR/cave_air/void_air | dryGuardAndAirAliases | Real ServerLevel alias mapping checked |
| Unloaded chunks / invalid height writes | dryGuardAndAirAliases | Preflight rejects before RNG/write; direct high write logged false |
| Actual cross-chunk generation | observed single slice | NOT_RUN: recorded slice touches one chunk; guard logic covers preflight only |
| General neighbor schedules/falling entities/drops/lighting | no comprehensive event observer | NOT_RUN apart from observed shutdown stack; flags3 API invocation is not proof all side effects match |
| Independent dedicated server | dedicated-server-console.log | PASS startup Done, default destructive command guard rejects, console stop, all dimensions saved, Gradle success; localhost25579/offline test world |
| Initial noninteractive dedicated stop | dedicated-server.log | Startup PASS; stdin closed, TERM graceful save, process143; not counted as clean console-stop pass |
| Project / B2 resource auditors | resource-audit.json, b2-resources.log | PASS; resources unchanged |
| Old Task003 resource auditor | core-resource-audit.json and baseline-old-resource-audit.log | FAIL pre-existing stale assumption that every SoftQuicksand filled-state variant points to same model; same failure in baseline; no expectation altered |
| Actual connected-client packets/correction counts/FOV/landing sounds/mode switching | no connected client in these tests | NOT_RUN; preserve as release gates |
| Actual player death/respawn/teleport/dimension/relogin | only server handler fixtures | NOT_RUN real lifecycle; arbitrary direct setPos especially unresolved |
| Natural Surface / original full physical parity | no registration or original game runtime | BLOCKED0/25 full branches, not tested as restored |

Paired motion observation (34-test run): old and injected each40 samples, y -54.99→-55.21207661198257, minimum per-tick delta -0.005912328566829217, mean -0.005551915299564137, standard deviation0.0008977976296141666. Both-UUID frames0 for both; injected UUID present25 frames then old resumes13. Exact values are fixture observations, not universal sinking coefficients. This adds observed comparison rather than arguing that unchanged Y code proves safety.

## Reproduction

```sh
export JAVA_HOME=/path/to/jdk17
# Optional cache location used in this execution: /workspace/work/task002-tools/gradle-home
bash docs/phase7/tools/reproduce.sh
```

Run from clean checkout with dependencies cached for --offline; remove --offline to fetch them first. Each run must have exclusive ownership of its GameTest working directory. A lingering lock is a failure, not a reason to delete a live server's lock. Native vectors are the repository's Phase6 test resources via GameTest-only system property; no private old JAR needed.

Dedicated smoke: create a disposable run/server/server.properties with level-name=MFQM_PHASE7_SMOKE, server-ip=127.0.0.1, server-port=25579, view/simulation-distance2, online-mode=false. After accepting EULA (already authorized in this project), run gradlew runServer in an interactive terminal. Wait for Done; issue `mfqm_phase7 dry 0 70 0 5 0` with default testWorld=false and verify rejection; `stop`; verify all dimensions saved. This does not test client login.

The logs retain network/auth-service failures from unavailable Yggdrasil key fetching; the localhost test server was offline. They do not constitute successful public authentication. Complete raw Gradle logs are preserved compressed; readable copies may strip trailing whitespace only.

Important timing limitation: a2-fixture-tick no-renewal assertion failed once. The final3-tick bounded observation passes but does not resolve the strict global timing discrepancy; it is not reported as an exact1-tick scheduling proof. Root cause remains unlocalized. The original2-tick input/log is retained. Minimum follow-up: correlate entity-manager registration, GameTest callback tick, Level END and state.updated in a connected/normal server before widening integration.


Latest final observation: `timing-diagnostic-run.log` **36 required tests passed with normal shutdown**, including the additional registered-entity timing test. Hold input2 is unchanged: tick697 consumes first contact (remaining1), tick698 consumes second (remaining0), tick699 releases (Level-1). Registered lease starts tick707, releases on the following recorded world tick, and tick709 has no state. The earlier registered-timing run failed its early hold snapshot (35/36 passed); that failure remains in registered-timing-verification.log. These intermittent early-fixture snapshots are not declared root-caused or erased by the latest green run. Strict original global scheduling/real players remain PARTIAL.
