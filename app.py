from flask import Flask, render_template, request, jsonify, json
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='abandoned-dogs.cdlurfzj5gl4.ap-northeast-2.rds.amazonaws.com', port=3306, user='wdragj',
                     passwd='dydwnstj71507350', db='test_database', charset="utf8")
cursor = db.cursor()


@app.route("/")  # Home page
def main_page():
    return render_template("index.html")


@app.route("/abandoned-dogs")  # Find dog page
def abandoned_dog_page():
    return render_template("dog_find.html")


@app.route("/abandoned-dogs/list", methods=["GET"])
def abandoned_dog_list():
    sql = "select * from dog_info order by breed_name_kr asc;"
    cursor.execute(sql)
    result = cursor.fetchall()

    dog_list = []
    for dog_info in result:
        dog_dict = {
            "breed_no": dog_info[0],
            "breed_name": dog_info[1],
            "breed_name_kr": dog_info[2],
            "dog_json": dog_info[3]
        }
        dog_list.append(dog_dict)

    return jsonify(dog_list)


@app.route("/survey")  # Survey page
def survey_page():
    return render_template("survey.html")


@app.route("/survey", methods=["POST"])  # Posing survey result
def survey_answer():
    # answer_receive = request.get_json()  # Stores user's survey answer

    # Afghan Hound / Affenpinscher
    sql = "select * from dog_info where dog_breed = 'Afghan Hound';"
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


if __name__ == "__main__":
    app.run(debug=True)
