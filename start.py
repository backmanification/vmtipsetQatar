from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Fuck You Edde, vi kör flask"

@app.route("/Ehsan/")
def page():
    return "Ehsan är lite bättre"
