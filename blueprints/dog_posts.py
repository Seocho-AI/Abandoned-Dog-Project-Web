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
                breed_predict_en = mix_predict[0]
                breed_chance = mix_predict[1]
                sql_2 = f"SELECT * FROM final_mixprinted WHERE breed = '{breed_predict_en}';"
            else:
                sql_2 = f"SELECT * FROM final_mixprinted WHERE breed_name_kr = '{breed}';"
            
            cursor.execute(sql_2)
            result_2 = cursor.fetchall()
            result_unbox_2 = result_2[0]

            if breed == "믹스견":
                breed_predict_kr = result_unbox_2[39]
                dog_info["kindCd_predict"] = breed_predict_kr
                dog_info["breed_chance"] = breed_chance

            dog_info["panel_data"] = {
                "a_adaptability": {
                    "A": result_unbox_2[3]*20,
                    "a1": result_unbox_2[4]*20,
                    "a2": result_unbox_2[5]*20,
                    "a3": result_unbox_2[6]*20,
                    "a4": result_unbox_2[7]*20,
                    "a5": result_unbox_2[8]*20,
                    "a6": result_unbox_2[9]*20
                },
                "b_friendliness": {
                    "B": result_unbox_2[10]*20,
                    "b1": result_unbox_2[11]*20,
                    "b2": result_unbox_2[12]*20,
                    "b3": result_unbox_2[13]*20,
                    "b4": result_unbox_2[14]*20
                },
                "c_health_groom": {
                    "C": result_unbox_2[15]*20,
                    "c1": result_unbox_2[16]*20,
                    "c2": result_unbox_2[17]*20,
                    "c3": result_unbox_2[18]*20,
                    "c4": result_unbox_2[19]*20,
                    "c5": result_unbox_2[20]*20,
                    "c6": result_unbox_2[21]*20
                },
                "d_train": {
                    "D": result_unbox_2[22]*20,
                    "d1": result_unbox_2[23]*20,
                    "d2": result_unbox_2[24]*20,
                    "d3": result_unbox_2[25]*20,
                    "d4": result_unbox_2[26]*20,
                    "d5": result_unbox_2[27]*20,
                    "d6": result_unbox_2[28]*20
                },
                "e_exercise": {
                    "E": result_unbox_2[29]*20,
                    "e1": result_unbox_2[30]*20,
                    "e2": result_unbox_2[31]*20,
                    "e3": result_unbox_2[32]*20,
                    "e4": result_unbox_2[33]*20
                }
            }
            dog_info["size"] = result_unbox_2[40]
            dog_info["origin"] = result_unbox_2[41]
            dog_info["usage"] = result_unbox_2[42]
            dog_info["height"] = result_unbox_2[43]
            dog_info["breed_weight"] = result_unbox_2[44]
            dog_info["color"] = result_unbox_2[45]
            dog_info["describe"] = result_unbox_2[46]
            dog_info["trait"] = result_unbox_2[47]

            # print(dog_info["panel_data"])
            return render_template("dog_info.html", dog_info=dog_info)

    # except Exception as e:
    #     print("/find_dog/dog_info ERROR")
    #     print(e)

    finally:
        cursor.close()
        db.close()