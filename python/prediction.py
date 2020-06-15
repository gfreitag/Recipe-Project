from flair.data import Sentence
from flair.models import SequenceTagger

model = SequenceTagger.load('output/best-model.pt')

fr=open('Pork-Medallions-with-Port-Sauce.txt','r')
for line in fr:
    sentence=Sentence(line)
    model.predict(sentence)
    print(sentence.to_tagged_string())
'''
sentence = Sentence('Add the pasta and stir')

model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence('Set oven to 350 degrees Fahrenheit and bake for 30 minutes to an hour')

model.predict(sentence)
print(sentence.to_tagged_string())

sentence = Sentence('3/4 cup chopped red onions')

model.predict(sentence)
print(sentence.to_tagged_string())

'''
