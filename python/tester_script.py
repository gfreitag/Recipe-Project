from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import TokenEmbeddings, WordEmbeddings, StackedEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
from pathlib import Path

columns={0: 'text', 1: 'label'}
dataPath='../data/'
corpus: Corpus = ColumnCorpus(dataPath, columns, train_file='train_data.txt', test_file='test_data.txt', dev_file='test_data.txt')

tag_type='label'
tag_dict=corpus.make_tag_dictionary(tag_type=tag_type)
print(tag_dict)

embedding_types = [WordEmbeddings('glove')]
embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

tagger: SequenceTagger = SequenceTagger(hidden_size=256, embeddings=embeddings, tag_dictionary=tag_dict,
                                        tag_type=tag_type, use_crf=True)

str_path = "/Users/gretafreitag/PycharmProjects/flairModel/venv/output/"
path = Path(str_path)

trainer: ModelTrainer = ModelTrainer(tagger, corpus)
trainer.final_test(path, eval_mini_batch_size=32)