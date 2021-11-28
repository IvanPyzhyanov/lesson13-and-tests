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
from flask import Flask
from pathlib import Path
app = Flask(__name__)


@app.route("/enroll",methods=[...])
def form_show():
    # TODO Напишите Ваш код здесь
    pass

@app.route("/enroll",methods=[...])
def form_submit():
    # TODO Напишите Ваш код здесь
    pass


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)  # Эта строка необходима, чтобы правильно искать json хранилища
    app.run()
