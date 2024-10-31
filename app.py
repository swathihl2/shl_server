from flask import Flask, render_template
from flask_cors import CORS

from controller.item_controller import item_bp
from controller.calculator_controller import calculator_bp
# from controller.prometheus_controller import prom_bp
from metrics.health_scheduler import start_scheduler

app = Flask(__name__)
CORS(app)

# start_scheduler()

app.register_blueprint(item_bp)
app.register_blueprint(calculator_bp)
app.register_blueprint(prom_bp)


@app.route('/')
def index():
    return render_template('home.html')

