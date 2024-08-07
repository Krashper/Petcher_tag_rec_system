import pandas as pd
import numpy as np
from steps.ingest_data import ingest_data
from steps.getting_similar_tags import get_similar_tags

def getting_tags(tag_count: int) -> list:
    '''Эта функция загружает матрицу косинусного сходства, запрашивает данные у пользователя и выдаёт похожие теги'''
    
    cosine_sim_matrix = ingest_data(r"Datasets\\Cosine_Sim_Matrix.csv", index_col=0)

    skills = ingest_data(r"Datasets\\Skills.csv")

    tags = list(skills["Skill"][:tag_count])

    user_tags = []

    for i in range(tag_count):
        print("Предложенные теги:")
        print(tags)

        user_tags.append(input(f"Выберите тег {i + 1}: "))

        print(f"Ваши теги: {user_tags}")
        
        tags = get_similar_tags(cosine_sim_matrix, user_tags, tag_count)


