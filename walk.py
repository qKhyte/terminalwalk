import time, random

col1 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
col2 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
col3 = ["O", "O", "O", "O", "O", "X", "O", "O", "O", "O"]
col4 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
col5 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]

playerPos = 0   
def checkPlayerX():
    global playerPos

    if "X" in col1:
        for i in col1:
            if (i == 'X'):
                break
            playerPos += 1
        return "col1"
    
    if "X" in col2:
        for i in col2:
            if (i == 'X'):
                break
            playerPos += 1
        return "col2"
    
    if "X" in col3:
        for i in col3:
            if (i == 'X'):
                break
            playerPos += 1
        return "col3"
    
    if "X" in col4:
        for i in col4:
            if (i == 'X'):
                break
            playerPos += 1
        return "col4"
    
    if "X" in col5:
        for i in col5:
            if (i == 'X'):
                break
            playerPos += 1
        return "col5"

def showBoard():
    global playerPos
    col1Str = ""
    col2Str = ""
    col3Str = ""
    col4Str = ""
    col5Str = ""
    for i in col1:
        col1Str += i + " "
    for i in col2:
        col2Str += i + " "
    for i in col3:
        col3Str += i + " "
    for i in col4:
        col4Str += i + " "
    for i in col5:
        col5Str += i + " "
    print(col1Str)
    print(col2Str)
    print(col3Str)
    print(col4Str)
    print(col5Str)
    userInput = ""
    while userInput != "w" and userInput != "a" and userInput != "s" and userInput != "d":
        userInput = input("Help for commands\n> ").lower()
    if userInput == "w":
        posy = checkPlayerX()
        if posy == "col1":
            showBoard()
        if posy == 'col2':
            col2[playerPos] = "O"
            col1[playerPos] = "X"
        if posy == 'col3':
            col3[playerPos] = "O"
            col2[playerPos] = "X"
        if posy == 'col4':
            col4[playerPos] = "O"
            col3[playerPos] = "X"
        if posy == 'col5':
            col5[playerPos] = "O"
            col4[playerPos] = "X"
        playerPos = 0

    if userInput == "s":
        posy = checkPlayerX()
        if posy == "col1":
            col1[playerPos] = "O"
            col2[playerPos] = "X"
        if posy == 'col2':
            col2[playerPos] = "O"
            col3[playerPos] = "X"
        if posy == 'col3':
            col3[playerPos] = "O"
            col4[playerPos] = "X"
        if posy == 'col4':
            col4[playerPos] = "O"
            col5[playerPos] = "X"
        if posy == 'col5':
            showBoard()
        playerPos = 0

    if userInput == "d":
        posx = checkPlayerX()
        if posx == "col1":
            if playerPos == 9 or playerPos == 0:
                playerPos = 0
                showBoard()
            col1[playerPos] = "O"
            col1[playerPos + 1] = "X"
        if posx == 'col2':
            if playerPos == 9 or playerPos == 0:
                playerPos = 0
                showBoard()
            col2[playerPos] = "O"
            col2[playerPos + 1] = "X"
        if posx == 'col3':
            if playerPos == 9 or playerPos == 0:
                playerPos = 0
                showBoard()
            col3[playerPos] = "O"
            col3[playerPos + 1] = "X"
        if posx == 'col4':
            if playerPos == 9 or playerPos == 0:
                playerPos = 0
                showBoard()
            col4[playerPos] = "O"
            col4[playerPos + 1] = "X"
        if posx == 'col5':
            if playerPos == 9 or playerPos == 0:
                playerPos = 0
                showBoard()
            col5[playerPos] = "O"
            col5[playerPos + 1] = "X"
    playerPos = 0

    if userInput == "a":
        posx = checkPlayerX()
        if posx == "col1":
            if playerPos == 9 or playerPos == 0:
                playerPos = 0
                showBoard()
            col1[playerPos] = "O"
            col1[playerPos - 1] = "X"
        if posx == 'col2':
            if playerPos == 9 or playerPos == 0:
                playerPos = 0
                showBoard()
            col2[playerPos] = "O"
            col2[playerPos - 1] = "X"
        if posx == 'col3':
            if playerPos == 9 or playerPos == 0:
                playerPos = 0
                showBoard()
            col3[playerPos] = "O"
            col3[playerPos - 1] = "X"
        if posx == 'col4':
            if playerPos == 9 or playerPos == 0:
                playerPos = 0
                showBoard()
            col4[playerPos] = "O"
            col4[playerPos - 1] = "X"
        if posx == 'col5':
            if playerPos == 9 or playerPos == 0:
                playerPos = 0
                showBoard()
            col5[playerPos] = "O"
            col5[playerPos - 1] = "X"
    playerPos = 0

    showBoard()    

showBoard()