# Phase9 test matrix

Statuses describe the exact scope exercised, not entire legacy parity. Linux, Java17.0.21, Forge47.2.0, MC1.20.1. No tests deleted or expectations changed.

| Check | Result | Evidence / limitation |
|---|---|---|
| Baseline main 6a44d6f GameTests | PASS 43/43, exit0 | logs/baseline.log; 2m15s. Baseline JUnit task UP-TO-DATE, retained XML has46 passed; not claimed freshly re-executed |
| Candidate final public clean test build runGameTestServer | PASS 46 JUnit +43 GameTests, exit0 | logs/public-clean-build-gametest.log, evidence/junit/; 2m10s; actual clean output |
| Private build clean test build | PASS 46 JUnit, exit0 | logs/private-build.log; final88 imported entries verified in reobf JAR, evidence/private-final-jar.json |
| Private GameTests | PASS 43/43, exit0 | logs/private-gametest.log; before final fluid block-item JSON/probe-frame metadata additions; physics and binding code identical; final public suite rerun after these additions |
| Source regression boundary | PASS | evidence/source-regression.json; all preexisting src except exact initializeClient texture/tint changes byte-identical; no source resource/test changes |
| Private dedicated server + client connection | PASS limited | logs/private-server.log; Phase9Visual joined, scene commands executed, stop saved/exit0; default gameplay flags unchanged |
| Actual private development client | PASS render checks; cleanup nonzero | logs/private-client-final.log +12 probe JSONs. Client captured before/after reload; later deliberate SIGTERM/Xvfb shutdown caused runClient exit1, not a clean-exit claim |
| quicksand world + hotbar | PASS visual | original quicksand; screenshot index only, pixels kept private |
| mud world + hotbar | PASS visual default | original mud; depth0–3 placed; shape unchanged, every face of each depth not independently captured |
| soft_quicksand world + hotbar | PASS visual default | original SoftQuicksand1, unfilled/filled geometry in scene; old metadata1/2 NOT_IMPLEMENTED |
| acid + bog still/flow world | PASS limited visual | flowing surfaces visible; atlas names are original still/flow. Acid12/8 frames, bog32/16; complete timing/direction parity NOT_RUN |
| leaves_pile | PARTIAL | baked face/particle original leaves; byte alpha0/255 preserved, cutout layer supplied; isolated transparency visual NOT_RUN |
| Other confirmed25 IDs | PARTIAL | deterministic original bytes / references; individual scene visual NOT_RUN |
| Fluid block-item model | PARTIAL | still top/bottom, flowing sides bound; original inventory geometry equivalence NOT_RUN |
| Buckets, multiface, GUI/entities/stains, old variants | UNRESOLVED | explicit mapping rows; existing vanilla placeholders retained |
| Reload | PASS limited | reloadResourcePacks completed after capture3, capture4–11 use original atlas; physical F3+T key NOT_RUN |
| Missing texture check | PASS sampled scene | no purple/black in inspected scene, no MFQM missing texture/invalid animation in client logs; not proof all catalog renders |
| Linux case/reference checks | PASS | lowercase modern paths, original case retained; importer model references + actual atlas stitching |
| Import safety/idempotence | PASS | logs/import-guard-tests.json: dryrun, second import same hashes, verify, user edits preserved, cleanup atomic refusal, unmanaged kept, source-tree denied, symlink escape refused |
| Missing private input | EXPECTED FAILURE | logs/missing-private-input.json, BLOCKED_PRIVATE_INPUT; no substitute assets |
| Private → public without clean | PASS | logs/mode-switch-no-clean.json, 36→0 PNG and marker removed by processResources; public delivered JAR independently scanned |
| Final public JAR | PASS content | logs/public-jar-verification.json; version0.0.9, Phase9/8/6 classes; no private images/audio/marker |
| Final private JAR | PASS content only | all88 generated files hashed against actual packaged entries; no original JAR modification |
| Formal launcher installed final JAR | NOT_RUN | development client used corresponding classes/resources; packaged content verified separately |
| Public client visuals | NOT_RUN | public GameTest dedicated startup verified; vanilla fallback models verified in final JAR |
| Windows / other resourcepack / production modpack | NOT_RUN | no compatibility claim |
| Historical manifests | PASS file-level | 1950 entries,0 missing/0 mismatch; not historical gameplay rerun |

Observed warnings/failures are retained: offline auth/public key endpoint failures, vanilla shader/sound warnings, Forge GameTest config-tracker shutdown error also present at baseline; Gradle suites exit0. First client intentionally terminated for probe update; second closed after captures; neither runClient exit is treated as a successful graceful shutdown. Initial ad-hoc source checker assertion was a checker string mismatch, corrected against actual baseline without changing product/tests (source-regression.json).

Logs private-build-summary.json/private-build-final.json describe earlier75-file iterations and are SUPERSEDED by private-build-verified.json + private-build.log + private-final-jar.json (88 files). No earlier hash is presented as the final artifact hash. Raw .log.gz files preserve exact log bytes; plain .log copies only normalize trailing whitespace for repository checks.
