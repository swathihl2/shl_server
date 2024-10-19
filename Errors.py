class NegativeNumberException(Exception):
    def __init__(self, negative_numbers):
        super().__init__(f"negative numbers not allowed: {', '.join(map(str, negative_numbers))}")
