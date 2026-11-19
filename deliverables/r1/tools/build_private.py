"""Build the R1 private artifact from a local original JAR (Java 17, Python 3)."""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
parser = argparse.ArgumentParser()
parser.add_argument("--jar", type=Path, required=True)
parser.add_argument("--offline", action="store_true")
parser.add_argument("--verify-only", action="store_true")
args = parser.parse_args()
out = ROOT / "local-original-assets/r1"
resources = out / "resources"
out.mkdir(parents=True, exist_ok=True)
importer = ROOT / "docs/phase9/tools/asset_pipeline.py"
cmd = [sys.executable, "-X", "utf8", str(importer), "--jar", str(args.jar), "--output", str(resources)]
if not args.verify_only:
    subprocess.run(cmd, check=True)
subprocess.run(cmd + ["--verify"], check=True)
jar = out / "mfqm-reborn-r1-private.jar"
if not args.verify_only:
    wrapper = ["cmd.exe","/d","/c","gradlew.bat"] if os.name == "nt" else ["./gradlew"]
    command = wrapper + ["clean","test","build","--console=plain",f"-PmfqmOriginalAssets={resources}"]
    if args.offline:
        command.append("--offline")
    with (out/"build.log").open("wb") as log:
        subprocess.run(command, cwd=ROOT/"forge-1.20.1",stdout=log,stderr=subprocess.STDOUT,check=True)
    shutil.copyfile(ROOT/"forge-1.20.1/build/libs/mfqm-reborn-0.1.0-r1-content.jar",jar)
manifest = json.loads((resources/".mfqm-import-manifest.json").read_text(encoding="utf-8"))
with zipfile.ZipFile(jar) as archive:
    for path,digest in manifest["files"].items():
        if hashlib.sha256(archive.read(path)).hexdigest()!=digest:
            raise ValueError(f"Packaged resource differs: {path}")
digest=hashlib.sha256(jar.read_bytes()).hexdigest()
record=out/"ARTIFACTS.json"
if args.verify_only:
    previous=json.loads(record.read_text(encoding="utf-8"))
    if previous["jar_sha256"]!=digest:
        raise ValueError("Private JAR differs from the recorded build")
    revision=previous["source_commit"]
else:
    revision = subprocess.run(["git","rev-parse","HEAD"],cwd=ROOT,capture_output=True,text=True).stdout.strip() if (ROOT/".git").exists() else None
if not revision:
    public_record=ROOT/"deliverables/r1/ARTIFACTS.json"
    revision=json.loads(public_record.read_text(encoding="utf-8"))["source_commit"] if public_record.exists() else "unknown archive checkout"
catalog=json.loads((ROOT/"forge-1.20.1/src/main/resources/data/mfqm/r1_content.json").read_text(encoding="utf-8"))
originals=set()
with zipfile.ZipFile(args.jar) as archive:
    originals={p for p in archive.namelist() if p.endswith(".png")}
packed_hashes=set(manifest["files"].values())
with zipfile.ZipFile(args.jar) as archive:
    matching=sum(hashlib.sha256(archive.read(p)).hexdigest() in packed_hashes for p in originals)
result = dict(source_commit=revision,jar_sha256=digest,
              original_jar_sha256=manifest["original_jar_sha256"],verified_entries=manifest["files"],
              mapped_catalog_rows=len(catalog), original_pngs=len(originals),
              original_pngs_without_identical_overlay_payload=len(originals)-matching,
              model_check="all generated model JSON hashes match packaged entries")
(out/"ARTIFACTS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k!="verified_entries"},indent=2))
print(f"Verified {len(manifest['files'])} entries in {jar}\nSHA256 {result['jar_sha256']}")
