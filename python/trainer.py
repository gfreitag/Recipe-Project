from simpletransformers.ner.ner_model import NERModel

training=input("Training data file:")

# Create a NERModel
model = NERModel('bert', 'bert-base-cased', use_cuda = False, args={'overwrite_output_dir': True})


# Train the model
model.train_model("data/"+training, args={"use_multiprocessing":False, "output_dir":"./output"})