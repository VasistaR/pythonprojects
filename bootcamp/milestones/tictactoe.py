choice = 0
player1puck = "A"
player2puck = "A"
count = 0
gamenotwon = True
row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]
def checkgamewon():
    if row1[0] == row1[1] and row1[1] == row1[2]:
        gamenotwon = False
    if row2[0] == row2[1] and row2[1] == row2[2]:
        gamenotwon = False
    if row3[0] == row3[1] and row3[1] == row3[2]:
        gamenotwon = False
    if row1[0] == row2[1] and row2[1] == row3[2]:
        gamenotwon = False
    if row3[0] == row2[1] and row2[1] == row1[2]:
        gamenotwon = False
    if row1[0] == row2[0] and row2[0] == row3[0]:
        gamenotwon = False
    if row1[1] == row2[1] and row2[1] == row3[1]:
        gamenotwon = False
    if row1[2] == row2[2] and row2[2] == row3[2]:
        gamenotwon = False
def move():
    if player1orplayer2():
        if player1puck == "X":
            if choice == 1:
                row3[0] = "X"
                printboard()
            if choice == 2:
                row3[1] = "X"
                printboard()
            if choice == 3:
                row3[2] = "X"
                printboard()
            if choice == 4:
                row2[0] = "X"
                printboard()
            if choice == 5:
                row2[1] = "X"
                printboard()
            if choice == 6:
                row2[2] - "X"
                printboard()
            if choice == 7:
                row1[0] - "X"
                printboard()
            if choice == 8:
                row1[1] = "X"
                printboard()
            if choice == 9:
                row1[2] = "X"
                printboard()
        if player1puck == "O":
            if choice == 1:
                row3[0] = "O"
                printboard()
            if choice == 2:
                row3[1] = "O"
                printboard()
            if choice == 3:
                row3[2] = "O"
                printboard()
            if choice == 4:
                row2[0] = "O"
                printboard()
            if choice == 5:
                row2[1] = "O"
                printboard()
            if choice == 6:
                row2[2] - "O"
                printboard()
            if choice == 7:
                row1[0] - "O"
                printboard()
            if choice == 8:
                row1[1] = "O"
                printboard()
            if choice == 9:
                row1[2] = "O"
                printboard()
    else:
        if player2puck == "X":
            if choice == 1:
                row3[0] = "X"
                printboard()
            if choice == 2:
                row3[1] = "X"
                printboard()
            if choice == 3:
                row3[2] = "X"
                printboard()
            if choice == 4:
                row2[0] = "X"
                printboard()
            if choice == 5:
                row2[1] = "X"
                printboard()
            if choice == 6:
                row2[2] - "X"
                printboard()
            if choice == 7:
                row1[0] - "X"
                printboard()
            if choice == 8:
                row1[1] = "X"
                printboard()
            if choice == 9:
                row1[2] = "X"
                printboard()
        if player2puck == "O":
            if choice == 1:
                row3[0] = "O"
                printboard()
            if choice == 2:
                row3[1] = "O"
                printboard()
            if choice == 3:
                row3[2] = "O"
                printboard()
            if choice == 4:
                row2[0] = "O"
                printboard()
            if choice == 5:
                row2[1] = "O"
                printboard()
            if choice == 6:
                row2[2] - "O"
                printboard()
            if choice == 7:
                row1[0] - "O"
                printboard()
            if choice == 8:
                row1[1] = "O"
                printboard()
            if choice == 9:
                row1[2] = "O"
                printboard()
def x_or_o():
    player1puck = input("Player1, do you choose the X or the O?: ")
    if player1puck == "X":
        player2puck = "O"
    else:
        player2puck = "X"
def choice():
    choice = int(input("Make a choice on the numpad: "))
    return choice
def player1orplayer2():
    ## when count is even, it is player1's turn
    if count % 2 == 0:
        return True
    else:
        return False
def starttictactoe():
    def printboard():
        print(row1)
        print("")
        print(row2)
        print("")
        print(row3)
    printboard()
    while gamenotwon:
        choice()
        move()
        checkgamewon()
    if not gamenotwon:
        print("Congratulations you won!")
starttictactoe()
