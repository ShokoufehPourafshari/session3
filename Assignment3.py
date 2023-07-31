print("Hello\n")
print("pleas choose a number :\n1) Start Game 1 Dice\n2) Exit")
play = input("what you have is: ")
import random

while True:
    if play == "1":
        roll = random.randint(1,6)
        print("your game result: ", roll)
        if roll == 6:
            print("here's your second chance")
            second_chance = random.randint(1,6)
            print("your second chance result: ", second_chance)
        else:
            break
    if play == "2":
        break
    else:
        print("Choose Invalid!")
