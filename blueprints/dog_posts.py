from datetime import datetime, timedelta
from flask import Blueprint, render_template, jsonify, request
import pymysql
import json
import ast


# ------------------- Flask Blueprint ------------------- #


dog_posts = Blueprint("dog_posts", __name__, template_folder="templates")


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


real_today = datetime.strftime(datetime.now(), '%Y%m%d')  # 진짜 오늘
today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
three_month = datetime.strftime(
    datetime.now() - timedelta(90), '%Y%m%d')  # 최근 3개월
today_year = today[:4]  # 이번년도


# ------------------- DOG POST PAGE API ------------------- #

# Retreive dog info based on received desertion No
@dog_posts.route("/dog_info", methods=["GET"])
def dog_info_page():
    try:
        db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
                        port=3306, user='kaist', passwd='0916', db='abandoned_dog', charset="utf8")
        cursor = db.cursor()

        if request.method == "GET":
            # Stores the dog desertionNo
            args = request.args
            desertion_no = args.get('id')

            # Retreive dog info from DB
            sql1 = f"SELECT * FROM dog_list WHERE desertionNo = '{desertion_no}';"
            cursor.execute(sql1)
            result1 = cursor.fetchall()
            result_unbox1 = result1[0]

            breed = result_unbox1[4]
            mix_predict = result_unbox1[21]

            dog_info = {
                "happenDt": result_unbox1[2],
                "happenPlace": result_unbox1[3],
                "kindCd": result_unbox1[4],
                "colorCd": result_unbox1[5],
                "age": result_unbox1[6],
                "weight": result_unbox1[7],
                "noticeNo": result_unbox1[8],
                "noticeSdt": result_unbox1[9][:4] + "/" + result_unbox1[9][4:6] + "/" + result_unbox1[9][6:],
                "noticeEdt": result_unbox1[10][:4] + "/" + result_unbox1[10][4:6] + "/" + result_unbox1[10][6:],
                "popfile": result_unbox1[11],
                "processState": result_unbox1[12],
                "sexCd": result_unbox1[13],
                "neuterYn": result_unbox1[14],
                "specialMark": result_unbox1[15],
                "careNm": result_unbox1[16],
                "careTel": result_unbox1[17],
                "orgNm": result_unbox1[19],
                "officetel": result_unbox1[20],
                "mixPredict": result_unbox1[21],
            }

            # Retreive breed info from DB
            if breed == "믹스견":
                mix_predict = ast.literal_eval(mix_predict)
                breed = mix_predict[0]
                sql_2 = f"SELECT * FROM final_mixprinted WHERE breed = '{breed}';"
            else:
                sql_2 = f"SELECT * FROM final_mixprinted WHERE breed_name_kr = '{breed}';"
            
            cursor.execute(sql_2)
            result_2 = cursor.fetchall()
            result_unbox_2 = result_2[0]

            dog_info["size"] = result_unbox_2[40]
            dog_info["origin"] = result_unbox_2[41]
            dog_info["usage"] = result_unbox_2[42]
            dog_info["height"] = result_unbox_2[43]
            dog_info["breed_weight"] = result_unbox_2[44]
            dog_info["color"] = result_unbox_2[45]
            dog_info["describe"] = result_unbox_2[46]

            return render_template("dog_info.html", dog_info=dog_info)

    # except Exception as e:
    #     print("/find_dog/dog_info ERROR")
    #     print(e)

    finally:
        cursor.close()
        db.close()