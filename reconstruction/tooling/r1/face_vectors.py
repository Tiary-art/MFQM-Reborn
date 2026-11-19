"""Evaluate the finite face/damage domain of three reviewed pure CFR selectors."""
import re
import subprocess
import tempfile
from pathlib import Path

def selected_faces(code, damages):
    lines = [line.partition(': ')[2] for line in code.splitlines()]
    start = next(i for i,s in enumerate(lines) if 'IIcon func_149691_a(int par1, int par2)' in s)
    end = lines.index('    }', start + 1)
    body = '\n'.join(lines[start + 1:end])
    body = re.sub(r'this\.IIconMArray\[(\d+)\]', r'\1', body)
    # Only reviewed switch/if/integer operations can enter the isolated selector.
    tokens = set(re.findall(r'[A-Za-z_]\w*', body))
    if tokens - {'switch','case','if','return','break','par1','par2','default','int','else'}:
        raise ValueError(tokens)
    textures = dict(re.findall(r'IIconMArray\[(\d+)\] = \w+\.func_94245_a\("morefunquicksandmod:([^"]+)"',code))
    program = ('class Faces { static int select(int par1,int par2){'+body+
               '} public static void main(String[] args){for(String arg:args)for(int f=0;f<6;f++)'
               'System.out.println(select(f,Integer.parseInt(arg)));}}')
    with tempfile.TemporaryDirectory() as temp:
        path = Path(temp)/'Faces.java'
        path.write_text(program,encoding='utf-8')
        output = subprocess.check_output(['java',str(path),*map(str,damages)],text=True).splitlines()
    return {d:[textures[x] for x in output[i*6:i*6+6]] for i,d in enumerate(damages)}
