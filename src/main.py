from src.data_loader import load_data
from src.data_preprocessing import preprocess_data
from src.feature_engineering import create_user_movie_matrix
from src.train_model import train_recommendation_model
from src.recommend_movies import recommend_movies
from src.exploratory_data_analysis import plot_rating_distribution

from src.utils.io_utils import save_recommendations

from src.utils.logger import logger

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(BASE_DIR, "C:\\Users\\user\\Desktop\\Personal projects\\Recommender system (Movie lens)\\movies.csv")

def main():

    logger.info("Starting recommendation system pipeline...")

    movies, ratings = load_data()

    movies, ratings = preprocess_data(movies, ratings)

    plot_rating_distribution(ratings)

    user_movie_matrix = create_user_movie_matrix(ratings)

    similarity_matrix = train_recommendation_model(user_movie_matrix)

    movie_name = "Toy Story (1995)"

    recommendations = recommend_movies(
        movie_name,
        movies,
        user_movie_matrix,
        similarity_matrix
    )

    print("\nRecommended Movies:\n")

    for movie in recommendations:
        print(movie)

    save_recommendations(
        recommendations,
        "outputs/recommended_movies.csv"
    )

    logger.info("Pipeline completed successfully.")


if __name__ == "__main__":
    main()