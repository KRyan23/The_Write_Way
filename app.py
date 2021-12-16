import os

from flask import (Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


myvar = Flask(__name__)

myvar.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
myvar.config["MONGO_URI"] = os.environ.get("MONGO_URI")
myvar.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(myvar)
#define a function to handle checking source files
@myvar.context_processor
def handle_context():
    return dict(os=os)
    
@myvar.route("/")
@myvar.route("/get_genre")


def get_genre():
    genre = mongo.db.genre.find()
    return render_template("genre.html", genre=genre)


@myvar.route("/policy")

def policy():
    policy = mongo.db.policy.find()
    return render_template("policy.html", policy=policy)


@myvar.route("/crime")

def crime():
    crime = mongo.db.crime.find()
    return render_template("crime.html", crime=crime, title="Crime")

@myvar.route("/fantasy")

def fantasy():
    fantasy = mongo.db.fantasy.find()
    return render_template("fantasy.html", fantasy=fantasy, title="Fantasy")


@myvar.route("/fiction")
    
def fiction():    
    fiction = mongo.db.fiction.find()
    return render_template("fiction.html", fiction=fiction, title="Fiction")


@myvar.route("/history")

def history():
    history = mongo.db.history.find()
    return render_template("history.html", history=history, title="History")


@myvar.route("/horror")

def horror():
    horror = mongo.db.horror.find()
    return render_template("horror.html", horror=horror, title="Horror")

@myvar.route("/thriller")

def thriller():
    thriller = mongo.db.thriller.find()
    return render_template("thriller.html", thriller=thriller, title="Thriller")


if __name__ == "__main__":
    myvar.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
      
# 
