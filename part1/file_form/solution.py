import os
from flask import Flask, render_template, request
from pathlib import Path
app = Flask(__name__)

@app.route('/', methods=["GET"])
def upload_page():
    return render_template("form.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['thefile']
    path = Path(os.path.abspath(__file__)).parent
    file.save(path.joinpath("uploads", file.filename))
    return "Файл загружен"


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()


# <!doctype html>
# <html lang="ru">
# <head>
#     <meta charset="UTF-8">
#     <title>Document</title>
# </head>
# <body>
# <h1>Категория</h1>
# <form action="/tours" method="get">
#    <input type="text" name="category">
#    <input type="submit" value="Найти">
# </form>
# <ul>
#   {% for tour in tours_match %}
#       <li>{{ tour.title }}</li>
#   {% endfor %}
# </ul>
# </body>
# </html>