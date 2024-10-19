# app.py
import re

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to SHL controller"


@app.route('/<path:path>')
def static_files(path):
    return f"you are visiting this site{path}"


@app.route('/stringcalc', methods=['GET', 'POST'])
def string_calc():
    data = request.get_json()
    numbers = data['numbers']
    print(numbers)
    result = 0
    try:
        if numbers:
            if numbers.startswith("//"):
                delimiter, numbers = numbers[2:].split("\n", 1)
                delimiter = re.escape(delimiter)
            else:
                delimiter = r'[,\n]'
            num_list = re.split(delimiter, numbers)
            result = sum(int(num) for num in num_list if num)

    except Exception as e:
        pass
    return f"_{numbers}_ {result}"

