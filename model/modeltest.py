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
    query = 'SELECT * FROM mixprinted_include'
    panel_info = pd.read_sql(sql=query, con=db)

    query = 'SELECT * FROM breeds_panel'
    breeds_panel = pd.read_sql(sql=query, con=db)

    query = 'SELECT * FROM adopter_data'
    adopter_data = pd.read_sql(sql=query, con=db)

    query = 'SELECT * FROM dog_list ' \
            'WHERE processState="보호중" AND kindCd != "믹스견"'
    dog_list_data = pd.read_sql(sql=query, con=db)

    query = 'SELECT * FROM breed_info'
    breed_info = pd.read_sql(sql=query, con=db)
    #user_survey_data = {key: 3 for key in survey_lst}

    user_survey_data={
        'user_age': '40대',
        'user_sex': '여성',
        'user_house_type': '아파트',
        'dog_experience': {
            'dog_experience_yn': '강아지를 키우고 있다',
            'dog_num': 3,
            'dog_time': 3
        },
        'dog_num': 3,
        'dog_time': 3,
        'user_family_size': '3인',
        'neighbor_agreement': '예',
        'user_kids': '예',
        'dog_size': '대형견',
        'shedding_level': 5,
        'bark_tolerance': 5,
        'spend_time': '적절한 : 6 ~ 10 시간',
        'spend_type': '실외 활동',
        'dog_sex': '암컷',
        'dog_environment': '실외',
        'dog_support_agreement': '아니오',
        'dog_health_agreement': '아니오',
        'want_dog_age': '자견(생후 2년 이하)',
        'neuter_yn': 'Y',
        'user_id': '1'
    }
    # print(breeds_panel.head())
    # print(adopter_data.head())
    # print(dog_list_data.head())
    recommender = ContentBasedRecommender(breeds_panel=breeds_panel,
                                          target_user_survey=user_survey_data,
                                          adopter_data=adopter_data,
                                          dog_list_data=dog_list_data,
                                          breed_info=breed_info,
                                          panel_info=panel_info)


    # #print(user)
    recommender.fit_transform(target_user_survey=user_survey_data)
    with open(file='content_based_recommender.pkl', mode='wb') as f:
        pickle.dump(recommender, f)
    recommender.predict(user_survey_data=user_survey_data)
    # for no in recommended_dogs:
    #     print(dog_list_data.loc[dog_list_data['desertionNo'] == no, :])

    print(recommender.get_processed_user_data())
    print(recommender.get_processed_dog_data())

finally:
    db.close()
