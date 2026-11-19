#!/usr/bin/env python3
"""Reviewed R0 findings. This edits analysis records only; it never edits game code."""
from pathlib import Path
from common import *
import argparse
p=argparse.ArgumentParser();p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();o=a.out_dir
review={
'MaterialProfile.java':('KEEP_TEMPORARILY','BlockQuicksand/BlockMud/BlockSoftQuicksand','3 profile enum cannot express original independent branch order and equipment/metadata; source explicitly says approximation','R2: per-material vectors then replace profile producer; keep motion safety'),
'LegacyBlocks.java':('KEEP_TEMPORARILY','research/original-phase3/01_ALL_SINKABLE_MATERIALS.csv','Shared SINKING/VISCOUS dispatch is construction classification, not independent original parity','R1 identity+variants then R2 dispatch per proven material'),
'CoatingLayer.java':('REPLACE_FROM_ORIGINAL','research/original-phase3/08_COATING_CAMERA_TEXTURE_SPEC.md','Whole model vanilla block texture; alpha min(.65,residueTicks/500) differs from typed masks/level/time','R3: versioned extra state + UV masks; retain residue NBT during migration'),
'CoatingHands.java':('KEEP_TEMPORARILY','research/original-phase3/08_COATING_CAMERA_TEXTURE_SPEC.md','First-person path must not be assumed third-person mask parity','R3: hand/skin/armor visual pairs'),
'LegacyFluids.java':('KEEP_TEMPORARILY','research/original-phase3/01_ALL_SINKABLE_MATERIALS.csv','All material fluid types share density1500 viscosity6000 motionScale0 supportsBoatingfalse; no legacy boat parity proof','R2-BOAT: isolate Boat status/submerged/gravity vs original contact branch, core3 matrix'),
'StuckLease.java':('KEEP_EXACT_OR_NECESSARY','research/original-mechanics-phase1/reports/03_stuck_and_tick_order.md','Last-writer lease/UUID update is evidence based; jumpMovementFactor is not ported by this reducer','Keep reducer; validate new producers before retiring old'),
'StuckAdapter.java':('KEEP_EXACT_OR_NECESSARY','docs/phase7/COMPLETION_REPORT.zh-CN.md','Server authority + once per tick + cleanup protect from double application; removal is not justified','Retain ownership cleanup; test crossings + same tick contacts'),
'OriginalContactBridge.java':('KEEP_TEMPORARILY','docs/phase8/COMPLETION_REPORT.zh-CN.md','Limited nonplayer QS contact must not be advertised full player/material physics','R2 contact closure before expanding gates'),
'MotionMath.java':('KEEP_TEMPORARILY','forge-1.20.1/docs/task-0035-b1/','Modern B1/B2 stability state machine not complete old Y algorithm; safety may be necessary','R2 compare ordered events/lowTPS Y before removing'),
'DryQuicksandCore.java':('KEEP_EXACT_OR_NECESSARY','research/original-phase5/02_SURFACE_BRANCH_CLOSURE.md','Pure core limited oracle domain is not production worldgen registration','R4 adapter with same RNG/write transaction traces'),
'OriginalTextureBindings.java':('KEEP_EXACT_OR_NECESSARY','docs/phase9/TEXTURE_MAPPING.csv','Private marker/resource manager is a modern bridge, not dead unoriginal behavior','Keep; validate actual packaged models/atlas'),
'Phase9RenderProbe.java':('KEEP_EXACT_OR_NECESSARY','docs/phase9/TEST_MATRIX.md','Opt-in DEV_ONLY screenshot probe; should remain inactive without property','Keep diagnostics disabled by default; do not use as installed JAR acceptance')}
rows=read(o/'mapping/AI_APPROXIMATION_AUDIT.csv')
for r in rows:
 name=Path(r['new_path']).name;r['owner']='reconstruction';r['pr']='R0 audit; no replacement execution'
 if name in review:
  decision,ev,diff,plan=review[name];r.update(decision=decision,original_refs=ev,difference_evidence=diff,replacement_plan=plan,proof_status='STATIC_REVIEW_PARTIAL_DYNAMIC_NOT_RUN')
for name in ['AI_APPROXIMATION_AUDIT','CODE_CLEANUP_DECISIONS']:write(o/'mapping'/(name+'.csv'),rows)
