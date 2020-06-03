"""
This program concatenates separate conll files into one, with a delimiter.
"""

import re
import os
import glob

wr = open("testing.txt", 'w')
for filename in glob.glob('*.conll'):
    with open(os.path.join(os.getcwd(), filename), 'r') as fr:
        for line in fr:
            wr.write(line)
        wr.write("\n-DOCSTART- -X- -X- O\n\n")
        fr.close()
wr.close()