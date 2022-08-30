from datetime import datetime, timedelta
from flask import Blueprint, render_template, jsonify, request
import pymysql


# ------------------- Connect Flask and PyMySQL ------------------- #


dog_posts = Blueprint("dog_posts", __name__, template_folder="templates")
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


# ------------------- DOG POSTS PAGE API ------------------- #


@dog_posts.route("/")  # Dog posts page
def find_dog_page():
    return render_template("dog_posts.html")


dog_info = {}
# Retrieve dog info from DB based on desertionNo received
@dog_posts.route("/dog_info", methods=["POST"])
def dog_info_post():
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
    
    # return jsonify(dog_info)
    return "hey"

@dog_posts.route("/dog_info", methods=["GET"])
def dog_info_get():
    return jsonify(dog_info)