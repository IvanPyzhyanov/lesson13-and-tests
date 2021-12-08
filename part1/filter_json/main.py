# У вас есть список путешествий в файле tours.json, 
# верните подходящих  туров. Подходящим считается тур, 
# цена которого больше параметра `from`, если он указан 
# и меньше параметра `to` если он указан. 
#
# Если ни один из параметов не указан, возвращается полный список. 

# import os
# from pathlib import Path
from flask import Flask, json, request, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/tours")
def page_index():
    with open("tours.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    price_from = request.args.get("from")
    price_to = request.args.get("to")
    if price_from:
        data = [base for base in data if int(price_from) <= base["price_tur"]]
    if price_to:
        data = [base for base in data if int(price_to) >= base["price_tur"]]
    return jsonify(data)

app.run()
# if __name__ == "__main__":
#     os.chdir(Path(os.path.abspath(__file__)).parent)
