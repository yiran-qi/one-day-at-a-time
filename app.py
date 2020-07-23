# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from datetime import datetime
from flask import request
from flask import redirect
from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv




# -- Initialization section --
app = Flask(__name__)

# first let's load environment variables in .env
load_dotenv()
# then store environment variables with new names 
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

# name of database
app.config['MONGO_DBNAME'] = 'planner'

# URI of database
# URI of database
app.config['MONGO_URI'] = f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@cluster0-7bt79.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
@app.route('/')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    # return render_template("login.html", time=datetime.now())
    if request.method == "GET":
        return render_template("login.html", time=datetime.now())
    else:
        username = request.form['username']
        #connect to a database
        events = mongo.db.events
        # add to the data base
        events.insert({'username': username})
        return redirect('/')

@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())
