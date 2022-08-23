from datetime import datetime, timedelta
from urllib.parse import urlencode, unquote, parse_qsl
import math
from flask import Flask, render_template, jsonify, json
import pymysql
import requests
import schedule
import time

app = Flask(__name__)
db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com', port=3306, user='kaist',
                     passwd='0916', db='abandoned_dog', charset="utf8")
cursor = db.cursor()

# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


today = datetime.today().strftime('%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 어제
today_year = today[:4]  # 이번년도


# ------------------- API 불러와서 DB에 적재 ------------------- #


def API_TO_DB():
    # url 입력
    url = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?"

    # query_string 입력
    query_string = urlencode(
        {
            "serviceKey": unquote("ieHW%2FCmVoKfe3X9EnL2OT8JoMTqCSRxMT9%2FE5Fr4spuLN4s4Hms5ZiIAZm%2BgvmlMkm06BDRPZHKyrNW4Qo%2F%2B2w%3D%3D"),
            "bgnde": "20190101",  # 20000101
            "endde": today,
            "upkind": "417000",  # 417000 = 개
            "kind": "",  # 000114 = 믹스견
            "state": "",  # protect = 보호 / notice = 공고 / null = 전체
            "pageNo": "1",
            "numOfRows": "1000",
            "_type": "json"
        }
    )

    # API 파라미터 딕셔너리 형태 저장
    query_dict = dict(parse_qsl(query_string))

    # 최종 요청 url 생성
    query_url = url + query_string

    # API 호출
    response = requests.get(query_url)

    # 딕셔너리 형태로 변환
    r_dict = json.loads(response.text)

    # 오픈 API 호출 결과 데이터의 개수 확인 및 저장
    num_of_rows = r_dict["response"]["body"]["numOfRows"]

    # 전체 데이터의 개수 확인 및 저장
    tot_cnt = r_dict["response"]["body"]["totalCount"]

    # 총 오픈 API 호출 횟수 계산 및 저장
    loop_cnt = math.ceil(tot_cnt/num_of_rows)

    print(tot_cnt)  # 전체 데이터의 개수 출력

    # open API 호출을 총 오픈 API 호출 횟수만큼 반복 실행
    for i in range(loop_cnt):
        # 페이지 수만큼 pageNo 증가
        query_dict["pageNo"] = i + 1

        # 다시 query_string 업데이트
        query_string = urlencode(query_dict)

        # 최종 요청 url 생성
        query_url = url + query_string

        # API 호출
        response = requests.get(query_url)

        # 딕셔너리 형태로 변환
        r_dict = json.loads(response.text)

        # "dogs" is a list and contains 1000 individual dog info as dict
        dogs = r_dict["response"]["body"]["items"]["item"]

        # iterate through each "dog" in "dogs"
        for dog in dogs:
            # "[개] 강아지 종" -> "강아지 종"
            dog["kindCd"] = dog["kindCd"][4:]

            # noticeNo가 API에서 불러온 dog 딕셔너리에 없을때 (에러 방지)
            if "noticeNo" not in dog.keys():
                dog["noticeNo"] = "없음"
                print(dog["desertionNo"], dog["noticeNo"])

        # API로 불러온 유기견들 DB에 넣기 위해 쿼리 실행
        sql = "REPLACE INTO `dog_list` VALUES (%(desertionNo)s, %(filename)s, %(happenDt)s, %(happenPlace)s, %(kindCd)s, %(colorCd)s, %(age)s, %(weight)s, %(noticeNo)s, %(noticeSdt)s, %(noticeEdt)s, %(popfile)s, %(processState)s, %(sexCd)s, %(neuterYn)s, %(specialMark)s, %(careNm)s, %(careTel)s, %(careAddr)s, %(orgNm)s, %(officetel)s);"
        cursor.executemany(sql, dogs)
        db.commit()
        print(i + 1, "번째", cursor.rowcount, "record inserted.")


# ------------------- 정해진 시간마다 API_TO_DB() 함수 호출 ------------------- #


schedule.every(5).days.do(API_TO_DB)


# ------------------- HOME PAGE FUNCTIONS ------------------- #


@app.route("/")  # Home page
def main_page():
    return render_template("index.html")


@app.route("/statistics", methods=["GET"])  # Get statistics in home
def get_statistics():
    # Total dog count in current year till today's date
    # select count(*) from dog_list where happenDt between '20220101' and '20220823';
    sql = f"select count(*) from dog_list where happenDt between '{today_year}0101' and '{yesterday}';"
    cursor.execute(sql)
    total_in_year = cursor.fetchall()
    total_in_year = total_in_year[0][0]

    # Total dog count (adopted) in current year till today's date
    sql = f"select count(*) from dog_list where happenDt between '{today_year}0101' and '{yesterday}' and processState = '종료(입양)';"
    cursor.execute(sql)
    adopt_in_year = cursor.fetchall()
    adopt_in_year = adopt_in_year[0][0]

    # Total dog count (euthanasia) in current year till today's date
    sql = f"select count(*) from dog_list where happenDt between '{today_year}0101' and '{yesterday}' and processState = '종료(안락사)';"
    cursor.execute(sql)
    death_in_year = cursor.fetchall()
    death_in_year = death_in_year[0][0]

    # Total dog count (protecting) in current year till today's date
    sql = f"select count(*) from dog_list where happenDt between '{today_year}0101' and '{yesterday}' and processState = '보호중';"
    cursor.execute(sql)
    protect_in_year = cursor.fetchall()
    protect_in_year = protect_in_year[0][0]

    # Number of rescued dogs today (yesterday)
    sql = f"select count(*) from dog_list where happenDt = '{yesterday}' and processState = '보호중';"
    cursor.execute(sql)
    rescued_today = cursor.fetchall()
    rescued_today = rescued_today[0][0]

    # Calculation
    adopt_in_year = int(round(adopt_in_year/total_in_year, 2)*100)
    death_in_year = int(round(death_in_year/total_in_year, 2)*100)

    return [rescued_today, adopt_in_year, death_in_year, protect_in_year]


# ------------------- FIND DOG PAGE FUNCTIONS ------------------- #


@app.route("/abandoned-dogs")  # Find dog page
def abandoned_dog_page():
    return render_template("find_dog.html")


@app.route("/abandoned-dogs/list", methods=["GET"])
def abandoned_dog_list():
    sql = "select breed_no, breed_name_kr from breed_info order by breed_name_kr asc;"
    cursor.execute(sql)
    result = cursor.fetchall()

    dog_list = []
    for dog_info in result:
        dog_dict = {
            "breed_no": dog_info[0],
            "breed_name_kr": dog_info[1]
        }
        dog_list.append(dog_dict)

    return jsonify(dog_list)


# ------------------- SURVEY PAGE FUNCTIONS ------------------- #


@app.route("/survey")  # Survey page
def survey_page():
    return render_template("survey.html")


@app.route("/survey", methods=["POST"])  # Posing survey result
def survey_answer():
    # answer_receive = request.get_json()  # Stores user's survey answer

    # Afghan Hound / Affenpinscher
    sql = "select * from breed_info where breed_name = 'Afghan Hound';"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = result[0]  # Tuple unboxing

    info_dict = {
        "breed_name": result[0],
        "breed_name_kr": result[1],
        "dog_info_json": json.loads(result[2])
    }

    # for question_type, rating in answer_receive.items():
    #     print(question_type, ":", rating)

    return info_dict  # Returning dog info from DB


# ------------------- DEBUG MAIN ------------------- #
if __name__ == "__main__":
    app.run(debug=True)
