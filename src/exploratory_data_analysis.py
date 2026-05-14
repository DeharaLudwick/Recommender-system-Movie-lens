import matplotlib.pyplot as plt
import seaborn as sns

from src.utils.logger import logger


def plot_rating_distribution(ratings):

    logger.info("Generating rating distribution plot...")

    plt.figure(figsize=(8, 5))

    sns.countplot(x='rating', data=ratings)

    plt.title("Movie Rating Distribution")

    plt.savefig("outputs/visualizations/ratings_distribution.png")

    plt.close()