# Known gaps and acceptance boundary

- Candidate curve and numerical tolerance need user gameplay approval; no legacy numerical parity claim.
- Surface Y twitch reported in OBS-09 remains intermittent and without a proven root cause. Correction counts and trace deltas are evidence, not proof that this symptom is fixed.
- The referenced MFQM-main (3).zip is not in the current attachment set. Work starts from actual merged main 79aac86 (audit PR4 merged), not the old Task 003 ZIP. ZIP equivalence has not been verified.
- Existing soft-sand 0.85 top, internal stack geometry, mud internal support surfaces, boats and conditional movement of blocks are intentionally unchanged. Some multi-layer mud runs land on an internal support, not bedrock.
- Wall-time allowance is capped at4 client ticks; longer stalls can legitimately require an exceptional correction. Prediction is not an anti-cheat replacement and must coexist with other movement mods through further compatibility tests.
- Audio callback observations do not establish audible device output. Missing sound callbacks on an unavailable OpenAL backend cannot establish absence of a landing sound.
- See TEST_RESULTS for real completed coverage versus remaining gaps. No unperformed scenario is considered passed.
