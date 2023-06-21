from django.db import models
import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd

class Iris(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    species = models.IntegerField(default=0)

    def __str__(self):
        return self.species

    def predict_species(self):
        # Load the trained machine learning model
        model = LogisticRegression()
        data = pd.read_csv('iris_dataset.csv')
        df = pd.DataFrame(data)
        X_train = df.drop('species', axis=1)
        y_train = df['species']
        model.fit(X_train, y_train)
        # Prepare the input data for prediction
        input_data = [[self.sepal_length, self.sepal_width, self.petal_length, self.petal_width]]
        input_data = np.array(input_data)

        prediction = model.predict(input_data)
        self.species = prediction[0]
        return self.species




