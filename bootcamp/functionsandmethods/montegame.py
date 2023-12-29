from random import shuffle
def shuffle_list(alist):
    shuffle(alist)
    print(alist)
guess = -1
def getguess():
    guess = input("What is your guess? 0, 1, or 2?")
def montegame():
    gamelist = [" ","O"," "]
    print(gamelist)
    shuffle_list(gamelist)
    if gamelist[guess] == "O":
        print("Correct guess!")
    else:
        print("Wrong guess, game over")
getguess()
montegame()
