import sys
import os
sys.path.append(os.path.abspath('.')+'/src')

from models.play import play
from models.solve import solve


def checkSource(data):
    print(len(data))
    if len(data) == 81 :
        print("check numbers")
        try :
            for c in data :
                int(c)
            return "sudoku"
        except ValueError:
            print("Wrong data, the sudoku should only contain numbers")
    elif os.path.exists(data):
        return "file"
    else :
        print("File not found or sudoku do not contains 81 numbers")
    return False
    



def start(mode):
    source = ""
    typeSource = ""
    while source == "" :
        data = input("Enter the source file or the 81 numbers of the sudoku  - (enter for default :sudokus.txt)\n> ")
        if data == "" :
            source = "src/sudokus.txt"
            typeSource = "file"
        else :
            typeSource = checkSource(data)
            if typeSource :
                source = data

    if mode == "play" :
        play(source, typeSource)
    if mode == "solve" :
        solve(source, typeSource)

if __name__=="__main__":
    print("Welcome to the soduku player")
    while True : 
        mode = input("Select a game mode : 'play' or 'solve' (q to exit)\n> ")
        if mode == "q":
            break
        elif mode in ["play", "solve"] :
            print(f"{mode} mode is selected")
            start(mode)
            continue
        print("You need to enter a game mode : 'play' or 'solve'")
