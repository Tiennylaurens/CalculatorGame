class CalculatorGames:
    def __init__(self, round):
        self.calculations = 0 
        self.round_off = round
        self.status = False

    def set_status(self, status):
        self.status = status

    def set_round_decimal(self, decimal):
        self.round_off = decimal 
    
    def get_status(self):
        return self.status

    def add(self, num1, num2):
        result = num1 + num2
        self.calculations += 1
        return round(result, self.round_off)

    def substract(self, num1, num2):
        result = num1 - num2
        self.calculations += 1
        return round(result, self.round_off)

    def multiply(self, num1, num2):
        result = num1 * num2
        self.calculations += 1
        return round(result, self.round_off)
    
    def divide(self, num1, num2):
        result = float(num1) / float(num2)
        self.calculations += 1
        return round(result, self.round_off)

    def to_the_power(self, num1, num2):
        result = num1 ** num2
        self.calculations += 1
        return round(result, self.round_off)
    
    def modular(self, num1, num2):
        result = num1 % num2
        return round(result, self.round_off)
