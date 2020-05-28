"""
This program takes .txt files with meal-master ingredient columns as input,
and outputs the same file with every ingredient on a new line. Also removes
unneeded whitespace.
"""

import re
import os
import glob
for filename in glob.glob('*.txt'):
    with open(os.path.join(os.getcwd(), filename), 'r') as fr:
        path = "./RecipeFolder23(3495items)"
        fullPath = os.path.join(path, filename)
        with open(os.path.join(os.getcwd(), fullPath), 'w') as fw:
            saw_ingredients = False
            done_ingredients = False
            print_ingredients=True
            preIng=[]
            col1=[]
            col2=[]
            postIng=[]
            for line in fr:
                line = line.strip()
                m = re.split(' {5,}', line)
                if len(m)>1:
                    saw_ingredients = True
                    col1.append(m[0])
                    col2.append(m[1])
                else:
                    if saw_ingredients:
                        saw_ingredients=False
                        for lines in col2:
                             fw.write(lines+'\n')
                        for lines in col1:
                             fw.write(lines+'\n')
                        col1.clear()
                        col2.clear()
                    fw.write(line+'\n')
            fw.close()
            fr.close()
