import numpy as np
import pandas as pd

from content_based_recommender import ContentBasedRecommender
import pickle
import dill

import pymysql

db = pymysql.connect(
    host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='kaist',
    passwd='0916',
    db='abandoned_dog',
    charset='utf8'
)
try:


    # breeds_data = pd.read_parquet("data/pre-processed/breeds.parquet")
    # want dog age, neuter_Yn 추가
    survey_lst=['user_id', 'user_age', 'user_sex', 'user_house_type', 'user_dog_experience',
                'neighbor_agreement', 'user_family_size', 'user_kids', 'dog_size',
                'shedding_level', 'bark_tolerance', 'spend_time', 'spend_type',
                'dog_sex', 'dog_environment', 'dog_support_agreement', 'dog_health_agreement',
                'want_dog_age', 'neuter_yn']


    # print(user_survey_data.iloc[0])

    # user = {}
    # user = dict(user_survey_data.iloc[0])
    #

    query = 'SELECT * FROM breeds_panel'
    breeds_panel = pd.read_sql(sql=query, con=db)

    query = 'SELECT * FROM adopter_data'
    adopter_data = pd.read_sql(sql=query, con=db)

    query = 'SELECT * FROM dog_list ' \
            'WHERE processState="보호중" AND kindCd != "믹스견"'
    dog_list_data = pd.read_sql(sql=query, con=db)

    #user_survey_data = {key: 3 for key in survey_lst}

    user_survey_data={
        'user_id': 1111,
        'user_age': '20대이하',
        'user_sex': 1,
        'user_house_type': '단독주택',
        'user_dog_experience': 1,
        'neighbor_agreement':'Y',
        'user_family_size': '2인',
        'user_kids':'예',
        'dog_size':'대형견',
        'shedding_level':4,
        'bark_tolerance':3,
        'spend_time':2,
        'spend_type':5,
        'dog_sex':'M',
        'dog_environment':3,
        'dog_support_agreement':'예',
        'dog_health_agreement':'예',
        'want_dog_age':'2022(년생)',
        'neuter_yn':'Y'
    }
    # print(breeds_panel.head())
    # print(adopter_data.head())
    # print(dog_list_data.head())
    recommender = ContentBasedRecommender(
        breeds_panel=breeds_panel,
        user_survey_data=user_survey_data,
        adopter_data=adopter_data,
        dog_list_data=dog_list_data
    )


    # #print(user)
    #recommender.predict(target_user_dict=user_survey_data)
    with open(file='survey_model/content_based_recommender.pkl', mode='wb') as f:
        pickle.dump(recommender, f)
    print(recommender.predict(target_user_dict=user_survey_data))

finally:
    db.close()
