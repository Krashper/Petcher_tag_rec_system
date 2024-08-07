from pipelines.data_preprocessig import data_preprocessing
from pipelines.getting_tags import getting_tags
import pandas as pd
import logging
from config_data.config import load_config


if __name__ == "__main__":
    try:
        logging.info("Starting app")

        data_preprocessing()

        config = load_config()

        getting_tags(tag_count=config.tag_count)
    
    except Exception as e:
        logging.error("Error during starting app:", e)

        raise e