from .ingredientExtractor import *
import torch
import random


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

    def __init__(self, ingredient_standarizer, recipe_source=None, model_filename=None):
        self.model = None
        self.ingredient_standardizer = ingredient_standarizer
        self.model_filename = model_filename
        self.recipe_source = recipe_source
        # if the filename is present, load the model.
        # Otherwise, create a new one.
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


if __name__ == "__main__":

    import plac

    # Here's a function to train the model from scratch
    def main(ingredient_fname, recipe_directory, model_directory):
        standardizer = IngredientStandardizer(ingredient_fname)
        model = IngredientCompletionModel(standardizer, recipe_source=recipe_directory)
        model.train(model_directory)

    plac.call(main)
