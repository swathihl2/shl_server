# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to SHL controller"

@app.route('/<path:path>')
def static_files(path):
    return f"you are visiting this site{path}"

@app.route('/stringcalc')
def static_files():
    data = request.get_json()
    result = 0 
    try; 

        if data:
           result = data
    except Exception as e:
        pass
    return f"{data} {result}"