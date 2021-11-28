# У вас есть список путешествий в файле tours.json
# по GET-запросу на адрес /tours верните данные в формате json

 

import os
from pathlib import Path
from flask import Flask, jsonify
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/tours", methods=["GET"])
def get_tours():
    # TODO Напишите Ваш код здесь
    pass


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()
