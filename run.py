import os
from flask import Flask
if os.path.exists("env.py"):
    import env


myvar = Flask(__name__)