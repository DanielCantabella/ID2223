# Instructions to run the end-to-end pipelines
1. First, create a free account on [hopsworks.ai](https://www.hopsworks.ai/)
2. Create a free account on [modal.com](https://modal.com/)
3. Create a free account on [huggingface.co](https://huggingface.co/)
4. Next, generate an API key on Hopsworks and set up every platform with it (just follow the assignment steps)
5. Next step is to install the different dependencies for the project:
`pip install -r requirements.txt`
6. Next you need to run the [feature pipeline notebook](wine-eda-and-backfill-feature-group.ipynb) to save the feature groups of our data in HopsWorks.
7. Then, you can run [“daily” feature pipeline script](wine-feature-pipeline-daily.py) to generate synthetic wine and run it once per day to add a new synthetic wine (you can use cronjob for example):
`modal run wine-feature-pipeline-daily.py`
8. After that, you can run the [training pipeline notebook](wine-training-pipeline.ipynb) to read training data with a Feature View from Hopsworks,
and train a Multilayer Perceptron Classifier model to predict if a wine’s quality is high or low.
9. In order to predict the quality of the new wine(s) added you can run the [batch inference pipeline script](wine-batch-inference-pipeline.py):
`modal run wine-batch-inference-pipeline.py`
10. If you want to see the user interface you should run [this script](huggingface-spaces-wine-monitor%2Fapp.py) to show the most recent wine quality prediction
and outcome, and a confusion matrix with historical prediction performance. If you want to enter or select feature values to predict
the quality of a wine for the features you entered, then you need to run [this script](huggingface-spaces-wine%2Fapp.py).
