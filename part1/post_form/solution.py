import os
from pathlib import Path
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/settings", methods=["GET", "POST"])
def update_settings():
    if request.method == "POST":
        settings = { 
            "project_name": request.form.get("project_name") ,
            "project_tagline": request.form.get("project_tagline") ,
        }
        with open("settings.json", "w") as f:
            json.dump(settings, f)

    if request.method == "GET":
        with open("settings.json", "r") as f:
            settings = json.load(f)

    return render_template("settings.html", settings=settings)

if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run()