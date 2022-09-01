from datetime import datetime, timedelta
from os import stat
from flask import Blueprint, render_template, jsonify, request
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


@find_dog.route("/thumbnail_page", methods=["GET"]) # Load thumbnails
def load_thumbnail():
    sql = "SELECT popfile, kindCd, sexCd, happenDt, noticeNo, processState, desertionNo FROM dog_list WHERE processState = '보호중' ORDER BY happenDt DESC;"
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
            "processState": dog_info[5],
            "desertionNo": dog_info[6]
        }
        dog_list.append(dog_dict)

    return jsonify(dog_list)


@find_dog.route("/filter", methods=["GET"]) # Load filters
def load_filter():
    # Fetching filter(region)
    sql_region = "SELECT DISTINCT(orgNm) FROM dog_list WHERE processState = '보호중';"
    cursor.execute(sql_region)
    result_region = cursor.fetchall()

    result_region_dict = {}
    for region in result_region:
        state_city = region[0].split(" ")
        state = state_city[0]
        if len(state_city) > 2:
            city = state_city[1] + state_city[2]
        elif len(state_city) == 1:
            city = state_city[0]
        else:
            city = state_city[1]

        if state not in result_region_dict:
            result_region_dict[state] = [city]
        else:
            result_region_dict[state].append(city)

    # Fetching filter(breed)
    sql_breed = "SELECT kindCd, COUNT(*) as count FROM dog_list WHERE processState = '보호중' GROUP BY kindCd ORDER BY kindCd ASC;"
    cursor.execute(sql_breed)
    result_breed = cursor.fetchall()

    result_breed_dict = {}
    for breed_count in result_breed:
        breed = breed_count[0]
        count = breed_count[1]
        result_breed_dict[breed] = count

    return jsonify(result_breed_dict, result_region_dict)


@find_dog.route("/dog_info")  # Dog posts page
def dog_info():
    return render_template("dog_info.html")


@find_dog.route("/dog_info/dog_post", methods=["GET", "POST"]) # Retreive dog info based on received desertion No
def dog_info_load():
    if request.method == "POST":
        desertion_no = request.form["desertionNo"]  # Stores the dog desertionNo
        sql = f"SELECT * FROM dog_list WHERE desertionNo = '{desertion_no}';"
        cursor.execute(sql)
        result = cursor.fetchall()
        result_unbox = result[0]

        global dog_info
        dog_info = {
            "happenDt": result_unbox[2],
            "happenPlace": result_unbox[3],
            "kindCd": result_unbox[4],
            "colorCd": result_unbox[5],
            "age": result_unbox[6],
            "weight": result_unbox[7],
            "noticeNo": result_unbox[8],
            "noticeSdt": result_unbox[9],
            "noticeEdt": result_unbox[10],
            "popfile": result_unbox[11],
            "processState": result_unbox[12],
            "sexCd": result_unbox[13],
            "neuterYn": result_unbox[14],
            "specialMark": result_unbox[15],
            "careNm": result_unbox[16],
            "careTel": result_unbox[17],
            "orgNm": result_unbox[19],
            "officetel": result_unbox[20],
            "mixPredict": result_unbox[21],
        }
        # return render_template("dog_info.html")
        # return jsonify(dog_info)
        return "Retreived dog info based on desertion no"
    elif request.method == "GET": # Load dog info to page
        return jsonify(dog_info)