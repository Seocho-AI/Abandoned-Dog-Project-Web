from datetime import datetime, timedelta
import pickle
from flask import Blueprint, render_template, request, jsonify
import pandas as pd
import numpy as np
import pymysql
from model.content_based_recommender import ContentBasedRecommender


# ------------------- Flask Blueprint ------------------- #


survey = Blueprint("survey", __name__, template_folder="templates")


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
today_year = today[:4]  # 이번년도


# ------------------- SURVEY PREDICT MODEL ------------------- #


# with open('content_based_recommender.pkl', 'rb') as f:
#     model = pickle.load(f)  # 단 한줄씩 읽어옴


# ------------------- SURVEY PAGE API ------------------- #


@survey.route("/")  # Survey page
def survey_page():
    return render_template("survey.html")


@survey.route("/result", methods=["GET"])  # Receiving survey answer
def survey_answer():
    try:
        db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
                             port=3306, user='kaist', passwd='0916', db='abandoned_dog', charset="utf8")
        cursor = db.cursor()

        sur_res = request.args  # Stores user's survey answer
        user_answer = {
            'user_age': sur_res.get('user_age'),
            'user_sex': sur_res.get('user_sex'),
            'user_house_type': sur_res.get('user_house_type'),
            'dog_experience': {
                'dog_experience_yn': sur_res.get('dog_experience'),
                'dog_num': int(sur_res.get('dog_num', 0)),
                'dog_time': int(sur_res.get('dog_time', 0))
            },
            'dog_num': int(sur_res.get('dog_num', 0)),
            'dog_time': int(sur_res.get('dog_time', 0)),
            'user_family_size': sur_res.get('user_family_size'),
            'neighbor_agreement': sur_res.get('neighbor_agreement'),
            'user_kids': sur_res.get('user_kids'),
            'dog_size': sur_res.get('dog_size'),
            'shedding_level': int(sur_res.get('shedding_level')),
            'bark_tolerance': int(sur_res.get('bark_tolerance')),
            'spend_time': sur_res.get('spend_time'),
            'spend_type': sur_res.get('spend_type'),
            'dog_sex': sur_res.get('dog_sex'),
            'dog_environment': sur_res.get('dog_environment'),
            'dog_support_agreement': sur_res.get('dog_support_agreement'),
            'dog_health_agreement': sur_res.get('dog_health_agreement'),
            'want_dog_age': sur_res.get('want_dog_age'),
            'neuter_yn': sur_res.get('neuter_yn'),
            'user_id': '1'
        }

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

        recommender = ContentBasedRecommender(breeds_panel=breeds_panel,
                                              target_user_survey=user_answer,
                                              adopter_data=adopter_data,
                                              dog_list_data=dog_list_data,
                                              breed_info=breed_info,
                                              panel_info=panel_info)

        # #print(user)
        recommender.fit_transform(target_user_survey=user_answer)

        with open(file='model/content_based_recommender.pkl', mode='wb') as f:
            pickle.dump(recommender, f)

        recommended_dogs, recommended_scores = recommender.predict(
            user_survey_data=user_answer)

        survey_to_data = recommender.get_processed_user_data()
        dog_data = recommender.get_processed_dog_data()

        survey_results = {
            "Ranking_Count" : len(recommended_dogs),  # Ranking_Count : 공고번호의 수 (List) 
            "D_No_Ranking" : recommended_dogs,        # D_No_Ranking : 내림차순 정렬된 공고번호 (List) 
            "Rec_Score" : recommended_scores,         # Rec_Score : 각 유사도 스코어 Percentage (List)
            "Survey_Score" : survey_to_data,          # Survey_Score : 설문조사 수치로 바꾼 딕셔너리 (Dict)
            "Dog_Scores" : dog_data                   # Dog_Scores : recommended_dogs의 공고번호의 개들 수치화 (List[Dict])
        }
        print(survey_results)
        
        return render_template("survey_result.html", survey_results = survey_results)
        # return jsonify(survey_results)

    # except Exception as e:
    #     print("/survey/result ERROR")
    #     print(e)

    finally:
        cursor.close()
        db.close()
