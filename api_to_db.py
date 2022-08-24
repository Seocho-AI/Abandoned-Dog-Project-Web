from datetime import datetime, timedelta
from urllib.parse import urlencode, unquote, parse_qsl
import math
import threading
import json
import pymysql
import requests


db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com', port=3306, user='kaist',
                     passwd='0916', db='abandoned_dog', charset="utf8")
cursor = db.cursor()


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
today_year = today[:4]  # 이번년도


# ------------------- API 불러와서 DB에 수정/삽입 ------------------- #


# url 입력
url = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?"


# API에서 오늘 유기견 정보 삽입
def db_insert_dog():
    # query_string 입력
    query_string = urlencode(
        {
            "serviceKey": unquote("ieHW%2FCmVoKfe3X9EnL2OT8JoMTqCSRxMT9%2FE5Fr4spuLN4s4Hms5ZiIAZm%2BgvmlMkm06BDRPZHKyrNW4Qo%2F%2B2w%3D%3D"),
            "bgnde": today,  # 20190101
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

    # 삽입 전용 API 파라미터
    # query_dict["bgnde"] = today
    # query_dict["endde"] = today

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
        sql = "REPLACE INTO dog_list(desertionNo, filename, happenDt, happenPlace, kindCd, colorCd, age, weight, noticeNo, noticeSdt, noticeEdt, popfile, processState, sexCd, neuterYn, specialMark, careNm, careTel, careAddr, orgNm, officetel) VALUES (%(desertionNo)s, %(filename)s, %(happenDt)s, %(happenPlace)s, %(kindCd)s, %(colorCd)s, %(age)s, %(weight)s, %(noticeNo)s, %(noticeSdt)s, %(noticeEdt)s, %(popfile)s, %(processState)s, %(sexCd)s, %(neuterYn)s, %(specialMark)s, %(careNm)s, %(careTel)s, %(careAddr)s, %(orgNm)s, %(officetel)s);"
        cursor.executemany(sql, dogs)
        db.commit()
        print(i + 1, "번째", cursor.rowcount, "record inserted.")

    # 1시간 마다 함수 반복
    threading.Timer(3600, db_insert_dog).start()


# API에서 20190101 ~ 어제 날짜 유기견 정보 업데이트
def db_update_dog():
    # query_string 입력
    query_string = urlencode(
        {
            "serviceKey": unquote("ieHW%2FCmVoKfe3X9EnL2OT8JoMTqCSRxMT9%2FE5Fr4spuLN4s4Hms5ZiIAZm%2BgvmlMkm06BDRPZHKyrNW4Qo%2F%2B2w%3D%3D"),
            "bgnde": "20190101",  # 20190101
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

        # API로 불러온 유기견들 DB에 넣기 위해 쿼리 실행
        sql = "UPDATE dog_list SET noticeSdt = %(noticeSdt)s, noticeEdt = %(noticeEdt)s, popfile = %(popfile)s, processState = %(processState)s WHERE desertionNo = %(desertionNo)s;"
        cursor.executemany(sql, dogs)
        db.commit()
        print(i + 1, "번째", cursor.rowcount, "record updated.")

    # 24시간 마다 함수 반복
    threading.Timer(86400, db_update_dog).start()