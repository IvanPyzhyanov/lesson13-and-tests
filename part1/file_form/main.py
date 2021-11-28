# У вас есть папка uploads, приложение main.py 
# и шаблон index.html

# Допишите два представления:

# Первое показывает форму загрузки файла
# Второе загружает файл  в папку "uploads" под любым 
# именем и возвращает текст "Файл загружен"

# 

import os
from flask import Flask
from pathlib import Path
app = Flask(__name__)

@app.route('/', methods=["GET"])
def upload_page():
    # TODO напишите Ваш код здесь
    pass

@app.route('/upload', methods=['POST'])
def upload_file():
    # TODO напишите Ваш код здесь
    pass


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()
