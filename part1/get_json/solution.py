import os
from pathlib import Path
from flask import Flask, jsonify
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/tours", methods=["GET"])
def get_tours():
     with open('tours.json', 'r')as f:
          tours = json.load(f)
     return jsonify(tours)


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()
