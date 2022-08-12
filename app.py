from flask import Flask, render_template, request, jsonify, json
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com', port=3306, user='wdragj',
                     passwd='dydwnstj71507350', db='test_database', charset="utf8")
cursor = db.cursor()


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/survey")
def survey_result():
    return render_template("survey-result.html")


@app.route("/survey", methods=["POST"])
def survey_answer():
    # answer_receive = request.get_json()  # Stores user's survey answer

    sql = "select * from dog_info where dog_breed = 'Afghan Hound';" # Afghan Hound / Affenpinscher
    cursor.execute(sql)
    result = cursor.fetchall()
    result = result[0]  # Tuple unboxing

    info_dict = {
        "dog_breed": result[0],
        "dog_breed_kr": result[1],
        "dog_info_json": json.loads(result[2])
    }

    # for question_type, rating in answer_receive.items():
    #     print(question_type, ":", rating)

    return info_dict


if __name__ == "__main__":
    app.run(debug=True)
