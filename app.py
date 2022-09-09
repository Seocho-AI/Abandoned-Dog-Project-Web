from datetime import datetime, timedelta
from flask import Flask, render_template
import pymysql
# from api_to_db import db_insert_dog, db_update_dog
from blueprints.dog_statistics import dog_statistics
from blueprints.find_dog import find_dog
from blueprints.dog_posts import dog_posts
from blueprints.filter_search import filter_search
from blueprints.survey import survey


# ------------------- Flask Blueprint ------------------- #


app = Flask(__name__)
app.register_blueprint(dog_statistics, url_prefix="/")
app.register_blueprint(find_dog, url_prefix="/find_dog")
app.register_blueprint(dog_posts, url_prefix="/find_dog")
app.register_blueprint(filter_search, url_prefix="/find_dog")
app.register_blueprint(survey, url_prefix="/survey")


# ------------------- GETTING TODAY'S YEAR/MONTH/DATE ------------------- #


today = datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')  # 오늘
yesterday = datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d')  # 어제
two_weeks_before = datetime.strftime(
    datetime.now() - timedelta(14), '%Y%m%d')  # 2주전
sixty_days_before = datetime.strftime(
    datetime.now() - timedelta(60), '%Y%m%d')  # 60일전
today_year = today[:4]  # 이번년도


# ------------------- HOME PAGE API ------------------- #


@app.route("/")  # Home page
def main_page():
    return render_template("index.html",)


# ------------------- 정해진 시간마다 API_TO_DB() 함수 호출 ------------------- #


# DB 삽입 함수 호출
# db_insert_dog()

# DB 업데이트 함수 호출
# db_update_dog()


# ------------------- DEBUG MAIN ------------------- #


if __name__ == "__main__":
    app.run(debug=True)
