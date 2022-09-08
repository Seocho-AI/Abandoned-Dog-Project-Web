from datetime import datetime, timedelta
import pickle
from flask import Blueprint, render_template, request, jsonify
import pandas as pd
import pymysql
# from cb_recommender import ContentBasedRecommender


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


@survey.route("/result", methods=["POST"])  # Posing survey result
def survey_answer():
    try:
        db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
                        port=3306, user='kaist', passwd='0916', db='abandoned_dog', charset="utf8")
        cursor = db.cursor()

        user_answer = request.get_json()  # Stores user's survey answer

        # Fix dog_experience answer (No experience)
        if user_answer["dog_experience"] == "없음":
            dog_experience_fix = {
                "dog_experience_yn": user_answer["dog_experience"],
                "dog_num": 0,
                "dog_time": 0
            }
            user_answer["dog_experience"] = dog_experience_fix
        else:  # Fix dog_experience answer (Currently own & Previously own)
            dog_experience_fix = {
                "dog_experience_yn": user_answer["dog_experience"],
                "dog_num": user_answer["dog_num"],
                "dog_time": user_answer["dog_time"]
            }
            user_answer["dog_experience"] = dog_experience_fix

        user_answer['user_id'] = '1'
        print(user_answer)

        query = 'SELECT * FROM breeds_panel'
        breeds_panel = pd.read_sql(sql=query, con=db)

        query = 'SELECT * FROM adopter_data'
        adopter_data = pd.read_sql(sql=query, con=db)

        query = 'SELECT * FROM dog_list ' \
                'WHERE processState="보호중" AND kindCd != "믹스견"'
        dog_list_data = pd.read_sql(sql=query, con=db)

        query = 'SELECT * FROM breed_info'
        breed_info = pd.read_sql(sql=query, con=db)

        user_survey_data = {
            'user_age': '50대',
            'user_sex': '여성',
            'user_house_type': '단독주택',
            'dog_experience': {
                'dog_experience_yn': '강아지를 키우고 있다',
                'dog_num': 6,
                'dog_time': 9
            },
            'dog_num': 6,
            'dog_time': 9,
            'user_family_size': '5인 이상',
            'neighbor_agreement': '아니오',
            'user_kids': '아니오',
            'dog_size': '중형견',
            'shedding_level': '8',
            'bark_tolerance': '3',
            'spend_time': '적절한 : 6 ~ 10 시간',
            'spend_type': '실외 활동',
            'dog_sex': '상관 없음',
            'dog_environment': '실내외 둘 다',
            'dog_support_agreement': '아니오',
            'dog_health_agreement': '예',
            'want_dog_age': '자견(생후 2년 이하)',
            'neuter_yn': 'Y',
            'user_id': '1'
        }

        recommender = ContentBasedRecommender(breeds_panel=breeds_panel,
                                                target_user_survey=user_answer,
                                                adopter_data=adopter_data,
                                                dog_list_data=dog_list_data,
                                                breed_info=breed_info)

        recommender.fit_transform(target_user_survey=user_answer)
        with open(file='content_based_recommender.pkl', mode='wb') as f:
            pickle.dump(recommender, f)
        recommended_dogs, recommended_scores = recommender.predict(
            user_survey_data=user_answer)

        # print(recommended_dogs)
        # print(recommended_scores)
        # print(recommender.get_processed_user_data())
        # print(recommender.get_processed_dog_data())

        return jsonify(recommender.get_processed_dog_data())
        # return jsonify(model.predict(user_survey_data=user_answer))

    except Exception as e:
        print("/survey/result ERROR")
        print(e)

    finally:
        cursor.close()
        db.close()