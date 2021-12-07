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

from flask import Flask, render_template, request
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
    cat = request.args.get("category")
    match_cat = []
    if cat:
        match_cat = [category for category in tours if cat.lower() in category["category"].lower()]
    else:
        return render_template("index.html", match_cat=tours)
    return render_template("index.html", match_cat=match_cat)

app.run()


