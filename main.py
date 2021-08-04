from os import name
import random

class Roll():
    def __new__(y):
        diceroll = random.randint(1,y)
        return int(diceroll)

class Dice():
    def sides():
        num_of_sides = int(input("Vælg terningens antal sider: "))
        return int(num_of_sides)

#class Gui():


class Game():
    def start():
        print("Velkommen til DiceRoll")
        name = input("Indtast dit navn: ")
        starttext = "Hejsa {}, lad os begynde".format(name)
        print(starttext)
        sides = Dice.sides()
        sides
        start_roll = Roll.__new__(sides)
        start_roll
        number_of_guesses = 0

        while number_of_guesses < 10:
            guessGui = "Gæt et tal mellem 1-{}: ".format(sides)
            guess = int(input(guessGui))
            number_of_guesses +=1
            if guess < start_roll:
                print("too low")
            elif guess > start_roll:
                print("too high")
            elif guess == start_roll:
                print("correct")
                exit()



Game.start()
