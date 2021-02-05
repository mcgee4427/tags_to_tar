
import json
import glob, os
import pathlib
from pathlib import Path
import fnmatch
#import tarfile
import os.path
import zipfile

def build_manifest(search_folder, manifest_filename, year, entity, output):
    manifest = []
    base_count = len(Path(search_folder).parts)

    for path in Path(search_folder).rglob(manifest_filename):
        with open(path) as f:
            data = json.load(f)
            # confirm the json is what we want
            if data['year'] == year and data['entity'] == entity:
                for i in data['include']:
                    os.chdir(path.parents[0])
                    rpath = ""
                    for p in path.parts[base_count:len(path.parts)-1]:
                        rpath = os.path.join(rpath,p)
                    print(rpath)
                    for file in glob.glob(i['files']):
                        manifest.append(os.path.join(rpath,file))

    return manifest

def zip_it(search_folder, output_file, manifest):
    os.chdir(search_folder)
    zf = zipfile.ZipFile(output_file, "w")
    for m in manifest:
        print(m)
        zf.write(m)
    zf.close()

jobs = json.load(open("config.json"))
for e in jobs['entities']:
    output_file = "{}.zip".format(e['output_file'])
    output_file = os.path.join(jobs['output_folder'],output_file)
    print(e['name'], e['output_file'],e['search_folder'],output_file)
    manifest = build_manifest(e['search_folder'], jobs['manifest_file'], jobs['year'], e['name'], output_file)
    zip_it(e['search_folder'], output_file, manifest)


