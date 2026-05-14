import pandas as pd

from src.config.config import MOVIES_DATA_PATH
from src.config.config import RATINGS_DATA_PATH


def load_data():
    movies = pd.read_csv("C:\\Users\\user\\Desktop\\Personal projects\\Recommender system (Movie lens)\\movies.csv")
    ratings = pd.read_csv("C:\\Users\\user\\Desktop\\Personal projects\\Recommender system (Movie lens)\\ratings.csv")

    return movies, ratings