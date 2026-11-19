"""Build item models from the reviewed original face/stack bindings."""
import json
from pathlib import PurePosixPath

def overlay(archive, catalog, output):
    for row in catalog:
        refs = []
        for source in row["textures"]:
            leaf = PurePosixPath(source).stem.lower()
            kind = "item" if "/items/" in source else "block"
            relative = f"{kind}/original/{leaf}"
            target = f"assets/mfqm/textures/{relative}.png"
            output[target] = archive.read(source)
            if source + ".mcmeta" in archive.namelist():
                output[target + ".mcmeta"] = archive.read(source + ".mcmeta")
            refs.append("mfqm:" + relative)
        if row["shape"] == "flat":
            model = {"parent":"minecraft:item/generated","textures":{"layer0":refs[0]}}
        elif len(refs) == 6:
            textures = dict(zip(("down","up","north","south","west","east"),refs))
            textures["particle"] = refs[0]
            if row["shape"] == "slab":
                faces = {key:{"texture":"#"+key} for key in list(textures)[:6]}
                model = {"parent":"minecraft:block/block","textures":textures,
                         "elements":[{"from":[0,0,0],"to":[16,8,16],"faces":faces}]}
            else:
                model = {"parent":"minecraft:block/cube","textures":textures}
        elif len(refs) == 2:
            model = {"parent":"minecraft:block/cube_bottom_top","textures":{"top":refs[0],"bottom":refs[0],"side":refs[1]}}
        else:
            model = {"parent":"minecraft:block/cube_all","textures":{"all":refs[0]}}
        data = (json.dumps(model,indent=2)+"\n").encode()
        output[f"assets/mfqm/models/item/{row['id']}.json"] = data
        if row['mode']=='block' and row['shape']=='cube':
            output[f"assets/mfqm/models/block/{row['id']}.json"] = data
    # The default square frame (32x32) cannot tile 32x304. Preserve the full row width,
    # all 19 strips, original frametime and every PNG byte.
    mucus = "assets/mfqm/textures/block/original/mucus_flowing.png.mcmeta"
    metadata = json.loads(output[mucus])
    metadata["animation"].update(width=32, height=16)
    output[mucus] = (json.dumps(metadata, indent=2) + "\n").encode()
