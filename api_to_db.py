from datetime import datetime, timedelta
from urllib.parse import urlencode, unquote, parse_qsl
import math
import threading
import json
import time
import pymysql
import requests


# ------------------- Connect PyMySQL ------------------- #


db = pymysql.connect(
    host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='kaist',
    passwd='0916',
    db='abandoned_dog',
    charset="utf8")
cursor = db.cursor()


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 어제
yesterday = datetime.strftime(
    datetime.now() - timedelta(2), '%Y%m%d')  # 어제 - 1
two_weeks_before = datetime.strftime(
    datetime.now() - timedelta(14), '%Y%m%d')  # 2주전
sixty_days_before = datetime.strftime(
    datetime.now() - timedelta(60), '%Y%m%d')  # 60일전
today_year = today[:4]  # 이번년도


# ------------------- API 불러와서 DB에 수정/삽입 ------------------- #


# 기타 품종들을 믹스견으로 바꾸기 위한 리스트
breed_names = ['골든 리트리버', '그레이 하운드', '그레이트 덴', '그레이트 피레니즈', '꼬똥 드 뚤레아', '네오폴리탄 마스티프', '노르포크 테리어', '노리치 테리어', '노퍽 테리어', '뉴펀들랜드', '닥스훈트', '달마시안', '댄디 딘몬트 테리어', '도고 까니리오', '도고 아르젠티노', '도고 아르젠티노', '도베르만', '도사', '동경견', '라브라도 리트리버', '라사 압소', '라이카', '래빗 닥스훈드', '랫 테리어', '레이크랜드 테리어', '로디지안 리즈백 ', '로트와일러', '로트와일러', '마리노이즈', '마스티프', '말라뮤트', '말티즈', '맨체스터테리어', '미니어쳐 닥스훈트', '미니어쳐 불 테리어', '미니어쳐 슈나우저', '미니어쳐 푸들', '미니어쳐 핀셔', '미디엄 푸들', '미텔 스피츠', '믹스견', '바센지', '바셋 하운드', '버니즈 마운틴 독', '베들링턴 테리어', '벨기에 그로넨달', '벨기에 쉽독', '벨기에 테뷰런', '벨지안 셰퍼드 독', '보더 콜리', '보르조이', '보스턴 테리어', '복서', '볼로네즈', '부비에 데 플랑드르', '불 테리어', '불독', '브뤼셀그리펀', '브리타니 스파니엘', '블랙 테리어', '비글', '비숑 프리제', '비어디드 콜리', '비즐라', '빠삐용', '사모예드', '살루키', '삽살개', '샤페이', '세인트 버나드', '센트럴 아시안 오브차카', '셔틀랜드 쉽독', '셰퍼드', '슈나우져', '스코티쉬 테리어', '스코티시 디어하운드', '스태퍼드셔 불 테리어', '스탠다드 푸들', '스피츠', '시바', '시베리안 허스키', '시베리안라이카', '시잉프랑세즈', '시츄', '시코쿠', '실리햄 테리어', '실키테리어', '아나톨리안 셰퍼드', '아메리칸 불독', '아메리칸 스태퍼드셔 테리어', '아메리칸 아키다', '아메리칸 에스키모', '아메리칸 코카 스파니엘',
               '아메리칸 핏불 테리어', '아메리칸불리', '아이리쉬 레드 앤 화이트 세터', '아이리쉬 세터', '아이리쉬 울프 하운드', '아이리쉬소프트코튼휘튼테리어', '아키다', '아프간 하운드', '알라스칸 말라뮤트', '에어델 테리어', '오브차카', '오스트랄리안 셰퍼드 독', '오스트랄리안 캐틀 독', '올드 잉글리쉬 불독', '올드 잉글리쉬 쉽독', '와이마라너', '와이어 폭스 테리어', '요크셔 테리어', '울프독', '웨스트 시베리언 라이카', '웨스트하이랜드화이트테리어', '웰시 코기 카디건', '웰시 코기 펨브로크', '웰시 테리어', '이탈리안 그레이 하운드', '잉글리쉬 세터', '잉글리쉬 스프링거 스파니엘', '잉글리쉬 코카 스파니엘', '잉글리쉬 포인터', '자이언트 슈나우져', '재패니즈 스피츠', '잭 러셀 테리어', '저먼 셰퍼드 독', '저먼 와이어헤어드 포인터', '저먼 포인터', '저먼 헌팅 테리어', '제주개', '제페니즈칭', '진도견', '차우차우', '차이니즈 크레스티드 독', '치와와', '카레리안 베어독', '카이훗', '캐벌리어 킹 찰스 스파니엘', '케니스펜더', '케리 블루 테리어', '케언 테리어', '케인 코르소', '코리아 트라이 하운드', '코리안 마스티프', '코카 스파니엘', '코카 푸', '코카시안오브차카', '콜리', '클라인스피츠', '키슈', '키스 훈드', '토이 맨체 스터 테리어', '토이 푸들', '티베탄 마스티프', '파라오 하운드', '파슨 러셀 테리어', '팔렌', '퍼그', '페키니즈', '페터데일테리어', '포메라니안', '포인터', '폭스테리어', '푸들', '풀리', '풍산견', '프레사까나리오', '프렌치 불독', '프렌치 브리타니', '플랫 코티드 리트리버', '플롯하운드', '피레니안 마운틴 독', '필라 브라질레이로', '핏불테리어', '허 배너스', '화이트리트리버', '화이트테리어', '휘펫']


# url 입력
url = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?"


# ------------------- API에서 새로 들어온 유기견 DB에 수정/삽입 ------------------- #
def db_insert_dog():
    # 시간 측정 시작
    start = time.time()

    # query_string 입력
    query_string = urlencode(
        {
            "serviceKey": unquote("ieHW%2FCmVoKfe3X9EnL2OT8JoMTqCSRxMT9%2FE5Fr4spuLN4s4Hms5ZiIAZm%2BgvmlMkm06BDRPZHKyrNW4Qo%2F%2B2w%3D%3D"),
            "bgnde": sixty_days_before,  # 20190101
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

            # 기타 품종들 믹스견으로 바꾸기
            if dog["kindCd"] not in breed_names:
                dog["kindCd"] = "믹스견"

            # noticeNo가 API에서 불러온 dog 딕셔너리에 없을때 (에러 방지)
            if "noticeNo" not in dog.keys():
                dog["noticeNo"] = "없음"
                print(dog["desertionNo"], dog["noticeNo"])

        # API로 불러온 유기견들 DB에 넣기 위해 쿼리 실행
        sql = "INSERT IGNORE INTO dog_list(desertionNo, filename, happenDt, happenPlace, kindCd, colorCd, age, weight, noticeNo, noticeSdt, noticeEdt, popfile, processState, sexCd, neuterYn, specialMark, careNm, careTel, careAddr, orgNm, officetel) VALUES (%(desertionNo)s, %(filename)s, %(happenDt)s, %(happenPlace)s, %(kindCd)s, %(colorCd)s, %(age)s, %(weight)s, %(noticeNo)s, %(noticeSdt)s, %(noticeEdt)s, %(popfile)s, %(processState)s, %(sexCd)s, %(neuterYn)s, %(specialMark)s, %(careNm)s, %(careTel)s, %(careAddr)s, %(orgNm)s, %(officetel)s);"
        cursor.executemany(sql, dogs)
        db.commit()
        print(i + 1, "번째 :", cursor.rowcount, "records inserted.")

    # 시간 측정 끝
    end = time.time()
    sec = (end - start)
    result_list = str(timedelta(seconds=sec)).split(".")
    print(f"{result_list[0]} : {end - start:.2f} sec")

    # 1시간 마다 함수 반복
    threading.Timer(3600, db_insert_dog).start()


# ------------------- API에서 20190101 ~ 어제 날짜 유기견 정보 업데이트 ------------------- #
def db_update_dog():
    # 시간 측정 시작
    start = time.time()

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

        # iterate through each "dog" in "dogs"
        for dog in dogs:
            # "[개] 강아지 종" -> "강아지 종"
            dog["kindCd"] = dog["kindCd"][4:]

            # 기타 품종들 믹스견으로 바꾸기
            if dog["kindCd"] not in breed_names:
                dog["kindCd"] = "믹스견"

        # API로 불러온 유기견들 DB에 넣기 위해 쿼리 실행
        sql = "UPDATE dog_list SET kindCd = %(kindCd)s, noticeSdt = %(noticeSdt)s, noticeEdt = %(noticeEdt)s, popfile = %(popfile)s, processState = %(processState)s WHERE desertionNo = %(desertionNo)s;"
        cursor.executemany(sql, dogs)
        db.commit()
        print(i + 1, "번째 :", cursor.rowcount, "records updated.")

    # 시간 측정 끝
    end = time.time()
    sec = (end - start)
    result_list = str(timedelta(seconds=sec)).split(".")
    print(f"{result_list[0]} : {end - start:.2f} sec")

    # 24시간 마다 함수 반복
    threading.Timer(86400, db_update_dog).start()
