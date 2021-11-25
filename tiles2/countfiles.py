import glob
import math
import os
import pandas as pd
import random
import re
import shutil


dest_dir = './src/'

# randomize the files list by renaming them
for dirpath, dirnames, filenames in os.walk(dest_dir):
    num = len([f for f in filenames if f.endswith("png")])
    print(f"{num} files total")
    side = int(math.sqrt(num))
    print(f"-tile {side}x{side} gives {side*side} images with {num-(side*side)} left over")

    rect = (side+1)*(side-1)
    print(f"-tile {side+1}x{side-1} gives {rect} images with {num-rect} left over")

    rect = (side+2)*(side-2)
    print(f"-tile {side+2}x{side-2} gives {rect} images with {num-rect} left over")

    rect = (side+1)*(side)
    print(f"-tile {side+1}x{side} gives {rect} images with {num-rect} left over")

    i = 0
    while i < 10 and side > 0:
        side = side-1
        if num % side == 0:
            print(f"-tile {side}x{num/side}")
            i = i + 1


