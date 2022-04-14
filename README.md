# Sudoku Solver
The sudoku solver is a Python project realized in the context of an introduction to programming course at INSA Lyon in 3rd year. The project consists in creating a sudoku solver. The skeleton of the project (only the signatures of the classes and functions) was given and we had to fill it. The solver uses a recursive technique.

# Development
## Project
```
- src/
    - models/
        - grid.py
        - solver.py
        - play.py
        - solve.py
    - start.py
    - sudokus.py
- tests/
    - test_grid.py
    - test_solver.py
```
The file `start.py` is the launcher of the interactive command line. `models/` contains all the classes and functions that are used to solve the sudokus. `tests/` contains the tests given to check our implementation. `sudokus.txt` is a text file that contains the sudokus in the format used: line of 81 (9x9) numbers where each 9 characters starts a new line and 0 means an empty cell.
## Install
```zsh
$ git clone https://github.com/theolemague/SudokuSolver.git
...
$ cd SudokuSolver
```
## Run
If you want to start the interactive command line you can just call play.py :
```zsh
$ python3 src/play.py
Welcome to the soduku player
Select a game mode : 'play' or 'solve' (q to exit)
> 
...
```
The interactive command line offer 2 possibilities : play sudoku or solve sudoku(s).
### Play sudoku
In game mode, you can play sudoku. You can either choose to import sudokus by adding a file, or enter directly the 81 numbers of the sudoku.
```zsh
Welcome to the soduku player
Select a game mode : 'play' or 'solve' (q to exit)
> play
play mode is selected
Enter the source file or the 81 numbers of the sudoku  - (enter for default :sudokus.txt)
> 200000060000075030048090100000300000300010009000008000001020570080730000090000004
81
check numbers
2 0 0  0 0 0  0 6 0 
0 0 0  0 7 5  0 3 0 
0 4 8  0 9 0  1 0 0 
0 0 0  3 0 0  0 0 0 
3 0 0  0 1 0  0 0 9 
0 0 0  0 0 8  0 0 0 
0 0 1  0 2 0  5 7 0 
0 8 0  7 3 0  0 0 0 
0 9 0  0 0 0  0 0 4 

Enter the positions x (row) and y (column) (from 1 to 9) of the cell and the value v (from 1 to 9) following the format: xyv (q to exit)
> 
...
```
### Solve sudoku
In solve mode, you can choose to enter the number 81 of a single sudoku you want to solve or enter the name of the file that contains multiple sudokus.
```zsh
Select a game mode : 'play' or 'solve' (q to exit)
> solve
solve mode is selected
Enter the source file or the 81 numbers of the sudoku  - (enter for default :sudokus.txt)
> 
Starting solver on src/sudokus.txt with a time-out of 2min...
[======================================= ] (100%)
Number of completed run: 244
Running times statistics: min = 19.238ms, average = 23.949ms, max = 52.701ms
Results are stored in : src/sudokus_solved.txt
...
Select a game mode : 'play' or 'solve' (q to exit)
> solve
solve mode is selected
Enter the source file or the 81 numbers of the sudoku  - (enter for default :sudokus.txt)
> 200000060000075030048090100000300000300010009000008000001020570080730000090000004
Given grid is
2 0 0  0 0 0  0 6 0 
0 0 0  0 7 5  0 3 0 
0 4 8  0 9 0  1 0 0 
0 0 0  3 0 0  0 0 0 
3 0 0  0 1 0  0 0 9 
0 0 0  0 0 8  0 0 0 
0 0 1  0 2 0  5 7 0 
0 8 0  7 3 0  0 0 0 
0 9 0  0 0 0  0 0 4 

2 7 3  4 8 1  9 6 5 
9 1 6  2 7 5  4 3 8 
5 4 8  6 9 3  1 2 7 
8 5 9  3 4 7  6 1 2 
3 6 7  5 1 2  8 4 9 
1 2 4  9 6 8  7 5 3 
4 3 1  8 2 9  5 7 6 
6 8 5  7 3 4  2 9 1 
7 9 2  1 5 6  3 8 4 

Soduku solved in 70.811ms
```
