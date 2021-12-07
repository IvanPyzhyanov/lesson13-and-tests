# У вас есть папка uploads, приложение main.py
# и шаблон index.html

# Допишите два представления:

# Первое показывает форму загрузки файла
# Второе загружает файл  в папку "uploads" под любым
# именем и возвращает текст "Файл загружен"

# 

# import os
# from pathlib import Path
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def upload_page():
    return render_template("form.html")

@app.route('/uploads', methods=["POST"])
def upload_file():
    f = request.files['the_file']
    f.save("uploads/filename")
    return "Файл загружен"

app.run()

# if __name__ == "__main__":
#     os.chdir(Path(os.path.abspath(__file__)).parent)

