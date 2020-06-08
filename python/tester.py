from simpletransformers.ner.ner_model import NERModel

modelIn=input("Directory of model:")
testing=input("Testing data file:")

# Create a NERModel
model = NERModel('bert', modelIn, args={"use_multiprocessing":False}, use_cuda=False)


# Evaluate the model
result, model_outputs, predictions = model.eval_model(testing)

# Check predictions
print(predictions[:5])
print("precision: ")
print(result["precision"])
print("recall: ")
print(result["recall"])
print("f1 score:")
print(result["f1_score"])
