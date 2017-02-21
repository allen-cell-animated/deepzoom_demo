import glob
import os
import pandas as pd
import shutil


dest_dir = './src/'


def pull_files(dataset):
    manifest = 'D:/src/cellbrowser-tools/data/' + dataset + '/auxiliary_spreadsheets/imageID_CellIndex_ometif*.xlsx'
    imgpath = 'Z:/software_it/danielt/demos/bisque/thumbnails/' + dataset + '/'
    inputfiles = [] + glob.glob(manifest)
    dfs = []
    for inputfile in inputfiles:
        dfs.append(pd.read_excel(inputfile))
    # Concatenate all data into one DataFrame
    big_frame = pd.concat(dfs, ignore_index=True)
    s = big_frame.to_csv(None, index=False, encoding='utf-8')
    s = s.replace(',', '').replace('.ome.tif', '.png').split('\n')
    for dirpath, dirnames, filenames in os.walk(imgpath):
        for filename in [f for f in filenames if f in s]:
            shutil.copy(os.path.join(dirpath, filename), dest_dir)

pull_files('nuc_cell_seg_delivery_20170210')
pull_files('nuc_cell_seg_delivery_20170217')
