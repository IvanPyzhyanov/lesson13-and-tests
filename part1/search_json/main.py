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

# import os
# from pathlib import Path
from flask import Flask, json, request, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/tours", methods=["GET"])
def get_tours():
    with open("tours.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    s = request.args.get("search")
    if s:
        match_data = [base for base in data if s.lower() in base["title"].lower()]
        return jsonify(match_data)
    return jsonify(data)

app.run()
# if __name__ == "__main__":
#     os.chdir(Path(os.path.abspath(__file__)).parent)

