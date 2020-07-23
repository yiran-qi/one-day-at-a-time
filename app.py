# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from datetime import datetime
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')

@app.route('/login')
def login():
    return render_template("login.html", time=datetime.now())

@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())
