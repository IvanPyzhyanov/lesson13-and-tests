import os
from flask import Flask, render_template, request
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
    category = request.args.get("category")
    tours_match = []
    if category:
        tours_match = [x for x in tours if x.get("category").lower().startswith(category.lower())]
    if not tours_match:
        tours_match = tours
    return render_template("index.html", tours_match=tours_match, category=category)


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