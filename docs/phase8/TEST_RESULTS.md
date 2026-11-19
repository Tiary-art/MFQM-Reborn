# Executed tests and reproducible boundaries

| Run / check | Actual result | Log / data |
|---|---|---|
| Phase7 baseline test + GameTest |45JUnit,36GameTests PASS; normal exit | logs/baseline.log |
| Same baseline plus visibility-gap input | Expected FAIL1; real UUID remains atworld280/last update278 | logs/baseline-visibility-repro.log; evidence/Phase8VisibilityBaseline.java |
| Initial candidate |39GameTests PASS, normal exit | logs/candidate-attempt1.log |
| Expanded candidate |42GameTests PASS, normal exit | logs/candidate-expanded.log |
| First rollback-inclusive clean run |43tests,2failures retained | logs/final-clean-test-build-gametest.log |
| Config diagnosis | observed enabled=false although fixture just settrue; living/nonexempt entity | logs/config-diagnostic.log |
| Watch-isolated candidate |43GameTests PASS, normal exit | logs/isolated-config-final.log |
| Final clean test build + GameTest |46JUnit (0failure/error/skip),43GameTests PASS, normal exit | logs/final-verified-clean.log; JUnit XML |
| Existing pure component cases |19Dry native-vector cases;8 lifecycle callbacks;112numeric vectors continue passing | PureComponentsTest XML, unchanged Phase6 resources |
| New static projection vectors |72branch cases, ordered outputs/duplicates checked | QuicksandContactsTest XML; static provenance manifest |
| Original helper native probe |9instructions body-identical;4side/player cases PASS | helper-probe logs; not original Minecraft gameplay |
| Real automatic collision | natural pig emits85→88, UUID present, old UUID absent, releases outside | PHASE8_AUTO / PHASE8_AUTO_PROOF in final log; no manual bridge/contact call in this test |
| Exact release across registration gap | actual post-update frame atN+1 isLevel-1/UUID absent, inspected atN+2 | trackedLeaseNotLostBeforeEntityVisibility; PHASE8_RELEASE |
| Shape worker | all world reads forbidden, filled/top/outline succeed off-thread | softShapeHasNoWorldReadsOnWorker; all43assertions include it |
| Mixed unsupported material | no new lease, old UUID retained | unsupportedMixedMaterialRetainsOldPath |
| Rollback command | real command clears own UUID, preserves foreign, disables3entries; stale flag cannot bypass latch | operatorDisableIsImmediateAndPreservesForeignUUID |
| Dry prior native slice |401events;12same-state false differences;56written final cells | PHASE7_DRY_NATIVE and phase7-traces |
| Dry loaded chunk boundary |443ordered API events;4chunks;12same-state false differences;final cells agree with Phase6 pure core | PHASE8_DRY_CHUNK; not labeled new full-native-callback evidence |
| Neighbor behavior | flags3 AIR write causes1real FallingBlockEntity; separate from core events | PHASE8_NEIGHBOR |
| Unloaded/height/AIR aliases | previous Phase7 real-world guards retained and passed | dryGuardAndAirAliases |
| Connected clients |2Minecraft clients concurrently;4captured sessions;643active lease frames | CLIENT_PLAYER_TEST_MATRIX, observations.json |
| Dedicated server |2sessions: Done, console stop, all dimensions saved, exit success | player-server*.log |
| Resource graph/no old image/audio import | current project/B2 auditors PASS | resource-audit.json; b2-resources.log |
| Old Task003 resource auditor | NOT_RUN again; known outdated filled-model assumption already failed in both Phase7 baseline/candidate | prior phase7 logs retained; not counted as a new pass |
| Original1.7.10 gameplay; full callback RNG; human motion/audio/comfort | NOT_RUN | known gaps |

Environment: Java17.0.21+9, Minecraft1.20.1, Forge47.2.0, Gradle8.1.1, Linux; raw framework logs are host UTC. Original JAR SHA remains2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b. Public artifacts contain no original JAR/texture/audio.

## Commands

From repository root, with JDK17 and cached dependencies:

```sh
python -B docs/phase8/tools/contact_vectors.py
bash forge-1.20.1/gradlew -p forge-1.20.1 clean test build runGameTestServer -Pphase7GameTestDir=run/phase8-candidate --offline --console=plain
python -B docs/phase8/tools/summarize_observations.py
python -B docs/phase8/tools/verify_results.py
python -B forge-1.20.1/tools/verify_project.py
python -B forge-1.20.1/tools/audit_b2_resources.py
```

A fresh replay uses tools/reproduce.sh with exclusive disposable working directory. Baseline: checkout b1461ba, run test/runGameTestServer first; copy only evidence/Phase8VisibilityBaseline.java into the baseline gametest package to repeat the intentional failure input. Do not delete a live world's session.lock.

Helper probe additionally needs the user's private old JAR:

```sh
python -B docs/phase8/tools/run_helper_probe.py --jar "$MFQM_LEGACY_JAR" --java-home "$JAVA_HOME"
```

Actual clients used `runClient -Pphase8Connect -Pphase8Name=Phase8One` / Phase8Two, DISPLAY=:88/softwareGL/null audio, to the localhost dedicated server. This development launch enables read-only3600-tick telemetry. Recreate only a backed-up named test world with EULA accepted, test gates explicit; follow USER_TEST_GUIDE for human acceptance. Client process cleanup after server disconnect used host termination, so normal GUI quit is NOT_RUN; these exit143 logs are not reclassified as product crashes or successful Gradle runs.
