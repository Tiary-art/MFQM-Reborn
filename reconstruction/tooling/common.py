import csv,json,hashlib
from pathlib import Path
def sha(b):return hashlib.sha256(b).hexdigest()
def ident(kind,symbol):return kind+':'+sha(symbol.encode())[:24]
def write(path,rows,fields=None):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 with path.open('w',newline='',encoding='utf-8')as f:
  w=csv.DictWriter(f,fieldnames=fields or list(dict.fromkeys(k for r in rows for k in r)),lineterminator='\n');w.writeheader();w.writerows(rows)
def read(path):
 with Path(path).open(encoding='utf-8-sig',newline='')as f:return list(csv.DictReader(f))
def dump(path,obj):
 Path(path).parent.mkdir(parents=True,exist_ok=True);Path(path).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
