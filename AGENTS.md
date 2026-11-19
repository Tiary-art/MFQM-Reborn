# Reconstruction governance

Use reconstruction/manifest and reconstruction/mapping as the structured source of truth; old research is evidence, not proof modern integration is complete. Read reconstruction/README.zh-CN.md before changing runtime code.

Every future restoration PR updates the relevant original object IDs, modern mappings, behavior cases, cleanup decisions and coverage from the same change. Preserve unresolved objects in denominators. BYTECODE_CONFIRMED signatures do not prove behavior parity. PRIVATE resources and original JARs must remain ignored.

Do not remove/rename existing registry IDs, states, NBT/config/network keys or stability protections without the paired original evidence, no-double-application proof, migration tests and rollback required by the R0 task. R0 runtime cleanup is deferred; no speculative deletion.

Run reconstruction/tooling/validate_database.py and report_coverage.py with explicit repo/output paths for database changes. Run clean test build and available GameTests for runtime changes, and retain raw logs and exact NOT_RUN statuses. Verify packaged JAR separately from development classpaths. Stop after the authorized work package; do not start R1–R5 automatically.
