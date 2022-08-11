from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost', port=3306, user='root',
                     passwd='WdragJ1003?', db='seocho_abandoned_dog', charset="utf8")
cursor = db.cursor()


@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")


@app.route("/survey", methods=["POST"])
def survey_answer():
    answer_receive = request.get_json()
    print(type(answer_receive))
    # print(answer)
    return "Answer received"


if __name__ == "__main__":
    app.run(debug=True)
