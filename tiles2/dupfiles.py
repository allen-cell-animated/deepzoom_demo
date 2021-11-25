import glob
import os
import pandas as pd
import pathlib
import random
import re
import shutil
import sys


dest_dir = './src/'

def dup_files(count, dryrun=True):
    # collect up all the files in dest_dir
    allfiles = []
    for dirpath, dirnames, filenames in os.walk(dest_dir):
        allfiles = [f for f in filenames if f.endswith("png")]

    # if count is greater than 0, we want to remove files
    # if count < 0, we want to duplicate files
    if count > 0:
        candidates = random.sample(allfiles, count)
        # remove -count files
        for i in range(len(candidates)):
            if dryrun:
                print("remove " + dest_dir + candidates[i])
            else:
                pathlib.Path(dest_dir + candidates[i]).unlink()
    elif count < 0:
        candidates = random.sample(allfiles, -count)
        # duplicate count files with new random prefix
        for i in range(len(candidates)):
            newname = str(random.randint(0,999999)).zfill(6) + candidates[i][6:]
            if (dryrun):
                print("copy "+ candidates[i] + " to " + newname)
            else:
                shutil.copy(dest_dir + candidates[i], dest_dir + newname)


if (len(sys.argv) > 1):
    # just go for it, using the first arg as the count value
    dup_files(int(sys.argv[1]), False)
