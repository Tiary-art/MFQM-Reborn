Raw *.log.gz preserve original bytes (gzip mtime0). Plain *.log only normalize trailing whitespace. JSON logs retain command outputs and expected guard failures. Early75-file private build summaries are superseded by private-build-verified.json/private-build.log (88 files).

Baseline JUnit task was UP-TO-DATE; retained XML46 pass is not a fresh baseline JUnit execution. Actual baseline/candidate GameTests43 pass; final candidate clean JUnit46 pass. Development clients intentionally closed after capture: their Gradle exit is nonzero, not masked as clean exit PASS.

Historical initial audit (516 rows/1828 entries) is superseded by expanded audit (1062 rows/1950 entries,16 manifests); both runs found0 missing/mismatches. All current Forge source/config/resource/test and earlier gameplay delivery/report/tool paths are additionally inventoried.

A packaging command initially ran from deliverables/phase9 instead of repo root, so README/manifest regeneration failed and the old checksum for updated ARTIFACTS.json did not match. Re-run from repo root regenerated metadata hashes; JAR hashes did not change. This was a packaging-check error, not a Gradle/test failure.
