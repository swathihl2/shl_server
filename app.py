# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to SHL controller"

@app.route('/<path:path>')
def static_files(path):
    return f"you are visiting this site{path}"
