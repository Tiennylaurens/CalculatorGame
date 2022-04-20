from random import randrange
from Calculator import CalculatorGames

calc = CalculatorGames(0)

class Game:
    def __init__(self, rounds):
        self.rounds = rounds
        self.player_rounds = 0
        self.number = randrange(1,11)
        self.operator = randrange(4,5)
        self.player_number = None
        self.player_operator = None

    def clear_player(self):
        self.player_operator = None
        self.player_number = None

    def set_number(self):
        self.number = randrange(1,11)

    def set_operator(self):
        self.operator = randrange(4,5)

    def up_rounds(self):
        self.player_rounds += 1

    def set_player_number(self, number):
        self.player_number = number

    def set_player_operator(self, number):
        self.player_operator = number

    def calc(self):
        num1 = input("num1: ")
        num2 = input("num2: ")
        operation = input("Add=1, Substract=2, Multiply=3, Divide=4: ")
        if operation == 1:
            result = calc.add(num1, num2)
        elif operation == 2:
            result = calc.substract(num1, num2)
        elif operation == 3:
            result = calc.multiply(num1, num2)
        elif operation == 4:
            result = calc.divide(num1, num2)
        else: 
            print("Unvalid input, Choose a number between 1 and 4 for the operator")
        
        if self.operator == 1:
            return result + self.number
        elif self.operator == 2:
            return result - self.number
        elif self.operator == 3:
            return result * self.number
        else:
            return result / self.number
    
    def play(self):
        while self.number != self.player_number or self.operator != self.player_operator:
            print(self.calc())
            player_operator = input("What do you think the operator is: Add=1, Substract=2, Multiply=3, Divide=4: ")
            player_number = input("what do you think the number is, Choose between 1 and 10: ")
            self.set_player_operator(player_operator)
            self.set_player_number(player_number)
            if self.player_number != self.number:
                print("the number is wrong")
            if self.player_operator != self.operator:
                print("the operator is wrong")
        print("Good job, You got them both right!")
        self.up_rounds()
        self.clear_player()
        self.set_number()
        self.set_operator()

game = Game(5)
while game.player_rounds is not game.rounds:
    game.play()
print("You won")

