from ingredientExtractor import *
import torch
import random
import os

class IngredientStandardizer(object):

    def __init__(self, ingredient_filename):
        self.word2index = {}
        self.index2word = {}
        ir=open(ingredient_filename,'r')
        for count, line in enumerate(ir):
            word2index[line]=count
            index2word[count]=line
        ir.close()
        # Read the file in and set the above member variables
        raise NotImplementedError()

    def word_to_index(self, word):
        # Maybe pre-test that it's present and return None or raise a special exception if not present.
        return self.word2index[word]

    def index_to_word(self, index):
        return self.index2word[index]


class IngredientCompletionModel(object):

    def __init__(self, ingredient_standarizer, model_filename=None):
        self.model = None
        self.ingredient_standardizer = ingredient_standarizer
        # if the filename is present, load the model.
        # Otherwise, create a new one.
        if os.path.exists(model_filename):
            #load model
        else:
            self.train()
        raise NotImplementedError()

    def recipes(self):
        # Generate a sequence of recipes
        raise NotImplementedError()

    def sample_pairs(self, recipe):
        # Generate a sequence of ingredient pairs from a single recipe
        extractor=Extractor('fullModel', recipe)
        extractor.compile_set_shallow()
        ingredList=extractor.get_ingreds()

        if len(ingredList) <= 1:
            raise ValueError()
        id_pairs = []
        for i in range(0, 20):
            # Maybe make this test outside the loop.
            center = random.choice(ingredList)
            context = random.choice(ingredList)
            while center == context:
                context = random.choice(ingredList)
            id_pairs.append((wordToIndex[center], wordToIndex[context]))
        return id_pairs
        #raise NotImplementedError()

    def train(self, model_dir='fullModel', epochs=100, learning_rate=0.01):
        raise NotImplementedError()

    def predict(self, ingredients):
        # Given a set of ingredients, predict what other ingredients should be present
        raise NotImplementedError()

    def get_input_layer(self, word_idx):
        x = torch.zeros(vocabulary_size).float()
        x[word_idx] = 1.0
        return x
