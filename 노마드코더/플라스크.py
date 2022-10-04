import re
from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home(): # name harry 라 적고 home.html {{}} 안에 변수 적어준다
    return render_template("home.html", name="harry")

@app.route("/search")
def hello():
    return render_template("search.html")

app.run("0.0.0.0")