
from flask import Flask, render_template
from flask_cors import CORS

from controller.item_controller import item_bp
from controller.calculator_controller import calculator_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(item_bp)
app.register_blueprint(calculator_bp)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/health')
def index():
    return "UP"
