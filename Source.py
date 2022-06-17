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
    gameWin = True
    if user_Choice == "Snake" and compChoice == "Water":
        print("User had chosen Snake and Computer had chosen Water")
        print("User has Won the Competition!")
        gameWin = True
    elif compChoice == "Snake" and user_Choice == "Water":
        print("User had chosen Water and Computer had chosen Snake")
        print("Computer has Won the Competition!")
        gameWin = False
    elif user_Choice == "Gun" and compChoice == "Snake":
        print("User had chosen Gun and Computer had chosen Snake")
        print("User has Won the Competition!")
        gameWin = True
    elif compChoice == "Gun" and user_Choice == "Snake":
        print("User had chosen Snake and Computer had chosen Gun")
        print("Computer has Won the Competition!")
        gameWin = False
    elif user_Choice == "Water" and compChoice == "Gun":
        print("User had chosen Water and Computer had chosen Gun")
        print("User has Won the Competition!")
        gameWin = True
    elif compChoice == "Water" and user_Choice == "Gun":
        print("User had chosen Gun and Computer had chosen Water")
        print("Computer has Won the Competition!")
        gameWin = False
    else:
        print("Match has been draw!")

    return gameWin


def game():
    ls = ["Snake", "Water", "Gun"]
    compChoice = random.choice(ls)
    print("Computer has chosen its value. Now its your turn.")
    user_Choice = userChoiceFunc(ls)
    winner = logic(user_Choice, compChoice)
    return winner

def start():
    user = 0
    comp = 0
    for i in range(10):
        winner = game()
        if winner == True: user += 1
        else: comp += 1

    print ("User have won ", user, " times.")
    print("Computer have won ", comp, " times.")
    if user > comp: print("User have won more games!")
    elif comp > user: print("Computer have won more games!")
    else: print("Both User and Computer won equal number of games!")

start()