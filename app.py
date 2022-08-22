from flask import Flask, render_template, request, jsonify, json
from datetime import datetime
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com', port=3306, user='wdragj',
                     passwd='dydwnstj71507350', db='abandoned_dog', charset="utf8")
cursor = db.cursor()


today = datetime.today().strftime('%Y%m%d')
todayYear = today[:4]

# ------------------- HOME PAGE FUNCTIONS ------------------- #


@app.route("/")  # Home page
def main_page():
    return render_template("index.html")


@app.route("/", methods=["GET"])  # Get statistics to home
def get_statistics():
    sql = f"select count(*) from dog_list where happenDt >= '{todayYear}0101';"
    print(sql)
    return

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
