from cleanup_data import X_test, y_test
from model import model
from utils import getGenre
import numpy as np

NUMBER_VALUES = 30


def formatPrediction(predictions, y_test):
    good = 0
    for prediction, y in zip(predictions, y_test):
        prediction_genre = getGenre(prediction)
        y_genre = getGenre(y)
        if prediction_genre == y_genre:
            good += 1
        print(
            f"prediction: {prediction_genre} | real result: {y_genre}")
    print(
        f"\ngood/total: {good}/{len(predictions)} - {round(100*good/len(predictions))}%")


model.load_weights('./models/bestmodel.h5')


predictions = model.predict(X_test[:NUMBER_VALUES])

formatPrediction(predictions, y_test[:NUMBER_VALUES])
