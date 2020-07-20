from .ingredientExtractor import *
import torch
from torch.autograd import Variable
import random
import os


class IngredientStandardizer(object):

    def __init__(self, ingredient_filename):
        self.word2index = {}
        self.index2word = {}
        with open(ingredient_filename, "r") as ir:
            for count, line in enumerate(ir):
                self.word2index[line] = count
                self.index2word[count] = line

    def word_to_index(self, word):
        # Maybe pre-test that it's present and return None or raise a special exception if not present.
        return self.word2index[word]

    def index_to_word(self, index):
        return self.index2word[index]

    def vocabulary_size(self):
        return len(self.word2index)


class IngredientCompletionModel(object):

    def __init__(self, ingredient_standarizer, recipe_source, model_filename=None, embedding_dims=5):
        self.model = None
        self.ingredient_standardizer = ingredient_standarizer
        self.model_filename = model_filename
        self.recipe_source = recipe_source
        self.embedding_dims = embedding_dims
        self.extractor = Extractor('full_model', recipe_source)
        if model_filename is None:
            self.create_new_model()
        else:
            self.load_model()

    def create_new_model(self):
        embedding_dims = self.embedding_dims
        vocabulary_size = self.ingredient_standardizer.vocabulary_size()
        W1 = Variable(torch.randn(embedding_dims, vocabulary_size).float(), requires_grad=True)
        W2 = Variable(torch.randn(vocabulary_size, embedding_dims).float(), requires_grad=True)
        self.model = (W1, W2)

    def save_model(self, filename):
        raise NotImplementedError()

    def load_model(self):
        raise NotImplementedError()

    def recipes(self):
        for recipe in self.extractor.get_recipes():
            yield recipe

    def sample_pairs(self, recipe):
        # Generate a sequence of ingredient pairs from a single recipe
        ingredList = list(recipe.keys())
        stdr = self.ingredient_standardizer

        if len(ingredList) <= 1:
            return []

        id_pairs = []
        for i in range(0, 20):
            center = random.choice(ingredList)
            context = random.choice(ingredList)
            while center == context:
                context = random.choice(ingredList)
            id_pairs.append((stdr.word_to_index(center), stdr.word_to_index(context)))
        return id_pairs

    def train(self, model_dir='fullModel', epochs=100, learning_rate=0.01):
        W1, W2 = self.model
        for epoch in range(epochs):
            for recipe in self.recipes():
                for center, context in self.sample_pairs(recipe):
                    # Do something
                    raise NotImplementedError()

    def predict(self, ingredients):
        # Given a set of ingredients, predict what other ingredients should be present
        raise NotImplementedError()

    def get_input_layer(self, word_idx):
        x = torch.zeros(vocabulary_size).float()
        x[word_idx] = 1.0
        return x

if __name__ == "__main__":

    import plac

    # Here's a function to train the model from scratch
    def main(ingredient_fname, recipe_directory, model_directory):
        standardizer = IngredientStandardizer(ingredient_fname)
        model = IngredientCompletionModel(standardizer, recipe_directory)
        model.train(model_directory)

    plac.call(main)
