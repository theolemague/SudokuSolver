import sys

from play_sudoku import play
from solve_sudoku import solve


def start(mode):
    data = input('Enter the source file or the sudoku (default sudokus.txt)\n> ')
    if data == '' :
        data = "sudokus.txt"
    if mode == 'play' :
        play(data)
    if mode == 'solve' :
        solve(data)

if __name__=='__main__':
    print('Welcome to the soduku player')
    while True : 
        mode = input('Select a game mode : "play" or "solve"\n> ')
        if mode == 'q':
            break
        elif mode in ['play', 'solve'] :
            print(f'{mode} mode is selected')
            start(mode)
            continue
        print('You need to enter a game mode : "play" or "solve"')
