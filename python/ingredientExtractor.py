from flair.data import Sentence
from flair.models import SequenceTagger
import glob
import re
import os

class Extractor:
    def __init__(self, model, recipes):
        self.ingreds={}
        self.recipes=recipes
        self.model = SequenceTagger.load(model + '/best-model.pt')

    @staticmethod
    def _find_ingredients(sentence: Sentence):
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
                stripped=stripped.lower()
                if "B-Ingredient" in token.annotation_layers["label"][0].value:
                    ingredList.append(stripped)
                if "I-Ingredient" in token.annotation_layers["label"][0].value:
                    if(len(ingredList)>0):
                        ingredList[-1] = ingredList[-1] + ' ' + stripped
                    else:
                        continue
        return ingredList

    #for a single folder containing recipe files
    def compile_set(self):
        for filename in glob.glob(self.recipes + '/*.txt'):
            fr = open(filename, 'r')
            for line in fr:
                sentence = Sentence(line)
                self.model.predict(sentence)
                sub_list = self._find_ingredients(sentence)
                for item in sub_list:
                    try:
                        self.ingreds[item]+=1
                    except KeyError:
                        self.ingreds[item]=1

    #For several sub-directories in one larger directory containing recipe files
    def compile_set_deep(self):
        for dir in os.walk(self.recipes):
            for filename in glob.glob(dir[0] + '/*.txt'):
                fr = open(filename, 'r')
                last=''
                for line in fr:
                    sentence = Sentence(line)
                    self.model.predict(sentence)
                    sub_list = self._find_ingredients(sentence)
                    for item in sub_list:
                        try:
                            self.ingreds[item] += 1
                        except KeyError:
                            self.ingreds[item] = 1
                        last=item
                if(self.ingreds[last]>=10):
                    print(filename+':\n')
                    print('last ingredient: '+item)
                    print('\n-----------\n')



    def get_ingreds(self):
        return self.ingreds

    def set_to_file(self, filename, flag):
        wr=open(filename, 'w')
        for item in self.ingreds:
            if(self.ingreds[item]>=10):
                wr.write(item+'\n')

    def set_to_file(self, filename):
        wr = open(filename, 'w')
        for item in self.ingreds:
            wr.write(item+'\n')

    def get_from_file(self, filename):
        r=open(filename,'r')
        for line in r:
            line = line.replace('\n', '')
            self.ingreds[line]=1

    def append_to_file(self, filename):
        a=open(filename, 'a+')
        for item in self.ingreds:
            if(self.ingreds[item]>=10):
                a.write(item+'\n')
