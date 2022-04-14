#!/usr/bin/env python3

import random
from models.grid import SudokuGrid

class PlaySudoku():

    def __init__(self, grid):
        self.grid = grid
        self.initial_grid = self.grid.copy()

    def getValues(self):
        print(self.grid)  
        res = input("Enter the positions x (row) and y (column) (from 1 to 9) of the cell and the value v (from 1 to 9) following the format: xyv (q to exit)\n> ")
        if "q" in res :
            return 0
        if " " in res :
            res.replace(" ", "")
        if len(res) > 3 or len(res) < 3 :
            print("Value given in the wrong format: give the x (row) and y (column) position and the value following the format: xyv") 
        else :
            try :
                for l in res :
                    if int(l) ==0 : 
                        raise ValueError
                self.checkValues(int(res[0])-1, int(res[1])-1, int(res[2]))
            except ValueError :
                print("Value given in the wrong format: should be numbers from 1 to 9")
  
    def checkValues(self, i, j, v):
        impossible_val =[]
        try :
            tested_i = int(i)
            tested_j = int(j)
            row = self.grid.get_row(tested_i)
            col = self.grid.get_col(tested_j)
            region = self.grid.get_region(int(tested_i/3), int(tested_j/3))
            for nb in row:
                impossible_val.append(nb)
            for nb in col:
                impossible_val.append(nb)
            for nb in region:
                impossible_val.append(nb)
            
            if self.initial_grid.initial_grid[tested_i][tested_j]!=0:
                print("/!\ Unable to change initial values")
            elif int(v) in impossible_val:
                print("/!\ The value entered is already in the row, column or region")
            else:
                self.grid.write(tested_i,tested_j,int(v))

        except TypeError:
            print("/!\ Only numbers are accepted")
        except IndexError:
            pass
            
    def checkFinish(self):
        for i in range(9):
            if 0 in self.grid.get_col(i):
                return False
        return True

def play(source, typeSource):
    grid = ""
    if typeSource == "file" :
        with open(source) as grids : 
            for i, _ in enumerate(grids):
                pass
            grids.seek(0)
            grid = grids.readlines()[random.randint(0, i)].replace("\n","")
    else :
        grid = source

    g = SudokuGrid(grid)
    play = PlaySudoku(g)
    Finished = False
    while not Finished:
        if play.getValues() == 0 :
            break
        Finished = play.checkFinish()
    print("Soduku finished")