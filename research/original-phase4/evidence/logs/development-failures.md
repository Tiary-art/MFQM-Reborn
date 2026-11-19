# Development observations and retained failures

Initial smoke execution failed with NoClassDefFoundError: net/minecraft/inventory/IInventory during verification. The declared contract interface was added to prepare.py; this is an environment setup failure, not an original mod bug. Its occurrence was observed in tool output; this note is not presented as a preserved raw log.

Current unresolved runs gard-moor-real and gard-moor-water-first retain full original ERROR event/stderr at generateMorass@801. The ordinary Block mock is not an original BlockMorass instance; no callback is skipped to fake success.

liquid-invalid-bound intentionally invokes isWL76, preserving the partial writes and IllegalArgumentException at nextInt0. It is an expected invalid-input case, not a natural generated default.

private-import-guard.json records the expected refusal to extract original pixels/audio into a Git worktree. No resource file was extracted.

First 64-case run had 13 independent Mud comparisons. A final additional all-layouts fixture covers all 128 local occupancy boolean layouts plus applied/refused write columns, giving 65 cases and 14 comparisons. Final all_checks completed; later asset audio mapping/guard were checked separately without rerunning unchanged game-model cases.

Publication whitespace check initially flagged CRLF line endings in two generated asset CSVs. The CSV writer now emits LF; the full branch whitespace check was repeated. This is an artifact formatting fix, not a gameplay/model failure.
