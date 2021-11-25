# get all the image files into one local directory
python getfiles.py
# print some useful numbers about how the tiling might look
python countfiles.py
# duplicate or remove some files
python dupfiles.py [number]
# re-run the tiling counter to verify zero remainders
python countfiles.py
# if remainders are zero, then we are ready to run the montage operation
magick montage -background "#000000" src\*.png .\cells.png
# examine image and add/remove cells from src\*.png to make it nice and square without empty space
# for example, from linux: select 35 files at random, and cp them to new filenames with random number prefixes
shuf -zn35 -e *.png  | xargs -0 -I % cp % "$(cat /dev/urandom | tr -cd '0-9' | head -c 5)_%"
# then repeat above magick step
copy cells.png ..\generator\deepzoom.py\examples\helloworld
cd ..\generator\deepzoom.py\examples\helloworld
python helloworld.py
# copy cells.dzi and cells_files into ./webpage/tiles subdir where ./webpage/index.html is pointing to it.
