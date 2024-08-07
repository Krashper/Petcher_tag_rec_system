import pandas as pd
import numpy as np


def get_average_cosine_similarity(tag, tag_list, cosine_sim_matrix):
    similarities = []
    
    for user_tag in tag_list:
        if user_tag in cosine_sim_matrix.index and user_tag in cosine_sim_matrix.columns:
            similarities.append(cosine_sim_matrix.loc[tag, user_tag])

    return np.mean(similarities) if similarities else 0


def get_similar_tags(cosine_sim_matrix: pd.DataFrame, tag_list: list, tag_count: int) -> list:
    tag_df = pd.DataFrame(cosine_sim_matrix.index, columns=["Name"])


    tag_df["Score"] = tag_df["Name"].apply(get_average_cosine_similarity, args=(tag_list, cosine_sim_matrix))

    result_tags = tag_df[~tag_df["Name"].isin(tag_list)].sort_values(by="Score", ascending=False)[:tag_count]

    return list(result_tags["Name"].values)