#!/usr/bin/env python3
"""Summarize complete vectors and actual JUnit XML; never manufacture test passes."""
from pathlib import Path
import xml.etree.ElementTree as E
from collections import Counter
import json,shutil
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'docs/phase6';V=ROOT/'forge-1.20.1/src/test/resources/phase6'
rows=[]
for p in (ROOT/'forge-1.20.1/build/test-results/test').glob('TEST-*.xml'):
 r=E.parse(p).getroot();rows.append({k:r.attrib[k]for k in ['name','tests','failures','errors','skipped','time']});shutil.copy(p,D/'logs'/p.name)
assert len(rows)==4 and sum(int(r['tests'])for r in rows)==45
assert all(int(r[k])==0 for r in rows for k in ['failures','errors','skipped'])
(D/'logs/junit-summary.json').write_text(json.dumps(rows,indent=2)+'\n')
text='''# Phase6 test matrix

All PASS entries below refer to offline Java/JVM/mocked API or artifact tests, **not original Minecraft runtime**.

## Dry: full ordered interface events

Each row is a JUnit DynamicTest under originalDryTraces. Sources: Phase5 native `.jsonl.gz`, except supplement-* captured this phase with unchanged original method and the Phase5 JVM harness. parent38 is a child slice of Phase5 dry-positive seed38, with every preceding passed-stream RNG call replayed and checked first. This is not a Java implementation of the Surface parent.

| Test ID | Seed | Extent | Fixture | RNG | Reads | Writes | Rejected writes | Repeated write positions | Result |
|---|---:|---:|---|---:|---:|---:|---:|---:|---|
'''
failed=duplicate=0
for line in (V/'dry-cases.tsv').read_text().splitlines():
 tag,seed,extent,fixture=line.split('\t');events=[l.split('\t')for l in(V/(tag+'.tsv')).read_text().splitlines()];counts=Counter(e[0]for e in events);seen=set();duplicates=reject=0
 for e in events:
  if e[0]=='W':
   pos=tuple(e[1:4]);duplicates+=pos in seen;seen.add(pos);reject+=e[-1]=='false'
 failed+=reject;duplicate+=duplicates
 text+=f'| {tag} | {seed} | {extent} | {fixture} | {counts["R"]} | {counts["Q"]} | {counts["W"]} | {reject} | {duplicates} | PASS |\n'
assert failed>0 and duplicate>0
text+='''
Writes are not deduplicated; rejected writes do not change test-grid state. Subsequent Q events compare real grid values. Identity comparison ignores metadata. Protected fixture means SoftQuicksand identities in the input: Dry still overwrites them where the original does; it does not inherit Mire's protection.

## Stuck and existing tests

| Test / check | Evidence | Result / boundary |
|---|---|---|
| originalEightCallbacks | Phase5 native and oracle123 events revalidated; all48 projected Tick/Level/attribute/property events compared in Java | PASS, 8 updates:145, no renewal, idle,145→128,50,255,0, absent property; collision alternates |
| all112MathVectors | Phase4 physics-vectors.csv | PASS112 rows, amount tolerance1e-12, op2 andLevel0; jump output outside scope |
| cleanupIsolationAndNegativeLevels | Explicit port contract negative/identity tests | PASS old UUID removed before absent-property check; other UUID preserved; negative Level unchanged; lease lasts until next Update |
| MudGeometryTest | Existing JUnit | PASS4 |
| SinkMathTest | Existing JUnit | PASS14 |
| MotionMathTest | Existing JUnit | PASS5 |
| clean test build | logs/gradle-clean-test-build.log | PASS45 JUnit, zero failure/error/skip,11 executed Gradle tasks |
| Phase2 static / Phase3 trace / Phase4 math | logs/historical-regressions.json; isolated copy | PASS; no historical evidence overwritten |
| Phase5 saved native vs independent VM | logs/phase5-saved-native.stdout | PASS62 full streams, historical declared domains |
| Supplemental original vs independent VM | logs/supplemental-oracle.json | PASS2050/2268/2204 full events; deny fixture explicitly matched to original mock World |
| Resource auditors (Task002/003/B2) | logs/project-resource-audit.json, task003-resources.json, b2-resource-audit.log | PASS; no original textures/audio imported |
| Call isolation / pure compile | logs/isolation.json | PASS547 old files unchanged,52 outside Java files scanned; javac empty dependency classpath |
| 1.7.10 client/server;1.20.1 gameplay/client connection/visual/netY | No live game launched | NOT_RUN |
| Original air-control/global Forge scheduling/collision callbacks/natural distribution | Excluded integration gates | NOT_RUN |

## Failures retained during development

Initial Java event mismatch (missing repeated neighbor read); equivalent RNG scientific-number text formatting; deny grid fixture mismatch and missing deny fixture in the independent VM; checkout CRLF normalization in the artifact guard. Corrected implementation/declared test environments and comparison representation, not expected numeric values. All input cases retained. Earlier Gradle failure logs and supplemental-oracle-initial.log are historical failed attempts, not the final result. A pre-test-source build log only tests the old suite; the authoritative final run is clean-test-build and its XML.
'''
(D/'TEST_MATRIX.md').write_text(text)
print('PASS:45 actual JUnit results;19 complete Dry vectors, failures and duplicates present in corpus')
