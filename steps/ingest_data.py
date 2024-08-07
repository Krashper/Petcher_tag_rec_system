import pandas as pd
import numpy as np


def ingest_data(path: str, index_col=None) -> pd.DataFrame:
    dataset = pd.read_csv(path, index_col=index_col)

    return dataset