# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Home"

@app.route('/<path:path>')
def static_files(path):
    return f"{path}"

if __name__ == '__main__':
    app.run(debug=True)
