import os

from flask import (Flask, flash, render_template,
    redirect, request, session, url_for, Markup)
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
    return dict(os=os)
    
@myapp.route("/")

@myapp.route("/genre")

def genre():
    genre = mongo.db.genre.find()
    news = mongo.db.news.find()
    return render_template("genre.html", genre=genre, news=news)


@myapp.route("/policy")

def policy():
    policy = mongo.db.policy.find()
    news = mongo.db.news.find()
    return render_template("policy.html", policy=policy, news=news)


@myapp.route("/crime")

def crime():
    crime = mongo.db.shortStories.find()
    news = mongo.db.news.find()
    return render_template("crime.html", crime=crime, title="Crime", news=news)

@myapp.route("/fantasy")

def fantasy():
    fantasy = mongo.db.shortStories.find()
    news = mongo.db.news.find()
    return render_template("fantasy.html", fantasy=fantasy, title="Fantasy", news=news)


@myapp.route("/fiction")
    
def fiction():    
    fiction = mongo.db.shortStories.find()
    news = mongo.db.news.find()
    return render_template("fiction.html", fiction=fiction, title="Fiction", news=news)


@myapp.route("/history")

def history():
    history = mongo.db.shortStories.find()
    news = mongo.db.news.find()
    return render_template("history.html", history=history, title="History", news=news)


@myapp.route("/horror")

def horror():
    horror = mongo.db.shortStories.find()
    news = mongo.db.news.find()
    return render_template("horror.html", horror=horror, title="Horror", news=news)


@myapp.route("/thriller")

def thriller():
    thriller = mongo.db.shortStories.find()
    news = mongo.db.news.find()
    return render_template("thriller.html", thriller=thriller, title="Thriller", news=news)


@myapp.route("/join", methods=["GET", "POST"])


def join():
    news = mongo.db.news.find()
    if request.method == "POST":
        
#check if username exists in database
        existing_user = mongo.db.user_accounts.find_one(
            {"pen_name": request.form.get("pen_name").lower()})
        pen = request.form.get('pen_name')
        message_failure = Markup("Were sorry but the Pen Name<br> '"+ "<span class='paragraph-styling'>" + pen.title() + "</span>" + "'<br> is already in use by another Author")
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
        
        message_success = Markup("Congratulations<br> '"
        + "<span class='paragraph-styling'>" + pen.title() + "'</span><br>" + "Registration Was Successful!"+"<p></p>"+
        "<h5 id='success-message-signin'></h5>")
        session["user"] = request.form.get("pen_name").lower()
        flash(message_success)
        
        
        
    return render_template("join.html", title="Join Us", news=news)


@myapp.route("/signin", methods=["GET", "POST"])

def signin():
    if request.method == "POST":
        signin = mongo.db.user_accounts.find_one(
            {"pen_name": request.form.get("pen_name").lower()})
        pen = request.form.get('pen_name')
        if signin:
            if check_password_hash(signin["password"], request.form.get("password")):
                session["user"] = request.form.get("pen_name").lower()
                
            else:
                message_failure = Markup("Were sorry but the password was incorrect")
                flash(message_failure)
                return redirect(url_for('signin'))
            
            return render_template('profilePage.html', title=pen)
            
        else:
                message_failure = Markup("Were sorry but the Pen Name<br> '"+ "<span class='paragraph-styling'>" + pen.title() + "</span>" + "'<br> Does not exist on our system")
                flash(message_failure)
                return redirect(url_for('signin'))

    return render_template("signin.html", title="Sign In")


@myapp.route("/resetPassword", methods=["GET", "POST"])

def resetPassword():
    if request.method == "POST":
        signin = mongo.db.user_accounts.find_one({"pen_name": request.form.get("pen_name").lower()})
        pen_name = request.form.get('pen_name')
        if signin:
            username = { "pen_name": request.form.get('pen_name') }
            newpassword = { "$set": { "password": generate_password_hash(request.form.get("password"))}}
            mongo.db.user_accounts.update_one(username, newpassword)
            message_success = Markup("The password for " +"<br>" + pen_name.title() + " was reset!")
            flash(message_success)
               
            return render_template('resetPassword.html', title="Reset Password" )
        else:
            message_failure = Markup("Please Check Your<br>'pen name' and 'password' ")
            flash(message_failure)
    return render_template("resetPassword.html", title="Reset Password")



@myapp.route("/profilePage/<pen_name>",  methods=["GET", "POST"])

def profilePage(pen_name):
    
    pen_name = mongo.db.user_accounts.find_one(
        {"pen_name": session["user"]})["pen_name"]
    title = pen_name
    
    if session["user"]:
        news = mongo.db.news.find()
        return render_template("profilePage.html", pen_name=pen_name, title=title, news=news)
    return redirect(url_for("signin"))


@myapp.route("/backtoprofile")

def backtoprofile():
    news = mongo.db.news.find()
    if session.get('user'):
        if session['user']:
                pen_name, title = session["user"], session["user"]
                return redirect(url_for('profilePage', pen_name=pen_name, news=news ))
    else:
        flash("You are not Logged in")
        return redirect(url_for("signin"))


@myapp.route("/signout")

def signout():
    if session:
        session.clear()
        flash("Sign Out Was Successful!")
    else:
        flash("You are not Signed In")
    return redirect(url_for("signin"))


@myapp.route("/create", methods=["GET", "POST"])

def create():
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
                    mongo.db.shortStories.insert_one(addstory)
                    flash("Well Done for getting your story published")
                    return redirect(url_for('profilePage', pen_name=pen_name))
            else:
                flash("Invalid action for user profile")
            return render_template("create.html", create=create, title=pen_name, news=news)   
       
# This is the main function for edit story
@myapp.route("/editStory", methods=["GET", "POST"])

def editStory(): 
    news = mongo.db.news.find()
    #story = mongo.db.shortStories.find_one({"_id": ObjectId(story_id)})
    #name = mongo.db.shortStories.name.find().sort("name", 1)
    if session.get('user'):
            if session['user']:
                pen_name = session["user"]
                stories = mongo.db.shortStories.find()
    return render_template("editStory.html", stories=stories, pen_name=pen_name, news=news)
    

@myapp.route("/updateStory/<story_id>")

def updateStory(story_id):
                #mongo.db.shortStories.remove({"_id": ObjectId(story_id)})
                flash("Congratulations The Story Was Updated")
                return redirect(url_for("editStory.html"))
               

@myapp.route("/deleteStory/<story_id>")

def deleteStory(story_id):
                mongo.db.shortStories.remove({"_id": ObjectId(story_id)})
                flash("Congratulations The Story Was Deleted")
                return redirect(url_for("removeStory"))
               


@myapp.route("/removeStory", methods=["GET", "POST"])

def removeStory():
    news = mongo.db.news.find()
    if session.get('user'):
            if session['user']:
                pen_name = session["user"]
                stories = mongo.db.shortStories.find()
    return render_template("removeStory.html", stories=stories, pen_name=pen_name, news=news)


@myapp.route("/updatePopularity/<genre>", methods=["GET", "POST"])

def updatePopularity(genre):
                    if session.get('user'):
                        if request.method == "POST":
                            name = { "name": request.form.get('name') }
                            popularity = { "$inc": { "popularity": 1 }}
                            mongo.db.shortStories.update_one(name, popularity)
                        return redirect(url_for(genre))
                    else:
                        message_failure = Markup("You Need To Be Signed In<br>to 'Like' A Story")
                        flash(message_failure)
                    return redirect(url_for("signin"))
               

@myapp.route("/search", methods=["GET", "POST"])

def search():
    #query = request.form.get("query")
    #stories = list(mongo.db.shortStories.find({"$text":{"$search": query}}))
    print("")


if __name__ == "__main__":
    myapp.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)