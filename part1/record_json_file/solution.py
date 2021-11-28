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
import os
from pathlib import Path
from flask import Flask, request
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/enroll", methods=["POST"])
def enroll():
    name, email, phone = request.json.get("name"), request.json.get("email"), request.json.get("phone")
    with open("enrollments.json","r") as f:
        content = json.load(f)
    with open("enrollments.json", "w") as f:
        content.append({"name": name, "email": email,"phone": phone})
        json.dump(content, f, ensure_ascii=False, indent=4)
    return "", 200

if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()