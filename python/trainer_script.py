from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import TokenEmbeddings, WordEmbeddings, StackedEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer

columns={0: 'text', 1: 'label'}
dataPath='../data/'

train_file=input("Training data file:")
test_file=input("Testing data file:")
dev_file=input("Dev data file:")
output_path=input("path to save model:")
corpus: Corpus = ColumnCorpus(dataPath, columns, train_file=train_file, test_file=test_file, dev_file=dev_file)

tag_type='label'
tag_dict=corpus.make_tag_dictionary(tag_type=tag_type)
print(tag_dict)

embedding_types = [WordEmbeddings('glove')]
embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)

tagger: SequenceTagger = SequenceTagger(hidden_size=256, embeddings=embeddings, tag_dictionary=tag_dict,
                                        tag_type=tag_type, use_crf=True)

trainer: ModelTrainer = ModelTrainer(tagger, corpus)
trainer.train(output_path, learning_rate=0.1, mini_batch_size=32,max_epochs=100)
