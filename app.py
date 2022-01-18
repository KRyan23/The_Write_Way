import os

from flask import (Flask, flash, render_template, redirect, request, session, url_for, Markup)
from flask_pymongo import PyMongo, MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


myapp = Flask(__name__)

myapp.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
myapp.config["MONGO_URI"] = os.environ.get("MONGO_URI")
myapp.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(myapp)
#define a function to handle checking source files
client = MongoClient()
@myapp.context_processor
def handle_context():
    """Get the list of user's environment variables."""
    return dict(os=os)

JOIN_MESSAGE_FAILURE = Markup(" is already<br> registered as a 'Pen Name'")
JOIN_MESSAGE_SUCCESS = Markup("<br>'Your Registration Was Successful!'")
PASSWORD_MESSAGE_FAILURE = "Please Check Your Username and Password"
PASSWORD_MESSAGE_SUCCESS = "Your Password Was reset!"
SIGNIN_MESSAGE_FAILURE = "You are not Logged in"
SIGNOUT_FAILURE = "You are not Signed In"
SIGNOUT_SUCCESS = "Sign Out Was Successful!"
CREATE_SUCCESS = "Well Done for getting your story published"
EDIT_FAILURE = "Invalid action for user profile"
UPDATE_SUCCESS = "The Story Has Been Updated"
DELETE_SUCCESS = "Congratulations The Story Was Deleted"
POPULARITY_FAILURE = Markup("You Need To Be Signed In<br>to 'Like' A Story")


@myapp.route("/")

@myapp.route("/get_genre")

def get_genre():
    """Loads the template for the 'genres' on the home page."""
    genre = mongo.db.genre.find()
    news = mongo.db.news.find()
    return render_template("genre.html", genre=genre, news=news)


@myapp.route("/get_policy")

def get_policy():
    """Loads the template for the 'policy' page."""
    policy = mongo.db.policy.find()
    news = mongo.db.news.find()
    return render_template("policy.html", policy=policy, news=news, title="Policy Page")


@myapp.route("/crime")

def crime():
    """Loads the template for the 'crime' genre."""
    crime = mongo.db.shortstories.find()
    news = mongo.db.news.find()
    return render_template("crime.html", crime=crime, title="Crime", news=news)

@myapp.route("/fantasy")

def fantasy():
    """Loads the template for the 'fantasy' genre."""
    fantasy = mongo.db.shortstories.find()
    news = mongo.db.news.find()
    return render_template("fantasy.html", fantasy=fantasy, title="Fantasy", news=news)


@myapp.route("/fiction")

def fiction():
    """Loads the template for the 'fiction' genre."""
    fiction = mongo.db.shortstories.find()
    news = mongo.db.news.find()
    return render_template("fiction.html", fiction=fiction, title="Fiction", news=news)


@myapp.route("/history")

def history():
    """Loads the template for the 'history' genre."""
    history = mongo.db.shortstories.find()
    news = mongo.db.news.find()
    return render_template("history.html", history=history, title="History", news=news)


@myapp.route("/horror")

def horror():
    """Loads the template for the 'horror' genre."""
    horror = mongo.db.shortstories.find()
    news = mongo.db.news.find()
    return render_template("horror.html", horror=horror, title="Horror", news=news)


@myapp.route("/thriller")

def thriller():
    """Loads the template for the 'thriller' genre."""
    thriller = mongo.db.shortstories.find()
    news = mongo.db.news.find()
    return render_template("thriller.html", thriller=thriller, title="Thriller", news=news)


@myapp.route("/get_join", methods=["GET", "POST"])

def get_join():
    """
    Handles the the signup of a new user.

    Redirects them to the signin page afterwards.

    """
    news = mongo.db.news.find()
    if request.method == "POST":
        existing_user = mongo.db.user_accounts.find_one(
            {"pen_name": request.form.get("pen_name").lower()})
        if existing_user:
            flash(JOIN_MESSAGE_FAILURE)
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

        session["user"] = request.form.get("pen_name").lower()
        flash(JOIN_MESSAGE_SUCCESS)
        return redirect(url_for("get_signin"))

    return render_template("join.html", title="Join Us", news=news)


@myapp.route("/get_signin", methods=["GET", "POST"])

def get_signin():
    """
    Handles the signin for registered users.

    Loads the profile page after signin.

    redirects invalid credentails back to signin.

    """

    news = mongo.db.news.find()

    if request.method == "POST":
        signin = mongo.db.user_accounts.find_one(
            {"pen_name": request.form.get("pen_name").lower()})
        pen = request.form.get('pen_name')
        if signin:
            if check_password_hash(signin["password"], request.form.get("password")):
                session["user"] = request.form.get("pen_name").lower()
                return render_template('profilepage.html', title=pen, news=news)
        flash(PASSWORD_MESSAGE_FAILURE)
        return redirect(url_for('get_signin'))

    return render_template("signin.html", title="Sign In", news=news)


@myapp.route("/resetpassword", methods=["GET", "POST"])

def resetpassword():
    """Resets the password for a registered user."""
    news = mongo.db.news.find()
    if request.method == "POST":
        signin = mongo.db.user_accounts.find_one({"pen_name": request.form.get("pen_name").lower()})
        pen_name = request.form.get('pen_name')
        if signin:
            username = { "pen_name": request.form.get('pen_name') }
            newpassword = {
                "$set": { "password": generate_password_hash(request.form.get("password"))}}
            mongo.db.user_accounts.update_one(username, newpassword)
            flash(pen_name + PASSWORD_MESSAGE_SUCCESS)
            return redirect(url_for("get_signin", news=news, title="Reset Password"))

        flash(PASSWORD_MESSAGE_FAILURE)
    return render_template("resetpassword.html", title="Reset Password", news=news)


@myapp.route("/profilepage/<pen_name>",  methods=["GET", "POST"])

def profilepage(pen_name):
    """Loads the profile page if signin was successful."""
    pen_name = mongo.db.user_accounts.find_one(
        {"pen_name": session["user"]})["pen_name"]
    title = pen_name
    if session["user"]:
        news = mongo.db.news.find()
        return render_template("profilepage.html", pen_name=pen_name, title=title, news=news)
    return redirect(url_for("get_signin", news=news))


@myapp.route("/backtoprofile")

def backtoprofile():
    """Brings the user back to the main profile page."""
    news = mongo.db.news.find()
    if session.get('user'):
        if session['user']:
            pen_name = session["user"]
    return redirect(url_for('profilepage', pen_name=pen_name, news=news, title="Profile Page"))


@myapp.route("/signout")

def signout():
    """Signs all active users out of their profile"""
    news = mongo.db.news.find()
    if session:
        session.clear()
        flash(SIGNOUT_SUCCESS)
    else:
        flash(SIGNOUT_FAILURE)
    return redirect(url_for("get_signin", news=news))


@myapp.route("/create", methods=["GET", "POST"])

def create():
    """
    Loads the create story template for a user.

    Creates the various key pairs for a users story.

    """
    news = mongo.db.news.find()
    if session.get('user'):
        if session['user']:
            pen_name = session["user"]
            if request.method == "POST":
                addstory = {
                "author": pen_name.lower(),
                "genre": request.form.get("genre").lower(),
                "name": request.form.get("name").lower(),
                "plot": request.form.get("plot").lower(),
                "content": request.form.get("content").lower(),
            "popularity": 1,}
                mongo.db.shortstories.insert_one(addstory)
                flash(CREATE_SUCCESS)
                return redirect(url_for('profilepage', pen_name=pen_name))

    return render_template("create.html", create=create, title=pen_name, news=news)


@myapp.route("/editstory")

def editstory():
    """Loads the edit story template for a user."""

    news = mongo.db.news.find()
    if session.get('user'):
        if session['user']:
            pen_name = session["user"]
            stories = mongo.db.shortstories.find()
    else:
        flash(EDIT_FAILURE)
    return render_template("editstory.html", stories=stories, pen_name=pen_name,
    news=news, title="Edit Story")


@myapp.route("/updatestory/<story_id>", methods=["GET", "POST"])

def updatestory(story_id):
    """
    For editing an existing users story.

    Edits the various key pairs for a users story.

    """

    pen_name = session["user"]
    if request.method == "POST":
        request.form.get("name").lower()
        changestory = {
                "genre": request.form.get("genre").lower(),
                "author": pen_name,
                "name": request.form.get("name").lower(),
                "plot": request.form.get("plot").lower(),
                "content": request.form.get("content").lower(),
                "popularity": 1,
                "updated": True,}
        mongo.db.shortstories.update({"_id": ObjectId(story_id)}, changestory)
        flash(UPDATE_SUCCESS)
    return redirect(url_for("editstory", pen_name=pen_name))


@myapp.route("/deletestory/<story_id>")

def deletestory(story_id):
    """Performs the deletion of a story."""
    mongo.db.shortstories.remove({"_id": ObjectId(story_id)})
    flash(DELETE_SUCCESS)
    return redirect(url_for("removestory"))


@myapp.route("/removestory", methods=["GET", "POST"])

def removestory():
    """Loads the remove story template for a user."""
    news = mongo.db.news.find()
    if session.get('user'):
        if session['user']:
            pen_name = session["user"]
            stories = mongo.db.shortstories.find()
    return render_template("removestory.html", stories=stories, pen_name=pen_name, news=news, title="Remove Story")


@myapp.route("/updatepopularity/<genre>", methods=["GET", "POST"])

def updatepopularity(genre):
    """
    Increments the popularity rating on a story.

    Brings user back to the same page after updating

    """

    if session.get('user'):
        if request.method == "POST":
            name = { "name": request.form.get('name') }
            popularity = { "$inc": { "popularity": 1 }}
            mongo.db.shortstories.update_one(name, popularity)
        return redirect(url_for(genre))

    flash(POPULARITY_FAILURE)
    return redirect(url_for("get_signin"))


if __name__ == "__main__":
    myapp.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
