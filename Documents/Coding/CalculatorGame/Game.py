from random import randrange
from Calculator import CalculatorGames

calc = CalculatorGames(4)

class CalcGame:
    def __init__(self):
        self.rounds = None
        self.player_rounds = 0
        self.number = None
        self.operator = None
        self.difficulty = None
        self.player_number = None
        self.player_operator = None
        self.calculation = None
        self.prev_calc = None
        self.prev_right = None
        self.prev_wrong = None

    def clear_rounds(self):
        self.rounds = None

    def set_calculation(self, calc):
        self.calculation = calc
    
    def set_prev_calc(self, calc):
        self.prev_calc = calc

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def set_rounds(self, rounds):
        self.rounds = rounds

    def clear_player(self):
        self.player_operator = None
        self.player_number = None
        self.player_rounds = 0
        self.difficulty = None
        self.prev_calc = None
        self.prev_right = None
        self.prev_wrong = None

    def clear_num_op(self):
        self.number = None
        self.operator = None
        self.calculation = None

    def set_new(self):
        if self.difficulty == 1:
            self.number = randrange(1,10)
            self.operator = randrange(1,3)
        elif self.difficulty == 2:
            self.number = randrange(1,10)
            self.operator = randrange(1,5)
        elif self.difficulty == 3:
            self.number = randrange(1,10)
            self.operator = randrange(1,5)

    def up_rounds(self):
        self.player_rounds += 1

    def set_player_number(self, number):
        self.player_number = number

    def set_player_operator(self, number):
        self.player_operator = number

    def calc(self):
        num1 = 0
        num2 = 0
        operation = 0
        result = 0
        act = 0
        
        if self.difficulty == 1:
            num1 = randrange(1,11)
        elif self.difficulty == 2:
            num1 = randrange(1,21)
        elif self.difficulty == 3:
            num1 = randrange(1,51)
       
        
        if self.difficulty == 1:
            num2 = randrange(1,11)
        if self.difficulty == 2:
            num2 = randrange(1,21)
        if self.difficulty == 3:
            num2 = randrange(1,51)

        if self.difficulty == 1:
            operation = randrange(1,3)
        if self.difficulty == 2:
            operation = randrange(1,5)
        if self.difficulty == 3:
            operation = randrange(3,5)

        if operation == 1:
            result = calc.add(num1, num2)
        elif operation == 2:
            result = calc.substract(num1, num2)
        elif operation == 3:
            result = calc.multiply(num1, num2)
        elif operation == 4:
            result = round(calc.divide(num1, num2), 4)
        elif operation == 5:
            result = calc.to_the_power(num1, num2)
        
        if self.operator == 1:
            act = float(result) + float(self.number)
        elif self.operator == 2:
            act = float(result) - float(self.number)
        elif self.operator == 3:
            act = float(result) * float(self.number)
        elif self.operator == 4:
            act = float(result) / float(self.number)
        elif self.operator == 5:
            act = float(result) ** float(self.number)
        
        if operation == 1:
            return("{} + {} = {}".format(num1, num2, act))
        elif operation == 2:
            return("{} - {} = {}".format(num1, num2, act))
        elif operation == 3:
            return("{} * {} = {}".format(num1, num2, act))
        elif operation == 4:
            return("{} / {} = {}".format(num1, num2, round(act, calc.round_off), 4))
        elif operation == 5:
            return("{} ^ {} = {}".format(num1, num2, act))
    
    def new_play_window(self):
        self.set_new()
        return self.calc()

    def play_wrong(self):
        return self.calc()

