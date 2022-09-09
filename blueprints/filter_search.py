from datetime import datetime, timedelta
from flask import Blueprint, render_template, jsonify, request
import pymysql
import json
import ast


# ------------------- Flask Blueprint ------------------- #


filter_search = Blueprint("filter_search", __name__, template_folder="templates")


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


real_today = datetime.strftime(datetime.now(), '%Y%m%d')  # 진짜 오늘
today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
three_month = datetime.strftime(
    datetime.now() - timedelta(90), '%Y%m%d')  # 최근 3개월
today_year = today[:4]  # 이번년도


# ------------------- FILTER SEARCH API ------------------- #


@filter_search.route("/filter/breed", methods=["GET"])  # Load filters
def load_filter_breed():
    try:
        db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
                     port=3306, user='kaist', passwd='0916', db='abandoned_dog', charset="utf8")
        cursor = db.cursor()
        # Fetching filter(breed)
        sql_breed = "SELECT DISTINCT(kindCd) FROM dog_list WHERE processState = '보호중' ORDER BY kindCd ASC;"
        cursor.execute(sql_breed)
        result_breed = cursor.fetchall()
        # print(result_breed[0])
        # breed_list = []
        # for breeds in result_breed:
        #     print(breeds[0])
        #     result_breed_dict = {}
        #     breed = breed_count[0]
        #     count = breed_count[1]
        #     result_breed_dict["breed"] = breed
        #     result_breed_dict["count"] = count
        #     breed_list.append(result_breed_dict)

        return jsonify(result_breed)

    except Exception as e:
        print("find_dog/filter/breed ERROR")
        print(e)

    finally:
        cursor.close()
        db.close()


@filter_search.route("/filter/city", methods=["GET"])  # Load filters
def load_filter_city():
    try:
        db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
                        port=3306, user='kaist', passwd='0916', db='abandoned_dog', charset="utf8")
        cursor = db.cursor()

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

        return jsonify(result_region_dict)

    except Exception as e:
        print("/find_dog/filter/city ERROR")
        print(e)

    finally:
        cursor.close()
        db.close()