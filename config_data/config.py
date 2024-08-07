from dataclasses import dataclass
from os import getenv
from environs import Env
import logging


@dataclass
class DataConfing:
    path: str = getenv("path", "")
    tag_count: int = getenv("TAG_COUNT", 1)


def load_config(path: str | None = None) -> DataConfing:
    try:
        env = Env()
        env.read_env(path)

        logging.info("Getting config data")
        return DataConfing(path=env("DATA_PATH"), tag_count=int(env("TAG_COUNT")))
    
    except Exception as e:
        logging.error("Error during loading config data:", e)
        raise e