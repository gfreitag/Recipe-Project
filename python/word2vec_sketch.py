class IngredientStandardizer(object):

    def __init__(self, ingredient_filename):
        self.word2index = None
        self.index2word = None
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
        raise NotImplementedError()

    def recipes(self):
        # Generate a sequence of recipes
        raise NotImplementedError()

    def sample_pairs(self, recipe):
        # Generate a sequence of recipe pairs from a single recipe
        raise NotImplementedError()

    def train(self, model_dir='fullModel', epochs=100, learning_rate=0.01):
        raise NotImplementedError()

    def predict(self, ingredients):
        # Given a set of ingredients, predict what other ingredients should be present
        raise NotImplementedError()

