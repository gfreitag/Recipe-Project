'''
Refrences this tutorial: https://towardsdatascience.com/implementing-word2vec-in-pytorch-skip-gram-model-e6bae040d2fb
'''

from ingredientExtractor import *
import torch
import random

def get_input_layer(word_idx):
    x = torch.zeros(vocabulary_size).float()
    x[word_idx] = 1.0
    return x


if __name__ == "__main__":
    random.seed()
    filename = input('Ingredient list: ')
    recipe = input('Recipe: ')
    indexToWord = {}
    wordToIndex = {}

    modelDir = 'fullModel'
    extractor = Extractor(modelDir, recipe)

    ingredDict = extractor.compile_set_shallow()
    ingredLiist = list(ingredDict.items())

    for counter, item in enumerate(filename):
        indexToWord[counter] = item
        wordToIndex[item]=counter
    volume = len(indexToWord)

    id_pairs=[]
    for i in range(0, 20):
        if len(ingredList) <= 1:
            break
        center = random.choice(ingredList)
        context = random.choice(ingredList)
        while center == context:
            context = random.choice(ingredList)
        id_pairs.append(wordToIndex[center], wordToIndex[context])
