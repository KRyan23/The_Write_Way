import os

from flask import (Flask, flash, render_template,
    redirect, request, session, url_for, Markup)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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


@myvar.route("/join", methods=["GET", "POST"])


def join():
    if request.method == "POST":
#check if username exists in database
        existing_user = mongo.db.user_accounts.find_one(
            {"pen_name": request.form.get("pen_name").lower()})
        pen = request.form.get('pen_name')
        message_failure = Markup("<div class='background-theme text-center '><h4 class='flash-message flex-wrap'>Were sorry but the Pen Name<br> '"+ "<span class='paragraph-styling'>" + pen + "</span>" + "'<br> is already in use by another Author</h4></div><br>")
        if existing_user:
	        flash(message_failure)
	        return redirect(url_for("join"))

        join = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "pen_name": request.form.get("pen_name").lower(),
            "city_name": request.form.get("city_name").lower(),
            "country_name": request.form.get("country_name").lower(),
            "email_name": request.form.get("email_name").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.user_accounts.insert_one(join)
        
        message_success = Markup("<div class='background-theme text-center'><h4 class='flash-message flex-wrap'>Congratulations<br> '"
        + "<span class='paragraph-styling'>" + pen + "'</span><br>" + "Registration Was Successful!"+"<p></p>"+
        "<h5 id='success-message-signin'></h5>"+"</h4></div><br>")
        session["user"] = request.form.get("pen_name").lower()
        flash(message_success)
        return redirect(url_for('profilePage', username=session["user"]))
        
        
    return render_template("join.html", title="Join Us")


@myvar.route("/signin", methods=["GET", "POST"])

def signin():
    if request.method == "POST":
        
        signin = mongo.db.user_accounts.find_one(
            {"pen_name": request.form.get("pen_name").lower()})
        pen = request.form.get('pen_name')
        if signin:
            if check_password_hash(
               signin["password"], request.form.get("password")):
               session["user"] = request.form.get("password")
               print("Login Successful")
               
            return render_template('profilePage.html', title=pen)
            
        else:
            flash("Username does not exist")
            return redirect(url_for('signin'))

    return render_template("signin.html", title="Sign In")


@myvar.route("/resetPassword")

def resetpassword():
    resetpassword = mongo.db.join.find()
    #Just need to add the logic to check both passwords match
    return render_template("resetPassword.html", resetpassword=resetpassword, title="Reset Password")

@myvar.route("/profilePage/<pen_name>", methods=["GET", "POST"])

def profilePage(pen_name):
    pen_name = mongo.db.user_accounts.find_one(
        {"pen_name": session["user"]})["pen_name"]
    return render_template("profilePage.html", pen_name=pen_name)


if __name__ == "__main__":
    myvar.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
