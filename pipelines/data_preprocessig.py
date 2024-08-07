import pandas as pd
import numpy as np
from steps.ingest_data import ingest_data
from steps.cleaning_data import clean_data
from config_data.config import DataConfing, load_config

def data_preprocessing() -> pd.DataFrame:
    '''Эта функция обрабатывает датасет HH.ru и формирует новый'''
    
    config: DataConfing = load_config()

    data_path: str = config.path

    data = ingest_data(data_path)

    clean_data(data=data)

    


