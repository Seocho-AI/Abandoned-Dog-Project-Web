from datetime import datetime, timedelta
from flask import Blueprint, render_template, jsonify, request
import pymysql
import json
import ast
import copy


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


@find_dog.route("/", methods=["GET", "POST"])  # Find dog page
def find_dog_page():
    try:
        db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
                             port=3306, user='kaist', passwd='0916', db='abandoned_dog', charset="utf8")
        cursor = db.cursor()

        survey = request.args.get('survey')

        if survey == "false":
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

            if state_select == "전체":  # 시군구: 전체 / 도시: 전체
                if breed_select == "전체":  # 종: 전체
                    sql = sql_start + sql_end
                else:  # 종: 선택
                    sql = sql_start + f"AND kindCd = '{breed_select}' " + sql_end
            else:  # 시군구: 선택
                if city_select == "전체":  # 도시: 전체
                    if breed_select == "전체":  # 종: 전체
                        sql = sql_start + \
                            f"AND orgNm LIKE '%{state_select}%' " + sql_end
                    else:  # 종: 선택
                        sql = sql_start + \
                            f"AND kindCd = '{breed_select}' AND orgNm LIKE '%{state_select}%' " + sql_end
                else:  # 도시: 선택
                    if breed_select == "전체":  # 종: 전체
                        sql = sql_start + \
                            f"AND orgNm LIKE '%{region_select}%' " + sql_end
                    else:  # 종: 선택
                        sql = sql_start + \
                            f"AND kindCd = '{breed_select}' AND orgNm LIKE '%{region_select}%' " + sql_end

        elif survey == "true":
            rec_list = request.args.get('rec_list') # Ranking list (desertionNo)
            rec_list_field = copy.deepcopy(rec_list)

            rec_list = ast.literal_eval(rec_list)
            rec_list = tuple(rec_list)
            
            rec_list_field = "(desertionNo, " + rec_list_field[1:-1] + ")"
            
            sql = f"SELECT popfile, kindCd, sexCd, happenDt, noticeNo, processState, desertionNo FROM dog_list WHERE desertionNo in {rec_list} ORDER BY FIELD{rec_list_field};"

            # Ranking list (percentage)
            rec_list_score = request.args.get('rec_list_score')
            rec_list_score = rec_list_score[1:-1]
            rec_list_score = rec_list_score.split(", ")
            for i, scores in enumerate(rec_list_score):
                scores = float(scores)
                scores = "{:.2%}".format(scores)
                rec_list_score[i] = scores
            
            # if request.method == 'POST':
            #     tot_trait_score_diff = request.json
            #     print(tot_trait_score_diff)
            #     print(type(tot_trait_score_diff))
            #     # tot_trait_score_diff = ast.literal_eval(tot_trait_score_diff)
            # else:
            tot_trait_score_diff = request.args.get('tot_trait_score_diff')
            # tot_trait_score_diff = tot_trait_score_diff.replace("'", "\"")
            tot_trait_score_diff = ast.literal_eval(tot_trait_score_diff)
            # print(tot_trait_score_diff)
            # print(type(tot_trait_score_diff))

        cursor.execute(sql)
        result = cursor.fetchall()

        # print(result)

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
            if survey == "true":
                dog_dict["rec_list_score"] = rec_list_score
                dog_dict["trait_score_diff"] = json.dumps(tot_trait_score_diff[dog_info[6]])
            dog_list.append(dog_dict)

        # print(dog_list[0])
        # return jsonify(dog_list)
        # return render_template("find_dog.html", response=json.dumps(dog_list))
        return render_template("find_dog.html", response=json.dumps(dog_list))

    # except Exception as e:
    #     print("/find_dog ERROR")
    #     print(e)

    finally:
        cursor.close()
        db.close()
