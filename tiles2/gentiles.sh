#!/usr/bin/env bash -x

# DO NOT USE; DEPRECATED;  SEE readme.txt FOR INSTRUCTIONS
exit

# my pyramid generator using imagemagick routines.
# first create the level0.png image.  this is the full sized, full rez image.
convert -resize 50% level0.png level1.png
convert -resize 50% level1.png level2.png
convert -resize 50% level2.png level3.png
convert -resize 50% level3.png level4.png
convert -resize 50% level4.png level5.png
convert -resize 50% level5.png level6.png
convert -resize 50% level6.png level7.png
convert -resize 50% level7.png level8.png
# now create tiles 512x512 each, from the different levels,
# of the form pyramid/L(level)_(tilex)_(tiley).png
convert level0.png -crop 512x512\! -background black -set filename:tile "%[fx:page.x/512]_%[fx:page.y/512]" +repage +adjoin "pyramid/L0_%[filename:tile].png"
convert level1.png -crop 512x512\! -background black -set filename:tile "%[fx:page.x/512]_%[fx:page.y/512]" +repage +adjoin "pyramid/L1_%[filename:tile].png"
convert level2.png -crop 512x512\! -background black -set filename:tile "%[fx:page.x/512]_%[fx:page.y/512]" +repage +adjoin "pyramid/L2_%[filename:tile].png"
convert level3.png -crop 512x512\! -background black -set filename:tile "%[fx:page.x/512]_%[fx:page.y/512]" +repage +adjoin "pyramid/L3_%[filename:tile].png"
convert level4.png -crop 512x512\! -background black -set filename:tile "%[fx:page.x/512]_%[fx:page.y/512]" +repage +adjoin "pyramid/L4_%[filename:tile].png"
convert level5.png -crop 512x512\! -background black -set filename:tile "%[fx:page.x/512]_%[fx:page.y/512]" +repage +adjoin "pyramid/L5_%[filename:tile].png"
convert level6.png -crop 512x512\! -background black -set filename:tile "%[fx:page.x/512]_%[fx:page.y/512]" +repage +adjoin "pyramid/L6_%[filename:tile].png"
convert level7.png -crop 512x512\! -background black -set filename:tile "%[fx:page.x/512]_%[fx:page.y/512]" +repage +adjoin "pyramid/L7_%[filename:tile].png"
convert level8.png -crop 512x512\! -background black -set filename:tile "%[fx:page.x/512]_%[fx:page.y/512]" +repage +adjoin "pyramid/L8_%[filename:tile].png"
