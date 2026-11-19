# Unmodified-physics baseline

Observation-only commit **da60f1026e755a9a3264190141d5981620fcff8e**, parent merged main79aac86. SinkMath, ContactSampler, lifecycle and physics order were unchanged; Engine only added correction counters and a diagnostic END callback. Separate immutable worktree ensured later candidate compilation did not replace baseline classes.

Actual graphical integrated client, real Dev player in survival, vanilla resource pack, Java17/Forge47.2.0. Started 2026-11-18 14:26:13 and completed14:38:49 Asia/Shanghai (raw logs UTC06:26:13–06:38:49). Suite ran all54 fixtures:27 real-player plus27 real-pig, three materials ×1/3/17layers ×0/3/10block drops. All27 real-player cases have260 settlement samples and >=239 ticks after first contact. The initial pig fixture disabled AI:18 elevated pig cases never fell and are INVALID. They must not be counted as contact coverage. Natural-pig reruns are recorded separately. These are idle input trials, not synthetic player movement.

Evidence: [compressed raw paired JSONL](evidence/baseline-traces.tar.gz), [per-case summary](evidence/baseline-summary.csv). Extraction: `tar -xzf baseline-traces.tar.gz`. The archive contains complete collected sessions, including one separately labeled quicksand keyboard-action attempt. Its labels distinguish it from the54 matrix cases; it is not a complete three-material manual-action matrix.

Observed player matrix:841 exceptional position corrections in27cases; maximum first recorded depth1.3blocks. High entry depth and repeated legacy_step_budget correction are reproducible observations. They do not prove the user's intermittent surface twitch was the same phenomenon. Preserve that report as unproven.

The baseline OpenAL backend could not initialize, so zero sound callbacks are **unavailable evidence**, not proof of silence. Candidate uses OpenAL No Output software backend for callback observation; acoustic before/after equivalence is therefore not established. HP/fall events can still be compared. Multi-layer mud can stop on existing internal mud support at Y63.7; this is not bedrock at the bottom of a17layer pool and is outside B1 geometry scope.

After the complete baseline suite, concurrent unbounded Java processes caused container memory pressure. A later candidate client was killed (exit137, cgroup OOM counter1); the idle dedicated server hit its watchdog. These failed attempts are retained in build/runtime logs. The initial baseline suite predates this event; later manual-action and startup attempts must not be used as ordinary performance acceptance. Development runs now cap game JVM heap at1GiB and Gradle at512MiB.

## Completed natural-pig replacement

The separate observation-only fixture revision394f3d11869c7f7b3456a5b9c33d95a19a5aa6f2 (tree d68add7e5d706d624a20fc73eade8b04bd33a52d) retains unchanged physics/state/network source. [Its exact fixture/build patch](evidence/baseline-fixture.patch) applies to da60f10. The corrected27natural-pig cases all actually contacted material, with260samples and >=241ticks after contact. Three baseline singleplayer material action sessions were also repeated with real keyboard input and a working No Output audio backend.

The accepted comparison now consists of27real-player cases from the initial suite plus27natural-pig cases from the corrected suite,54per build. [Baseline accepted matrix](evidence/baseline-accepted-matrix.csv) and [candidate accepted matrix](evidence/candidate-accepted-matrix.csv) select the valid cases explicitly. Raw fixed-pig/action evidence is in [baseline-natural-and-actions.tar.gz](evidence/baseline-natural-and-actions.tar.gz); original invalid traces remain in the initial archive for audit.
