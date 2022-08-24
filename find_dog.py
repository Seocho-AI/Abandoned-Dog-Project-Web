from datetime import datetime, timedelta
from flask import Blueprint, render_template, jsonify
import pymysql


# ------------------- Connect Flask and PyMySQL ------------------- #


find_dog = Blueprint("find_dog", __name__, template_folder="templates")
db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com', port=3306, user='kaist',
                     passwd='0916', db='abandoned_dog', charset="utf8")
cursor = db.cursor()


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
today_year = today[:4]  # 이번년도


# ------------------- FIND DOG PAGE API ------------------- #


@find_dog.route("/")  # Find dog page
def find_dog_page():
    return render_template("find_dog.html")


@find_dog.route("/thumbnail_page", methods=["GET"])
def load_thumbnail():
    sql = "SELECT popfile, kindCd, sexCd, happenDt, noticeNo, processState FROM dog_list ORDER BY happenDt DESC LIMIT 100;"
    cursor.execute(sql)
    result = cursor.fetchall()

    dog_list = []

    for dog_info in result:
        dog_dict = {
            "popfile": dog_info[0],
            "kindCd": dog_info[1],
            "sexCd": dog_info[2],
            "happenDt": dog_info[3],
            "noticeNo": dog_info[4],
            "processState": dog_info[5]
        }
        dog_list.append(dog_dict)

    return jsonify(dog_list)
