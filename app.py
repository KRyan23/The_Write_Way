import os

from flask import (Flask, flash, render_template,
    redirect, request, session, url_for, Markup)
from flask_pymongo import PyMongo, MongoClient
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
client = MongoClient()
@myvar.context_processor
def handle_context():
    return dict(os=os)
    
@myvar.route("/")

@myvar.route("/genre")

def genre():
    genre = mongo.db.genre.find()
    return render_template("genre.html", genre=genre)


@myvar.route("/policy")

def policy():
    policy = mongo.db.policy.find()
    return render_template("policy.html", policy=policy)


@myvar.route("/crime")

def crime():
    crime = mongo.db.shortStories.find()
    return render_template("crime.html", crime=crime, title="Crime")

@myvar.route("/fantasy")

def fantasy():
    fantasy = mongo.db.shortStories.find()
    return render_template("fantasy.html", fantasy=fantasy, title="Fantasy")


@myvar.route("/fiction")
    
def fiction():    
    fiction = mongo.db.shortStories.find()
    return render_template("fiction.html", fiction=fiction, title="Fiction")


@myvar.route("/history")

def history():
    history = mongo.db.shortStories.find()
    return render_template("history.html", history=history, title="History")


@myvar.route("/horror")

def horror():
    horror = mongo.db.shortStories.find()
    return render_template("horror.html", horror=horror, title="Horror")


@myvar.route("/thriller")

def thriller():
    thriller = mongo.db.shortStories.find()
    return render_template("thriller.html", thriller=thriller, title="Thriller")


@myvar.route("/join", methods=["GET", "POST"])


def join():
    if request.method == "POST":
        
#check if username exists in database
        existing_user = mongo.db.user_accounts.find_one(
            {"pen_name": request.form.get("pen_name").lower()})
        pen = request.form.get('pen_name')
        message_failure = Markup("<div class='background-theme text-center '><h4 class='flash-message flex-wrap'>Were sorry but the Pen Name<br> '"+ "<span class='paragraph-styling'>" + pen.title() + "</span>" + "'<br> is already in use by another Author</h4></div><br>")
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
        + "<span class='paragraph-styling'>" + pen.title() + "'</span><br>" + "Registration Was Successful!"+"<p></p>"+
        "<h5 id='success-message-signin'></h5>"+"</h4></div><br>")
        session["user"] = request.form.get("pen_name").lower()
        flash(message_success)
        
        
        
    return render_template("join.html", title="Join Us")


@myvar.route("/signin", methods=["GET", "POST"])

def signin():
    if request.method == "POST":
        signin = mongo.db.user_accounts.find_one(
            {"pen_name": request.form.get("pen_name").lower()})
        pen = request.form.get('pen_name')
        if signin:
            if check_password_hash(signin["password"], request.form.get("password")):
                session["user"] = request.form.get("pen_name").lower()
                
            else:
                message_failure = Markup("<div class='background-theme text-center '><h4 class='flash-message flex-wrap'>Were sorry but the password was incorrect</h4><p></p></div><br>")
                flash(message_failure)
                return redirect(url_for('signin'))
            
            return render_template('profilePage.html', title=pen)
            
        else:
                message_failure = Markup("<div class='background-theme text-center '><h4 class='flash-message flex-wrap'>Were sorry but the Pen Name<br> '"+ "<span class='paragraph-styling'>" + pen.title() + "</span>" + "'<br> Does not exist on our system</h4></div><br>")
                flash(message_failure)
                return redirect(url_for('signin'))

    return render_template("signin.html", title="Sign In")


@myvar.route("/resetPassword", methods=["GET", "POST"])

def resetPassword():
    if request.method == "POST":
        signin = mongo.db.user_accounts.find_one({"pen_name": request.form.get("pen_name").lower()})
        pen_name = request.form.get('pen_name')
        if signin:
            username = { "pen_name": request.form.get('pen_name') }
            newpassword = { "$set": { "password": generate_password_hash(request.form.get("password"))}}
            mongo.db.user_accounts.update_one(username, newpassword)
            message_success = Markup("<div class='background-theme text-center'><h4 class='flash-message flex-wrap'>Password for " + pen_name.title() + " was reset<p></p>" +
            "</h4></div><br>")
            flash(message_success)
               
            return render_template('resetPassword.html', title="Reset Password" )
        else:
            message_failure = Markup("<div class='background-theme text-center'><h4 class='flash-message flex-wrap'>Please Check username and or email for '" + pen_name.title() + "<p></p>" +
            "</h4></div><br>")
            flash(message_failure)
    return render_template("resetPassword.html", title="Reset Password")



@myvar.route("/profilePage/<pen_name>",  methods=["GET", "POST"])

def profilePage(pen_name):
    
    pen_name = mongo.db.user_accounts.find_one(
        {"pen_name": session["user"]})["pen_name"]
    title = pen_name
    
    if session["user"]:
        return render_template("profilePage.html", pen_name=pen_name, title=title)

        
    return redirect(url_for("signin"))


@myvar.route("/backtoprofile")

def backtoprofile():
    print("backtoprofile function accesed")
    if session.get('user'):
        if session['user']:
                pen_name, title = session["user"], session["user"]
                return redirect(url_for('profilePage', pen_name=pen_name ))


@myvar.route("/signout")

def signout():
    if session:
        session.clear()
        message_success = Markup("<div class='background-theme text-center'><h4 class='flash-message flex-wrap'>Sign Out Was Successful!"+"<p></p>"+
        "</h4></div><br>")
        flash(message_success)
    else:
        message_failure = Markup("<div class='background-theme text-center'><h4 class='flash-message flex-wrap'>You are not Signed In<p></p></h4></div><br>")
        flash(message_failure)
    return redirect(url_for("signin"))


@myvar.route("/create", methods=["GET", "POST"])

def create():
        if session.get('user'):
            if session['user']:
                print("logged in")
                pen_name = session["user"]
                if request.method == "POST":
                    addstory = {
                "author": pen_name.lower(),
                "genre": request.form.get("genre").lower(),
                "name": request.form.get("name").lower(),
                "plot": request.form.get("plot").lower(),
                "content": request.form.get("content").lower(),
                "popularity": 1,          
                                }
                    mongo.db.shortStories.insert_one(addstory)

                    message_success = Markup("<div class='background-theme text-center'><h4 class='flash-message flex-wrap'>Well Done for getting your story published<p></p></h4></div><br>")
                    flash(message_success)
                    return redirect(url_for('profilePage', pen_name=pen_name))
            else:
                message_failure = Markup("<div class='background-theme text-center'><h4 class='flash-message flex-wrap'>Invalid action for user profile<p></p></h4></div><br>")
                flash(message_failure)
            return render_template("create.html", create=create, title=pen_name)   
       
    
@myvar.route("/editStory", methods=["GET", "POST"])

def editStory():
    if session.get('user'):
            if session['user']:
                pen_name = session["user"]
                #stories = mongo.db.shortStories.find_one({"_id": ObjectId(story_id)})
                #names = mongo.db.shortstories.find().sort("name", 1)
                #print(stories)
                           
                stories = mongo.db.shortStories.find()
               
                return render_template("editStory.html", stories=stories, title=pen_name)


@myvar.route("/removeStory", methods=["GET", "POST"])

def removeStory():
    flash("Remove Story")
    return Markup("<h1>Remove Story</h1>")


@myvar.route("/search", methods=["GET", "POST"])

def search():
    #query = request.form.get("query")
    #crime = list(mongo.db.crime.find({"$text":{"$search": query}}))
    #flash(query)
    return render_template("crime.html", crime=crime)



if __name__ == "__main__":
    myvar.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)