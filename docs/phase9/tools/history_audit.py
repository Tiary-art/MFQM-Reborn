#!/usr/bin/env python3
"""Audit current public delivery evidence; hashes verify files, never gameplay claims."""
from pathlib import Path
import csv,json,hashlib,subprocess,re
R=Path(__file__).resolve().parents[3];D=R/'docs/phase9'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
tracked=set(subprocess.check_output(['git','ls-files'],cwd=R,text=True).splitlines());rows=[]
def row(phase,category,path,status=None,evidence='',severity='NONE',blocker=''):
 p=R/path if path else None;exists=p.is_file()if p else False
 ignored=False
 if path:ignored=subprocess.run(['git','check-ignore','-q',path],cwd=R).returncode==0
 rows.append(dict(phase=phase,category=category,path=path,sha256=sha(p)if exists else'',git_tracked=path in tracked,git_ignored=ignored,status=status or('PRESENT_VERIFIED'if exists and path in tracked else'PRESENT_UNVERIFIED'if exists else'MISSING_REQUIRED'),evidence=evidence,severity=severity,capability_verification='FILE/CONTENT EVIDENCE ONLY; historical runtime not re-executed here',blocker=blocker))
for phase,root in [('1','research/task-001'),('1-research','research/original-mechanics-phase1'),('2','research/original-phase2'),('3','research/original-phase3'),('4','research/original-phase4'),('5','research/original-phase5'),('6','docs/phase6'),('7','docs/phase7'),('8','docs/phase8')]:
 files=[p for p in sorted(tracked)if p.startswith(root+'/')]
 for p in files:
  if p.endswith(('.md','.json','.csv','.py','.java','.toml','.gradle','.sh')):
   row(phase,'report/tool/evidence',p,evidence='Current tracked tree; historical reports retained')
 if not files:row(phase,'stage-root',root,'BLOCKED_NO_EVIDENCE','No tracked stage root under this historical name',blocker='Do not infer missing obligations from a directory label alone')
for phase,path in [('Task002','deliverables/task-002/mfqm-reborn-0.0.2-dev.jar'),('Task003','deliverables/task-003/mfqm-reborn-0.0.3-dev.jar'),('B1','deliverables/task-0035-b1/mfqm-reborn-0.0.3.5-b1-candidate.jar'),('B2','deliverables/task-0035-b2/mfqm-reborn-0.0.3.5-b2-candidate.jar'),('8','deliverables/phase8/mfqm-reborn-phase8-controlled.jar')]:row(phase,'install-jar',path,evidence='Tracked binary; Phase8 checksum record / historical deliverables')
for phase in ['6','7']:row(phase,'separate install JAR','','NOT_REQUIRED','Task/report did not require a distributed candidate; reports explicitly say no new gameplay JAR published')
row('8','previous workspace-only JAR','','SUPERSEDED','PR15/edeb2f1 fixed the earlier absence; current deliverables/phase8 is tracked',severity='PREVIOUS_HIGH_FIXED')
row('8','version-string risk','deliverables/phase8/mfqm-reborn-phase8-controlled.jar','PRESENT_VERIFIED','Contains actual Phase8 classes despite old B2 candidate version string; Phase9 uses a new version',severity='MEDIUM_LABEL_ONLY')
for phase,path in [('6','forge-1.20.1/src/main/java/art/tiary/mfqm/legacy/StuckLease.java'),('6','forge-1.20.1/src/main/java/art/tiary/mfqm/legacy/DryQuicksandCore.java'),('7','forge-1.20.1/src/main/java/art/tiary/mfqm/integration/StuckAdapter.java'),('8','forge-1.20.1/src/main/java/art/tiary/mfqm/integration/OriginalContactBridge.java')]:row(phase,'current implementation',path,evidence='Current code exists; Phase9 tests compare baseline/candidate, not a claim full legacy physics restored')
# Cross-check the current assembly, configs/resources/tests and earlier gameplay delivery reports.
for path in sorted(tracked):
 if path.startswith(('forge-1.20.1/src/','forge-1.20.1/tools/','forge-1.20.1/docs/','deliverables/task-'))or path in ['forge-1.20.1/build.gradle','forge-1.20.1/gradle.properties','forge-1.20.1/settings.gradle','forge-1.20.1/TASK_002_REPORT.md','forge-1.20.1/TASK_003_REPORT.md']:
  row('historical/current-assembly','source/config/resource/test/report/tool',path,evidence='Tracked current assembly; source/content check, not historical runtime parity')
with(D/'HISTORICAL_DELIVERY_AUDIT.csv').open('w',newline='')as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
# Current hash manifests: detect actual missing/mismatched entries without rewriting old reports.
manifests=[]
for p in sorted(R/path for path in tracked if Path(path).name in ['SHA256SUMS','SHA256SUMS.txt']and not path.startswith(('docs/phase9/','deliverables/phase9/'))):
 base=p.parent.parent if p==R/'forge-1.20.1/docs/task-0035-audit/evidence/SHA256SUMS'else p.parent
 result={'path':str(p.relative_to(R)),'relative_base':str(base.relative_to(R)),'files':0,'missing':[],'mismatched':[]}
 for l in p.read_text().splitlines():
  if not l.strip()or l.startswith('#'):continue
  digest,name=l.split('  ',1);target=base/name;result['files']+=1
  if not target.is_file():result['missing'].append(name)
  elif sha(target)!=digest:result['mismatched'].append(name)
 manifests.append(result)
# Accessible Codex worktree status, excluding ignored build/private outputs on purpose.
worktrees=[]
for p in sorted((R.parents[0]).glob('mfqm-*')):
 if p==R or not(p/'.git').exists():continue
 x=subprocess.run(['git','-C',str(p),'ls-files','--others','--exclude-standard'],capture_output=True,text=True)
 worktrees.append({'worktree':p.name,'access':'ACCESSIBLE'if x.returncode==0 else'NOT_VERIFIABLE','untracked_project_paths':x.stdout.splitlines()if x.returncode==0 else[],'ignored_private/build_files':'not considered missing required public deliverables'})
outputs=[]
for p in sorted(Path('/workspace/outputs').glob('MFQM-Phase8/*')):
 if p.is_file():outputs.append({'name':p.name,'sha256':sha(p),'classification':'SUPERSEDED workspace copy; Phase8 install JAR now tracked in deliverables/phase8'})
(D/'history-audit-details.json').write_text(json.dumps({'base_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),'rows':len(rows),'manifests':manifests,'worktrees':worktrees,'accessible_workspace_outputs':outputs,'private_inputs':'intentionally not public deliverables; no original assets copied by audit'},indent=2)+'\n')
print(json.dumps({'audit_rows':len(rows),'manifest_entries':sum(x['files']for x in manifests),'missing':sum(len(x['missing'])for x in manifests),'mismatched':sum(len(x['mismatched'])for x in manifests),'worktrees':len(worktrees)},indent=2))
