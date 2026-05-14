import pandas as pd

from src.utils.logger import logger


def create_user_movie_matrix(ratings):

    logger.info("Creating user-movie matrix...")

    user_movie_matrix = ratings.pivot_table(
        index='movieId',
        columns='userId',
        values='rating'
    )

    user_movie_matrix.fillna(0, inplace=True)

    logger.info("Matrix created successfully.")

    return user_movie_matrix