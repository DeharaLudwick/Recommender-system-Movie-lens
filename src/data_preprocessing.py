import pandas as pd

from src.utils.logger import logger


def preprocess_data(movies, ratings):

    logger.info("Removing duplicates...")

    movies.drop_duplicates(inplace=True)
    ratings.drop_duplicates(inplace=True)

    logger.info("Removing missing values...")

    movies.dropna(inplace=True)
    ratings.dropna(inplace=True)

    logger.info("Filtering inactive users...")

    active_users = ratings['userId'].value_counts()
    active_users = active_users[active_users > 20].index

    ratings = ratings[ratings['userId'].isin(active_users)]

    logger.info("Filtering unpopular movies...")

    popular_movies = ratings['movieId'].value_counts()
    popular_movies = popular_movies[popular_movies > 20].index

    ratings = ratings[ratings['movieId'].isin(popular_movies)]

    logger.info("Preprocessing complete.")

    return movies, ratings