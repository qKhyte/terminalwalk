import random

CHARACTER = ""
while len(CHARACTER) != 1 or CHARACTER == "O":
    CHARACTER = input("Select Character\n> ")

col1 = [">", ".", ".", ".", ".", ".", ".", ".", ".", "."]
col2 = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
col3 = [".", ".", ".", ".", ".", CHARACTER, ".", ".", ".", "."]
col4 = [".", ".", "O", ".", ".", ".", ".", ".", ".", "."]
col5 = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]

playerPos = 0   
def changeBoard():
    global col1
    global col2
    global col3
    global col4
    global col5
    global playerPos
    col1 = [">", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    col2 = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    col3 = [".", ".", ".", ".", ".", CHARACTER, ".", ".", ".", "."]
    col4 = [".", ".", "O", ".", ".", ".", ".", ".", ".", "."]
    col5 = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    playerPos = 0
    showBoard()

def checkPlayerX():
    global playerPos

    if CHARACTER in col1:
        for i in col1:
            if (i == CHARACTER):
                break
            playerPos += 1
        return "col1"
    
    if CHARACTER in col2:
        for i in col2:
            if (i == CHARACTER):
                break
            playerPos += 1
        return "col2"
    
    if CHARACTER in col3:
        for i in col3:
            if (i == CHARACTER):
                break
            playerPos += 1
        return "col3"
    
    if CHARACTER in col4:
        for i in col4:
            if (i == CHARACTER):
                break
            playerPos += 1
        return "col4"
    
    if CHARACTER in col5:
        for i in col5:
            if (i == CHARACTER):
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
            if col1[playerPos] == ">": changeBoard()
            if col1[playerPos] == "O":
                playerPos = 0
                showBoard()
            col2[playerPos] = "."
            col1[playerPos] = CHARACTER
        if posy == 'col3':
            if col2[playerPos] == ">": changeBoard()
            if col2[playerPos] == "O":
                col1[playerPos] = "O"
            col3[playerPos] = "."
            col2[playerPos] = CHARACTER
        if posy == 'col4':
            if col3[playerPos] == ">": changeBoard()
            if col3[playerPos] == "O":
                col2[playerPos] = "O"
            col4[playerPos] = "."
            col3[playerPos] = CHARACTER
        if posy == 'col5':
            if col4[playerPos] == ">": changeBoard()
            if col4[playerPos] == "O":
                col3[playerPos] = "O"
            col5[playerPos] = "."
            col4[playerPos] = CHARACTER
        
        playerPos = 0

    if userInput == "s":
        posy = checkPlayerX()
        if posy == "col1":
            if col2[playerPos] == ">": changeBoard()
            if col2[playerPos] == "O":
                col3[playerPos] = "O"
            col1[playerPos] = "."
            col2[playerPos] = CHARACTER
        if posy == 'col2':
            if col3[playerPos] == ">": changeBoard()
            if col3[playerPos] == "O":
                col4[playerPos] = "O"
            col2[playerPos] = "."
            col3[playerPos] = CHARACTER
        if posy == 'col3':
            if col4[playerPos] == ">": changeBoard()
            if col4[playerPos] == "O":
                col5[playerPos] = "O"
            col3[playerPos] = "."
            col4[playerPos] = CHARACTER
        if posy == 'col4':
            if col5[playerPos] == ">": changeBoard()
            if col5[playerPos] == "O": 
                playerPos = 0
                showBoard()
            col4[playerPos] = "."
            col5[playerPos] = CHARACTER
        if posy == 'col5':
            showBoard()
        playerPos = 0

    if userInput == "d":
        posx = checkPlayerX()
        if posx == "col1":
            if playerPos == 9:
                playerPos = 0
                showBoard()
            if col1[playerPos + 1] == ">": changeBoard()
            if col1[playerPos + 1] == "O": col1[playerPos + 2] = "O"
            col1[playerPos] = "."
            col1[playerPos + 1] = CHARACTER
        if posx == 'col2':
            if playerPos == 9:
                playerPos = 0
                showBoard()
            if col2[playerPos + 1] == ">": changeBoard()
            if col2[playerPos + 1] == "O": col2[playerPos + 2] = "O"
            col2[playerPos] = "."
            col2[playerPos + 1] = CHARACTER
        if posx == 'col3':
            if playerPos == 9:
                playerPos = 0
                showBoard()
            if col3[playerPos + 1] == ">": changeBoard()
            if col3[playerPos + 1] == "O": col3[playerPos + 2] = "O"
            col3[playerPos] = "."
            col3[playerPos + 1] = CHARACTER
        if posx == 'col4':
            if playerPos == 9:
                playerPos = 0
                showBoard()
            if col4[playerPos + 1] == ">": changeBoard()
            if col4[playerPos + 1] == "O": col4[playerPos + 2] = "O"
            col4[playerPos] = "."
            col4[playerPos + 1] = CHARACTER
        if posx == 'col5':
            if playerPos == 9:
                playerPos = 0
                showBoard()
            if col5[playerPos + 1] == "O": col5[playerPos + 2] = "O"
            col5[playerPos] = "."
            col5[playerPos + 1] = CHARACTER
    playerPos = 0

    if userInput == "a":
        posx = checkPlayerX()
        if posx == "col1":
            if playerPos == 0:
                playerPos = 0
                showBoard()
            if col1[0] == "O":
                showBoard()
            if col1[playerPos - 1] == ">": changeBoard()
            if col1[playerPos - 1] == "O": col1[playerPos - 2] = "O"
            col1[playerPos] = "."
            col1[playerPos - 1] = CHARACTER
        if posx == 'col2':
            if playerPos == 0:
                playerPos = 0
                showBoard()
            if col2[0] == "O":
                playerPos = 0
                showBoard()
            if col2[playerPos - 1] == ">": changeBoard()
            if col2[playerPos - 1] == "O": col2[playerPos - 2] = "O"
            col2[playerPos] = "."
            col2[playerPos - 1] = CHARACTER
        if posx == 'col3':
            if playerPos == 0:
                playerPos = 0
                showBoard()
            if col3[0] == "O":
                playerPos = 0
                showBoard()
            if col3[playerPos - 1] == ">": changeBoard()
            if col3[playerPos - 1] == "O": col3[playerPos - 2] = "O"
            col3[playerPos] = "."
            col3[playerPos - 1] = CHARACTER
        if posx == 'col4':
            if playerPos == 0:
                playerPos = 0
                showBoard()
            if col4[0] == "O":
                playerPos = 0
                showBoard()
            if col4[playerPos - 1] == ">": changeBoard()
            if col4[playerPos - 1] == "O": col4[playerPos - 2] = "O"
            col4[playerPos] = "."
            col4[playerPos - 1] = CHARACTER
        if posx == 'col5':
            if playerPos == 0:
                playerPos = 0
                showBoard()
            if col5[playerPos - 1] == ">": changeBoard()
            if col5[0] == "O":
                playerPos = 0
                showBoard()
            if col5[playerPos - 1] == "O": col5[playerPos - 2] = "O"
            col5[playerPos] = "."
            col5[playerPos - 1] = CHARACTER
    playerPos = 0

    showBoard()    

showBoard()
