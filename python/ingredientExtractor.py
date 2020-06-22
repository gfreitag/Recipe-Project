from flair.data import Sentence
from flair.models import SequenceTagger
import glob
import re

class Extractor:
    def __init__(self, model, recipes):
        self.ingreds=set()
        self.model=model
        self.recipes=recipes

    @staticmethod
    def _find_ingredients(self, sentence: Sentence):
        ingredList = []
        for token in sentence:
            if "Ingredient" in token.annotation_layers["label"][0].value:
                stripped = token.text.replace("Token: [0-20]", '')
                stripped = stripped.replace('.', '')
                stripped = stripped.replace(';', '')
                stripped = stripped.replace(',', '')
                stripped = stripped.replace(':', '')
                stripped = stripped.replace('-', '')
                stripped = stripped.replace('\n', '')
                if "B-Ingredient" in token.annotation_layers["label"][0].value:
                    ingredList.append(stripped)
                if "I-Ingredient" in token.annotation_layers["label"][0].value:
                    ingredList[-1] = ingredList[-1] + ' ' + stripped
        return ingreds

    def compile_set(self):
        for filename in glob.glob(self.recipes + '/*.txt'):
            fr = open(filename, 'r')
            for line in fr:
                sentence = Sentence(line)
                self.model.predict(sentence)
                sub_list = _find_ingredients(sentence)
                for item in sub_list:
                    self.ingreds.add(item)

    def get_ingreds(self):
        return self.ingreds