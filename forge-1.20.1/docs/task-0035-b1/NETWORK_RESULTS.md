# Dedicated two-client observations

Actual localhost Forge47.2.0 dedicated server, offline test accounts **Dev** (survival subject) and **Observer** (creative observer on the safe platform). Server source labeldd99b5d, clients6fd205a; their finite unmounted movement/landing code is identical, with later server-side-only diagnostic thread ownership guards. Both have version0.0.3.5-b1-candidate and channel2-b1. Join/list logs confirm both clients concurrently online. No fake player or forged movement/acknowledgement packets were used.

## Routes and measurements

Dev connected directly to127.0.0.1:25565, then reconnected through25566/25567/25568. Observer stayed directly connected. Opaque loopback TCP proxy adds25/75/150ms to each read chunk in each direction, with65536byte chunks/backpressure. This models delay and head-of-line batching, not packet loss or a full WAN.

Separate Minecraft status-PING/PONG measurements through the same routes (three samples per route):

| Nominal added RTT | Measured status RTT range |
|---:|---:|
|0ms|0.204–6.237ms|
|50ms|54.251–71.521ms|
|150ms|151.455–195.701ms|
|300ms|301.866–302.296ms|

These are measured status protocol round trips, **not the player's keepalive latency field**. The actual routes, proxy connection logs and scripts are retained. Nominal settings must not be presented as exact measured player RTT.

## Completed delayed movement cases

Each route ran real-player quicksand, mud and soft_quicksand cases with3layers and10block entry. Timed disposable-world functions start a case every280server ticks and return the player to a safe platform. Commands set only starting fixtures/diagnosis; the connected client performs all intervening vanilla movement and B1 prediction. Each trace lasts260server ticks and contains259–260ENDsamples; first contact is followed for at least232ticks. Operator input during these cases is idle.

| Route | Completed material cases | Corrections total | Minimum post-contact ticks | Minimum HP |
|---|---:|---:|---:|---:|
|direct|3|2|235|20|
|nominal50ms|3|1|238|20|
|nominal150ms|3|2|233|20|
|nominal300ms|3|4|232|20|

The earlier direct quicksand trace token85789e2b is a separate preliminary case, excluded from the12case comparison (and retained). After its trace expired, the idle player eventually drowned and was actually respawned through the client UI onto the safe platform. It is not a successful indefinite-survival claim.

Corrections remain exceptional, rather than being sent every ordinary movement tick. Retained teleport/acknowledgement timestamps document those events. A correction reason identifies the configured budget boundary; it does **not** prove that every delayed legitimate position batch deserves a visible correction. The tolerance is still a candidate, and rare visible pullback remains a risk. No claim is made that the original intermittent Y twitch has been conclusively reproduced or fixed.

Observer screenshots are real sampled views, not a continuous video. They establish the observed viewpoint and concurrent subject; server/client JSONL establish sampled motion. No all-WAN or all-camera smoothness guarantee follows.

## Low TPS and long landing

Low-TPS fixture is the explicit permission4 command `mfqm motionload 200 100`:200server ticks with100ms deliberate server-thread sleep. It is separate from diagnostics, default off, bounded, and logs BEGIN/END. Exact observed tick/nano intervals and completed low-TPS case results are in the evidence index and final report.

Long17layer quicksand/soft-sand landing tests use explicitly logged temporary regeneration to keep the subject alive long enough to reach bedrock; normal custom oxygen/drowning requests remain active. This intervention cannot establish ordinary deep-pit survival or ordinary HP conservation. It permits checking the long motion/fall history and sound callbacks. The park function clears the effect. Mud's existing internal support surface is reported separately and is not changed by B1.

## Environment limitations

The first unbounded concurrent launch suffered one container OOM kill and an idle server watchdog timeout; failed logs are preserved. Development JVMs were subsequently capped at1GiB and Gradle512MiB. The session later paused/resumed its environment: server stdin detached, so subsequent authorized test commands used the Observer operator client. No active material trace spans that pause. Raw UTC timestamps show the gap; completed data is not described as a continuous uninterrupted benchmark.

## Completed low-TPS cases and transfers

Measured timing uses200consecutive server END intervals ending immediately after each logged LOAD_END marker.

| Case | ENDsamples | Effective meanTPS | MedianTPS | Observed landingY | Corrections | Fall hurt/sound requests |
|---|---:|---:|---:|---:|---:|---:|
|17layer quicksand, regeneration|899|8.343|8.798|48.0 bedrock top|2|0 /0|
|3layer mud, no regeneration|359|8.310|8.784|63.7 internal mud support|1|0 /0|
|17layer soft sand, regeneration|899|8.178|8.850|48.0 bedrock top|4|0 /0|

Deep subjects have minimumHP18 and real drowning hurt requests; no fall-hurt or generic/block-fall sound callback occurred. Local measured descent minima are−0.030/−0.019678/−0.033blocks per client tick. Server END deltas can aggregate client ticks during lowTPS. All records have finite Y/vy and unique settlement ticks; correction runs are at most one consecutive sampled server tick in these datasets. These are observed runs, not a general smoothness guarantee.

Real transfer labels dimension_before /dimension_nether /dimension_return each contain159ENDsamples. The first is active soft sand, the latter two are clear withair300/HP20; movement speed query is approximately0.1 and the visible HUD clears. The operator explicitly loaded four Nether chunks to prepare a safe disposable platform, and removed the force-load afterward. Initial fill attempts were rejected because chunks were not loaded; they are retained in the console log. Server shutdown was normal and the full development-server run ended BUILD SUCCESSFUL, despite the earlier detached-stdin error on environment resume.
