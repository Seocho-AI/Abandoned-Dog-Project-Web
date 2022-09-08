from datetime import datetime, timedelta
from flask import Blueprint, render_template, jsonify, request
import pymysql
import json
import ast


# ------------------- Flask Blueprint ------------------- #


find_dog = Blueprint("find_dog", __name__, template_folder="templates")


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


real_today = datetime.strftime(datetime.now(), '%Y%m%d')  # 진짜 오늘
today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
three_month = datetime.strftime(
    datetime.now() - timedelta(90), '%Y%m%d')  # 최근 3개월
today_year = today[:4]  # 이번년도


# ------------------- FIND DOG PAGE API ------------------- #


@find_dog.route("/", methods=["GET"])  # Find dog page
def find_dog_page():
    try:
        db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
                     port=3306, user='kaist', passwd='0916', db='abandoned_dog', charset="utf8")
        cursor = db.cursor()

        ds_select = request.args.get('ds')
        de_select = request.args.get('de')
        state_select = request.args.get('state')
        city_select = request.args.get('city')
        region_select = f"{state_select} {city_select}"
        breed_select = request.args.get('breed')

        # print(breed_select)

        ds_select = "".join(ds_select.split("-"))
        de_select = "".join(de_select.split("-"))

        sql_start = f"SELECT popfile, kindCd, sexCd, happenDt, noticeNo, processState, desertionNo FROM dog_list WHERE processState = '보호중' AND happenDt BETWEEN '{ds_select}' AND '{de_select}' "
        sql_end = "ORDER BY happenDt DESC;"

        if state_select == "전체": # 시군구: 전체 / 도시: 전체
            if breed_select == "전체": # 종: 전체
                sql = sql_start + sql_end
            else: # 종: 선택
                sql = sql_start + f"AND kindCd = '{breed_select}' " + sql_end
        else: # 시군구: 선택
            if city_select == "전체": # 도시: 전체
                if breed_select == "전체": # 종: 전체
                    sql = sql_start + \
                        f"AND orgNm LIKE '%{state_select}%' " + sql_end
                else: # 종: 선택
                    sql = sql_start + \
                        f"AND kindCd = '{breed_select}' AND orgNm LIKE '%{state_select}%' " + sql_end
            else: # 도시: 선택
                if breed_select == "전체": # 종: 전체
                    sql = sql_start + \
                        f"AND orgNm LIKE '%{region_select}%' " + sql_end
                else: # 종: 선택
                    sql = sql_start + \
                        f"AND kindCd = '{breed_select}' AND orgNm LIKE '%{region_select}%' " + sql_end

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

        # print(dog_list[0])
        # return jsonify(dog_list)
        # return render_template("find_dog.html", response=json.dumps(dog_list))
        return render_template("find_dog.html", response=json.dumps(dog_list))

    except Exception as e:
        print("/find_dog ERROR")
        print(e)

    finally:
        cursor.close()
        db.close()