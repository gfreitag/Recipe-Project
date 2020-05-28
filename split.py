"""
This program takes Meal-master .mmf files with multiple recipes and converts to multiple 
.txt files, stripping some of the noise and removing the delimiter.
"""

import re

fileName=input("Please give filename:\n")
f=open(fileName,encoding="iso-8859-1")

contents=f.read()
recipes=re.split('\nM{5}\n',contents)

for i in range(len(recipes)):
    titleFull=re.findall('Title: .*\n',recipes[i])
    if(len(titleFull)>=1):
        recipes[i]=recipes[i].replace('MMMMM----- Recipe via Meal-Master (tm) v8.02','\n')
        recipes[i]=recipes[i].replace('-----Meal-Master','')
        recipes[i] = recipes[i].replace(' \n','\n')
        recipes[i] = recipes[i].replace('\n\n','\n')
        recipes[i] = recipes[i].replace('\n\n', '')
        title=re.split('\: ',titleFull[0])
        titleStr=title[1].rstrip()
        titleStr=titleStr.replace(' ','-')
        titleStr=titleStr.replace('/',',')
        newFile="{rec_name}.txt".format(rec_name=titleStr)
        r=open(newFile,'w')
        r.write(recipes[i])
        r.close()
f.close()

