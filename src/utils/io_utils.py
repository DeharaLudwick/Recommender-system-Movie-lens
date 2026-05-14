import pandas as pd


def save_recommendations(recommendations, output_path):

    df = pd.DataFrame(recommendations, columns=['Recommended Movies'])

    df.to_csv(output_path, index=False)