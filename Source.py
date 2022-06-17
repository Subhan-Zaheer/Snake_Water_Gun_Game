"""
    ------- Snake Water and Gun Game
snake and water, win = snake
water and gun, win = water
snake and gun, win = gun
"""
import random
def userChoiceFunc(ls):
    while True:
        choice = input("Press \'S\' for snake, \'W\' for water and \'G\' for gun : ")
        if choice == 's' or choice == 'S' or choice == 'w' or choice == 'W' or choice == 'g' or choice == 'G':
            break
    userChoice = ""
    if choice == 's' or choice == 'S':
        userChoice = ls[0]
    elif choice == 'w' or choice == 'W':
        userChoice = ls[1]
    else:
        userChoice = ls[2]

    return userChoice


def logic(user_Choice, compChoice):
    if user_Choice == "Snake" and compChoice == "Water":
        print("User had chosen Snake and Computer had chosen Water")
        print("User has Won the Competition!")
    elif compChoice == "Snake" and user_Choice == "Water":
        print("User had chosen Water and Computer had chosen Snake")
        print("Computer has Won the Competition!")
    elif user_Choice == "Gun" and compChoice == "Snake":
        print("User had chosen Gun and Computer had chosen Snake")
        print("User has Won the Competition!")
    elif compChoice == "Gun" and user_Choice == "Snake":
        print("User had chosen Snake and Computer had chosen Gun")
        print("Computer has Won the Competition!")
    elif user_Choice == "Water" and compChoice == "Gun":
        print("User had chosen Water and Computer had chosen Gun")
        print("User has Won the Competition!")
    elif compChoice == "Water" and user_Choice == "Gun":
        print("User had chosen Gun and Computer had chosen Water")
        print("Computer has Won the Competition!")
    else:
        print("Match has been draw!")


def game():
    ls = ["Snake", "Water", "Gun"]
    compChoice = random.choice(ls)
    print("Computer has chosen its value. Now its your turn.")
    user_Choice = userChoiceFunc(ls)
    logic(user_Choice, compChoice)

game()