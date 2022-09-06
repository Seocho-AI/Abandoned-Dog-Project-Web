from datetime import datetime, timedelta
from flask import Blueprint, jsonify
import pymysql


# ------------------- Connect Flask and PyMySQL ------------------- #


dog_statistics = Blueprint("dog_statistics", __name__,
                           template_folder="templates")
db = pymysql.connect(
    host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com',
    port=3306,
    user='kaist',
    passwd='0916',
    db='abandoned_dog',
    charset="utf8")
cursor = db.cursor()


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
today_year = today[:4]  # 이번년도


# ------------------- STATISTICS API ------------------- #
# Get statistics in home
@dog_statistics.route("/dog_statistics", methods=["GET"])
def get_statistics():
    # Total dog count in current year till today's date
    # select count(*) from dog_list where happenDt between '20220101' and '20220823';
    sql = f"select count(*) from dog_list where happenDt between '{today_year}0101' and '{today}';"
    cursor.execute(sql)
    total_in_year = cursor.fetchall()
    total_in_year = total_in_year[0][0]
    

    # Total dog count (adopted) in current year till today's date
    sql = f"select count(*) from dog_list where happenDt between '{today_year}0101' and '{today}' and processState = '종료(입양)';"
    cursor.execute(sql)
    adopt_in_year = cursor.fetchall()
    adopt_in_year = adopt_in_year[0][0]
    

    # Total dog count (euthanasia) in current year till today's date
    sql = f"select count(*) from dog_list where happenDt between '{today_year}0101' and '{today}' and processState = '종료(안락사)';"
    cursor.execute(sql)
    death_in_year = cursor.fetchall()
    death_in_year = death_in_year[0][0]
    

    # Total dog count (protecting) in current year till today's date
    sql = f"select count(*) from dog_list where happenDt between '{today_year}0101' and '{today}' and processState = '보호중';"
    cursor.execute(sql)
    protect_in_year = cursor.fetchall()
    protect_in_year = protect_in_year[0][0]
    

    # Number of rescued dogs today (yesterday)
    sql = f"select count(*) from dog_list where happenDt = '{today}' and processState = '보호중';"
    cursor.execute(sql)
    rescued_today = cursor.fetchall()
    rescued_today = rescued_today[0][0]
    

    # Calculation
    adopt_in_year = int(round(adopt_in_year/total_in_year, 2)*100)
    death_in_year = int(round(death_in_year/total_in_year, 2)*100)

    return jsonify(rescued_today, adopt_in_year, death_in_year, protect_in_year)
