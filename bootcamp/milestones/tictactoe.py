def starttictactoe():
    choice = 0
    player1puck = int(input("Player1, do you choose the X or the O? 1 for X and 2 for O: "))
    player2puck = 6
    if player1puck == 1:
            player2puck = 2
    else:
        player2puck = 1
        player1puck = 2
    count = 0
    gamenotwon = True
    player1orplayer2 = True
    row1 = ["","",""]
    row2 = ["","",""]
    row3 = ["","",""]
    def printboard():
        print(row1)
        print("")
        print(row2)
        print("")
        print(row3)        
    def move():
        if player1orplayer2:
            if player1puck == 1:
                if choice == 1:
                    row3[0] = "X"
                if choice == 2:
                    row3[1] = "X"
                if choice == 3:
                    row3[2] = "X"
                if choice == 4:
                    row2[0] = "X"
                if choice == 5:
                    row2[1] = "X"
                if choice == 6:
                    row2[2] = "X"
                if choice == 7:
                    row1[0] = "X"
                if choice == 8:
                    row1[1] = "X"
                if choice == 9:
                    row1[2] = "X"
            if player1puck == 2:
                if choice == 1:
                    row3[0] = "O"
                if choice == 2:
                    row3[1] = "O"
                if choice == 3:
                    row3[2] = "O"
                if choice == 4:
                    row2[0] = "O"
                if choice == 5:
                    row2[1] = "O"
                if choice == 6:
                    row2[2] = "O"
                if choice == 7:
                    row1[0] = "O"
                if choice == 8:
                    row1[1] = "O"
                if choice == 9:
                    row1[2] = "O"
        else:
            if player2puck == 1:
                if choice == 1:
                    row3[0] = "X"
                if choice == 2:
                    row3[1] = "X"
                if choice == 3:
                    row3[2] = "X"
                if choice == 4:
                    row2[0] = "X"
                if choice == 5:
                    row2[1] = "X"
                if choice == 6:
                    row2[2] = "X"
                if choice == 7:
                    row1[0] = "X"
                if choice == 8:
                    row1[1] = "X"
                if choice == 9:
                    row1[2] = "X"
            if player2puck == 2:
                if choice == 1:
                    row3[0] = "O"
                if choice == 2:
                    row3[1] = "O"
                if choice == 3:
                    row3[2] = "O"
                if choice == 4:
                    row2[0] = "O"
                if choice == 5:
                    row2[1] = "O"
                if choice == 6:
                    row2[2] = "O"
                if choice == 7:
                    row1[0] = "O"
                if choice == 8:
                    row1[1] = "O"
                if choice == 9:
                    row1[2] = "O"
    def checkgamewon():
        if row1[0] == row1[1] == row1[2]:
            gamenotwon = False
        if row2[0] == row2[1] == row2[2]:
            gamenotwon = False
        if row3[0] == row3[1] == row3[2]:
            gamenotwon = False
        if (row1[0] == row2[1] == row3[2]):
            gamenotwon = False
        if row3[0] == row2[1] == row1[2]:
            gamenotwon = False
        if row1[0] == row2[0] == row3[0]:
            gamenotwon = False
        if row1[1] == row2[1] == row3[1]:
            gamenotwon = False
        if row1[2] == row2[2] == row3[2]:
            gamenotwon = False
    printboard()
    while gamenotwon:
        choice = int(input("Make a choice on the numpad: "))
        move()
        printboard()
        checkgamewon()
        player1orplayer2 = not player1orplayer2
    if not gamenotwon:
        print("Congratulations you won!")
starttictactoe()
