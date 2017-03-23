python getfiles.py
magick montage -background "#000000" src\*.png .\cells.png
# examine image and add/remove cells to make it nice and square without empty space
# copy cells.png into ..\generator\deepzoom.py\examples\helloworld
cd ..\generator\deepzoom.py\examples\helloworld
python helloworld.py
# copy cells.dzi and cells_files into ./tiles subdir where index.html is pointing to it.
