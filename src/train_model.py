from sklearn.metrics.pairwise import cosine_similarity

import joblib

from src.config.config import SIMILARITY_MATRIX_PATH
from src.config.config import USER_MOVIE_MATRIX_PATH
from src.utils.logger import logger


def train_recommendation_model(user_movie_matrix):

    logger.info("Training recommendation model...")

    similarity_matrix = cosine_similarity(user_movie_matrix)

    logger.info("Saving trained model...")

    joblib.dump(similarity_matrix, SIMILARITY_MATRIX_PATH)
    joblib.dump(user_movie_matrix, USER_MOVIE_MATRIX_PATH)

    logger.info("Training completed.")

    return similarity_matrix