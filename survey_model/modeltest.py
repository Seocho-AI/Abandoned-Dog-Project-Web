import pickle
import pandas as pd
import numpy as np
with open('survey_model/content_based_recommender.pickle', 'rb') as f:
    model = pickle.load(f)  # 단 한줄씩 읽어옴

breeds_data = pd.read_parquet("survey_model/data/pre-processed/breeds.parquet")
user_survey_data = pd.read_parquet(
    "survey_model/data/pre-processed/user_survey_data.parquet")

user = {}
user = dict(user_survey_data.iloc[0])

print(model.predict(target_user_dict=user))
# print(model.predict())

# model.predict(target_user_dict=dict)