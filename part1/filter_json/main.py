# У вас есть список путешествий в файле tours.json, 
# верните подходящих  туров. Подходящим считается тур, 
# цена которого больше параметра `from`, если он указан 
# и меньше параметра `to` если он указан. 
#
# Если ни один из параметов не указан, возвращается полный список. 

import os
from pathlib import Path
from flask import Flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/tours")
def page_index():
    # TODO напишите Ваш код здесь
    pass


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()