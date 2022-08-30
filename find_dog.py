from datetime import datetime, timedelta
from os import stat
from flask import Blueprint, render_template, jsonify
import pymysql


# ------------------- Connect Flask and PyMySQL ------------------- #


find_dog = Blueprint("find_dog", __name__, template_folder="templates")
db = pymysql.connect(
    host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='kaist',
    passwd='0916',
    db='abandoned_dog',
    charset="utf8")
cursor = db.cursor()


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


real_today = datetime.strftime(datetime.now(), '%Y%m%d')  # 진짜 오늘
today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
three_month = datetime.strftime(
    datetime.now() - timedelta(90), '%Y%m%d')  # 최근 3개월
today_year = today[:4]  # 이번년도


# ------------------- FIND DOG PAGE API ------------------- #


@find_dog.route("/")  # Find dog page
def find_dog_page():
    return render_template("find_dog.html")


@find_dog.route("/thumbnail_page", methods=["GET"])
def load_thumbnail():
    sql = "SELECT popfile, kindCd, sexCd, happenDt, noticeNo, processState FROM dog_list WHERE processState = '보호중' ORDER BY happenDt DESC;"
    cursor.execute(sql)
    result = cursor.fetchall()

    dog_list = []
    for dog_info in result:
        dog_dict = {
            "popfile": dog_info[0],
            "kindCd": dog_info[1],
            "sexCd": dog_info[2],
            "happenDt": dog_info[3][:4] + "/" + dog_info[3][4:6] + "/" + dog_info[3][6:],
            "noticeNo": dog_info[4].replace("-", " ")[:5],
            "processState": dog_info[5]
        }
        dog_list.append(dog_dict)

    return jsonify(dog_list)


@find_dog.route("/filter", methods=["GET"])
def load_filter():
    # Fetching filter(region)
    sql_region = "SELECT DISTINCT(LEFT(noticeNo, 5)) FROM dog_list WHERE processState = '보호중';"
    cursor.execute(sql_region)
    result_region = cursor.fetchall()

    result_region_dict = {}
    for region in result_region:
        state_city = region[0].split('-')
        state = state_city[0]
        city = state_city[1]
        if state not in result_region_dict.keys():
            result_region_dict[state] = [city]
        else:
            result_region_dict[state].append(city)

    # Fetching filter(breed)
    sql_breed = "SELECT DISTINCT(kindCd) FROM dog_list WHERE processState = '보호중' ORDER BY kindCd ASC;"
    cursor.execute(sql_breed)
    result_breed = cursor.fetchall()
    result_breed_list = []

    for breed in result_breed:
        result_breed_list.append(breed[0])

    return jsonify(result_breed_list, result_region_dict)
