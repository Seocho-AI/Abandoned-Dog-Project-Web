from datetime import datetime, timedelta
import pickle
from flask import Blueprint, render_template, request
import pandas as pd
import pymysql


# ------------------- Connect Flask and PyMySQL ------------------- #


survey = Blueprint("survey", __name__, template_folder="templates")
db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com', port=3306, user='kaist',
                     passwd='0916', db='abandoned_dog', charset="utf8")
cursor = db.cursor()


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
today_year = today[:4]  # 이번년도


# ------------------- SURVEY PREDICT MODEL ------------------- #


with open('survey_model/content_based_recommender.pickle', 'rb') as f:
    model = pickle.load(f)  # 단 한줄씩 읽어옴

breeds_data = pd.read_parquet("survey_model/data/pre-processed/breeds.parquet")


# ------------------- SURVEY PAGE API ------------------- #


@survey.route("/")  # Survey page
def survey_page():
    return render_template("survey.html")


@survey.route("/result", methods=["POST"])  # Posing survey result
def survey_answer():
    user_answer = request.get_json()  # Stores user's survey answer

    # Afghan Hound / Affenpinscher
    # sql = "select * from breed_info where breed_name = 'Afghan Hound';"
    # cursor.execute(sql)
    # result = cursor.fetchall()
    # result = result[0]  # Tuple unboxing

    # info_dict = {
    #     "breed_name": result[0],
    #     "breed_name_kr": result[1],
    #     "dog_info_json": json.loads(result[2])
    # }

    # for question_type, rating in answer_receive.items():
    #     print(question_type, ":", rating)

    # Returning predicted dog breed list
    return model.predict(target_user_dict=user_answer)
