# B1 evidence index

Runtime source ends at **dd99b5d**. Later commits package documentation/evidence and the reproducible JAR. All raw data below was actually collected; invalid attempts remain labeled, not replaced with manufactured values.

## Primary comparison

| Dataset | Accepted cases | Selection |
|---|---:|---|
|Baseline|54|27real players from da60f10 +27natural pigs from394f3d1|
|Candidate|54|27real players from f73565d +27natural pigs from f91251e|

[Baseline accepted CSV](baseline-accepted-matrix.csv) · [Candidate accepted CSV](candidate-accepted-matrix.csv). Each accepted case has260ENDsamples and >=200ticks after first contact (player minima239baseline/237candidate; natural pig minima241both).

Raw archives:

- [baseline-traces.tar.gz](baseline-traces.tar.gz): original observation-only paired traces. The18elevated NoAI pig cases never contact material and are INVALID. The9height0NoAI pig cases are historical and excluded from natural-pig acceptance. baseline_action_qs was attempted during later resource pressure and is not the complete action matrix.
- [baseline-natural-and-actions.tar.gz](baseline-natural-and-actions.tar.gz): corrected natural-pig cases and manual sessions. The three manual_player_*_L1_H0 sessions are the repeated baseline material action observations. An older3layer manual setup is retained separately and is not counted as a repeated action acceptance case.
- [candidate-integrated-traces.tar.gz](candidate-integrated-traces.tar.gz): initial matrix, corrected pigfix_cand cases and the three integrated manual material-action sessions. Initial NoAI cases remain excluded as above.
- [dedicated-traces.tar.gz](dedicated-traces.tar.gz): raw files grouped by server/player/observer. This includes valid controls,12primary delayed cases,3loaded cases,3dimension observations and partial/invalid attempts. The number of files is not the number of passed cases. Automatically started manual_* traces immediately superseded by net*/lowtps* labels are not extra accepted cases. action_qs and action_qs_valid have no settlement samples and are INVALID (dead operator). action_qs_alive, action_mud_alive and action_soft_alive are the valid dedicated keyboard sessions.

The baseline fixture-only revision is reproducible from da60f10 with [baseline-fixture.patch](baseline-fixture.patch); original tree hash d68add7e5d706d624a20fc73eade8b04bd33a52d. Its physics/state/network source is unchanged. [Original test hashes](original-tests.sha256) identify the four untouched original test source files relative to main79aac86.

## Dedicated/timing/landing

[Network/lifecycle CSV](network-cases.csv) · [Low-TPS timing](low-tps-timing.json) · [Measured status RTT](status-rtt.jsonl) · [Actual server config](mfqm-server.toml).

The12primary route cases exclude preliminary net0_quicksand token85789e2b. Three real low-TPS cases use the explicit bounded200×100ms load fixture while Dev remains on the nominal300ms route. Low-TPS timing is measured from200consecutive server END intervals ending immediately after each LOAD_END marker. Deep quicksand/soft-sand runs use temporary regeneration and do not establish ordinary survival. Y48 is the actual bedrock top in17layer fixtures; mudY63.7 is the unchanged internal mud support.

Current candidate sound callbacks prove requests, not physical speaker output. Ordinary stone and outside-cliff controls contain vanilla fall sound IDs and actual fall hurt requests. Deep loaded cases contain drowning requests and no fall-hurt/fall-sound requests. Early baseline audio backend failure makes its missing sound callbacks unavailable evidence, not proof of silence.

Actual dimension_before /dimension_nether /dimension_return files contain159samples each. In-material soft-sand state precedes clear Nether/overworld state; the speed query and visible HUD clearing are captured in screenshots. These are actual transfers, not mock-player lifecycle events.

## Builds and failures retained

[Final delivery build/test log](logs/24-delivery-validation.log) · [JUnit XML](junit/) · [Dedicated runtime log](logs/22-final-network-server.log).

- 01/02: observation build/package; 03: initial baseline client.
- 04/05: candidate automated iterations; 09/17/18/23: later build/regression iterations.
- 06/07: unbounded simultaneous-process attempt: one client exit137/cgroup OOM and idle server watchdog timeout. Retained as FAILED attempts.
- 10: failed X11 MIT-SHM launch; 11: successful bounded candidate integrated run.
- 12/14: dedicated controls/action attempts and valid repeats;13/19: intermediate dedicated launches.
- 15/16: corrected natural-pig baseline/candidate runs.
- 20/21/22: final real two-client dedicated runs. The environment paused/resumed, detaching stdin; actual later commands used the Observer operator client. No active material trace spans this gap. Runtime22 subsequently stopped normally and ended BUILD SUCCESSFUL; its elapsed time includes the pause.
- 24: exact final-runtime-source delivery validation:23JUnit,20required GameTests, BUILD SUCCESSFUL. Original18JUnit/15GameTest assertions retained unchanged.

[proxy50.log](logs/proxy50.log), [proxy150.log](logs/proxy150.log), [proxy300.log](logs/proxy300.log) record actual loopback route connections. Status PING/PONG is a separate measured protocol probe, not a player keepalive latency field.

Screenshots are unedited native captures in [screenshots/](screenshots/). [player-entry.svg](player-entry.svg) is a standard plot of measured JSONL positions, not an AI image or game texture. No continuous video or audible-device validation is claimed.

[SHA256SUMS](SHA256SUMS) covers the evidence files except this self-referential checksum file. The original private1.7.10JAR was not altered or included; its SHA-256 remains2a0809e13f2267b0eb981606164e863bc52bcdc326120b0ca27fd845a2f0db6b.
