import numpy as np


def precision_at_k(recommended, relevant, k=10):

    recommended_k = recommended[:k]

    relevant_set = set(relevant)

    hits = len(set(recommended_k) & relevant_set)

    return hits / k