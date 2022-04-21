from random import randrange
from Calculator import CalculatorGames

calc = CalculatorGames(2)

class Game:
    def __init__(self, rounds):
        self.rounds = rounds
        self.player_rounds = 0
        self.number = None
        self.operator = None
        self.player_number = None
        self.player_operator = None
    
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
            self.operator = randrange(3,7)



    def clear_player(self):
        self.player_operator = None
        self.player_number = None

    def set_new(self):
        if self.difficulty == 1:
            self.number = randrange(1,11)
            self.operator = randrange(1,3)
        if self.difficulty == 2:
            self.number = randrange(1,21)
            self.operator = randrange(1,5)
        if self.difficulty == 3:
            self.number = randrange(1,51)
            self.operator = randrange(3,7)

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
            operation = randrange(1,7)

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
            act = result + self.number
        elif self.operator == 2:
            act = result - self.number
        elif self.operator == 3:
            act = result * self.number
        elif self.operator == 4:
            act = result / self.number
        elif self.operator == 5:
            act = result ** self.number
        else: 
            act = result % self.number
        
        if operation == 1:
            print("{} + {} = {}".format(num1, num2, act))
        elif operation == 2:
            print("{} - {} = {}".format(num1, num2, act))
        elif operation == 3:
            print("{} * {} = {}".format(num1, num2, act))
        elif operation == 4:
            print("{} / {} = {}".format(num1, num2, act))
        elif operation == 5:
            print("{} ^ {} = {}".format(num1, num2, act))
        else: 
            print("{} % {} = {}".format(num1, num2, act))
    
    def play(self):
        while self.number != self.player_number or self.operator != self.player_operator:
            self.calc()
            player_operator = input("What do you think the operator is: Add=1, Substract=2, Multiply=3, Divide=4, To the power of=5, Modulo=6: ")
            player_number = input("what do you think the number is: ")
            self.set_player_operator(player_operator)
            self.set_player_number(player_number)
            if self.player_number != self.number:
                print("the number is wrong")
            if self.player_operator != self.operator:
                print("the operator is wrong")
        print("Good job, You got them both right!")
        self.up_rounds()
        self.clear_player()
        self.set_new()
game = Game(5)
game.set_difficulty(input("Choose your difficulty: 1=easy 2=normal 3=hard: "))
while game.player_rounds is not game.rounds:
    game.play()
print("You won!")

