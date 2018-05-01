import glob
import os
import pandas as pd
import random
import re
import shutil


dest_dir = './src/'
imgpath = '//allen/aics/animated-cell/Allen-Cell-Explorer/Allen-Cell-Explorer_1.2.0/Cell-Viewer_Thumbnails/'

# just get ALL files from this dir into a flat list.  name collisions will be overwritten
def pull_files(dataset):
    for dirpath, dirnames, filenames in os.walk(dataset):
        for filename in [f for f in filenames if len(f.split('_')) == 3]:
            shutil.copy(os.path.join(dirpath, filename), dest_dir)

for dirpath, dirnames, filenames in os.walk(imgpath):
    for dirname in dirnames:
        pull_files(imgpath + dirname)

# randomize the files list by renaming them
for dirpath, dirnames, filenames in os.walk(dest_dir):
    for filename in [f for f in filenames]:
        newname = str(random.randint(0,99999)).zfill(5) + filename
        os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, newname))
