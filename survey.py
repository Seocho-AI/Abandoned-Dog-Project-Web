from datetime import datetime, timedelta
import pickle
from flask import Blueprint, render_template, request, jsonify
import pandas as pd
import pymysql


# ------------------- Connect Flask and PyMySQL ------------------- #


survey = Blueprint("survey", __name__, template_folder="templates")
db = pymysql.connect(
    host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='kaist',
    passwd='0916',
    db='abandoned_dog',
    charset="utf8")
cursor = db.cursor()


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
today_year = today[:4]  # 이번년도


# ------------------- SURVEY PREDICT MODEL ------------------- #


with open('survey_model/content_based_recommender.pkl', 'rb') as f:
    model = pickle.load(f)  # 단 한줄씩 읽어옴


# ------------------- SURVEY PAGE API ------------------- #


@survey.route("/")  # Survey page
def survey_page():
    return render_template("survey.html")


@survey.route("/result", methods=["POST"])  # Posing survey result
def survey_answer():
    user_answer = request.get_json()  # Stores user's survey answer
    user_answer['user_id'] = '1'

    query = 'SELECT * FROM breeds_panel'
    breeds_panel = pd.read_sql(sql=query, con=db)

    query = 'SELECT * FROM adopter_data'
    adopter_data = pd.read_sql(sql=query, con=db)

    query = 'SELECT * FROM dog_list ' \
            'WHERE processState="보호중" AND kindCd != "믹스견"'
    dog_list_data = pd.read_sql(sql=query, con=db)

    query = 'SELECT * FROM breed_info'
    breed_info = pd.read_sql(sql=query, con=db)

    model.fit(breeds_panel=breeds_panel,
              target_user_survey=user_answer,
              adopter_data=adopter_data,
              dog_list_data=dog_list_data,
              breed_info=breed_info)

    # return user_answer
    return jsonify(model.predict(user_survey_data=user_answer))
