# У вас есть файл с данными настроек settings.json, 
# шаблон формы для редактирования лежит в файле settings.html. 
# Допишите представление, которое в ответ на GET-запрос 
# выводит данные из формы в шаблоне settings, 
# а в ответ на POST запрос заменяет данные 
# в файле и выводит форму уже с обновленными данными. 
 

import os
from pathlib import Path
from flask import Flask, render_template, request, json

app = Flask(__name__)


@app.route("/settings", methods=["GET", "POST"])
def update_settings():
     if request.method == "POST":
         name = request.form.get("project_name")
         tagline = request.form.get("project_tagline")
         input_data = {"project_name": name, "project_tagline": tagline}
         with open("settings.json", "w", encoding="UTF-8") as file:
             json.dump(input_data, file, ensure_ascii=False)
         with open("settings.json", "r", encoding="UTF-8") as file:
             data_json = json.load(file)
         return render_template("settings.html", settings=data_json)
     else:
         with open("settings.json", "r", encoding="UTF-8") as file:
            data_json = json.load(file)
         return render_template("settings.html", settings=data_json)


# if __name__ == "__main__":
#     os.chdir(Path(os.path.abspath(__file__)).parent)
app.run()
