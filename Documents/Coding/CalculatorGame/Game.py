from random import randrange
from Calculator import CalculatorGames
import time

calc = CalculatorGames(5)

class Game:
    def __init__(self):
        self.rounds = 0
        self.player_rounds = 0
        self.number = None
        self.operator = None
        self.player_number = None
        self.player_operator = None
        self.difficulty = None
        self.start = 0
        self.end = 0
        self.time = 0
    
    def set_start(self):
        self.start = int(time.time())
    
    def set_end(self):
        self.end = int(time.time())
    
    def calculate_time(self):
        self.time = self.end - self.start

    def set_rounds(self, rounds):
        self.rounds = rounds
    
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if self.difficulty == 1:
            self.number = randrange(1,11)
            self.operator = randrange(1,3)
        if self.difficulty == 2:
            self.number = randrange(1,21)
            self.operator = randrange(1,5)
        if self.difficulty == 3:
            self.number = randrange(1,51)
            self.operator = randrange(3,6)

    def clear_player(self):
        self.player_operator = None
        self.player_number = None

    def set_new(self):
        if self.difficulty == 1:
            self.number = randrange(1,11)
            self.operator = randrange(1,3)
        elif self.difficulty == 2:
            self.number = randrange(1,21)
            self.operator = randrange(1,5)
        elif self.difficulty == 3:
            self.number = randrange(1,51)
            self.operator = randrange(3,6)
        
        if self.rounds > self.player_rounds:
            print("\nOn to the next one")
            time.sleep(0.9)
        else:
            print("\nYou finished all the rounds")
            time.sleep(0.9)

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
            operation = randrange(1,6)

        if operation == 1:
            result = calc.add(num1, num2)
        elif operation == 2:
            result = calc.substract(num1, num2)
        elif operation == 3:
            result = calc.multiply(num1, num2)
        elif operation == 4:
            result = calc.divide(num1, num2)
        elif operation == 5:
            result = calc.to_the_power(num1, num2)
        else: 
            result = calc.modular(num1, num2)
        
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
        else: 
            act = float(result) % float(self.number)
        
        if operation == 1:
            return("{} + {} = {}".format(num1, num2, act))
        elif operation == 2:
            return("{} - {} = {}".format(num1, num2, act))
        elif operation == 3:
            return("{} * {} = {}".format(num1, num2, act))
        elif operation == 4:
            return("{} / {} = {}".format(num1, num2, act))
        elif operation == 5:
            return("{} ^ {} = {}".format(num1, num2, act))
        else: 
            return("{} % {} = {}".format(num1, num2, act))
    
    def play(self):
        while self.number != self.player_number or self.operator != self.player_operator:
            print("\n{}".format(self.calc()))
            player_operator = input("\nWhat do you think the operator is: Add=1, Substract=2, Multiply=3, Divide=4, To the power of=5, Modulo=6: ")
            player_number = input("\nwhat do you think the number is: ")
            self.set_player_operator(player_operator)
            self.set_player_number(player_number)
            if self.player_number != self.number:
                time.sleep(1)
                print("\nthe number is wrong")
            if self.player_operator != self.operator:
                time.sleep(1)
                print("\nthe operator is wrong")
        time.sleep(0.9)
        print("\nGood job, You got them both right!")
        time.sleep(0.9)
        self.up_rounds()
        self.clear_player()
        self.set_new()
        
    
    def start_game(self):
        self.set_start()
        self.set_difficulty(input("Choose your difficulty: 1=easy 2=normal 3=hard: "))
        self.set_rounds(input("Amount of rounds: "))
        while self.player_rounds != self.rounds:
            self.play()
        self.set_end()
        self.calculate_time()
        print("\nCongratulations!\nYou won!")
        print("It took you {} calculations and {} seconds".format(calc.get_calculations(), self.time))
        
