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
from flask import session
import bcrypt
# -- Initialization section --
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
# first let's load environment variables in .env
load_dotenv()
# then store environment variables with new names
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
# name of database
app.config['MONGO_DBNAME'] = 'planner'
# URI of database
app.config['MONGO_URI'] = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@cluster0.sw1ze.mongodb.net/planner?retryWrites=true&w=majority"
mongo = PyMongo(app)
# -- Routes section --


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html", time=datetime.now())


@app.route("/signup", methods=["GET", "POST"])
def signup():
    users = mongo.db.users
    hashpass = bcrypt.hashpw(
        request.form['password'].encode('utf-8'), bcrypt.gensalt())
    users.insert({"name": request.form["name"], "username": request.form["username"], "password": str(
        object=hashpass, encoding='utf-8')})
    session["user"] = request.form["name"]
    return render_template("input.html", time=datetime.now())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['name']})
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['user'] = request.form['name']
                return render_template("calendar.html", time=datetime.now())
        # if no successful match, display an error
        return "Unsuccessful username/password log in attempt"


@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    if request.method == "GET":
        return render_template("calendar.html", time=datetime.now())
    else:
        title = request.form["title"]
        categories = request.form["categories"]
        entry_date = request.form["entry_date"]
        notes = request.form["notes"]
        # username = mongo.db.users["username"]
        # Connect to a database
        events = mongo.db.events
        # if "user" in session:
        #     collection.find({"name": session["user"]})
        collection = events.find({})
        # Add to the database
        events.insert({"title": title, "categories": categories, "entry_date": entry_date, "notes": notes})
        # Return data to user
        return render_template("calendar.html", collection=collection, time=datetime.now())


@app.route("/form", methods=['POST'])
def form():
    return render_template("input.html", time=datetime.now())

@app.route("/events", methods=['GET'])
def events():
    return render_template("events.html", time=datetime.now())
