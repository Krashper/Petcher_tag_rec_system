import pandas as pd


def save_data(data: pd.DataFrame, path: str) -> None:
    data.to_csv(path)