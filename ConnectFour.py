import os
import ast

SaveFile = "ConnectFour.txt"

class ccolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def Clear():
    os.system("cls")

def CreateSaveGame():
    if not os.path.exists(SaveFile):
        open(SaveFile, 'w')

def Save(Data, Filename):
    f = open(Filename, "w")
    temp = ','.join(map(str, Data))
    f.write(temp)
    f.close()

def Read(Filename):
    with open(Filename, 'r') as f:
        temp = f.read()
        output = ast.literal_eval(temp)
        f.close()
        return output

def InitGameTable(NewGame):
    cols = 7
    rows = 6
    global GameTable

    GameTable = [["-" for i in range(cols)] for j in range(rows)]

    if (NewGame == 0):
        GameTable = Read(SaveFile)

    return GameTable

def PrintTable():
    print("  1   2   3   4   5   6   7")

    for row in GameTable:
        print("| ", end="")
        for item in row:
            if item == 0:
                print(ccolors.BLUE + "0" + ccolors.ENDC.format(item), end=" | ")
            elif item == 1:
                print(ccolors.RED + "0" + ccolors.ENDC.format(item), end=" | ")
            elif item == "-":
                print("-", end=" | ")
        print(" ")


def Entry():
    Clear()
    print("Welcome to Connect Four\n" + "------------------------\n" + "Select one option below:\n\n" + "Begin - start a new game\n" + "Open - continue a prior game\n")
    NewGameStr = str(input("Enter option > "))
    if (NewGameStr == "Begin" or NewGameStr == "begin"):
        NewGame = 1
    elif (NewGameStr == "Open" or NewGameStr == "open"):
        NewGame = 0
    return NewGame

def Input(CurrentPlayer):
    i = -1
    if (CurrentPlayer == 0): # Blue
        print(ccolors.BLUE + "\nBlue's Turn" + ccolors.ENDC)
    elif (CurrentPlayer == 1): # Red
        print(ccolors.RED + "\nRed's Turn" + ccolors.ENDC)

    GoCol = int(input("\nEnter Column > ")) - 1

    while (GameTable[i][GoCol] != "-"):
        i -= 1

    GameTable[i][GoCol] = CurrentPlayer
    Save(GameTable, SaveFile)

def CheckDik():
    CheckDik = 0
    for i in range(len(GameTable)):
        for j in range(len(GameTable[i])): #I vert, J horiz
            #print(GameTable[i][j], GameTable[i+1][j], GameTable[i+2][j], GameTable[i+3][j])
            #print(GameTable[1][1], GameTable[1][2], GameTable[1][3], GameTable[1][4])
            if (GameTable[i][j] == GameTable[i+1][j] == GameTable[i+2][j] == GameTable[i+3][j] != "-"):
                CheckDik = 1
            elif (GameTable[i+1][j] == GameTable[i+2][j] == GameTable[i+3][j] == GameTable[i+4][j] != "-"):
                CheckDik = 1
            elif (GameTable[i+2][j] == GameTable[i+3][j] == GameTable[i+4][j] == GameTable[i+5][j] != "-"):
                CheckDik = 1
        #print(CheckDik)
        return CheckDik

def CheckHorizon():
    CheckHorizon = 0
    for i in range(len(GameTable)):
        for j in range(len(GameTable[i])):
            #print("HORIZON")
            #print(GameTable[i][0], GameTable[i][1], GameTable[i][2], GameTable[i][3])
            if (GameTable[i][0] == GameTable[i][1] == GameTable[i][2] == GameTable[i][3] != "-"):
                CheckHorizon = 1
            elif (GameTable[i][1] == GameTable[i][2] == GameTable[i][3] == GameTable[i][4] != "-"):
                CheckHorizon = 1
            elif (GameTable[i][2] == GameTable[i][3] == GameTable[i][4] == GameTable[i][5] != "-"):
                CheckHorizon = 1
            elif (GameTable[i][3] == GameTable[i][4] == GameTable[i][5] == GameTable[i][6] != "-"):
                CheckHorizon = 1
            ##
            elif (GameTable[i+1][0] == GameTable[i+1][1] == GameTable[i+1][2] == GameTable[i+1][3] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+1][1] == GameTable[i+1][2] == GameTable[i+1][3] == GameTable[i+1][4] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+1][2] == GameTable[i+1][3] == GameTable[i+1][4] == GameTable[i+1][5] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+1][3] == GameTable[i+1][4] == GameTable[i+1][5] == GameTable[i+1][6] != "-"):
                CheckHorizon = 1
            ##
            elif (GameTable[i+2][0] == GameTable[i+2][1] == GameTable[i+2][2] == GameTable[i+2][3] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+2][1] == GameTable[i+2][2] == GameTable[i+2][3] == GameTable[i+2][4] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+2][2] == GameTable[i+2][3] == GameTable[i+2][4] == GameTable[i+2][5] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+2][3] == GameTable[i+2][4] == GameTable[i+2][5] == GameTable[i+3][6] != "-"):
                CheckHorizon = 1
            ##
            elif (GameTable[i+3][0] == GameTable[i+3][1] == GameTable[i+3][2] == GameTable[i+3][3] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+3][1] == GameTable[i+3][2] == GameTable[i+3][3] == GameTable[i+3][4] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+3][2] == GameTable[i+3][3] == GameTable[i+3][4] == GameTable[i+3][5] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+3][3] == GameTable[i+3][4] == GameTable[i+3][5] == GameTable[i+3][6] != "-"):
                CheckHorizon = 1
            ##
            elif (GameTable[i+4][0] == GameTable[i+4][1] == GameTable[i+4][2] == GameTable[i+4][3] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+4][1] == GameTable[i+4][2] == GameTable[i+4][3] == GameTable[i+4][4] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+4][2] == GameTable[i+4][3] == GameTable[i+4][4] == GameTable[i+5][5] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+4][3] == GameTable[i+5][4] == GameTable[i+5][5] == GameTable[i+5][6] != "-"):
                CheckHorizon = 1
            ##
            elif (GameTable[i+5][0] == GameTable[i+5][1] == GameTable[i+5][2] == GameTable[i+5][3] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+5][1] == GameTable[i+5][2] == GameTable[i+5][3] == GameTable[i+5][4] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+5][2] == GameTable[i+5][3] == GameTable[i+5][4] == GameTable[i+5][5] != "-"):
                CheckHorizon = 1
            elif (GameTable[i+5][3] == GameTable[i+5][4] == GameTable[i+5][5] == GameTable[i+5][6] != "-"):

                CheckHorizon = 1
        return CheckHorizon

def CheckDiag():
    CheckDiag = 0

    for i in range(len(GameTable)):
        for j in range(len(GameTable[i])):
            #problem here
            #print(GameTable[i][j], GameTable[i + 1][j - 1], GameTable[i + 2][j - 2], GameTable[i + 3][j - 3])
            if (GameTable[i][j] == GameTable[i-1][j-1] == GameTable[i-2][j-2] == GameTable[i-3][j-3] != "-"): #backwards diag *NOT WORKING IDK Y*
                CheckDiag = 1
                ######
            if (GameTable[5][6] == GameTable[4][5] == GameTable[3][4] == GameTable[2][3] != "-"):
                CheckDiag = 1
            elif (GameTable[4][6] == GameTable[3][5] == GameTable[2][4] == GameTable[1][3] != "-"):
                CheckDiag = 1
            elif (GameTable[3][6] == GameTable[2][5] == GameTable[1][4] == GameTable[0][3] != "-"):
                CheckDiag = 1
            elif (GameTable[5][5] == GameTable[4][4] == GameTable[3][3] == GameTable[2][2] != "-"):
                CheckDiag = 1
            elif (GameTable[4][5] == GameTable[3][4] == GameTable[2][3] == GameTable[1][2] != "-"):
                CheckDiag = 1
            elif (GameTable[3][5] == GameTable[2][4] == GameTable[1][3] == GameTable[0][2] != "-"):
                CheckDiag = 1
            elif (GameTable[5][4] == GameTable[4][3] == GameTable[3][2] == GameTable[2][1] != "-"):
                CheckDiag = 1
            elif (GameTable[4][4] == GameTable[3][3] == GameTable[2][2] == GameTable[1][1] != "-"):
                CheckDiag = 1
            elif (GameTable[3][4] == GameTable[2][3] == GameTable[1][2] == GameTable [0][1] != "-"):
                CheckDiag = 1
            elif (GameTable[5][3] == GameTable[4][2] == GameTable[3][1] == GameTable[2][0] != "-"):
                CheckDiag = 1
            elif (GameTable[4][3] == GameTable[3][2] == GameTable[2][1] == GameTable[1][0] != "-"):
                CheckDiag = 1
            elif (GameTable[3][3] == GameTable[2][2] == GameTable[1][1] == GameTable[0][0] != "-"):
                CheckDiag = 1


                print("diag flag")

            #long shitty method (monkey style)
            elif (GameTable[5][0] == GameTable[4][1] == GameTable[3][2] == GameTable[2][3] != "-"):
                CheckDiag = 1
            elif (GameTable[4][1] == GameTable[3][2] == GameTable[2][3] == GameTable[1][4] != "-"):
                CheckDiag = 1
            elif (GameTable[3][2] == GameTable[2][3] == GameTable[1][4] == GameTable[0][5] != "-"):
                CheckDiag = 1
            elif (GameTable[4][0] == GameTable[3][1] == GameTable[2][2] == GameTable[1][3] != "-"):
                CheckDiag = 1
            elif (GameTable[3][1] == GameTable[2][2] == GameTable[1][3] == GameTable[0][4] != "-"):
                CheckDiag = 1
            elif (GameTable[3][0] == GameTable[2][1] == GameTable[1][2] == GameTable[0][3] != "-"):
                CheckDiag = 1
            elif (GameTable[5][1] == GameTable[4][2] == GameTable[3][3] == GameTable[2][4] != "-"):
                CheckDiag = 1
            elif (GameTable[4][2] == GameTable[3][3] == GameTable[2][4] == GameTable[1][5] != "-"):
                CheckDiag = 1
            elif (GameTable[3][3] == GameTable[2][4] == GameTable[1][5] == GameTable[0][6] != "-"):
                CheckDiag = 1
            elif (GameTable[5][2] == GameTable[4][3] == GameTable[3][4] == GameTable[2][5] != "-"):
                CheckDiag = 1
            elif (GameTable[4][3] == GameTable[3][4] == GameTable[2][5] == GameTable[1][6] != "-"):
                CheckDiag = 1
            elif (GameTable[5][3] == GameTable[4][4] == GameTable[3][5] == GameTable[2][6] != "-"):
                CheckDiag = 1
            return CheckDiag

def FindWinner():
    FoundWinner = 0
    if(CheckDik() == 1):
        FoundWinner = 1
        print("Vertical Match")
    elif(CheckHorizon() == 1):
        FoundWinner = 1
        print("Horizontal Match")
    elif(CheckDiag() == 1):
        FoundWinner = 1
        print("Diagonal Match")
    return FoundWinner

def Exit():
    print("\nSelect one option below:\n\n" + "Continue - continue to a new game\n" + "Quit - quit game\n")
    ExitStr = str(input("Enter option > "))
    if (ExitStr == "Continue" or ExitStr == "continue"):
        Exit = 1
    elif (ExitStr == "Quit" or ExitStr == "quit"):
        Exit = 0
        exit()
    return Exit

def MainGame():
    CurrentPlayer = 0

    CreateSaveGame()
    InitGameTable(Entry())

    while (FindWinner() == 0):

        Clear()

        PrintTable()

        Input(CurrentPlayer)

        CheckDiag()

        CurrentPlayer = 1 - CurrentPlayer
    else:
        Clear()
        FindWinner()
        PrintTable()
        print("Game Over")
        if (Exit() == 1):
            MainGame()

MainGame()
