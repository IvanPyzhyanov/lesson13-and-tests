from flask import Flask, render_template, request
app = Flask(__name__)


tours =   [
   { "title": "Винный тур", "price_tur": 2000 },
   { "title": "Тифлис - город модерна","price_rur": 4900  },
   { "title": "Квест-экскурсия по Тбилиси","price_tur": 5800 },
   { "title": "Лучшие панорамы вечернего города", "price_tur": 1800 },
   { "title": "Болгар — Северная Мекка", "price_tur": 1800 }
]


@app.route("/tours")
def page_index():
    tour_name = request.args.get("s")
    tours_match=[]
    if tour_name:
        s = tour_name.lower()
        tours_match = [x for x in tours if s in x.get("title").lower()]
    return render_template("index.html", tours=tours_match, tours_count=len(tours_match))

if __name__ == "__main__":
    app.run()


# <!doctype html>
# <html lang="ru">
# <head>
#    <meta charset="UTF-8">
#    <title>Document</title>
# </head>
# <body>
#    <form action="/tours">
#        <input type="text" name="s" value="{{ s }}">
#        <input type="submit" value="Искать">
#    </form>
# <h1>Найдено: {{ tours_count }}</h1>
# {% if tours_count %}
# <ul>
# {% for tour in tours %}
#     <li>{{ tour.title }}</li>
# {% endfor %}
# </ul>
# {% endif %}
# </body>
# </html>