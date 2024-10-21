import re

from flask import Flask, request, render_template
from errors import NegativeNumberException
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/<path:path>')
def static_files(path):
    return f"you are visiting this site{path}"

@app.route('/stringcalc', methods=['GET', 'POST'])
def string_calc():
    data = request.get_json()
    numbers: str = data['numbers']
    print(numbers)
    result = 0
    try:
        if numbers:
            num_list = re.findall(r'-?\d+', numbers)

            negatives = [int(num) for num in num_list if int(num) < 0]
            if negatives:
                raise NegativeNumberException(negatives)

            result = sum(int(num) for num in num_list)

    except NegativeNumberException as e:
        return f"error: {e.__str__()}"
    return f"{result}"
