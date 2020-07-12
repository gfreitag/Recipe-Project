'''
References this tutorial: https://towardsdatascience.com/implementing-word2vec-in-pytorch-skip-gram-model-e6bae040d2fb
'''

from ingredientExtractor import *
import torch
import random


# function for converting to one-hot
def get_input_layer(word_idx):
    x = torch.zeros(vocabulary_size).float()
    x[word_idx] = 1.0
    return x


# enumerating full ingredient list
def get_index_ingreds():
    indexToWord = {}
    wordToIndex = {}
    filename = input('Ingredient list: ')
    for counter, item in enumerate(filename):
        indexToWord[counter] = item
        wordToIndex[item] = counter
    return indexToWord, wordToIndex


# prepare for training with one recipe
def setup(recipe, wordToIndex):
    random.seed()

    modelDir = 'fullModel'
    extractor = Extractor(modelDir, recipe)

    ingredDict = extractor.compile_set_shallow()
    ingredList = list(ingredDict.items())

    id_pairs = []
    for i in range(0, 20):
        if len(ingredList) <= 1:
            break
        center = random.choice(ingredList)
        context = random.choice(ingredList)
        while center == context:
            context = random.choice(ingredList)
        id_pairs.append((wordToIndex[center], wordToIndex[context]))
    return id_pairs


def train_loop(epochs, train_rate):
    for i in range(0, epochs):
        # For every recipe:
            id_pairs = setup(recipe, wordToIndex)
            # convert to one-hot-encoding
            # run through weights?
            # back propagate
            # Use clever pytorch tools
    # return loss, etc


if __name__ == "__main__":
    indexToWord, wordToIndex = get_index_ingreds()
    train_loop(100, 0.001)





