# 003.5-B2 candidate

Minecraft 1.20.1 / Forge 47.2.0 / Java17. Install the same JAR on both client and dedicated server. Back up saves; this is a partial recovery candidate.

49 legacy Block registrations and 13 native Forge fluid families. Not all legacy behaviors are restored (44 PARTIAL, 5 REGISTERED_ONLY). See `forge-1.20.1/docs/task-0035-b2/COMPLETION_REPORT.zh-CN.md` and KNOWN_GAPS.md before reviewing.

Validation: 23 JUnit + 29 GameTest pass; real singleplayer smoke and dedicated server with two clients exercised selected paths. Unperformed scenarios are explicitly listed. Original legacy JAR/art/audio are not included.
