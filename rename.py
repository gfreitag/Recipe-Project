"""
This program renames files to be ascii compatible. 
"""

import os
import re

for filename in os.listdir("./RecipeFolder16(150items)"):

    src = './RecipeFolder16(150items)/' + filename
    dst=filename
    nonAlpha=[]
    for char in filename:
        if(not char.isalnum()):
            nonAlpha.append(char)
    for chars in nonAlpha:
        dst = dst.replace(chars,'-')

    dst=dst.replace("-txt","")
    dst = './RecipeFolder16(150items)/' + dst +'.txt'

    # rename() function will
    # rename all the files
    os.rename(src, dst)