from flair.data import Sentence
from flair.models import SequenceTagger

model = SequenceTagger.load('output/best-model.pt')

fr=open('../data/example_recipe.txt','r')
for line in fr:
    sentence=Sentence(line)
    model.predict(sentence)
    print(sentence.to_tagged_string())

