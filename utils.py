import pandas as pd
import numpy as np


def allGenres():
    df = pd.read_csv("./dataset/spotify_dataset_train.csv")
    genre_col = df.iloc[:, -1:]
    genre_arr = genre_col.to_numpy()
    genre_with_duplicate = np.squeeze(genre_arr, axis=1)
    genres = np.unique(genre_with_duplicate)
    return genres


def getGenre(oneHot):
    index = np.argmax(oneHot)
    return allGenres()[index]
