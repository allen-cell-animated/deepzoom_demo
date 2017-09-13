import glob
import os
import pandas as pd
import random
import re
import shutil


dest_dir = './src/'


# just get ALL files from this dir into a flat list.  name collisions will be overwritten
def pull_files(dataset):
    imgpath = '//allen/aics/animated-cell/Allen-Cell-Explorer/Allen-Cell-Explorer_1.1.0/Cell-Viewer_Thumbnails/' + dataset + '/'
    for dirpath, dirnames, filenames in os.walk(imgpath):
        for filename in [f for f in filenames if len(f.split('_')) == 3]:
            shutil.copy(os.path.join(dirpath, filename), dest_dir)

pull_files('2017_03_08_Struct_First_Pass_Seg')
pull_files('2017_05_15_tubulin')
pull_files('2017_06_28_lamin')
pull_files('2017_07_21_Tom20')

# randomize the files list by renaming them
for dirpath, dirnames, filenames in os.walk(dest_dir):
    for filename in [f for f in filenames]:
        newname = str(random.randint(0,99999)).zfill(5) + filename
        os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, newname))
