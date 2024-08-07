import pandas as pd
import numpy as np
from steps.save_data import save_data
from collections import defaultdict
from itertools import combinations
from sklearn.metrics.pairwise import cosine_similarity


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    hh_skills = data["Keys"]
    hh_skills = hh_skills.apply(lambda x: eval(x)) # перевод строки в список

    final_hh_skills = hh_skills.explode() # перевод из строки в список

    user_skills = pd.DataFrame(final_hh_skills.value_counts().index[:10000], columns=["Skill"]) # отбор 10000 самых популярных навыков

    save_data(user_skills, r"Datasets\\Skills.csv") # сохранение датафрейма

    matrix_compatibility = create_matrix_compatibility(hh_skills=hh_skills, user_skills=list(user_skills["Skill"]))

    save_data(matrix_compatibility, r"Datasets\\Matrix_Compatibility.csv")

    create_cosine_sim_matrix(matrix_compatibility)


def create_matrix_compatibility(hh_skills: pd.DataFrame, user_skills: list):
    occurrence_dict = defaultdict(lambda: defaultdict(int)) # Создание 2-уровнего словаря

    for lst in hh_skills:
        pairs = combinations(lst, 2) # создание всевозможных пар для каждой строки со скиллами
        
        for tag1, tag2 in pairs:
            if tag1 in user_skills and tag2 in user_skills:
                occurrence_dict[tag1][tag2] +=1
                occurrence_dict[tag2][tag1] +=1

    occurence_df = pd.DataFrame(occurrence_dict).fillna(0)

    return occurence_df


def create_cosine_sim_matrix(occurence_df: pd.DataFrame):
    cosine_sim_matrix = pd.DataFrame(cosine_similarity(occurence_df.T), 
                                 index=occurence_df.columns, 
                                 columns=occurence_df.columns)

    save_data(cosine_sim_matrix, r"Datasets\\Cosine_Sim_Matrix.csv")