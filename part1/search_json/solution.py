import os
from pathlib import Path
from flask import Flask, jsonify, request
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/tours")
def page_index():
     with open('tours.json', 'r')as f:
          tours = json.load(f)
     starts=request.args.get("starts", False)
     ends = request.args.get("ends", False)
     if starts:
        tours =  [x for x in tours if x.get("price_tur") >= starts]
     if ends:
        tours =  [x for x in tours if x.get("price_tur") <= ends]
     return jsonify(tours)
   


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()