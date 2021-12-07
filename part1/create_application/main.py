# У вас есть форма с полями имя, телефон, почта 
# и есть json файл enrollments.json, 
#
# Напишите 2 view-функции:
# При GET-запросе показываем форму
# При POST запросе на адрес /enroll добавляем объект в json-файл
# После добавления условия необходимо выводить на страницу надпись 
# `Данные записаны`
#
#
import os
from flask import Flask, request, render_template
import json
from pathlib import Path

app = Flask(__name__)


@app.route("/enroll", methods=['GET'])
def form_show():
    return render_template('index.html')

@app.route("/enroll", methods=['POST'])
def form_submit():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    input_data = {"name": name, "email": email, "phone": phone}
    with open("enrollments.json", 'r', encoding="UTF-8") as file:
        save_data = json.load(file)
        save_data.append(input_data)
    with open("enrollments.json", 'w', encoding="UTF-8") as file:
        json.dump(save_data, file, ensure_ascii=False)
    return "Данные записаны"


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)  # Эта строка необходима, чтобы правильно искать json хранилища
    app.run()
