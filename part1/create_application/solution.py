from flask import Flask, render_template, request
import json
from pathlib import Path
import os
app = Flask(__name__)


@app.route("/enroll", methods=["GET"])
def get_form():
    return render_template("index.html")


@app.route("/enroll", methods=["POST"])
def post_form():
    name, email, phone = request.form.get("name"),  request.form.get("email"), request.form.get("phone")
    application = {
        "name": name, "email": email, "phone": phone,
    }
    with open('enrollments.json', 'r', encoding='utf-8') as f:
        current_data = json.load(f)
        current_data.append(application)
    with open('enrollments.json', 'w', encoding='utf-8') as f:
        json.dump(current_data, f, ensure_ascii=False, indent=4)
    return "Данные записаны"


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)  # Эта строка необходима, чтобы правильно искать json хранилища
    app.run()
