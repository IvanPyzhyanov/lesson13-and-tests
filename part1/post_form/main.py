# У вас есть файл с данными настроек settings.json, 
# шаблон формы для редактирования лежит в файле settings.html. 
# Допишите представление, которое в ответ на GET-запрос 
# выводит данные из формы в шаблоне settings, 
# а в ответ на POST запрос заменяет данные 
# в файле и выводит форму уже с обновленными данными. 
 

import os
from pathlib import Path
from flask import Flask

app = Flask(__name__)


@app.route("/settings", methods=["GET", "POST"])
def update_settings():
     # TODO Напишите Ваш код здесь
     pass

if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()
