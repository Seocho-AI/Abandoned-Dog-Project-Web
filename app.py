from flask import Flask, render_template, request, jsonify, json
import pymysql
import pprint
import requests

app = Flask(__name__)
db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com', port=3306, user='wdragj',
                     passwd='dydwnstj71507350', db='abandoned_dog', charset="utf8")
cursor = db.cursor()


encode = "ieHW%2FCmVoKfe3X9EnL2OT8JoMTqCSRxMT9%2FE5Fr4spuLN4s4Hms5ZiIAZm%2BgvmlMkm06BDRPZHKyrNW4Qo%2F%2B2w%3D%3D"  # 인증키
url = 'http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?bgnde=20211201&endde=20211231&upkind=417000&pageNo=1&numOfRows=1000&_type=json&serviceKey={}'.format(
    encode)
response = request.get(url)

# 데이터 값 출력해보기
contents = response.text

# 데이터 결과값 예쁘게 출력해주는 코드
pp = pprint.PrettyPrinter(indent=4)
print(pp.pprint(contents))

# ------------------- HOME PAGE FUNCTIONS ------------------- #


@app.route("/")  # Home page
def main_page():
    return render_template("index.html")

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
    sql = "select * from breed_info where dog_breed = 'Afghan Hound';"
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
