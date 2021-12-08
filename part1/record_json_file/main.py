# У вас есть файл enrollments.json, 
# куда вы записываете запросы студентов.
# В данном Вам необходимо создать view-функцию которая:
# При POST-запросе на адрес /tours получает данные о студенте
# и сохраняет их в файле enrollments.json для дальнейшего использования.
#
# Сейчас в файле enrollments.json имеется одна запись необходимо сделать так,
# Чтобы после добавления второй записи первая не исчезда
#
# Данные для POST-запроса Вы можете придумать любые, важно лишь то,
# чтобы были заполнены поля "name", "email", "phone"
#
# import os
# from pathlib import Path
from flask import Flask, json, jsonify, request, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/enroll", methods=['GET'])
def form_show():
    return render_template('index.html')

@app.route("/enroll", methods=["POST"])
def enroll():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    input_data = {"name": name, "email": email, "phone": phone}
    with open("enrollments.json", 'r', encoding="UTF-8") as file:
        save_data = json.load(file)
        save_data.append(input_data)
    with open("enrollments.json", 'w', encoding="UTF-8") as file:
        json.dump(save_data, file, ensure_ascii=False)
    return render_template("index.html")

app.run()
# if __name__ == "__main__":
#     os.chdir(Path(os.path.abspath(__file__)).parent)
