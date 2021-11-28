# У вас есть шаблон с формой поиска туров по категориям, 
# допишите вьюшку и шаблон так, чтобы при отправке формы 
# выводился список подходящих названий.
# В данном задании для отправки формы используется get-запрос c параметром `category`
# Также внесите соответствующие правки в Шаблон.
#
# Если поисковая форма оставлена пустой, вернуть полный список туров.
# Подходящим является тур, у которого поисковая строка содержится в начале названия. 
# Регистр не учитывается.
# 

import os
from flask import Flask
from pathlib import Path
app = Flask(__name__)

tours =   [
  { "title": "Винный тур", "price_rur": 2000, "category": "bus" },
  { "title": "Тифлис - город модерна", "price_rur": 4900, "category": "walk" },
  { "title": "Квест-экскурсия по Тбилиси", "price_rur": 5800, "category": "quest" },
  { "title": "Лучшие панорамы вечернего города", "price_rur": 1800, "category": "walk"},
  { "title": "Болгар — Северная Мекка", "price_rur": 1800, "category": "bus" }
]

@app.route("/tours")
def get_by_category():
    # TODO Напишите свою функцию здесь
    pass

if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)  # Эта строка необходима, чтобы правильно искать json хранилища
    app.run()
