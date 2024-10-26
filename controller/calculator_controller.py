# controllers/calculator_controller.py
from flask import Blueprint, request
import re

calculator_bp = Blueprint('calculator_bp', __name__)

class NegativeNumberException(Exception):
    def __init__(self, negatives):
        self.negatives = negatives

    def __str__(self):
        return f"Negatives not allowed: {', '.join(map(str, self.negatives))}"

@calculator_bp.route('/')
def index():
    return "<h1>Welcome to the String Calculator API</h1>"

@calculator_bp.route('/stringcalc', methods=['GET', 'POST'])
def string_calculator():
    if request.method == 'POST':
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
            return f"error: {e.__str__()}", 400  # Return a 400 Bad Request
        return f"{result}"
    return "Please send a POST request with a JSON body."
