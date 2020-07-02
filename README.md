# Recipe-Project

This is a personal project for training a machine learning model on food recipes, using named entity recognition(NER). I downloaded over 140,000 recipes, and have about 200 annotated to be used in training and testing. 

Currently, the trained model is able to extract ingredients with an f1 score of about 0.893. It has been trained on around 200 annotated recipes, and evaluated with a hold-out set of about 30.

The goal for this project is to find a way to "auto-complete" ingredients when they are missing from a recipe.

Makes use of the [Flair framework](https://github.com/flairNLP/flair)
