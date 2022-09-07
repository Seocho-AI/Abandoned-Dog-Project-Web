from datetime import datetime, timedelta
from flask import Blueprint, render_template, jsonify, request
import pymysql
import json


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


@find_dog.route("/filter/breed", methods=["GET"])  # Load filters
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


@find_dog.route("/filter/city", methods=["GET"])  # Load filters
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


# Retreive dog info based on received desertion No
@find_dog.route("/dog_info", methods=["GET"])
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
                print(mix_predict)
                print(type(mix_predict))
            else:
                sql2 = f"SELECT * FROM breed_info WHERE breed_name_kr = '{breed}';"
                cursor.execute(sql2)
                result2 = cursor.fetchall()
                result_unbox2 = result2[0]

                dog_info["size"] = result_unbox2[3]
                dog_info["origin"] = result_unbox2[4]
                dog_info["usage"] = result_unbox2[5]
                dog_info["height"] = result_unbox2[6]
                dog_info["breed_weight"] = result_unbox2[7]
                dog_info["color"] = result_unbox2[8]
                dog_info["describe"] = result_unbox2[9]

            return render_template("dog_info.html", dog_info=dog_info)

    except Exception as e:
        print("/find_dog/dog_info ERROR")
        print(e)

    finally:
        cursor.close()
        db.close()