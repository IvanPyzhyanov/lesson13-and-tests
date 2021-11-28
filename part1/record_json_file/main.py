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
from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/enroll", methods=["POST"])
def enroll():
    # TODO напишите Ваш код здесь
    pass

if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()