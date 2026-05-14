import pandas as pd

from src.utils.logger import logger


def recommend_movies(
    movie_title,
    movies,
    user_movie_matrix,
    similarity_matrix,
    top_n=10
):

    logger.info(f"Generating recommendations for: {movie_title}")

    movie_index = movies[movies['title'] == movie_title].index[0]

    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommended_movies = similarity_scores[1:top_n + 1]

    recommendations = []

    for movie in recommended_movies:
        index = movie[0]
        recommendations.append(movies.iloc[index]['title'])

    logger.info("Recommendations generated successfully.")

    return recommendations