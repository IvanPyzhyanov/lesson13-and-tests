# У вас есть словарь со списком туров. Создайте вьюшку, 
# которая при обращении к /tours показывает форму, 
# которая отправляет данные самой себе методом get. 
# При отправке на /tours запроса (есть квери-параметр `s`) 
# выводит подходящие результаты и их количество. 
# Подходящие результаты будут содержать в названии s (регистр не учитывается). 
# Поле поиска выводится всегда.
#
# Пример запроса:
# /tours?s=панорамы

# Пример ответа (необходимо дополнить шаблон):
# <h1>Найдено: 2</h1>
# <ul>
#     <li>Найденный элемент 1</li>
# </ul>
#

from flask import Flask, render_template, request
app = Flask(__name__)

tours =   [
   { "title": "Винный тур", "price_tur": 2000 },
   { "title": "Тифлис - город модерна","price_tur": 4900  },
   { "title": "Квест-экскурсия по Тбилиси","price_tur": 5800 },
   { "title": "Лучшие панорамы вечернего города", "price_tur": 1800 },
   { "title": "Болгар — Северная Мекка", "price_tur": 1800 }
]


@app.route("/tours")
def page_index():
    s = request.args.get("s")
    match_tour = []
    if s:
        for tour in tours:
            if s.lower() in tour["title"].lower():
                match_tour.append(tour["title"])
    return render_template("index.html", match_tour=match_tour, count_tour=len(match_tour))

if __name__ == "__main__":
    app.run()


