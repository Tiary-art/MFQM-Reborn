#!/usr/bin/env python3
import argparse,zipfile,xml.etree.ElementTree as E,json
from pathlib import Path
from common import *
p=argparse.ArgumentParser();p.add_argument('--repo-root',type=Path,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();r=a.repo_root;xml=list((r/'forge-1.20.1/build/test-results/test').glob('TEST-*.xml'));counts={k:sum(int(E.parse(p).getroot().get(k,0))for p in xml)for k in['tests','failures','errors','skipped']};assert xml and not counts['failures']and not counts['errors']
log=(a.out_dir/'evidence/logs/clean-build-gametest.log').read_text(encoding='utf-8');assert 'All 43 required tests passed'in log and 'BUILD SUCCESSFUL'in log
jar=next((r/'forge-1.20.1/build/libs').glob('*.jar'))
with zipfile.ZipFile(jar)as z:
 assert not any(x.endswith(('.png','.ogg'))for x in z.namelist())
 assert 'art/tiary/mfqm/integration/OriginalContactBridge.class'in z.namelist()
dump(a.out_dir/'checks/R0_TEST_RESULTS.json',dict(status='PASS_EXISTING_TEST_SCOPE_ONLY',junit=counts,gametests_passed=43,build_exit=0,jar_path=str(jar),jar_sha256=sha(jar.read_bytes()),jar_mode='PUBLIC_SOURCE_BUILD',new_r0_install_jar_distributed=False,reason='R0 changes analysis tools/database only; no new gameplay binary promised. Existing Phase9 tracked deliverable retained.',original_1_7_10_game='NOT_RUN',windows='NOT_RUN',formal_launcher='NOT_RUN',real_multiplayer='NOT_RUN',r0_e='NOT_ATTEMPTED'))
