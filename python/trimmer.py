'''
trimmer.py takes a dict of ingredients, then strips it to be purely alphabetical and without some of the artifacts
from label prediction.
'''

from ingredientExtractor import *
import re

modelDir='fullModel'
recDir='/Users/gretafreitag/RecipeProject/data/RecipeCorpus'

extractor=Extractor(modelDir, recDir)
extractor.get_from_file('condensedIngreds.txt')

ingredients=extractor.get_ingreds()
ingredientsCopy=ingredients.copy()

for ingredient in ingredientsCopy:
    ingStr=str(ingredient)
    change=False
    for char in ingStr:
        if (not char.isalpha()):
            if(char != ' '):
                ingStr = ingStr.replace(char,'')
                change=True
    if(re.search('mmmmm',ingStr) is not None):
        ingStr = ingStr.replace('mmmmm', '')
        change=True
    if change is True:
        extractor.ingreds.pop(ingredient)
        extractor.ingreds[ingStr]=1
extractor.set_to_file('fullIngSet.txt')



