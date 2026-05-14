from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
INFERENCE_DATA_DIR = DATA_DIR / "inference"

MODELS_DIR = BASE_DIR / "models"
OUTPUTS_DIR = BASE_DIR / "outputs"

MOVIES_DATA_PATH = RAW_DATA_DIR / "movies.csv"
RATINGS_DATA_PATH = RAW_DATA_DIR / "ratings.csv"

CLEANED_MOVIES_PATH = PROCESSED_DATA_DIR / "cleaned_movies.csv"
CLEANED_RATINGS_PATH = PROCESSED_DATA_DIR / "cleaned_ratings.csv"

USER_MOVIE_MATRIX_PATH = MODELS_DIR / "user_movie_matrix.pkl"
SIMILARITY_MATRIX_PATH = MODELS_DIR / "similarity_matrix.pkl"
MOVIE_INDEX_PATH = MODELS_DIR / "movie_index.pkl"