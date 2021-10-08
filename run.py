import os
from flask import Flask
if os.path.exists("env.py"):
    import env


myvar = Flask(__name__)


@myvar.route("/")
def this_is_a_test_function():
    return "This means our test function in python is working"


if __name__ == "__main__":
    myvar.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)