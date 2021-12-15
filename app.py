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


if __name__ == "__main__":
    myvar.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
      
# 
