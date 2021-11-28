# У вас есть список путешествий в файле tours, 
# верните список подходящих туров.
# Подходящим считается тут, название которого
# начинается с поисковой строки, без учета регистра.
# 
# Для поиска названия используйте query-параметр `search`
#
# Если поисковая строка не задана или пустая, возвращается 
# полный список. Помните, что ответ возвращается 
# в формате json и оборачивается в jsonify.
#
# Пример запроса без параметра:
# /tours
#
# Пример запроса с параметром:
# /tours?search=бо

import os
from pathlib import Path
from flask import Flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/tours", methods=["GET"])
def get_tours():
    # TODO напишите Ваш код здесь
    pass


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()
